# 11) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin

import pandas as pd
a = {'A': [1, 2], 'B': [3, 4]}
df2 = pd.DataFrame(a)
print(df2)
print(df2.loc[df2['A'] > 1])