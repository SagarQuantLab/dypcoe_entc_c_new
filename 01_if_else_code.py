# if
my_age = 19
if my_age > 18:
    print(f"I am adult, because my age is : {my_age}")

# if else
if my_age > 18:
    print("I am adult")
elif my_age == 18:
    print("Turing adult")
else:
    print("I am minor")

# reducing if code block
age_status = False
if isinstance(my_age, int):
    age_status = True
    
print(age_status)


my_string = "MadaM"
reveresed_string = my_string[::-1]
if my_string == reveresed_string:
    print(f"{my_string} is a paladrome")