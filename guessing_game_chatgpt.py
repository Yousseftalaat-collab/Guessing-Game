import random

def play_game():
    min_attempts = None
    print("🎮 Welcome to the Guessing Game!")
    
    while True:
        pc_number = random.randint(1, 10)
        attempts = 0
        
        while True:
            try:
                guess = int(input("🤔 Pick a number between 1 and 10: "))
                if not 1 <= guess <= 10:
                    print("Please choose a number in the range 1-10.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess == pc_number:
                print("🎉 Amazing! You guessed it right!")
                break
            elif guess < pc_number:
                print("🔼 Hint: Try a higher number.")
            else:
                print("🔽 Hint: Try a lower number.")

        print(f"📊 You guessed it in {attempts} attempts.")
        if min_attempts is None or attempts < min_attempts:
            min_attempts = attempts
            print("🏅 That's your best score so far!")

        print(f"🥇 Best score (least attempts): {min_attempts}")

        again = input("🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

play_game()
