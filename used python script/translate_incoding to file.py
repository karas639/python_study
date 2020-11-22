from os import listdir
from os.path import isfile, join

path=input("enter path: ")
#path = './' # 다른 디렉토리에 이 스크립트를 넣는 경우 수정해서 사용
encoding_in = 'utf-8-sig'
encoding_out = 'ansi'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and '.txt' in f]

for f in onlyfiles :
    try :
        s = open(f, mode = 'r', encoding = encoding_in).read()
        print(s)
        open(f, mode = 'w', encoding = encoding_out).write(s)
        # break # 1개만 테스트해 보고 싶으면 주석 해제하고 실행
    except :
        print(f + ' has been maybe re-encoded already. passed.')

result=input("filename: ")
read_file = open(path+result, encoding='utf-8-sig')
lines = read_file.readlines()
key = "결과 :"
def export():
    for index, line in enumerate(lines):
        if key in line:
            x=print(line)
            print(x)
            #y=x.strip('결과 :')
            #print(y)
export()
