'''리스트와 내장함수(2)'''
a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a)) #리스트에 값이 몇개가 있는

for i in range(len(a)):
    print(a[i], end=' ') # i에 값을 하나하나 넣으면서 출력하는데 옆으로 출력(end)
    
print()

for x in a:
    print(x, end=' ') #위 for 문과 똑같이 출력됨
print()

for y in a:
    if y%2==1:
        print(y, end=' ')
print()


for z in enumerate(a):
    print(z)    #z가 튜플이라는 자료형으로 출력됨 (소괄호가 튜플형)

print()


b=(1,2,3,4,5)
print(b[0])
# 튜플이 리스트와 다른 것은 b[0]에 1의 값이 있는데 새로운 값을 넣고자하는 경우 에러발생
# b[0]=7 --> 실행하는 순간 에러발생, b가 리스트[] 일 경우는 가능
# print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()



#all 함수, for문이 a에 접근하여 x의 값이 될때 그 값을 60과 비교하는데,
#현재 a의 값이 해당 조건에 비교하여 참일 경우 참을 리턴,
#하나라도 거짓이면 거짓을 리턴한다


if all(60>x for x in a):    
    print("YES")
else:
    print("NO")


if all(50>x for x in a):
    print("YES")
else:
    print("NO")

    

    
