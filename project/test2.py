# 출생아 수 
import pandas as pd
df = pd.read_excel('./project/506101_20250530203900136_excel.xlsx', skiprows=2,nrows=2, index_col=0)
# print(df.iloc[0])

# 데이터 시각화
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15

plt.plot(df.index, df.iloc[0])
plt.show()