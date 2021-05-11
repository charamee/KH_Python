from ntpath import sep

subject=['java','javascript','python']

for i in subject:
    print(i, end=' ') #end 공백으로 옆으로 출력 
else:
    #반복문에서의 else는 반복문이 정상 종료 되었을때 실행된다 
    print('재밌다..')
    
for i in range(1,100):
    print(i, end=' ')
print()
for i in range(10,0,-1):
    print(i,end='')
print()
for i in range(1,10,2):
    print(i, end=' ')
print()

print('----------')
print('<구구단>')
for i in range(2,10):
    print('<<'+str(i)+'단>>')
    for j in range(1,10):
        #print(str(i)+'*'+str(j)+'='+str(i*j))
        print(i,'*',j,'=',i*j,sep=' ')
    print()














