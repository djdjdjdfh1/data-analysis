# 여러 그래프
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('./Pandas/score.xlsx')

fig, axs = plt.subplot(2,2, figSize=(15,10))
fig.suptitle('여러 그래프')

axs[0,0].bar(df['이름'], df['국어'], label='국어점수')
axs[0,0].set_title('첫번쨰 그래프')
axs[0,0].legend()
axs[0,0].set(xlabel='이름', ylabel='점수')
axs[0,0].set_facecolor('lightgray')

axs[0,1].bar(df['이름'], df['수학'], label='수학점수')
axs[0,1].bar(df['이름'], df['영어'], label='영어점수')
axs[0,1].set_title('두번째 그래프')
axs[0,1].legend()

axs[1,0].barh(df['이름'], df['과학'], label='과학점수')

axs[1,1].bar(df['이름'], df['과학'], label='과학점수')