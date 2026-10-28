# tool to generate the modules.md content
#


import copy
import fnmatch
import re
import string
import sys
from pathlib import Path

KAMWEBURL = "https://kamailio.org"

MODMAPNAME = {
    "pvx": "pv",
    "kx": "kemi",
}

MODMAPFUNC = {
    "alias_db": {
        "lookup": "alias_db_lookup",
        "lookup_ex": "alias_db_lookup",
    },
    "app_jsdt": {
        "dofile": "jsdt_dofile",
        "dostring": "jsdt_dostring",
        "run": "jsdt_run",
    },
}
MARKDOWN_PUNT = string.punctuation.replace("_", "")


def replace_punctuation(text, replace):
    return re.sub("[%s]" % re.escape(MARKDOWN_PUNT), replace, text)


class DocGenerator(object):
    PATH_MODULES_DOCS = Path("../docs/modules/")
    markdown_string = ""

    def read_file_to_string(self, filename):
        path = self.PATH_MODULES_DOCS / filename
        if path.is_file():
            with path.open("r") as myfile:
                return myfile.read() + "\n"
        return ""

    def markdown_header(self):
        self.markdown_string += self.read_file_to_string("header.md")

    def markdown_write(self, msg):
        parent = self.PATH_GENERATED_MARKDOWN.parent
        parent.mkdir(mode=0o776, parents=True, exist_ok=True)
        with open(self.PATH_GENERATED_MARKDOWN, "w") as f:
            f.write(self.markdown_string.removesuffix("\n\n") + "\n")
        print(f"{msg} {self.PATH_GENERATED_MARKDOWN}")


class ModuleDocGenerator(DocGenerator):
    module = "unknown"
    output = ""

    def __init__(self, module, methods):
        self.module = module
        self.methods = methods
        self.PATH_GENERATED_MARKDOWN = (
            self.PATH_MODULES_DOCS / f"{module}" / f"{module}.md"
        )

    def execute(self):
        self.markdown_section_heading()
        self.markdown_section_content()
        self.markdown_write("Markdown doc created successfully at")
        return self.output

    def markdown_section_heading(self):
        self.markdown_string += f"# {self.module} #\n\n"
        kmodname = MODMAPNAME[self.module] if self.module in MODMAPNAME else self.module
        tdesc = f"kamailio.cfg::module::{kmodname}.html"
        turl = f"{KAMWEBURL}/docs/modules/devel/modules/{kmodname}.html"
        self.markdown_string += f"* 📖[{tdesc}]({turl})\n\n"
        self.markdown_string += self.read_file_to_string(
            f"{self.module}/{self.module}.header.md"
        )
        # one header level lower for index
        self.output = copy.deepcopy(self.markdown_string.replace("#", "##"))

    def markdown_section_content(self):
        if self.module == "core":
            module_prefix = ""
        else:
            module_prefix = self.module + "."

        kmodtoc = "Exported functions:\n\n"
        kmodtoc_out = "Exported functions:\n\n"
        kmodtext = ""
        kmodname = MODMAPNAME[self.module] if self.module in MODMAPNAME else self.module

        for value in self.methods:
            thdr = f"KSR.{module_prefix}{value['name']}"
            tlink = replace_punctuation(thdr, "").lower()
            tdesc = f"KSR.{module_prefix}{value['name']}\\(\\)"
            turl_ext = f"modules/{self.module}.md#{tlink}"
            kmodtoc += f"* [{tdesc}](#{tlink})\n"
            kmodtoc_out += f"* [{tdesc}]({turl_ext})\n"
            kmodtext += f"## {thdr} ##\n\n"

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

            # Generate the output string for the markdown page
            kmodtext += f"```cpp\n{return_value} KSR.{module_prefix}{value['name']}({params_value});\n```\n\n"
            kfuncname = value["name"]
            if kmodname in MODMAPFUNC:
                if value["name"] in MODMAPFUNC[kmodname]:
                    kfuncname = MODMAPFUNC[kmodname][value["name"]]
            tdesc = f"kamailio.cfg::function::{kfuncname}\\(\\)"
            turl = f"{KAMWEBURL}/docs/modules/devel/modules/{kmodname}.html#{kmodname}.f.{kfuncname}"
            kmodtext += f"* 📖[{tdesc}]({turl})\n\n"

            func_doc = self.read_file_to_string(
                f"{self.module}/{self.module}.header.md"
            ).strip()
            if len(func_doc) > 0:
                kmodtext += func_doc + "\n\n"
        self.markdown_string += kmodtoc + "\n" + kmodtext
        self.output += kmodtoc_out + "\n"


