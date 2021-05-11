n=input('숫자를 입력하세요:')
lst=list()
a,b=0,1
while a<int(n):
    lst.append(a)
    a,b = b, a+b
print(lst)