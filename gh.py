import numpy as np

scores = [89, 56, 34, 76, 89, 98]
first_arr = np.array(scores)
print(first_arr)

S = np.sum(first_arr)
print(S)

mn = np.min(first_arr)
mx = np.max(first_arr)
print(mn)
print(mx)

e = np.random.random((2, 2))  # create an array filled with random values
print(e)

datamean =np.mean(first_arr)
print(datamean)
datasum=np.sum(first_arr)
print(datasum)