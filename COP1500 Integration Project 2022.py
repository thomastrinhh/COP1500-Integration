"""
Integration Project for COP 1500.
Author: Thomas Trinh
"""

import math
import time
import random

# Introductory statement.
# Asks for user's name and verifies if name contains only letters.
name = input("What is your name? ")
while not name.isalpha():
    print("Your name cannot contain any numbers or symbols! Please try again.")
    name = input("What is your name? ")
if name.isalpha():
    print('\nHello ' + name + '! ', end='')
    print()
    print('I can aid in performing various computations as well as provide '
          'entertainment.')
    print('You are currently in the console.')


def dot():
    """
Function allows for pauses between outputs in order to make program
appear more human.
    """
    for _ in range(3):
        print(".", end="")
        time.sleep(0.3)


def math_calculator(user_num1, operator, user_num2):
    """
Program accepts the parameters from math_main and computes them based on the
selected operator chosen by the user. Function can compute addition,
subtraction, division, and exponents
    :param user_num1:
    :param operator:
    :param user_num2:
    """

    solution = 0

    print()
    # Addition arithmetic.
    if operator == "+":
        solution = float(user_num1) + float(user_num2)
        print(user_num1, "+", user_num2, "=", solution)
    # Subtraction arithmetic.
    elif operator == "-":
        solution = float(user_num1) - float(user_num2)
        print(user_num1, "-", user_num2, "=", solution)
    # Multiplication arithmetic.
    elif operator == "*":
        solution = float(user_num1) * float(user_num2)
        print(user_num1, "*", user_num2, "=", solution)
    # Division arithmetic.
    elif operator == "/":
        solution = float(user_num1) / float(user_num2)
        print(user_num1, "/", user_num2, "=", solution)
        if user_num1 > user_num2:
            remainder = float(user_num1) % float(user_num2)
            print("(" + user_num2, "divides into", user_num1,
                  format(float(user_num1) // float(user_num2), "0.0f"), end="")
            print(" time(s) with a remainder of ",
                  format(remainder, "0.0f"), ".)", sep="")
    # Computes exponents.
    elif operator == "^":
        solution = float(user_num1) ** float(user_num2)
        print(user_num1, "^", user_num2, "=", solution)

    # Provides users the option to round the yielded value.
    round_for_user = input("\nWould you like me to round this value? ")
    if round_for_user.lower() == "yes" or round_for_user.lower() == "y":
        # Asks user how many decimal places they would like to round to.
        decimal_places = int(input("How many places would you like me to "
                                   "round to? "))
        try:
            int(decimal_places)
        except ValueError or TypeError:
            print('\nThat is not a valid integer ' + name +
                  '. Please try again.\n')
        rounded_value = round(solution, decimal_places)
        print("\nSolution rounded to", decimal_places, "decimal places:",
              rounded_value)
        time.sleep(1)
        main()
    elif round_for_user.lower() == "no" or round_for_user.lower() == "n":
        time.sleep(1)
        main()
    else:
        print("Oops! Sorry but that is an invalid input", name,
              ". Returning back to console.", sep="")
    time.sleep(1)
    main()


def math_main():
    """
This function takes two individual integer inputs from the user and an
operator. It passes these arguments as parameters to math_calculator function.
    """
    user_num1 = input("\nEnter your first number: ")
    try:
        float(user_num1)
    except ValueError or TypeError:
        print("Oops! That does not appear to be a valid number. "
              "Please try again. ")
        math_main()
    print('\nAddition: [+] \nSubtraction: [-] \nMultiplication: '
          '[*] \nDivision: [/] \nExponential values: [^]\n')
    operator_list = ["+", "-", "*", "/", "^"]
    operator = input("Choose from the list of operators above: ")
    while operator not in list(operator_list):
        print("Oops! That does not appear to be a valid operator. "
              "Please try again. ")
        operator = input("Choose from the list of operators: ")
    user_num2 = input("\nEnter your second number: ")
    try:
        float(user_num2)
    except ValueError or TypeError:
        print("Oops! That does not appear to be a valid number. "
              "Please try again. ")
        math_main()
    # Passes argument to math_calculator function as parameter.
    math_calculator(user_num1, operator, user_num2)


def radians():
    """
Function converts value inputted by user to either radians or degrees by using
pi from math module.
    """
    # Conversion of radians to degrees or vice versa.
    degree = math.pi / 180
    radian = 180 / math.pi

    number = input("\nInput a number: ")
    # Verifies if numbers are integers or not.
    try:
        float(number)
        validation = True
    except ValueError:
        validation = False
    if not validation:
        print('\nThat is not a valid integer ' + name + '. Please try again.')
        radians()
    rad_or_deg = input("Would you like to convert to radians or degrees? ")
    if rad_or_deg.lower() == "rad" or rad_or_deg.lower() == "radians":
        print(number, "radians is equal to",
              format(float(number) * radian, "0.3f"), "degrees.")
    if rad_or_deg.lower() == "deg" or rad_or_deg.lower() == "degrees":
        print(number, "degrees is equal to",
              format(float(number) * degree, "0.3f"), "radians.\n")
    main()


def mean_med_range_calculator(ask_user, length, data):
    """
This function computes mean median and range based off the parameters passed
from mean_med_range_inputs.
    :param ask_user:
    :param length:
    :param data:
    """
    if ask_user.lower() == 'mean':
        # Takes sum of list and divides it by the # of elements in the list.
        counter = length
        range_value = sum(data) / counter
        print("The mean value out of the", length,
              "values you entered was:", range_value)

    if ask_user.lower() == "median":
        # If length of list is odd, median is middle value inside list
        if length % 2 != 0:
            half_of_list = int(length / 2)
            median = data[half_of_list]
            print("The median value out of the", length,
                  "values you entered was:", median)

        # If length of list is even, no middle value exists. More work needed
        else:
            # Calculates median between both middle values in list
            half_1 = int(length / 2) - 1
            half_2 = int(length / 2)
            sum_midpoints = (data[half_1] + data[half_2])
            median = (sum_midpoints / 2)
            print("The median value out of the", length,
                  "values you entered was:", median)
    elif ask_user.lower() == "range":
        # Takes maximum value from list and subtracts it by the minimum value.
        max_value = max(data)
        range_value = max_value - data[0]
        print("The range value out of the", length,
              "values you entered was:", range_value)
    main()


def mean_med_range_inputs():
    """
This function accepts the inputs from the user as arguments and passes them
to mean_med_range_calculator as parameters.
First input is mean, median, or range. Second input is list length.
Third input are the values inside the list.
    """
    data = []
    length = 0

    ask_user = input("\nWould you like to calculate mean, median, or range? ")
    if ask_user.lower() == "mean" or ask_user.lower() == "median" \
            or ask_user.lower() == "range":
        # Determines length of list.
        n = input("\nHow many values would you like to compute? ")
        # Verifies if length of list is an integer value.
        try:
            int(n)
            validation = True
        except ValueError or TypeError:
            validation = False
        if not validation:
            print("Oops! That does not appear to be a valid number. "
                  "Please try again.")
            mean_med_range_inputs()

        length = int(n)

        print("Okay! You chose to enter", length, "values. ")

        # Prompts user for values to be entered in list. 
        for _ in range(length):
            number = input("Enter a number: ")
            try:
                float(number)
                validation = True
            except ValueError or TypeError:
                validation = False
            if not validation:
                print("Oops! That does not appear to be a valid number. "
                      "Please try again.")
                mean_med_range_inputs()
            values = float(number)
            data.append(values)
            data.sort()
    else:
        print("Oops! Sorry but that is an invalid input. Please enter either"
              "mean, median, or range! Navigating back to console. ")
        main()
    # Passes arguments to mean_med_range_calculator function.
    mean_med_range_calculator(ask_user, length, data)


def guessing_game():
    """
This function is a game that generates a random number and prompts user
to guess it. First input asks user if they would like to begin, following
inputs are the number guesses that must range from 1-10.
    """
    print("\n\nFor this game you will have three tries at guessing a random "
          "number I have chosen.")
    print("Let's start.")
    print()
    # Generates random value from random module.
    random_value = random.randint(1, 10)
    for _ in range(3):
        guess_value = int(input("Guess a number between 1 and 10: "))
        if guess_value != random_value:
            print("That is not the value I am thinking of!\n")
        elif guess_value == random_value:
            print("Good job! The value was indeed", random_value, end=".")
            print()
            time.sleep(1)
            main()
    print("You have used up all three of your chances. The correct number was",
          random_value, end=".")
    main()


def dice_roll():
    """
Function below emulates dice rolls. Generates two random integers ranging from
1-6 to simulate this. Sum of these random "dice rolls" are computed and user
must guess the sum correctly to win.
    """
    print("\n\nFor this game you will bet on the sum of two dice rolls.")
    print("If you guess the correct total of the two, "
          "you win. If not you lose.")
    sum_roll = 0
    guess_roll = input("\nWhat do you think the sum "
                       "of your two rolls will be? ")
    try:
        int(guess_roll)
        validation = True
    except ValueError:
        validation = False
    if not validation:
        print('\nThat is not a valid value. Please try again.\n')
    print("You selected", guess_roll, end="!")
    print("\nLet's see how lucky you are today.")
    begin = input("\nPress ENTER to roll your dice. ")
    if begin == "":
        # First roll generates a random number from one to six.
        print("\nRolling", end="")
        dot()
        roll_1 = random.randint(1, 6)
        sum_roll += roll_1
        print("\nYou rolled a", roll_1, end="!")

        # Second roll generates another random number from one to six.
        for _ in range(1):
            print("\n\nRolling again", end="")
            dot()
            roll_2 = random.randint(1, 6)
            # Computes the sum from the two dice rolls.
            sum_roll += roll_2
            print("\nYou rolled a", roll_2, end="!")
            print("\n")
        # If user guessed correct number, winning message will appear.
        if sum_roll == guess_roll:
            print("You win! The sum of your two rolls was", sum_roll, end="")
            print(" which was equal to your guess of", guess_roll, end="!")
            time.sleep(1)
        else:
            # If user guessed the incorrect number, losing message appears.
            print("You lost! The sum of your two rolls was", sum_roll, end="")
            print(" which was NOT equal to your guess of", guess_roll, end="!")
            time.sleep(1)
    print()
    main()


def directory():
    """
Function below is a directory that explains the meanings behind all functions
stored in main function in case the user is confused.
    """
    print("\nALL AVAILABLE COMMANDS:")
    print("Commands are denoted within quotation marks.\n")
    print("'math' = general arithmetic "
          "(addition, subtraction, multiplication, division, etc.)")
    print("'radians' = calculates radian and degree value of any number")
    print("'mmr' = calculates mean, median, and range "
          "of any set of given numbers")
    print("'guess' = generates a random number and "
          "gives user three chances at guessing it")
    print("'dice' = dice game that prompts user to bet on the sum of two di")
    terminate = input('\nPress ENTER when you are ready '
                      'to return back to the console.\n')
    if terminate == "":
        main()
    else:
        main()


def main():
    """
This is the main function. This function acts as a console that allows the
user to traverse through different functions.
    """
    print("\nYou are currently in the console.")
    print("Console Commands:")
    print("\n'math'")
    print("'radians'")
    print("'mmr'")
    print("'guess'")
    print("'dice'")
    print("'terminate'")
    # Takes user to desired function or calls directory (help menu)
    guide = input("\nEnter a command or type 'directory' for assistance: ")
    if guide.lower() == 'math':
        print('Okay ' + name + '. Navigating to math calculator', end='')
        dot()
        math_main()
    elif guide.lower() == 'radians':
        print('Okay ' + name +
              '. Navigating to the radians and degrees calculator', end='')
        dot()
        radians()
    elif guide.lower() == 'mmr':
        print('Okay ' + name +
              '. Navigating to mean, median, and range calculator', end='')
        dot()
        mean_med_range_inputs()
    elif guide.lower() == 'guess':
        print('Okay ' + name +
              '. Navigating to the guessing game', end='')
        dot()
        guessing_game()
    elif guide.lower() == 'dice':
        print('Okay ' + name + '. Navigating to dice game.', end='')
        dot()
        dice_roll()
    elif guide.lower() == "terminate":
        print("Thanks for stopping by ", name, "!", sep="")
        # This utilizes the exit function from sys module to end program.
        import sys
        sys.exit()
    elif guide.lower() == 'directory':
        directory()
    else:
        print("Oops! Sorry but that is an invalid input ", name,
              ". Returning back to console.", sep="")
        main()


main()
