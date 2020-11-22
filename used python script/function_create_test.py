import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
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
    return


def main():
    ip1 = '172.53.250.211'
    ip2 = '172.52.250.110'
    ip3 = '172.50.1.67'
    port = 21
    banner1 = retBanner(ip1, port)

    if banner1:
        print ("[+] " + ip1 + ": " + str(banner1.strip('\n'))
#        checkVulns(banner1)

    #banner2 = retBanner(ip2, port)

    #if banner2:
     #   print ('[+] ' + ip2 + ': ' + str(banner2.strip('\n'))
      #  checkVulns(banner2)
    #banner3 = retBanner(ip3, port)
    #if banner3:
     #   print ('[+] ' + ip3 + ': ' + str(banner3.strip('\n'))
      #  checkVulns(banner3)

if __name__ == '__main__':
    #main()
