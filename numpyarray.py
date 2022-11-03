import numpy as np

#result = np.array([1,3,5,7,9])
#result = np.arange(1,10)
#result = np.arange(10,100,3) 
#result = np.zeros(10) # sadece sıfırlardan oluşur .
#result = np.ones(10)
#result = np.linspace(0,100,5)
#result = np.linspace(0,5,5)
#result = np.random.randint(10) 0 ve 9 dahil değer dönderir.
#result = np.random.randint(1,10,3)
#result = np.random.rand(5)
#nparray = np.arange(50)
#result = nparray.reshape(5,10)
#print(result.sum(axis=1))satır
#print(result.sum(axis=0))sütun



rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
#result = rnd_numbers.max()
#result = rnd_numbers.mean()
#result = rnd_numbers.min()
#result = rnd_numbers.argmax()
result = rnd_numbers.argmin()
print(result)

