my_list = [10, 20, 30, 40]

# simple for loop
for i in my_list:
    print(i)

# for loop for index
for i in range(len(my_list)):
    print(i, my_list[i])

# for loop using enumeration
for i, each_value in enumerate(my_list):
    print(i, each_value)