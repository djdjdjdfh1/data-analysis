# 범례
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y, label='Line 1', marker='o', color='blue', linestyle='None')
plt.legend(loc='upper left')
# plt.show()

plt.plot(x,y, linestyle='--')
# plt.figure(figsize=(10, 5))
# plt.show()
