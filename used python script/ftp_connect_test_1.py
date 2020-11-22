import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("172.53.250.211",21))
ans = s.recv(1024)

s1 = socket.socket()

try:
    s1.connect(("172.53.250.212",21))
except Exception as e:
    print ("[-] Error = "+str(e))


if ("FreeFloat Ftp Server (version 1.00)" in str(ans)):
    print ("[+] FreeFloat FTP Server is vulnerable.")
elif ("3Com 3CDaemon FTP Server Version 2.0" in str(ans)):
    print ("[+] 3CDaemon FTP server is vulnerable.")
elif ("Ability Server 2.34" in str(ans)):
    print ("[+] Ability Ftp Server is vulnerable.")
elif ("Sami FTP Server 2.0.2" in str(ans)):
    print ("[+] Sami FTP Server is vulnerable.")
else:
    print ("[-] FTP Server is not vulnerable.")

#fx = socket.socket()
#fx.connect(("172.52.250.110",445))

