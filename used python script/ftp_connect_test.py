import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.9.131",21))
ans = s.recv(1024)
print (ans)
