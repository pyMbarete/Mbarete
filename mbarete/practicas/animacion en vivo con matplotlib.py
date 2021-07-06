import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
global xData, yData

xData=[]
yData=[]

fig, ax = plt.subplots()
ax.set_xlim(0,205)
ax.set_ylim(0,12)
line,= ax.plot(0,0)
#random.randrange(10)*0.1
def animationFrame(i):
	xData.append(i)
	yData.append((1.01**i)+(random.randrange(10)*0.1))
	line.set_xdata(xData)
	line.set_ydata(yData)
	return line,
#np.arange(0,10,0.01)
print(np.arange(0,100,1))
animation = FuncAnimation(
	fig, 
	func=animationFrame, 
	frames=np.arange(0,205,1),
	interval=1
	)
plt.show()