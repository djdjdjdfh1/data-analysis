# 파일 저장
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.savefig('plot.png', dpi=100)