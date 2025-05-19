# Pandas
import pandas as pd
# 1. Series
temp = pd.Series([-20, -10, 10, 20])
print(temp)

temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
print(temp['Jan'])
