# Matplotlib
import matplotlib 
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 12
x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)
plt.title('Line Graph Example')
plt.xlabel('X-axis', color='blue', loc='right')
plt.ylabel('Y-axis', color='red', loc='top')
plt.show()