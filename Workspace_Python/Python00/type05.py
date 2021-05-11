#Set (집합)

#생성자
a=set(['1','2','3','4','4'])
print(a)

#생성자에 iterable 한 객체를 넣으면 set의 값으로 변환 (반복 가능한것, 순서대로 하나씩 가져오는것)
b=set('hello')
print(b)


# {} 사용
c = {'a','b','c','hello','1','2','3'}
print(c)

c.add('world')
print(c)

#합집합, 교집합
print(a.union(b))
print(a | b)

print(a.intersection(c))
print(a&c)
