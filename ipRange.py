baseAddress = "192.168.0."

hostAddresses = range(20)

ipRange = []

for i in hostAddresses:
    ipRange.append(baseAddress+str(i))
    
for ipAddr in ipRange:
    print ipAddr
