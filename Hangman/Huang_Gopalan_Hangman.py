from __future__ import print_function
import random
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
intList = "1234567890"

ascii = [

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    M""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    MA""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    MAR""",


"""
   _________              
    |/   |                     
    |   (_)       
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    MARV""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    MARVE""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    MARVEL"""]

def hangman_display(guessed, secret):
    """
    Takes a string, secret, and runs it with guessed argument. If the char is in
    secret, it adds the char to display. Otherwise, it adds a - and at the end
    returns display.
    """
    display = ""
    
    for char in secret:
        if char == " ":
            display += " "
        elif char in guessed:
            display += char
        else:
            display += "-"
    
    return display
    
def hangman():
    """
    Takes in no arguments for this function and chooses a random choice from a
    list of possible secret words. It then takes in a input/guess to check with 
    the secret. If the len of guess is more than 1, it will break the code. If 
    guess if not in the alphabet and is not an integer, it will run the for loop
    that checks the if the char is in secret, it adds the char to display. 
    Otherwise, it adds a - and at the end returns display. If the number of 
    guesses is more than 6, it will print game over and prompt if the user wants
    to play again. If you guess all the letters, it will end the game and print
    you win.
    """
    win = False
    secret_word_list = [
    "Black Panther", 
    "Thor Ragnorak", 
    "Spiderman Homecoming", 
    "Avengers Infinity War", 
    "Antman and the Wasp", 
    "Guardians of the Galaxy", 
    "Captain America", 
    "Iron Man ", 
    "The Incredible Hulk", 
    "Captain Marvel", 
    "Doctor Strange", 
    "Avengers Age of Ultron"
    ]
    secret = random.choice(secret_word_list)
    guessed_letters = []
    guessNumber = 1
    display = ""
    print(" ")
    print("================================================")
    print("Welcome to the Marvel Movies Hangman!")
    print("All possible words are from Marvel Movies.")
    print("You can get 6 incorrect guesses before you lose.")
    print("You can only enter in 1 letter at a time, unless")
    print("you know what the entire word is.")
    print("================================================")
    print("Your word is ...")
    time.sleep(3)
    for char in secret:
        if char != " ":
            display += "-"
        else:
            display += " "
    print(display)
    display = ""
    print("================================================")
    print("Enter in \"Cheat\" to view secret.")
    
    while guessNumber <= 6:  # Keeps running unless user gets more than 6 
        print("")            # incorrect guesses
        for char in secret:
            if char == " ":  # Prints out the display with dashes for the user
                display += " "
            elif char.upper() in guessed_letters or char.lower() in guessed_letters:
                display += char
            else:
                display += "-"
        if display.upper() == secret.upper(): # If the user guessed all the words
                print("Congratulations! You Win!") 
                print("The word was:", secret, end=".")
                win = True # It breaks the code and sets win to True, so that 
                break      # it does not print the lose text as well when the loop
                           # is broken.
            
        print("Guess:", guessNumber)
        print(ascii[guessNumber - 1])
        print("Guessed Characters -", ", ".join(guessed_letters))
        print("Word:", display)
        display = ""
        addingGuess = True
        appendLetter = True
        guess = raw_input("Enter your guess: ")
        
        print("================================================")
        
        if len(guess) == 1:  # Only runs if guess is 1 character
            # Conditional for already guessed letters
            if guess.upper() in guessed_letters or guess.lower() in guessed_letters:
                print("You already guessed \"" + guess,end="\". ")
                guessNumber += 1
                addingGuess = False
                appendLetter = False
                
            # Adds to used list    
            if appendLetter == True:
                guessed_letters.append(guess)
            
            # If letter is not in secret    
            if addingGuess == True:    
                if guess.upper() not in secret.upper():
                    print("Oof, not in secret.")
                    if guess not in alphabet and guess not in intList:
                        print("No special characters.")
                        display = ""
                    guessNumber += 1
                    display = ""
                    
        # If length of the guess if greater than 1 and is == to cheat
        elif guess.lower() == "cheat":
            print("Cheater...")
            time.sleep(1)
            print("The word is", secret)
            print("Please return to the game!")
            print("================================================")
            time.sleep(1)
            
        # If length of the guess if greater than 1 and is == to the secret    
        elif guess.lower() == secret.lower():
            print("Congratulations! You Win!")
            print("The word was:", secret, end=".")
            win = True
            break
        
        # If the length is greater than 1 and not equal to cheat or the secret
        else:
            print("You should only enter 1 character.")
            guessNumber += 1
        
    # If the code breaks and win is still == to False
    if win == False:
        print("You lost!") 
        print("The actual word was:",secret, end=".")
        print(ascii[guessNumber - 1])
        
    # Rerunning the code
    print("\n")
    print("Would you like to play again? (Y/N)")
    answer = raw_input(">> ")
    if answer.upper() == "Y":
        hangman()
    else:
        print("Bye, thanks for playing!")
        
hangman()