# DICTIONARY
# Mutable, key, Ordered, {}, No-duplicates
my_dict = {
    "Name": "Rohan",
    "Age" : 30,
    "Gender": "Male",
}

# accessing keys
for each_key in my_dict.keys():
    print(each_key)

# access values
for each_value in my_dict.values():
    print(each_value)

# access keys and values
for each_key, each_value in my_dict.items():
    print(each_key, each_value)

# access value of key
print(my_dict["Name"])

# assigning different name
my_dict["Name"] = "Sohan"
print(my_dict)


###################################################
# Item      Mutable      Ordered     define      Duplicates     Access

# List      Yes             Yes         []          Yes         index
# Dict      Yes             Yes         {}          No          keys
# Tuple     No              Yes         ()          Yes         index
# set       No              No          ()          No          -