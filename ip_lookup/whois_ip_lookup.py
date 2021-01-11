import re #정규표현식 모듈
import urllib.request
import json

#file을 이용하여 입력값 넣기
file_in = open("ip.txt", 'r')
file_out = open("ip_result.txt", 'w')

#p = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/)?$")
while True:
    line = file_in.readline()
    #print(line)
    p1 = re.sub("\d{1,3}(\/)?$","0",line)
    if not line:
        break
    else:
        p2 = p1.strip()
        p3 = p2+"/24"
        #print(p3)
        #print(p.match(line))

        whois_key = '2020061011345550462421'
        query = "http://whois.kisa.or.kr/openapi/ipascc.jsp?query=" + p2 + "&key="+ whois_key + "&answer=json";
        request = urllib.request.urlopen(query).read().decode("utf-8")
        #print(request.strip())
        data = re.findall('[A-Z]{1,2}',request)
        countrycode = "("+data[-1]+")"
        print(p3, countrycode)
        
            
file_in.close()
file_out.close()
