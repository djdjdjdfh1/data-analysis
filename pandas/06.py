# 6. 데이터 선택
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
# column 선택
print(df[['이름', '키']])

# COlumn 선택 (정수 index)
print(df.columns[0])
print(df.columns[2])
print(df[df.columns[-1]])
# 슬라이싱
print(df[['이름','키']][:3])