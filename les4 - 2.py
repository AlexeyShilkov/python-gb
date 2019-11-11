from random import randint

my_list = [randint(0, 10) for i in range(15)]
print(my_list)

new_list = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(new_list)