class IndexDocGenerator(DocGenerator):
    PATH_GENERATED_MARKDOWN = Path("../docs/modules.md")

    # Contains the output until it should be written to disk
    markdown_string = ""

    def execute(self, data):
        # Validate that we got some methods back. 155 is an arbitrary large number.
        if len(data) < 1:
            print("ERR: Invalid data")
            sys.exit(1)
        functions_parsed = self.parse_function_list(data)
        self.output_markdown(functions_parsed)

    def parse_function_list(self, functions):
        data = {}

        for elem in functions:
            module = elem["module"]

            # TODO: What about the hdr, pv, x sub-module?
            if module == "":
                module = "core"

            if module not in data:
                data[module] = []

            data[module].append(
                {"name": elem["name"], "return": elem["ret"], "params": elem["params"]}
            )

        return data

    def output_markdown(self, data):
        self.markdown_header()

        for key in sorted(data):
            methods = data[key]
            # Sort the functions by name alphabetically
            methods = sorted(methods, key=lambda k: k["name"])
            mg = ModuleDocGenerator(key, methods)
            self.markdown_string += mg.execute()
        self.markdown_write("Markdown doc index created successfully at")


class KemiFileExportParser(object):
    # These functions are created by a macro so makes the parsing somewhat tricky,
    # for now they are statically defined
    macro_functions = {
        "t_set_auto_inv_100": "int state",
        "t_set_disable_6xx": "int state",
        "t_set_disable_failover": "int state",
        "t_set_no_e2e_cancel_reason": "int state",
        "t_set_disable_internal_reply": "int state",
    }

    # These files export the KEMI functions in a special way so we map them manually
    # TODO: Discuss with @miconda if core/HDR/pv/x should be added as well or not
    special_exports = [
        # {"filename": "kemi.c", "export": "_sr_kemi_core", "folder": "/core/"},
        # {"filename": "kemi.c", "export": "_sr_kemi_hdr", "folder": "/core/"},
        # {"filename": "app_lua_mod.c", "export": "sr_kemi_app_lua_rpc_exports", "folder": "/modules/app_lua/"}
    ]

    def generate_kemi_export_list(self, source_path):
        files = self.list_c_files_in_directory(source_path)
        lists = []

        for file in files:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()

            export_name = self.find_c_file_kemi_export(file, lines)
            if export_name:
                export_functions = self.extract_c_file_kemi_export_lines(
                    file, lines, export_name
                )
                lists = lists + export_functions
                print(
                    "Found ", len(export_functions), "functions", "Total:", len(lists)
                )

        # Handle some special files separately
        for elem in self.special_exports:
            file = source_path + elem["folder"] + elem["filename"]
            with open(file) as f:
                lines = f.readlines()
            lists = lists + self.extract_c_file_kemi_export_lines(
                file, lines, elem["export"]
            )

        return lists

    def find_c_file_kemi_export(self, filename, lines):
        param = None

        for line in lines:
            if line.find("sr_kemi_modules_add") >= 0:
                line = line.lstrip(" ")
                line = line.lstrip("\t")
                if line.find("sr_kemi_modules_add") == 0:
                    param = line[line.find("(") + 1 : line.find(")")]
                    print("INFO: ---- Found export", filename, param)
                    break
                else:
                    if line != "int sr_kemi_modules_add(sr_kemi_t *klist)\n":
                        print("ERR: Possible error at line: ", filename, line)
                        sys.exit(1)

        return param

    def extract_c_file_kemi_export_lines(self, filename, lines, export_name):
        list_functions = []
        find_start = True

        for line in lines:
            if find_start and line.find("static sr_kemi_t " + export_name + "[]") >= 0:
                find_start = False
            elif not find_start:
                if line.find("};") >= 0:
                    break
                line = line.lstrip(" \t")
                line = line.rstrip()
                list_functions.append(line)

        if len(list_functions) < 1:
            print("ERR: Couldn't parse file for exported functions: ", export_name)
            sys.exit(1)

        parsed_list = self.parse_kemi_export_c_lines(filename, list_functions)

        return parsed_list

    def parse_kemi_export_c_lines(self, filename, lines):
        elements = []
        function_lines = []
        temp_function = ""

        # We look for str_init which would be the start of each exported function
        for line in lines:
            if line.find("str_init") >= 0:
                if temp_function != "":
                    function_lines.append(temp_function)
                    temp_function = ""
            temp_function += line

        if temp_function != "":
            function_lines.append(temp_function)

        # Now we parse each exported function to extract its declaration
        for func in function_lines:
            function_lines_split = func.split(",{")

            if len(function_lines_split) < 2:
                print("ERR: Incorrect function line", func)
                sys.exit(1)

            declarations = function_lines_split[0].split(",")
            params = function_lines_split[1]

            # Extract the content from the definitions
            val_module = declarations[0]
            val_module = val_module[val_module.find('("') + 2 : val_module.find('")')]
            val_function = declarations[1]
            val_function = val_function[
                val_function.find('("') + 2 : val_function.find('")')
            ]

            if declarations[2] == "SR_KEMIP_INT":
                val_return = "int"
            elif declarations[2] == "SR_KEMIP_STR":
                val_return = "string"
            elif declarations[2] == "SR_KEMIP_NONE":
                val_return = "void"
            elif declarations[2] == "SR_KEMIP_BOOL":
                val_return = "bool"
            elif declarations[2] == "SR_KEMIP_XVAL":
                val_return = "xval"
            else:
                print("ERR: Invalid return value", declarations[2], func)
                sys.exit(1)

            val_c_function = declarations[3].strip()

            # Count how many parameters the KEMI C function expects
            val_params = []
            itr = 0
            for val in params.rstrip("},").split(","):
                itr += 1
                # KEMI function has a maximum of 6 params
                if itr > 6:
                    break
                pm = val.strip()
                if pm == "SR_KEMIP_INT":
                    val_params.append("int")
                elif pm == "SR_KEMIP_STR":
                    val_params.append("str")
                elif pm == "SR_KEMIP_NONE":
                    continue
                else:
                    print("Invalid return value", declarations[2], func)
                    sys.exit(1)

            if itr != 6:
                print("ERR: Couldn't iterate the params: ", params)
                sys.exit(1)

            param_string = self.find_c_function_params(
                filename, val_c_function, val_return
            )
            param_string = self.prettify_params_list(
                val_function, param_string, val_params
            )

            elements.append(
                {
                    "module": val_module,
                    "name": val_function,
                    "ret": val_return,
                    "params": param_string,
                }
            )

        return elements

    def prettify_params_list(self, function_name, function_declaration, kemi_types):
        # Validate the quantity and types of declaration vs export
        if function_declaration == "" and len(kemi_types) == 0:
            return ""

        params = function_declaration.split(",")

        if params[0].find("sip_msg_t") >= 0 or params[0].find("struct sip_msg") >= 0:
            params.pop(0)

        if len(params) != len(kemi_types):
            print(
                "ERR: Mismatching quantity of params. Declaration for",
                function_name,
                ":",
                function_declaration,
                "KEMI:",
                kemi_types,
            )
            sys.exit(1)

        for declared, type in zip(params, kemi_types):
            declared = declared.replace("*", "")
            declared = declared.strip().split(" ")[0]
            if declared != type:
                print(
                    "ERR: Mismatching type of params for",
                    function_name,
                    ":",
                    function_declaration,
                    " | ",
                    kemi_types,
                    " | Declared: ",
                    declared,
                    " Type: ",
                    type,
                )
                sys.exit(1)

        param_string = ""

        for param in params:
            param = param.strip()
            param = param.replace("*", "")
            if param[:3] == "str":
                temp = param.split(" ")
                param = "str" + ' "' + temp[1] + '"'
            param_string += param + ", "

        # Clean up the presentation of the params
        param_string = param_string.rstrip(", ")
        return param_string

    def find_c_function_params(self, filename, function_name, return_type):
        # First we try with the same file to find the declaration
        param_string = self.search_file_for_function_declaration(
            filename, function_name, return_type
        )
        # If we couldn't find it, let's try all files in the same folder as the first file
        if param_string:
            return param_string
        else:
            files = self.list_c_files_in_directory(filename.parent)
            for file in files:
                param_string = self.search_file_for_function_declaration(
                    file, function_name, return_type
                )
                if param_string:
                    return param_string

        if function_name in self.macro_functions:
            return self.macro_functions[function_name]

        print(
            "ERR: Couldn't find the function declaration",
            filename,
            function_name,
            return_type,
        )
        sys.exit(1)

    def search_file_for_function_declaration(
        self, filename, function_name, return_type
    ):
        # print "Searching file", filename, "for", function_name
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        param_string = None
        found = False
        temp_string = ""
        return_match = return_type

        # KEMI has some magic where most functions actually return INTs but KEMI maps them to void/bool
        if return_type == "void" or return_type == "bool":
            return_match = "int"

        if return_type == "xval":
            return_match = r"sr_kemi_xval_t([ \t])*\*"

        # Look for declarations in format:    static? return_type function_name(
        r = re.compile(
            r"^(?:static )?" + return_match + r"[ \t]*(" + function_name + r")[ \t]*\("
        )
        for line in lines:
            m = r.match(line)
            if m:
                found = True
            if found:
                temp_string += line
                if line.find("{") >= 0:
                    param_string = temp_string[
                        temp_string.find("(") + 1 : temp_string.find(")")
                    ]
                    break

        return param_string

    def list_c_files_in_directory(self, path):
        matches = []
        for root, dirnames, filenames in path.walk():
            for filename in fnmatch.filter(filenames, "*.c"):
                matches.append(root / filename)
        return matches


if __name__ == "__main__":
    try:
        kam_src = Path(sys.argv[1])
        if not kam_src.is_dir():
            raise Exception("Not a valid directory")
    except Exception:
        print(
            "Please provide the path to the Kamailio src folder as the first argument"
        )
        sys.exit(1)

    print("Parsing the source")
    parser = KemiFileExportParser()
    data = parser.generate_kemi_export_list(kam_src)
    fgen = IndexDocGenerator()
    fgen.execute(data)
    print("Done")
