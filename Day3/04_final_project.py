# Tresure Hunting Game

print(
    "Welcome to Tresure Island !!!\n Your mission is to find the tresure....")
print(
    "You were trying to find the tresure and suddenly you come to a road where you need to take a turn "
)
print("")
path = input("Left or Right ? :")
if path == "Left":
    print("You fell into a hole\n GAME OVER !!!")

elif path == "Right":
    print("You have came across a lake")
    choice_lake = input(
        "Do you want to wait for a boat or cross lake by swimming.\n Wait or Swim ?: "
    )
    if choice_lake != "Wait":
        print(
            "GAME OVER !!! \n You tried to cross the lake by swimming but crocodile ate you as soon as you jumped in a lake "
        )
    elif choice_lake == "Wait":
        print("You have crossed the lake unharmed by waiting for the boat !!!")
        door = input(
            "You see 3 doors infront of you in one of them is resure is hidden.\n Which door you want to open?\n Blue,Red,Yellow \n "
        )
        if door == "Red":
            print(
                "GAME OVER !!! \n Fire comming out from the RED door burnt you down "
            )
        elif door == "Blue":
            print(
                "GAME OVER !!! \n You opened the door which demon was living in"
            )
        elif door == "Yellow":
            print(
                "Congratulation  \n You found the TREASURE which was hidden for centuries..."
