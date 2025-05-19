# 6. 데이터 선택
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
# column 선택
print(df[['이름', '키']])