# lamda 파라미터 : 리턴될 값 

hap01 = lambda a,b: a+b 
print(hap01(10,20))

gob = lambda a,b: a*b
print((gob(10,20)))

hap02 = lambda a,b,c: a+b+c
print((hap02(10,20,30)))

a=[(1,'one',9),(2,'two',8),(3,'three',7),(4,'four',6)]
a.sort(key=lambda a:a[0])
print(a)

min01 = (lambda x,y:x if x<y else y)(11,22) # 참일때if 조건 else 거짓  
print(min01)

#min02 = (lambda x,y:x if x<y else y)  
#print(min02(11,22) -> 호출할때 값을 넣어주어도 된다 

min02 = (lambda x,y:x if x<y else y)(22,10) # 참일때if 조건 else 거짓  
print(min02)

b = lambda x:(lambda newx: x+ newx)
print(b(100)(90))

#c = lambda newx: 100 + newx
c=b(100)
print(c)
# d = 100+90 
d=c(90)
print(d)



#1~100 사이에서의 5의 배수 출력
#0이면 거짓 나머지는 참을 리턴한다.  
e = lambda x:bool(x%5)
#print(e(9))
five=[i for i in range(1,100) if not e(i)]
print(five)

#None == null 
f=lambda x: x if(x%5 != 0) else None
res=[i for i in range(1,100) if not f(i)]
print(res)


result = [i for i in range(1,100) if not (lambda x :x if (x%5 !=0) else None)(i)]
print(result)













