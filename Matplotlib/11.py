# 산점도 그래프
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./Pandas/score.xlsx')
df['학년'] = [3,3,2,1,2,3,3,2]
plt.scatter(df['영어'], df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
sizes = np.random.rand(8) * 500
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], alpha=0.5, cmap='viridis')

plt.show()