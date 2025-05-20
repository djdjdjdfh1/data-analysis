# 데이터 정렬
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df.sort_values('키', ascending=False)) # 키를 기준으로 내림차순 정렬
print(df.sort_values(['수학', '영어'], ascending=[True, False])) # 수학 오름차순, 영어 내림차순 정렬