import random
import string

user_words = input("Enter words for password: ").split(' ')
lst = []
splch = ['!', '@', '#', '$', '%', '*', '^', '&']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for word in user_words:
    lst.append(word)

num_digits = int(input("Enter the number of digits: "))
num_special_chars = int(input("Enter the number of special characters: "))

random.shuffle(lst)  # Shuffle the list of words to randomize their order

password = ""

# Add words, special characters, and digits to the password
for word in lst:
    password += word
    if num_special_chars > 0:
        char2 = random.choice(splch)
        password += char2
        num_special_chars -= 1
    if num_digits > 0:
        char3 = random.choice(digit)
        password += char3
        num_digits -= 1

print(f"Password = {password}")
