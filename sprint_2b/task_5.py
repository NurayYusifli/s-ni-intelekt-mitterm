# 5) s1-dən 25-dən böyük elementləri seçin

import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s1.index =['w', 'x', 'y', 'z']
n = s1[s1 > 25]
print(n)