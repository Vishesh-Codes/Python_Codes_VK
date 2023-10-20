#==========================================
# Game Development: Snake Water Gun
#==========================================

import random

# asks for how many times a player wants to play
def count():
    a = input("How many times would you like to play?? --> ")
    if a.isnumeric() == True and int(a) > 0:
        return int(a)
    elif a.startswith("exit"):
        exit()
    else:
        print("\nKindly choose only positive integers above 0")
        return count()

# returns computer's choice
def computer():
    options = ["snake", "water", "gun"]
    com_choice = random.choice(options)
    return com_choice

# returns player's choice
def user():
    user_choice = input("Choose any one of these: Snake(1) or Water(2) or Gun(3)  -->  ").lower()
    if user_choice.startswith('s') or user_choice == '1':
        return "snake"
    elif user_choice.startswith('w') or user_choice == '2':
        return "water"
    elif user_choice.startswith('g') or user_choice == '3':
        return "gun"
    elif user_choice.startswith("exit"):
        exit()
    else:
        print("\nOption does not exist")
        return user()
    
# shows player's and computer's choice together
def show_choices():
    print(f"\nYour choice is '{u}' and computer's choice is '{c}'")

# performs interaction with user while playing the game
def game_process():
    global com_win, user_win, draw
    com_win = 0
    user_win = 0
    draw = 0
    for i in range(limit):
        global c, u
        c = computer()
        u = user()
        if c == "snake" and u == "water":
            show_choices()
            print("You Lose. Snake drunk your water.\n")
            com_win += 1
        elif c == "snake" and u == "gun":
            show_choices()
            print("You won. Snake killed by your gun.\n")
            user_win += 1
        elif c == "water" and u == "gun":
            show_choices()
            print("You Lose. Your gun drown in water.\n")
            com_win += 1
        elif c == "water" and u == "snake":
            show_choices()
            print("You won. Snake drunk the water.\n")
            user_win += 1
        elif c == "gun" and u == "snake":
            show_choices()
            print("You Lose. Snake killed by the gun.\n")
            com_win += 1
        elif c == "gun" and u == "water":
            show_choices()
            print("You won. The gun drown in water.\n")
            user_win += 1
        else:
            show_choices()
            print("Both are same! It became draw\n")
            draw += 1

# shows the game result
def game_result(a, b):
    print(f"You won\t\t={user_win} time(s)")
    print(f"Computer won\t={com_win} time(s)")
    print(f"Draw\t\t={draw} time(s)")
    if user_win > com_win:
        print(f"Finally, you won by {user_win-com_win} point(s)")
    elif user_win == com_win:
        print(f"Finally, game draw")
    else:
        print(f"Tohse na ho pai, you lose by {com_win-user_win} points")

# asks from the player that would you like to play again or not
def play_again():
    ask = input("\n\nWould you like to play again??\nyes(1) or no(2)\n--> ")
    if ask == "yes" or ask == "1":
        return start_game()
    elif ask == "no" or ask == "2":
        print("\nGame ended. We hope you have enjoyed so far.\nSee you again.")
        exit()
    else:
        print("\nOption does not exist")
        return play_again()

# starts the game when a player wants to play and so on
def start_game():
    print("\n\n" + "Welcome to the Snake-Water-Gun game\n\n".center(100, " "))
    global limit
    limit = count()
    game_process()
    game_result(user_win, com_win)
    play_again()

#=====================
# Program Starts Here
#=====================

start_game()