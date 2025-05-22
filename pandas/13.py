# 함수 적용
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')

def add_cm(height):
    return  str(height) + 'cm'

df['키'] = df['키'].apply(add_cm)
print(df)

def capitalize_name(lang):
    if pd.notnull(lang):
        return lang.capitalize()
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize_name)
print(df)
# print(df.groupby('학교').mean())
# print(df.groupby('학교').size())