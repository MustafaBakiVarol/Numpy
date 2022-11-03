import numpy as np


#python list
pylist = [1,2,3,4,5,6,7,8,9]

#numpy list
nparray = np.array([1,2,3,4,5,6,7,8,9])

print(type(nparray))
print(type(pylist))

pylistmulti = [[1,2,3,],[4,5,6],[7,8,9]]

#numpy ile çok boyutlu dizileri oluşturabiliyoruz.
nparraymulti = nparray.reshape(3,3)

print(pylistmulti)
print(nparraymulti)

