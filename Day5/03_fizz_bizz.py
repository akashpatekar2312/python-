init = 100
for number in range (1,init + 1 ):
    if number % 3 == 0 and number % 5 == 0:
        init += number
        print (f"FizzBizz")
    elif number % 3 == 0:
        init += number
        print (f"Fizz")
    elif number % 5 == 0:
        init += number
        print (f"Bizz")
    else:
        print(number)
