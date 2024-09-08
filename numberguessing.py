import random
computer_choice=int(random.randint(1,100))
#print(computer_choice)
def game():
    level=input("type easy or hard ")

    no_of_guess=0
    if level=="easy":
        no_of_guess=10
    else:
        no_of_guess=5
    while(no_of_guess):
        user_choice=int(input("make a guess: "))
        if(user_choice>computer_choice):
            print("LOWER NO PLEASE")
            no_of_guess-=1
            print(f"you have left only {no_of_guess} lives")
            print("guess again")

        elif(computer_choice>user_choice):
            print("HIGHER NO PLEASE")
            no_of_guess-=1
            print(f"you have left only {no_of_guess} lives")
            print("guess again")
        else:
            print(f"you have guessed the letter {computer_choice} and {user_choice}")
            break
    if(no_of_guess==0):
        print("you are out of your lives")

game()
