my_simple_concat = "Hallo" + " " + "Welt"
print(my_simple_concat)

my_con_cat = "Katze" + " " + "Cat" + " " + "Kitten" + " " + "😺"
print(my_con_cat)

user_first_name = "Peter"
user_last_name = "Musterfrau"
user_age = 45
user_Gender = "Frau"

email_greeting = "Hey" + " " + user_Gender + " " + user_first_name + " " + user_last_name + ","
print(email_greeting)

email_text = "Happy Birthday! You are now: " + str(user_age)
print(email_text)

my_path = "C:/user/me/images"
my_file_base_name = "image"
my_file_index = "001"
my_file_extension = ".png"
full_file_path = my_path + "/" + my_file_base_name + my_file_index + my_file_extension
print(full_file_path)

test = 1 + int(float("1.0"))
print(test)