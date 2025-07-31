import random

attempts_list= []

def show_score():
    if not attempts_list:
        print("There's currently no high score, start plaing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


attempts = 0
rand_number = random.randint(1,10)

print("Hola! are you intrested to play the guessing game!")
player_name=input("what is your name? ")
wanna_play= input(
    f"Hi, {player_name} , let is go to play guessing game?"
    " (Enter Yes/No) " 
).lower()

if wanna_play== "no":
    print ("it is cool,thanks! ")
    exit()
else:
    show_score()

while wanna_play=="yes":
    try:
        guess = int(input(" pick a number between 1 and 10:"))
        if(guess < 1 or guess > 10):
            raise ValueError (" please guess a number within the given range")
        
        attempts +=1
        attempts_list.append(attempts)

        if (guess == rand_number):
            print("Nice, you got it")
            print(f"It took you {attempts} attempts!")
            wanna_play = input("Would you like to play again (Enter Yes/No): " ).lower()

            attempts_list.append(attempts)
            
            if wanna_play == "no":
                print ("that is cool, have a gog day.")
            else:
                attempts=0
                rand_number= random.randint(1,10)
                show_score
                continue
        elif (guess > rand_number):
            print("It's lower!")
        else:
            print("It's higher!")

    except ValueError as err:
        print(err)
