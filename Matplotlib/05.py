import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]
# plt.plot(x, y, marker='o')
labels = ['강백호', '서태웅', '정대만']
values = [194, 192, 180]
colors = ['red', 'green', 'blue']
plt.bar(labels, values, color=colors, alpha=0.7, width=0.5)
plt.show()