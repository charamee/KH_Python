#pip install numpy  -> 수치해석 
#pip install matplotlin -> 그래프( 시각화) 

#import <module_name> as <alias>
import numpy as np 
import matplotlib.pyplot as plt


def plt01():
    x = np.arange(0,11)
    y= x
    #print(x)
    
    plt.plot(x,y)
    
    plt.xlabel('x')
    plt.xlabel('y')
    # 범례 
    plt.legend(['y=x'])
    
    plt.show()
    
    

    
    
plt01()