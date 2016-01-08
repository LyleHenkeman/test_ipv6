# test_ipv6
some code to test IPv6 connectivity

Example

Result with correct working IPv6:
```
$ python test_ipv6.py 
ipv6testhost is www.google.com
canonname ('2a00:1450:400c:c09::68', 443, 0, 0)
socket connect: IPv6 test successful. Enabling IPv6
Yes, IPv6 connection via HTTP http://[2a00:1450:400c:c09::68]/
Yes, IPv6 connection via HTTPS https://[2a00:1450:400c:c09::68]/
Done
```


No working IPv6:
```
$ python test_ipv6.py 
ipv6testhost is www.google.com
canonname ('2a00:1450:400c:c09::68', 443, 0, 0)
socket connect: Cannot reach IPv6 test host. Disabling IPv6
No IPv6 connection via HTTP http://[2a00:1450:400c:c09::68]/
No IPv6 connection via HTTPS https://[2a00:1450:400c:c09::68]/
Done
```
