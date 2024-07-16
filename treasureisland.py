print("Welcome to Treasure Island \n Your mission is to find the treasure")
choice1=input("you're at a crossroad, where do you want to go?  type 'right' or 'left'\n ").lower()
if choice1=="left":
    choice2=input("You've come to a lake. There is an island in the middle of the lake?Type 'wait' or 'swim'\n ").lower()
    if choice2=="wait":
        choice3=input("You have to choose the door? type 'red' ,'blue' and 'yellow'\n" ).lower()
        if choice3=="yellow":
            print("you win")
        elif choice3=="blue":
            print("goblins ate you. game over") 
        else:
            print("you fell into a mountain. Game over") 
    else:
        print("pirana fish will eat you . Game over")
else:
    print("game over. you fell into a big hole")
    
