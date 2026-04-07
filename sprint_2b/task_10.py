# 10) df2-dən 'r1' sətrini seçin

import pandas as pd
a = ((1, 2), (3, 4))
df2 = pd.DataFrame(a)
df2.index = ['r1', 'r2']
# print(df2)
print(df2.loc['r1'])
