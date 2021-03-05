import random
import numpy as np

l = []

cnt = 0
while cnt < 25:
    num = random.randint(1, 40)
    if not num in l:
        l.append(num)
        cnt += 1

arr = np.array(l)
arr_5by5 = arr.reshape(5, 5)
print(arr_5by5)