import pandas as pd

a = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(a)

# 4) s2-dən 'q' indeksli elementi seçin
n = s2['q']
print(n)