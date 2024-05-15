# Write a python program of a roller coster ticketting system using if else

height = int(input("Please Enter your height : "))


if height >= 120: 
    age = int(input("Please Enter your age: "))
    print("You can ride the roller coster...")
    want_picture = (input("Do you want a picture Y / N ? "))
    if age < 12 :
        bill = 5
    elif age <= 18 :
       bill = 7
    elif age > 18 :
        bill = 12

    if want_picture != "Y" :
        print (f"Your bill is {bill}")
    if want_picture == "Y" :
        bill = bill + 3
        print (f"Your bill is {bill}")
else:
    print("You need to grow your height before riding the roller coster !!!")
