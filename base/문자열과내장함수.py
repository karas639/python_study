'''문자열과 내장함수'''

'''
'''

msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #문자하나하나를 인덱스로 접근이 가
print(tmp.find('I'))
print(tmp.count('T'))
print(msg)
print(msg[:2])
print(msg[:3])
print(msg[3:5])
print("==================")

print(len(msg))
for i in range(len(msg)): #i는 0부터 9까지 돈다
    print(msg[i], end=' ')
print()


for x in msg:
    print(x, end=' ')
print()

msg1="dongwook KIM"
for x in range(len(msg1)):
    print(msg1[x], end=' ')
print()

for x in msg:
    if x.isupper(): #x가 대문자이면 참(isupper), 반대로 소문자 참은 islower
        print(x, end='')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): #문자열에 대해 알파벳만 출
        print(x, end='')
print()

tmp='AZ'
# Ascii 넘버 확인 - ord

for x in tmp:
    print(ord(x)) #ord가 아스키넘버를 출력하는 것
#A의 아스키넘버는 65
#Z의 아스키넘버는 90


tmp1=(tmp.lower())
print(tmp1)

for x in tmp1:
    print(ord(x))

#아스키넘버에 해당되는 문자를 출력 ord와 반대 -> chr
tmp=66
print(chr(tmp))
