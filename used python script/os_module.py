import sys
import os
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print ('[-] '+ str(filename) + 'does not exist.')
        exit(0)

    if not os.access(filename, os.R_OK):
        print ('[-] ' + str(filename) + 'access denied.')
        exit(0)
    print ('[+] Reading Vulnerabilities From: ' + str(filename))
