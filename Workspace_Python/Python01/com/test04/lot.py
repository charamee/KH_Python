import random

def lotto():
    result = set()
    
    while len(result) <=6: # len() 안에 있는 객체의 length 
        ran = random.randint(1, 45)
        result.add(ran)
    lst = sorted(result)
    print(lst)
    

if __name__=='__main__':
    lotto()