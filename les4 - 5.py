from functools import reduce

def my_func(par_1, par_2):
    return par_1 * par_2

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_func, my_list))