import matplotlib.pyplot as plt

labels = ['강백호', '서태웅', '정대만']
values = [194, 192, 180]
colors = ['red', 'green', 'blue']
plt.barh(labels, values, color=colors, alpha=0.7)
plt.xlim(175,195)
plt.show()
bar = plt.bar(labels,values)
bar[0].set_hatch('/')
bar[1].set_hatch('..')
bar[2].set_hatch('x')
plt.show()