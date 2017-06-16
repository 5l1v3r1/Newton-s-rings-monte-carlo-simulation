import random
import math
import matplotlib.pyplot as plt
R = 3
L = 0.2
PI = 3.1415
DARTS = 2**13
# 画个图看看
fig = plt.figure() 
axes = fig.add_subplot(111)
for I in range(1,DARTS):  
    x,y = random.uniform(-3,3),random.uniform(-3,3)
    p = (math.cos(PI*((x**2+y**2)/(R*L)+1/2)))**2
    axes.plot(x, y,'ro',markersize = p)
plt.axis('equal') # 防止图像变形

plt.show()
