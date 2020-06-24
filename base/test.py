"""a="student"
print(type(a))
"""
#출력방식
"""print("number")
a,b,c=1,2,3
print(a,b,c)
print("number", a,b,c)
print("====================")
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print("====================")
"""
#a,b,c=1,2,3
#print(a, end=' ')
#print(b, end=' ')
#print(c, end=' ')
"""
print("---")
d,e,f=4,5,6
print(d,e,f)
print("number :", d,e,f)
print("====")

"""

#변수입력과 연산자
'''a, b=input("숫자를 입력하세요 :").split() # 1 2 과 같이 띄어쓰기 하여 값을 입력
print(type(a)) # a와 b가 스트링 형(문자)으로 나와서 더하기가 안되고 붙여출력
c=a+b
print(a+b)
print(type(c)) # c도 역시 str형
print(c)
'''

'''a, b=input("숫자를 입력하세요 :").split()
a=int(a)
print(a)
print(type(a))
b=int(b)
print(b)
print(a+b)'''

'''
# int형으로 한번에 바꾸는 법 map, int 사용하여 정수화 시켜서 출력하기
# 연산자도 실습
a, b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b) #나누기
print(a//b) #몫
print(a%b) # a를 b로 나눈 나머지
print(a**b) #a를 b번 곱한
'''
'''
# 실수형과 정수형의 사칙연산 -> 결과는 실수형이된다?
a=4.3
b=5
c=a+b
#실수가 정수보다 넓은 범위이기 때문에 결과는 실수형으로 나온다(float형으로.)
print(c)
'''
