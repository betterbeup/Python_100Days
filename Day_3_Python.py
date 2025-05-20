#Day_3_Python

##Rollercoaster tickets and picture
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in inches\n"))
# bill = 0

# if height >= 48:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?\n"))
#     if age <= 12:
#         bill = 5
#         print(f"Your child ticket is ${bill}")
#     elif age <= 17:
#         bill = 10
#         print(f"Your teenager ticket is ${bill}")
    # elif age >= 45 and age <= 55:
    #     bill = 0
    #     print(f"Your midlife crisis ticket is ${bill}")
#     else:
#         bill = 15
#         print(f"Youour adult ticket is ${bill}")
#     wants_photo = input("Do you want a photo on your ride? y for yes, n for no \n")
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your final bill is ${bill}")    
# else:
#     print("You can NOT ride the rollercoaster")

# = is assigning a variable, == is equal to, >= greater than or equal to
# % Modulo Operator % is the remainder of a division sequence
#Example is 10 % 5 = 0  or 10 % 3 = 1

# first_number = int(input("What is a number you want to check\n"))

# if first_number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
##Pizza delivery
# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want, S, M, or L: ")
# pepperoni = input("Do you want pepperonies on your pizza?: ")
# extra_cheese = input("Do you want extra cheese on your pizza?: ")
# tax = 1.06
# bill = 0

# if size == "s":
#     bill = 8
# elif size == 'm':
#     bill = 10
# elif size == 'l':
#     bill = 12
# else:
#     print("You inputted the wrong inputs, try again")    
# if pepperoni == 'y':
#     bill += 3
# if extra_cheese == 'y':
#     bill += 2.5
# total_bill = round(bill * tax, 2)
# print(f"Your final bill is {total_bill}")

#logical operators
# and, or, not
# a = 12
# a > 10 and a < 13
# a > 10 or a < 9
# not a < 10 == true

##Day_3_Project Crazy Castle
# print("Welcome to Crazy Castle!\nYour mission is to escape from the Crazy Castle.\nYou are in the basement.")
# directions1 = input("Do you want to take the left or the right to try to escape?\n")
# if directions1 == "left":
#     print("Good, there's only one guard to destroy in the left door.")
#     weapon = input("You are now in the weapons station do you want an axe or a sword within distance before the guard gets to you?\n")
#     if weapon == "axe":
#         print("Swing your axe fast and take down the guard before he gets to you!")
#     elif weapon == "sword":
#         print("Test your samuari might and defeat the guard before he gets you first!")
#     directions2 = input("Good job defeating the guard! Do you want to take the ladder in the room or explore the basement?\n")
#     if directions2 == "ladder":
#         print("Good job you are on the main floor and you see a window in sight, and you went through the window and escaped from the Crazy Castle!")
#     elif directions2 == "explore":
#         print("Since you decided to explore the basement, the other 5 guards found you and chopped off your legs and now you're stuck here forever!")
# elif directions1 == "right":
#     print("Oh no you are surrounded by 5 guards and now they have locked you away again and chopped off your legs, try again!")

