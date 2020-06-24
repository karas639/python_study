# fastcampus
# list
'''a = [0, 1, 2, 3, 4, 10, 100, 200, 300]
print(a[0])
print(a[4])
'''

# dictionary, 인덱스가 없음

a = {'Korea': 'Seoul',
     'Canada' : 'Ottawa',
     'USA': 'Washington D.C'}

print(a)
#print(a[0]) #인덱스가 없기 때문에 에러남

b = {}
print(type(a))
print(type(b))

b = {0:1, 1:6, 7:9, 8:10}
print(b[0]) #b[]안에오는 숫자는 인데스가 아니라 키 값이다. 즉, 0,1,7,8을 제외한 키값의 숫자를
#입력하면 에러가 발생

#print(b[2]) #2는 키값이 없기 때문에 에러가 발

#  키 값 추가
a['Japan'] = 'Tokyo'
a['China'] = 'Beijing'

print(a)

# 키 값은 해쉬값으로 저장되어 동일한 키값은 존재할 수 없다.
# 존재하는 키에 새로운 값을 넣으면 덮어씌워진다.

a = {'a':1, 'b':2, 'c':3}
b = {'a':2, 'd':4, 'e':5}
# 위와 같은 경우 동일 키 값에 대해서는 업데이트가 되며 나머지 중복되지 않는 키값들은 병합
a.update(b)
print(a)

a.pop('b')
print(a)

c = 100
print(c)

del c
#print(c)
print(a)
print(a['c'])

#dict 초기화
#a.clear()
print(a)

#in : 키값 존재 확인
b = [1, 2, 3, 4, 5, 6, 7, 9, 10, 100]
a = {'a':1, 'b':2, 'c':3}
print(100 in b)
print('b' in a)

#value 접근
a['b']
print("===========")
a.get('d') # get을 하면 프로그램이 죽지 않음
print(a.get('d'))

