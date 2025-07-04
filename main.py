import random
random_choice = random.choice([0 , 1 , -1])

computer = random_choice
youstr = input("Enter ,R for rock , P for paper , S for scissors : ")
you_dict = {"r":-1 , "p":0 , "s":1}
dict_again = {-1:"rock" , 0:"Paper" , 1:"Scissors"}

you = you_dict[youstr]

print(f"you choosed {dict_again[you]} and Computer chosed {dict_again[computer]}")
if (you == computer):
    print("Its a draw")
else:
    if(you == -1 and computer == 0):
        print("You lost")
    elif(you == -1 and computer == 1):
        print("You win")
    elif(you == 0 and computer == 1):
        print("You Lost")
    elif(you == 0 and computer == -1):
        print("You win")
    elif(you == 1 and computer == 0):
        print("You win")
    elif(you == 1 and computer == -1):
        print("You Lost")