# Random Password Generator 
import random
print (" Welcome to the password generator !!\n")
ask = int(input("what should be length of your password ?\n \n"))
char = int(input("How many letters you want in your password ? \n"))
num =  int(input("How many numbers you want in your password ? \n"))
sym = int(input("How many symbols you want in your password ? \n"))
vrfy_length = (char + num + sym)
if vrfy_length < ask :
     print (f"The number of letters,numbers and symbols you told to include in your password is less than your desired length of password which is {ask}!!!\n Please provide appropriate input")
elif vrfy_length > ask :
     print (f"The number of letters,numbers and symbols you told to include in your password is greater than your desired length of password which is {ask}!!!\n Please provide appropriate input")
else :
   print ("")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_']

# Total items in lists in order of declaration 52 10 12

#strech = [ "{letters}", "{numbers}", "{symbols}" ]
# EASY METHOD : 
#       (The password only randomize the letters,nubers and symbols and not their positions !!)

# password = ""
# for i in range (num):
#     password += random.choice(letters)

# for i in range (num):
#     password += random.choice(numbers)

# for i in range (num):
#     password += random.choice(symbols)
    
# print (password)

# pwlen = len(password)
# new_pw = random.choice(password)
# print (new_pw)


# HARD METHOD :
#       (This Method will randomize the letters,numbers and symbols along with their positions)
password_list = ""
for i in range (num):
    password_list += random.choice(letters)

for i in range (num):
    password_list += random.choice(numbers)

for i in range (num):
    password_list += random.choice(symbols)
    
print (password_list)

pwlen = len({password_list})
new_pw = random.choice(password_list)
random.shuffle(new_pw)
print (new_pw)

