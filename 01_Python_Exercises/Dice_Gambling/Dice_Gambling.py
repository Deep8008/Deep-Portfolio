from random import randint
print("Welcome to the gambling game!\n\
      The game rules:\n\
      a dice will roll and you should guess the number.\n\
      if your guess was right, i will pay 50$ to you, and if it wasn't right, you should give me 30$.")

balance = 500
game = True
dice = randint(1, 6)

while game == True:
    print("dice is rolling...")
    print("guess the number:")
    guess = int(input())
    print("dice rolled,\nYour Guess Is: ", guess)
    if guess == dice:
        print(f"the number is right!! ({dice})\nyou won 50$, Congrats!")
        balance += 50
        print(f"Balance: {balance}")
        continue
    else:
        print(f"you lost! the number is wrong!\nthe number was {dice}!")
        balance -= 30
        print(f"Balance: {balance}")
    dice = randint(1, 6)
        
    if balance < 30:
        game = False
        print(f"you are broke, you lost all of your money on gambling!\nBalance: {balance}")
