# 8) df1-ə ('r1', 'r2') sətir və ('c1', 'c2') sütun adlarını təyin edin

import pandas as pd
a = ((1, 2), (3, 4))
df1 = pd.DataFrame(a)
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print(df1)