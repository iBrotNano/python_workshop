my_user_age = input("Please enter your age: ")
print("You entered:", my_user_age)
print(type(my_user_age))

try:
    my_user_age = int(my_user_age)
    my_user_age += 1
    print("Next year, you will be:", my_user_age)
except Exception as e:
    print("The input was not a valid integer.")
    print(e)

print("End of program.")