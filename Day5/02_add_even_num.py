target = int(input("Enter a number between 1 to 1000: \n"))
init = 0

for number in range (init,target + 1) :
    if number % 2 == 0 :
        init += number
print (f"The Addition of even numbers between 1 to {target} is \n{init}")
