import numpy as np
import time
import sys
a=np.array([1,2,3,4])
print(a)
# python list and its size
l = range(1000)
print(sys.getsizeof(5) * len(l))
# numpy array and it's size
arr = np.arange(1000)
print(arr.size * arr.itemsize)
