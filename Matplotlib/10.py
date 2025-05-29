import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Others']

plt.pie(values, labels=labels, autopct='%.1f', startangle=90, wedgeprops={'width': 0.6})
plt.show()