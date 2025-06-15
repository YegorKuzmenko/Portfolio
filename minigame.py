import random


secret = random.randint(1,10)
tries = 3

print("Я загадал число,попробуй угадай")

while tries > 0:
    guess = int(input("Введи свое число:"))
    if guess == secret:
        print("Ты угадал")
        break
    elif guess < secret:
        print("Мое число больше")
        
    else:
        print("Мое число меньше")
        
    tries -= 1
    
if tries == 0:
    print("Ты проиграл, мое число :", secret)
        

        