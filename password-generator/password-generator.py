import random
import string

length = int(input("enter password length: "))
while length < 8:
    print("password should be atleast 8 characters")
    length = int(input("enter password length: "))

has_upper = input("include uppercaseletter? (yes/no)").lower
has_numbers = input("include numbers? (yes/no)").lower
has_special_character = input("include special character? (yes/no)").lower


character_pool = string.ascii_lowercase

if has_upper == 'yes':
    character_pool += string.ascii_uppercase

if has_numbers=='yes':
    character_pool += string.digits

if has_special_character == 'yes':
    character_pool += string.punctuation


password_list = []
for i in range(2):
    char = random.choice(string.ascii_uppercase)
    password_list.append(char)
    num = random.choice(string.digits)
    password_list.append(num)


punc = random.choice(string.punctuation)
password_list.append(punc)


remaining_length = length - len(password_list)

for i in range(remaining_length):
    one_character = random.choice(character_pool)
    password_list.append(one_character)

random.shuffle(password_list)
password = "".join(password_list)


print(f"the password is {password}")