import socket

#NX='172.52.250.55'
#EX='172.52.250.56'
#HX='172.52.250.57'
#FX='172.52.250.58'
#CM='172.52.250.59'
#DRM='172.52.250.110'

def monitor(ip, port):
    
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
#        banner = s.recv(1024)
#        return banner
    except:
        return

def port_check():
    portList = [21,22,25,80,81,445]
    if monitor(NX,(" in str(banner)):
        print ("[+] FreeFloat FTP Server is vulnerable.")
    elif ("3Com 3CDaemon FTP Server Version 2.0" in str(banner)):
        print ("[+] 3CDaemon FTP server is vulnerable.")
    elif ("Ability Server 2.34" in str(banner)):
        print ("[+] Ability Ftp Server is vulnerable.")
    elif ("Sami FTP Server 2.0.2" in str(banner)):
        print ("[+] Sami FTP Server is vulnerable.")
    else:
        print ("[-] FTP Server is not vulnerable.")
    return

def main():
    #portList = [21,22,25,80,81,111]
    for x in range(200, 255):
        ip = '172.53.250.'+str(x)
        #ip = '192.168.100.'+str(x)
        for port in portList:
            result = retBanner(ip, port)
            if result:
                print ("[+] " + str(ip) + ": " + str(port))
                checkVulns(result)

if __name__ == '__main__':
    main()
