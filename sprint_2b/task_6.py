# 6) s1-də 20-dən böyük elementləri 10-a bölün 

import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s1.index =['w', 'x', 'y', 'z']
m = s1[s1 > 20]
m = m / 20
print(m)