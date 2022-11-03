from urllib.parse import _ResultMixinBytes
import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

result = numbers1 + numbers2 # +10 gibi bir değer yazarsak mesela dizinin her elemanın 10 ekler.
print(numbers1)
print(numbers2)
#toplamları olduğu gibi farklarıda alınabilir.
result = np.sin(numbers1) #sinüsünü alır bize bir liste dönderir.

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

result = np.vstack((mnumbers1,mnumbers2)) # dikey olarak birleştirme işlemi.
result = np.hstack((mnumbers1,mnumbers2)) # yatay olarak birleştirir.

result = numbers1 > 1
print(result)
print(mnumbers1)
