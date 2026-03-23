# STRING SLICING
my_string = "This is the ENTC students"

# accessing the first variable of string
print(my_string[0])

# accessing 'This'
print(my_string[0:4])

# accessing this using interval
print(my_string[0:4:2])

# access last element of string
print(my_string[-1])

# reverse the entire string
print(my_string[::-1])

# reverse students 
print(my_string[:-9:-1])

# use replace
udpated_string = my_string.replace("s", "X")
print(udpated_string)