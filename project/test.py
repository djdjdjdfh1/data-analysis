# 인구 피라미드
import pandas as pd
df_m = pd.read_excel('./project/202501_202504_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,E:Y')
# print(df_m)
df_m.iloc[0] = df_m.iloc[0].str.replace(',', '').astype(int) 
# print(df_m.iloc[0])

df_w = pd.read_excel('./project/202501_202504_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,AB:AV')
df_w.columns = df_m.columns
df_w.iloc[0] = df_w.iloc[0].str.replace(',', '').astype(int) 
# print(df_w)
# 데이터 시각화
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 7))
plt.barh(df_m.columns, -df_m.iloc[0] // 1000, color='blue', label='남자' )
plt.barh(df_w.columns, df_w.iloc[0] // 1000, color='red', label='여자' )
plt.title('2025년 1월 인구 피라미드')
plt.show()
