# 데이터 선택 (loc row 기준)
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df.loc['1번'])
print(df.loc['5번'])
print(df.loc[['1번','2번'], '영어'])
print(df.loc[['1번','2번'], ['영어', '수학']])