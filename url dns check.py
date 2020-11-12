from os import listdir
from os.path import isfile, join

import os
import subprocess

#a = input("enter :")

input_path=input("enter path: ")
#path = listdir(input_path)

input_file = input("filename: ")


# open 한 상태에서 subprocess 사용 시 에러?
'''
file = open(input_path+input_file, 'r')
print(file)
lines = file.readline()
'''
file = input_path+input_file
file1 = open(file, 'r')
lines = file1.readline()
print(file1)
#-----------------------------------------
print(lines)

#for x in lines:
# 윈도우에서 명령어 직접 실행
#    os.system('ping ' +x)
#명령 실행 결과를 0,1로 반환
'''
    result_call = subprocess.call('ping' +x, shell=True)
    print(result_call)
'''
# 실행 결과를 stdout
for x in lines:
    #result_sub = subprocess.run(["nslookup", x], shell=True, capture_output=True, encoding='utf-8')
    result_sub = subprocess.check_output(["nslookup", lines], shell=True, universal_newlines=True)
    #result_sub = subprocess.check_output(["nslookup", x], shell=True)
    print(result_sub)
    type(result_sub)

