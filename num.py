
import numpy as np
  
b = np.zeros(2, dtype = int)
print("Matrix b : ", b)

a = np.zeros([2, 2], dtype = int)
print("\nMatrix a :", a)

c = np.zeros([3, 3])
print("\nMatrix c : ", c)


#Addition
a = np.array([5, 72, 100])
b = np.array([2, 5, 10])
c = np.array([1, 2, 3])
add_ans = a+b
print("\n",add_ans)

add_ans = np.add(a, b)
print(add_ans)

add_ans = a+b+c
print(add_ans)

add_ans = np.add(a, b,c)
print(c)