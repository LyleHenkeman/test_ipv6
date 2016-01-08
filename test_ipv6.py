ipv6testhost = "www.google.com"

import socket
import urllib
import sys

# to avoid errors like the below because of using the literal ipv6 instead of domain name
# ssl.CertificateError: hostname '2a00:1450:4013:c01::66' doesn't match either of '*.google.com', '*.android.com', 
opt_out_of_certificate_verification = True
if opt_out_of_certificate_verification:
    try:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
    except:
        pass

print "ipv6testhost is", ipv6testhost

hostipv6info = socket.getaddrinfo(ipv6testhost, 0, socket.AF_INET6, 0, socket.IPPROTO_TCP)

for item in hostipv6info:

	try:
		af, socktype, proto, canonname, sa = item
		print "canonname", sa
		sock = socket.socket(af, socktype, proto)
		sock.settimeout(2)  # 2 second timeout
		sock.connect(sa[0:2])
		sock.close()
		print('socket connect: IPv6 test successful. Enabling IPv6')

	except socket.error:
		print('socket connect: Cannot reach IPv6 test host. Disabling IPv6')

	except:
		print('socket connect: Problem during IPv6 connect. Disabling IPv6. Reason: %s', sys.exc_info()[0])


	ipv6address = item[4][0]

	url = "http://[" + ipv6address + "]/"
	#print "url is", url
	try:
		f = urllib.urlopen(url)
		print "Yes, IPv6 connection via HTTP", url
		f.read()
	except:
		print "No IPv6 connection via HTTP", url


	url = "https://[" + ipv6address + "]/"
	#print "url is", url
	try:
		f = urllib.urlopen(url)
		print "Yes, IPv6 connection via HTTPS", url
		f.read()
	except:
		print "No IPv6 connection via HTTPS", url

print "Done"

