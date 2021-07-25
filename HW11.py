from functools import reduce
a_list = [2,3,6,8,10,5,2]

b_list = list(map(lambda x: x**2, filter(lambda x: x % 3 == 2 and x > 4,a_list)))
##print(bList)

bob = [['CSCI51P', 78], ['Econ52', 94],['Econ151', 60],['Math101', 95], ['Math60', 82]]

tim = [['CSCI51P', 90], ['CSCI62', 92],['Math101', 87],['Econ51', 97]]

###filter(lambda x: type(x[1]) == int, Tim)


avg_list = reduce(lambda x,y: x + y, list(map(lambda x: x[1], tim)), 0)/len(tim)
print(avg_list)

# import numpy as np

# bob = np.array(bob)
# print(bob[:, 1].astype(int))

# bob_scores = bob[:, 1].astype(int)
# bob_avg = np.average(bob_scores)
# print(bob_avg)
