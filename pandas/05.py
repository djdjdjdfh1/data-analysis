# 데이터 확인
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

# 데이터 프레임 확인
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
print(df.values)
print(df.columns)
print(df.shape)
print(df.info)
print(df['키'].describe())
print(df['키'].min())
print(df['키'].max())
print(df['키'].nlargest(3))
print(df['키'].mean())
print(df['SW특기'].count())