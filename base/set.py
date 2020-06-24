#set , 값만으로 이루어진 딕셔너리
a = {1, 1, 2 ,3 ,3 ,4 ,1 ,5}
print(a)
#print(a[0])

a = {}


print("------------------------")
a = [1, 1, 2 ,3 ,3 ,4 ,1 ,5]
print(a)

b = set(a)
print(b)

a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print(a.issubset(b)) # 부분집합 


