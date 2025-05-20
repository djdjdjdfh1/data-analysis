# 데이터 선택 (조건)
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df['키'] >= 185)
filt = df['키'] >= 185
print(df[~filt]) # filt를 역으로 적용

print(df.loc[df['키'] >= 185, ['이름', '수학', '과학']]) # loc를 사용하여 조건에 맞는 데이터 선택

print(df.loc[(df['키'] >= 185) & (df['수학'] >= 90), ['이름', '수학', '과학']]) # loc를 사용하여 조건에 맞는 데이터 선택
print(df.loc[(df['키'] >= 185) | (df['학교'] == '북산고')]) # loc를 사용하여 조건에 맞는 데이터 선택
filt = df['이름'].str.startswith('송')
print(df[filt])
filt = df['이름'].str.contains('태')
print(df[~filt])

langs = ['Python', 'Java']
filt = df['SW특기'].isin(langs)
print(df[filt])
print(df['SW특기'].str.contains('Java', na=True))
