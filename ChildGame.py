# Stone paper scissors Game
# import pyinstaller
import random
chracters=[ "1", "2", "3"]
print( "1 for stone","2 for paper","3 for scissors")
computer_choice= random.choice(chracters)
no_of_chance=10
chance=0
human_point=0
computer_point=0


while no_of_chance > chance:

    Your_input=input(" Select your input\nStone " " Paper " " Scissors ")
    computer_input =random.choice(chracters)
    # if both input same value

    if computer_input==Your_input:
        print("Match Tie\n kumbh ke bhai na mila gaye\n\n")

    # If you input value is stone
    elif  Your_input=="1" and computer_input=="2":
       computer_point = computer_point +1
       print("bhai mujhe paper ne pakad liya  \n computer wins 1 point\n\n")
       chance = chance +1

    elif  Your_input=="1" and computer_input=="3":
        human_point = human_point +1
        print("pathar se scissors ko todh dala \n you wins 1 point\n\n")
        chance = chance + 1
   #if you input paper

    elif  Your_input=="2" and computer_input=="1":
        human_point = human_point +1
        print("paper se pathar ko pakadh liya \n you wins 1 point\n\n")
        chance = chance + 1



    elif  Your_input=="2" and computer_input=="3":
        computer_point = computer_point +1
        print("Me barbadh ho gya kachi ne mujhe kar diya \n computer wins 1 point\n\n")
        chance = chance + 1


    #if your input value is scissors

    elif Your_input == "3" and computer_input == "1":
        computer_point = computer_point + 1
        print("Mujhe kuchal diya gya!! \n computer wins 1 point\n\n")
        chance = chance + 1

    elif Your_input == "3" and computer_input == "2":
        human_point = human_point + 1
        print("kach!!! kach!!! kat paper ko \nyou wins 1 point\n\n")
        chance = chance + 1

        # declaring winners
        print("Game Over\n")
    elif computer_point > human_point:
        print(f"Mr. computer wins by Mr. champ point {computer_point} and your point is {human_point}")


    elif computer_point < human_point:
        print(f"You wins the match by Your point {computer_point} and the losser points is {human_point}")

    else: print("game over")










