import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./Pandas/score.xlsx')
print(df)
plt.plot(df['지원번호'], df['키'])
plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()