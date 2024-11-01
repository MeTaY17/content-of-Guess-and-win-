import numpy as np
import tkinter as tk

def initialize_game():
    # Select a random number between 1 and 100
    global current_number, count, limit, canvas, GRID_SIZE, CELL_SIZE
    current_number = np.random.randint(1, 201)
    
    
    count = 0
    limit = 5

    # Initialize the main window
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Guessing Game with 2D Display Panel \n"+
               "if your guess is low , the mark guess is blue\n"+
               "if your guess is hight, the mark guess is red\n"+
               "if your guess is corect, the mark guess is green")

    # Define grid size and panel dimensions
    GRID_SIZE = 20
    CELL_SIZE = 20
    canvas_width = CELL_SIZE * GRID_SIZE
    canvas_height = CELL_SIZE * GRID_SIZE

    # Create a canvas
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=0,pady=0)

    # Draw a grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x1 = i * CELL_SIZE           # Calculate the top-left x coordinate
            y1 = j * CELL_SIZE           # Calculate the top-left y coordinate
            x2 = x1 + CELL_SIZE          # Calculate the bottom-right x coordinate
            y2 = y1 + CELL_SIZE          # Calculate the bottom-right y coordinate
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")  # Draw the rectangle

    # Start the main game loop
    main(root)

def map_guess_to_coordinates(guess):
    # Map the number to a grid position in 100x100 pixels
    row = (guess - 1) // GRID_SIZE
    col = (guess - 1) % GRID_SIZE
    return col, row

def check(current_number, user_guess):
    global count
    count += 1  # Increment the count on each guess

    # Get the coordinates to color the cell
    col, row = map_guess_to_coordinates(user_guess)

    if user_guess < current_number:
        if (current_number - user_guess) <= 5:
            print("Focus a little bit more, you are very close.")
        else:
            print("You have to increase your guess.")
        canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE, 
                                (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE, 
                                fill="blue", outline="black")  # Mark guess in blue

    elif user_guess > current_number:
        if (user_guess - current_number) <= 5:
            print("Focus a little bit more, you are very close.")
        else:
            print("You have to decrease your guess.")
        canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE, 
                                (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE, 
                                fill="red", outline="black")  # Mark guess in red

    else:
        print("Good Job! You guessed the correct number.")
        canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE, 
                                (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE, 
                                fill="green", outline="black")  # Mark correct guess in green

    # Display the remaining guesses
    print(f"You have only {limit - count} limit. Be careful!")

def play_loop(root):
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game.lower() not in ["y", "n"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        root.destroy()  # Close the current window
        initialize_game()  # Start a new game
    elif play_game.lower() == "n":
        print("Thanks for playing! We expect you back again!")
        root.destroy()  # Close the window and exit

def main(root):
    global count

    # Game loop
    while count < limit:
        try:
            # Get user's guess
            if 0 < current_number <= 50:
                print("The number that you'll guessing number in between 0 and 51")
                user_guess = int(input("Guess the number (1-51). Good luck: "))
                
            elif 51 <= current_number <= 100:
                print("The number that you'll guessing number in between 50 and 101")
                user_guess = int(input("Guess the number (50-101). Good luck: "))
                 
            elif 101 <= current_number <= 150:
                print("The number that you'll guessing number in between 100 and 151")
                user_guess = int(input("Guess the number (100-151). Good luck: "))
                
            elif 151 <= current_number <= 200:
                print("The number that you'll guessing number in between 150 and 200")
                user_guess = int(input("Guess the number (150-201). Good luck: "))


            if (user_guess < 1) or (user_guess > 200):
                print("Please guess a number between 1 and 201.")
                continue
            
            # Call the check function
            check(current_number, user_guess)

            # Break the loop if the guess is correct
            if user_guess == current_number:
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # End game condition when the limit is reached or correct guess
    if count == limit:
        print(f"Sorry, you've reached the limit! The correct number was {current_number}.")
        
    # Ask if the user wants to play again
    play_loop(root)

# Start the game for the first time
initialize_game()
