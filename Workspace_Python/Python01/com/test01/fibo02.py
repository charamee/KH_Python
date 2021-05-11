def fibo01(n):
    a,b = 0,1 
    
    while a<n :

        print(a,end=' ')

        a,b = b, a+b
    

def fibo02(n):
    a,b = 0,1 
    i=0
    while i<n :

        print(a,end=' ')

        a,b = b, a+b
        i+=1
    
if __name__=='__main__':
    level=input('숫자를 입력하세요 :')
    fibo01(int(level))
    print()
    fibo02(int(level))