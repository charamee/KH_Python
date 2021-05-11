#tuple : ( )
#수정 불가능한 list
#생성자
a=tuple()
print(a)
#a.append(1)
#print(a)
b=tuple([1,2,'3'])
print(b)


# {( ) 사
c=(1,2,3,4,5)
print(c)
#c[1] = 'two'
#print(c)

d=tuple(range(3,6))
print(d)
print(c+d)

#tuple을 list로
e=list(d)
print(e)
e.append(6)
print(e)
#list를 tuple로
f= tuple(e)
print(f)
#f.append(6)

#unpacking
g,h,i,j = f
print(g)
print(h)
print(i)
print(j)


lst = list(range(1,10))
print(lst)
print(lst[4:7])

i=1
while i<=10:
    if i>5:
        break
    print(i,end='')
    i+=1
else:
        print('i=', str(i))



for i in range(1,10):
    if i% 2 ==0:
        continue
    print(i)
else:
        print('i=',i)
        
























