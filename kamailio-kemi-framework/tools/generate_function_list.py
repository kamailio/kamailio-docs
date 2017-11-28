# This file generates the modules.md content
# This file should be run in an environment where there is one, and only one, Kamailio install built from source
import os, json, sys


class ModuleDocGenerator(object):
    PATH_GENERATED_JSON = "./generated_functions.json"
    PATH_GENERATED_MARKDOWN = "../docs/modules.md"
    # A source file in the tm module
    SEARCH_DOCS_TM_FILE = "tm_load.c"

    # Contains the output until it should be written to disk
    markdown_string = ""
    path_docs = ""

    def execute(self):
        path_kamctl = self.find("kamctl", "/")

        # Obtain the KEMI function list through KAMCTL RPC
        failed = os.system(path_kamctl + " rpc app_python.api_list > " + self.PATH_GENERATED_JSON)

        if failed != 0:
            print "ERR: Failed to execute KAMCTL"
            exit()

        functions_raw = json.load(open(self.PATH_GENERATED_JSON))

        # Validate that we got some methods back. 155 is an arbitrary large number.
        if functions_raw["result"]["msize"] < 155:
            print "ERR: Invalid JSON RPC response"
            exit()

        functions_parsed = self.parse_function_list(functions_raw["result"]["methods"])
        self.output_markdown(functions_parsed)

        print "Markdown doc created successfully at " + self.PATH_GENERATED_MARKDOWN

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def parse_function_list(self, functions):
        data = {}

        for elem in functions:
            props = elem["func"]
            module = props["module"]

            # The core and hdr submodule are documented in a different section
            # TODO: What about the pvx module?
            if module == "" or module == "hdr":
                continue

            if module not in data:
                data[module] = []

            data[module].append({"name": props["name"], "return": props["ret"], "params": props["params"]})

        return data

    def output_markdown(self, data):
        self.markdown_header()

        for key in sorted(data):
            methods = data[key]
            methods = sorted(methods, key = lambda k: k['name'])

            self.markdown_section_heading(key)
            self.markdown_section_content(key, methods)
            self.markdown_write()

        return True

    def markdown_header(self):
        self.markdown_string += "<!-- This file is auto-generated. Any manual modifications will be deleted -->\n"'' \
        # TODO: Move the below markdown to a file in ../docs/modules/something.md
        self.markdown_string += "# KEMI Module Functions #\n"
        self.markdown_string += "The following sections lists all exported KEMI functions. More information regarding the function can be found by clicking the KEMI declaration which will take you the original modules documentation. \n"
        return True

    def markdown_section_heading(self, heading):
        self.markdown_string += "## " + heading + " ##\n"
        # TODO: Lookup if a file such as ../docs/modules/module.header.md exists and if so inject the markdown here
        return True

    def markdown_section_content(self, module, methods):
        module_prefix = module + "."

        for value in methods:
            self.markdown_string += "#### KSR." + module_prefix + value["name"] + "() ####\n"

            # Sanitize the return values
            if value["return"] == "none":
                return_value = "void"
            else:
                return_value = value["return"]

            # Sanitize the parameter values
            if value["params"] == "none":
                params_value = ""
            else:
                params_value = value["params"]

            docs_params = self.generate_param_definitions(params_value, module, value["name"])

            # Generate the output string for the markdown page
            self.markdown_string += "KEMI declaration: " "<a target='_blank' href='/docs/modules/devel/modules/" + module + ".html#" \
                                    + module + ".f." + value["name"] + "'> `" + return_value + " " + value["name"] \
                                    + "(" + params_value + ")` </a> \n\n"

            # If we found a definition in the Docs let's present it as well
            if params_value != docs_params:
                self.markdown_string += "Docs declaration: `" + return_value + " " + value[
                    "name"] + "(" + docs_params + ")`\n"

            # TODO: Lookup if a file such as ../docs/modules/module.function.md exists and if so inject the markdown here
        return True

    def markdown_write(self):
        f = open(self.PATH_GENERATED_MARKDOWN, "w")
        f.write(self.markdown_string)
        f.close()
        return True

    def generate_param_definitions(self, params_kemi, module, function):
        if params_kemi == "":
            return ""

        # print params_kemi, module, function
        params_original = self.find_function_parameters(module, function)

        if params_original is None:
            return params_kemi

        # Remove redundant information
        if params_original == "str" or params_original == "str" or params_original == "int" or params_original == "integer" or params_original == "param":
            return ""

        return params_original

    def find_function_parameters(self, module, function):
        path_modules = self.locate_docs_path()
        path_readme = path_modules + module + "/README"

        if not os.path.isfile(path_readme):
            print "ERR: Could not find README for module: " + module
            return None

        with open(path_readme) as f:
            content = f.readlines()

        match = False

        for line in content:
            if line.find(function + "(") >= 0:
                match = True
                break
            elif line.find(function + " (") >= 0:
                match = True
                break

        if not match:
            print "ERR: Could not find definition for function: " + module + "." + function
            return None

        # Get all content between parenthesises
        params = line[line.find("(") + 1:line.find(")")]
        if params == "":
            return None

        return params

    def locate_docs_path(self):
        if self.path_docs == "":
            # We look for a file in the Kamailio source and work our way backwards from there
            path = self.find(self.SEARCH_DOCS_TM_FILE, "/")
            if path:
                strip_path = "tm/" + self.SEARCH_DOCS_TM_FILE
                path = path[:-len(strip_path)]
                self.path_docs = path
                return path
            else:
                print "ERR: Could not find the path to the Kamailio source"
                exit()
        else:
            return self.path_docs


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    fgen = ModuleDocGenerator()
    fgen.execute()
