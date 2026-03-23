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

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender": "Male"
}

for each_key in my_dict.keys():
    print(my_dict[each_key])