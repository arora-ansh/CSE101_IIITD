import numpy as np 
from matplotlib import pyplot

def line(x,y):
	pyplot.title("graph")
	pyplot.xlabel("x-axis")
	pyplot.ylabel("y-axis")
	pyplot.subplot(1,1,1)
	pyplot.plot(x,y,"b")
	pyplot.show()

m=float(input())
c=float(input())
x=np.arange(0,11)
y=m*x+c
line(x,y)



