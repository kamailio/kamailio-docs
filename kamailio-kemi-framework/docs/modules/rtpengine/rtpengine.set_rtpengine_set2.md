This function is the sibling function to [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set). The original module function is declared as
`set_rtpengine_set(setid[, setid])`.

In KEMI set_rtpengine_set() takes only the first parameter and set_rtpengine_set2() allows for the second optional parameter to be passed.

```
KSR.rtpengine.set_rtpengine_set(2, 1);
KSR.rtpengine.rtpengine_offer();
```

Please review the documentation for [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set) for more information.