# Random Password Generator 
import random
print (" Welcome to the password generator !!\n")
ask = int(input("What will be the length of your password ?\n"))
char = int(input("How many letters you want in your password ? \n"))
num =  int(input("How many numbers you want in your password ? \n"))
sym = int(input("How many symbols you want in your password ? \n"))
vrfy_length = (char + num + sym)
if vrfy_length < ask :
    print (f"The number of letters,numbers and symbols you told to include in your password is less than your desired length of password which is {ask}!!!\n Please provide appropriate input")
elif vrfy_length > ask :
    print (f"The number of letters,numbers and symbols you told to include in your password is greater than your desired length of password which is {ask}!!!\n Please provide appropriate input")
else :
    print("")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_']
print (vrfy_length)
# 52 10 12




