import random as r

win_dict = {"rock": "scissor", "paper": "rock", "scissor": "paper"}
mapper_dict = {0:"rock", 1:"paper", 2:"scissor"}

def play():

    print("WELCOME TO THE ROCK PAPER SCISSOR GAME!!")
    best_of = int(input("Enter the Best of how many times: "))
    machine_won = 0
    user_won = 0

    while best_of > 0:
        machine_choice = mapper_dict.get(r.randint(0,2))        
        user_choice = input("Choose among Rock/Paper/Scissor: ").lower()
        
        if machine_choice == user_choice:
            print(("Machine Choice: {} | User_Choice: {} | Result: {}").format(machine_choice,user_choice,"Its a tie!!"))
        elif win_dict[machine_choice] == user_choice:
            print(("Machine Choice: {} | User_Choice: {} | Result: {}").format(machine_choice,user_choice,"Machine won!!"))
            machine_won += 1
        else:
            print(("Machine Choice: {} | User_Choice: {} | Result: {}").format(machine_choice,user_choice,"User won!!"))  
            user_won += 1          
        
        best_of -= 1

    if machine_won > user_won:
        print("Finally Machine won the game!!")
    elif machine_won == user_won:
        print("Finally Its a Tie!!")
    else:
        print("Finally User won the game!!")

    if input("Do you want to continue(y/n): ") == "y":
        play()
        
    return 1
        
        


if __name__  == "__main__":
    play()
