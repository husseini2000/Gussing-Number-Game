import random


def wel_message():
    """print welcome message"""

    print('********************************')
    print('Welcome to the number guess game')
    print('********************************')


def number_to_guess():
    """ Initialise the number to be guessed """

    low = int(input("\nEnter the lowest number: "))
    high = int(input("Enter the highest number: "))
    comp_num = random.randint(low, high)
    return comp_num


def guessing_num():
    print("\nI  am thinking of a number…")
    guess = int(input("Guess the number I am thinking of: "))
    return guess


# Function to cheat the player the correct random number
def cheat_mode(num, guessed):
    if num == -1:
        print('the number you needed to guess is ', guessed)
        num = int(input('Please guess again: '))
    return num


# Function to print summary about the whole game
def game_status(game_number, user_num, number_of_tries):
    # Check to see if they did guess the correct number
    if game_number == user_num:
        print('\nWell done you won!')
        print('The number you needed to guess was ', game_number)
        print('You took', number_of_tries, 'goes to complete the game')
    else:
        print("\nSorry - you lose")
        print('The number you needed to guess was ', game_number)


def guess_checking(random_num, guessed_number, tries=1, flag='y'):
    while flag == 'y':
        while random_num != guessed_number:
            print('Sorry wrong number')
            # Check to see they have not exceeded the maximum
            # number of attempts if so break out of loop otherwise
            # give the user come feedback
            if tries == 4:
                break
            elif guessed_number < random_num:
                # Calculate the difference between the two numbers
                difference = random_num - guessed_number
                print('\nYour guess was lower than the number')
                # Check if the difference is equal 1
                if difference == 1:
                    print('\nYour guess is within 1 of the actual number')
            else:
                # Calculate the difference between the two numbers
                difference = guessed_number - random_num
                print('\nYour guess was higher than the number')
                # Check if the difference is equal 1
                if difference == 1:
                    print('\nYour guess is within 1 of the actual number')
            # Obtain their next guess and increment number of attempts
            guessed_number = int(input('Please guess again: '))
            guessed_number = cheat_mode(guessed_number, random_num)
            tries += 1
        # Call game_status
        game_status(random_num, guessed_number, tries)
        flag = input('Do you want play again\nEnter (y/n): ')


def play_game():
    """play the game"""
    wel_message()
    comp = number_to_guess()
    # Obtain their initial guess
    guess_num = cheat_mode(guessing_num(), comp)
    guess_checking(comp, guess_num)


play_game()
