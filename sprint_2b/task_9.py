# 9) Python: {'A': [1, 2], 'B': [3, 4]} dictionary-dən df2 yaradın
#     R: list(A = c(1, 2), B = c(3, 4)) listindən df2 yaradın 

import pandas as pd
a = {'A': [1, 2], 'B': [3, 4]}
df2 = pd.DataFrame(a)
print(df2)