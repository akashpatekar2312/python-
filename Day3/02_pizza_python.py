# small = 15, medium = 20, large = 25, 
# pepperoni = S=2 , M=3 , L=3
# cheese = 1
print ("Welcome to the python pizza \n")
size = input("What size of pizza you want ? S,M,L\n")
pepperoni = input("Do you want to add pepperoni to your pizza ?\n")
cheese = input("Do you want to add extra cheese in your pizza ? \n")
bill = 0

if size == "S" :
    bill = 15
    if pepperoni == "Y":
        bill = bill + 2
        if cheese == "Y" :
            bill =  bill + 1
    print (f"Your total bill is ${bill}")   

if size == "M" :
    bill = 20
    if pepperoni == "Y":
        bill = bill + 3
        if cheese == "Y" :
            bill = bill + 1
    print (f"Your total bill is ${bill}")    

if size == "L" :
    bill = 25
    if pepperoni == "Y":
        bill = bill + 3
        if cheese == "Y" :
            bill = bill + 1
    print (f"Your total bill is ${bill}")           

