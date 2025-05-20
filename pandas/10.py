# 결측치
import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx', index_col='지원번호')
# 데이터 채우기 fillna
print(df.fillna('없음'))

df['학교'] = np.nan
print(df) 
print(df.fillna('모름'))

df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df.dropna(axis='index', how='any')) # 모든 값이 결측치인 행 삭제
df['SW특기'].fillna('확인 중', inplace=True)
print(df)