Return values corresponding the pseudo-variables exported by TLS module, related
to TLS connection and certificates. The parameter has to be the name of the
pseudo-variable (without `$`).

Example:

```
local vPeerSubjectCn = KSR.tls.cget("tls_peer_subject_cn");
```
