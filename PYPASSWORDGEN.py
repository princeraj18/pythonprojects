import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letter = int(input("Enter a number of letter : "))
nr_symbol = int(input("Enter a number of symbols : "))
nr_number = int(input("Enter a number of numbers : "))
#EASY LEVEL
 password =""
for char in range(0,nr_letter):
  password += random.choice(letters)
for char in range(0,nr_symbol):
   password += random.choice(symbols)
for char in range(0,nr_number):
  password += random.choice(numbers)
print(password)

#HARD LEVEL
password_list=[]
for char in range(0,nr_letter):
  password_list.append(random.choice(letters))
for char in range(0,nr_symbol):
  password_list.append(random.choice(symbols))
for char in range(0,nr_number):
  password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
  password+=char
print(f"your final password is {password}")