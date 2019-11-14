import pdb
import timeit

a = [1, 2, 3, 4, 5]
b = [3, 5, 7, 8, 9]
c = a+b

pdb.set_trace() # enter ? in cmd of pdb to get all valid data that can be provided to pdb. To print use 'display' in pdf console.

t = timeit.timeit('[str(i) for i in range(10)]')
print(t)

t = timeit.timeit('map(str, [i for i in range(10)])')
print(t)