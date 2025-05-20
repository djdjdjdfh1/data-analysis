# 데이터 선택 (iloc)
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df.iloc[0])
print(df.iloc[4])
print(df.iloc[0:5])
print(df.iloc[0, 1]) # 0번째 위치의 1번쨰 데이터 
print(df.iloc[4, 2]) # 5번째 위치의 2번쨰 데이터
print(df.iloc[[0,1], [3,4]]) 