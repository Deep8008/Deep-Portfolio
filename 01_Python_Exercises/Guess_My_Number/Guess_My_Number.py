import random

bigger_answer = ("My number is smaller than yours<")

smaller_answer = ("My number is bigger than yours>")

right_answer = ("You guessed the Right number!")

tell_guess = ("Please tell a number: ")

def welcome():
    print("Welcome To Guess_My_Number game!\n\
          when you start the game, i will choose a number between 1 to 20\n\
          then you should guess it and i will i will guide you until you guess the right number\n\
          let the game begin...")


def finish(number, count):
    print(f"My number was ({number}) and you guessed it in ({count}) times!")
    answer = input("Do you want to play again? (yes/no): ")
    if answer.upper() in ["Y", "YES"]:
        return True
    elif answer.upper() in ["N", "NO"]:
        return False
    else:
        print("invalid answer! please answer with (y, yes, n, no)")


def win(computer_number, guess):
    return computer_number == guess


def answer(computer_number, guess):
    if computer_number < guess:
        return bigger_answer
    elif computer_number > guess:
        return smaller_answer
    else:
        return right_answer


def get_a_guess():
    ans = int(input(tell_guess))
    return ans


welcome()
continue_playing = True
while(continue_playing):
    computer_number = random.randint(1, 20)
    
    guess = 0
    count = 0
    
    while(not win(computer_number, guess)):

        count += 1
        guess = get_a_guess()

        print(answer(computer_number, guess))
    continue_playing = finish(computer_number, count)
