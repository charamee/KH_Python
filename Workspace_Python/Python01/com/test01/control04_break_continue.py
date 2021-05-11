
i=1
while i <=10:
    if i>5:
        break # break로 멈추면 정상종료로 인식하지 않아서 else 미출력
    print(i)
    i+=1
else:
    print('i',i,sep='=')
    
for i in range(1,10):
    if i%2 ==0:
        continue
    print(i)
else:
    print('i',i,sep='=')