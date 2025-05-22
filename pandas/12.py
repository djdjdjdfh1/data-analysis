# COlumn 수정
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df['학교'].replace({'북산고': '상북고'}, inplace=True))

df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

df['결과'] = 'Fail'
df.loc[df['총합'] > 400, '결과'] = 'PASS'
print(df)
df.drop(columns=['통합'])
df.drop(columns=['국어', '영어', '수학'])
print(df)
df.drop(index='4번')
print(df)
filt = df['수학'] < 80
print(df[filt].index)