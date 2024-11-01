# feedback they should what do for it
import tkinter 
import random 

# select a random number between 1 and 100
current_number = random.randint(1,100)


count = 0 
limit = 5

def check(current_number,user_guess):  
    global count
    count+=1 # Increment the count on each guess
    
    if (user_guess < current_number):

        if (current_number - user_guess) <= 5:
            print("Focus a litte bit more you are very close")
        else:
            print("You have to increase the your guess")

    elif (user_guess > current_number):

        if  (user_guess - current_number) <= 5:
            print("Focus a litte bit more you are very close")

        else:        
            print("You have to dicrease the yourr guess")

    else:
        print("Good Job. You guessed true number")
    
    #Display the remainig guesses
    print(f"You have only {limit - count} limit. Be careful!")

       
def play_loop():
    global play_game , current_number, count
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game.lower() not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        count = 0  # Reset the count
        current_number = random.randint(1, 100)  # Generate a new random number
        main()  # Start the game again
    elif play_game.lower() == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
        
def main():
    global count
    
    #GAme loop
    while count < limit:
        try:
            #Get user's guess
            user_guess =int(input("Guess the number (1-100). GOOd luck: "))

            if (user_guess < 1) or (user_guess > 100):
                print("Please guess a number between 1 and 100")
                continue
            
            #Call the check function
            check(current_number, user_guess)


            #Break the loop if the guess is correct
            if user_guess == current_number:
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # End game condition when the limit is reached or correct guess
    if count == limit:
        print(f"Sorry, you've reached the limit! The correct number was {current_number}.")
        
    # Ask if the user wants to play again
    play_loop()

main()

       
# def play_game():
#     total_try = 5
    
    



  