# Sprint_1a task


# 1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.

a = 123
a = str(a)
print(type(a))

# 2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.

a = 19.99
a = int(a)
print(a)

# 3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.

a = "500"
a = int(a)
a = a / 2
print(a)

# 4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.

a = 8
b = 12
print(a < b)   
print(a == b)

# 5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.

x,y,z = 5,10,15
print(x < y)   
print(y < z)

# 6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.

a = 25
print(a / 4)
print(a % 4)
print(a // 4)

# 7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.

a = 3
a = a ** 4
print(a)

# 8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.

a = 75.5
a = int(a)
print(type(a))


# 9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.

n = 20 
print((n > 10) or (n < 5))
print((n > 15) and (n < 25))

# 10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.

a = "42.8"
a = float(a)
a = int(a)
print(type(a)) 



# Sprint_1b task


# 1) s = "Programming" yaradın. Uzunluğunu və ilk simvolunu çap edin.

s = "Programming" 
print(len(s))
print(s[0])

# 2) s1 = "Hello" və s2 = "World" yaradın. Onları boşluqla birləşdirin və nəticəni çap edin.

s1 = "Hello"
s2 = "World" 
print(s1 +' '+ s2)

# 3) text = "Python" yaradın. Son simvolunu çap edin.

text = "Python"
l = len(text)
print(text[l - 1])

# 4) s = "Artificial" yaradın. "Art" hissəsini ilə çıxarın və çap edin.

s = "Artificial"
print(s[0:3])

# 5) word = "Code" yaradın. Tərsinə çevirin və nəticəni çap edin.

word = "Code"
print(word[::-1])

# 6) s = "abcdefgh" yaradın. Hər ikinci simvolu alın və çap edin.

s = "abcdefgh"
print(s[::2])

# 7) text = "data" yaradın. Onu bir sətrlik kodla böyük hərflərə və kiçik hərflərə çevirib çap edin.

text = "data"
print(text.upper())
print(text.lower())

# 8) s = "Python-R-Java" yaradın. "-" ilə ayırın (split("-")) və nəticəni çap edin.

s = "Python-R-Java"
print(s.split("-"))

# 9) ad = "Ayxan" və yaş = 25 yaradın. f-string ilə "Ayxan 25 yaşındadır" çap edin.

ad = "Ayxan"
yaş = 25
print(f"{ad} {yaş} yaşındadır")

# 10) s = "salam-dunya" yaradın. "-"ni boşluqla əvəz edin və nəticəni çap edin.

s = "salam-dunya"
print(s.replace("-", " "))



# Sprint_2a_task


# 1) 5, 10, 15, 20 rəqəmlərindən ibarət “rəqəmlər” adlı list/vector yaradın

num = [5, 10, 15, 20]
print(num)

# 2) “rəqəmlər” listinin/vectorunun uzunluğunu tapın

print(len(num))

# 3) “rəqəmlər” listinə/vectoruna 25 elementini əlavə edin

num.append(25)
print(num)

# 4) “rəqəmlər” listinin/vectorunun 2-ci indeksinə 12 elementini əlavə edin

num.insert(1,12)
print(num)


# 5) 1, 2, 3 və 4, 5, 6 listlərini/vectorlarını birləşdirin

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(list_1 + list_2)

# 6) “rəqəmlər” listindən/vectorundan 2-ci və 3-cü elementləri seçin

print(num[1:3])

# 7) “rəqəmlər” listinin/vectorunun ilk elementini 50 ilə əvəz edin 

num[0] = 50
print(num)

# 8) “rəqəmlər” listində/vectorunda 19 elementinin olub-olmadığını yoxlayın

n = len(num)
print(n == 19)

# 9) "a", "b", "a", "c" listində/vectorunda "a" elementinin neçə dəfə təkrarlandığını tapın

list =["a", "b", "a", "c"]
a = list.count('a')
print(a)

# 10) "x", "y", "x", "z" listindən/vectorundan "x" elementlərini silin

list =["x", "y", "x", "z"]
list.remove('x')
list.remove('x')
print(list)

# 11) 7, 2, 9, 1 listini/vectorunu azalan sırayla sıralayın

a = [7, 2, 9, 1]
a.sort()
a.reverse()
print(a)

# 12) “rəqəmlər” listindən/vectorundan 10-dan böyük elementləri seçin
print(num)
for i in num:
    if i > 10:
        print(i)




# Sprint_2b_task


# 1) 10, 20, 30, 40 elementlərindən ibarət s1 adlı series/vector yaradın

s1 ={10, 20, 30, 40}
print(s1)

# 2) s1-ə 'w', 'x', 'y', 'z' indekslərini təyin edin

s1 = {'w', 'x', 'y', 'z'}
a = 0
for i in s1:
    print(f'{i} indexsi: {a}')
    a += 1 


# 3) Python: {'p': 5, 'q': 10, 'r': 15} dictionary-dən s2 adlı Series yaradın

import pandas as pd
Python = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(Python)
print(s2)

#     R: list(p = 5, q = 10, r = 15) listindən v2 adlı named vektor yaradın
# 4) s2-dən 'q' indeksli elementi seçin
# 5) s1-dən 25-dən böyük elementləri seçin
# 6) s1-də 20-dən böyük elementləri 10-a bölün 
# 7) ((1, 2), (3, 4)) listindən/vectorundan df1 adlı dataframe yaradın
# 8) df1-ə ('r1', 'r2') sətir və ('c1', 'c2') sütun adlarını təyin edin
# 9) Python: {'A': [1, 2], 'B': [3, 4]} dictionary-dən df2 yaradın
#     R: list(A = c(1, 2), B = c(3, 4)) listindən df2 yaradın 
# 10) df2-dən 'r1' sətrini seçin
# 11) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin