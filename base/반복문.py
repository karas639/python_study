'''
반복문(for, while)


a=range(10)
print(list(a))

a=range(1,11)
print(list(a))


for i in range(10):
    print(i)

for x in range(10):
    print("hello")

for a in range(1,11):
    print(a)



for i in range(10, 0, -1):
    print(i)

for r in range(10, 0, -2):
    print(r)

'''

print("====================while 문===================")
'''
i=1
while i<=10:
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True: #True는 무한반복을 의미
    print(i)
    if i==10:
        break
    i+=1 #i=i+1과 동일
    


for i in range(1, 11):
    if i%2==0:
        continue  #짝수는 continue하여 print(i)를 하지 않고 지나가버림
    print(i)



for i in range(1, 11):
    print(i)
    if i>15:  #if문이 참이 될일이 없으니 else문까치 처리하여 11을 출
        break
else:
    print(112)

'''
'''

반복문을 이용한 문제 풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지 합 구하기
3) N의 약수출력하기

n=int(input())
for i in range(1, n+1):
    print(i)



n=int(input())
for i in range(1, n+1):
    if i%2==1:
        print(i)

n=int(input())
sum=0
for i in range(1, n+1):
    sum=sum+i
print(sum)
'''


n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ')

print("============")        

n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i)

        
