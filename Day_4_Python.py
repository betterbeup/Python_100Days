#Day_4_Python learning and project (randomization)
import random
# import my_first_module_Day4

##Random examples
# print(my_first_module_Day4.my_favorite_number)
# random_integer = random.randint(1, 10)
# print(random_integer)
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
# random_float = random.uniform(1, 10)
# print(random_float)
##Head or Tails Program
# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("Heads")
# elif random_heads_or_tails == 1:
#     print("Tails")
# else:
#     print('error')

##lists
# my_favorite_fruits = ["pinapples", "mangoes", "kiwis"]
# my_favorite_fruits.append("bananas")
# my_favorite_fruits.extend(["oranges", "apples", "watermelon"])
# do_you_like_watermelon = input("Do you like watermelon? y or n\n")
# if do_you_like_watermelon == 'n':
#     my_favorite_fruits.pop()
# print(my_favorite_fruits)

##Banker roulette(my solution)
# friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# random_picker = random.randint(0, 4)
# print(friends[random_picker])
# #Teachers solution
# print(random.choice(friends))

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Celery", "Potatoes", "Tomatoes"]

##Rock Paper Scissors Project!
rps_list = ["Rock", "Paper", "Scissors"]
print("Are you ready to play Rock Paper Scissors!?!?!")
decision = int(input("Which do you choose, 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
computer_decision = random.randint(0, 2)
if decision == 0 and computer_decision == 1:
    print("You lose, you picked Rock, and the computer picked Paper!")
elif decision == 1 and computer_decision == 2:
    print("You lose, you picked Paper, and the computer picked Scissors!")
elif decision == 2 and computer_decision == 0:
    print("You lose you picked Scissors, and the computer picked Rock!")
elif decision == 0 and computer_decision == 2:
    print("You win, you picked Rock, and the computer picked Scissors!")
elif decision == 1 and computer_decision == 0:
    print("You win, you picked Paper, and the computer picked Rock!")
elif decision == 2 and computer_decision == 1:
    print("You win, you picked Scissors, and the computer picked paper!")
else:
    print(f"It was a draw! You both picked {rps_list[decision]}!")





