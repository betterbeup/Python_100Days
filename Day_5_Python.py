import random
#Day 5 of Python Learning, Loops, Range, and Code Blocks
#For Loops
# fruits = ["Pineapples", "Mangoes", "Kiwi"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# student_scores = [50, 87, 120, 90, 43, 88, 72, 101, 141, 100]
# total_exam_score =  sum(student_scores)
# average_exam_score = total_exam_score / len(student_scores)
# max_score = print(max(student_scores))
# print(total_exam_score)
# print(average_exam_score)
# max_score_for_loop = 0
# previous_number = 0
# #imitate max
# for num in student_scores:
#     if num >= num and previous_number <= num:
#         previous_number = num
# print(previous_number)

#Range function
# for number in range(1, 11, 3):
#     print(number)
# total_addition = 0
# for number_addition in range(1, 101):
#     total_addition += number_addition
# print(total_addition)
##
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

##Password Generator
lowercase_and_uppercase_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]
print("Welcome to a high security password generator!")
total_letters = input("How many letters would you like in your password?\n")
total_numbers = input("How many numbers would you like in your password?\n")
total_symbols = input("How many symbols would you like in your password?\n")
final_password_list = ""
for letter in range(1, int(total_letters) + 1):
    final_password_list += lowercase_and_uppercase_alphabet[random.randint(0,51)]
for number in range(1, int(total_numbers) + 1):
    final_password_list += numbers[random.randint(0,9)]
for symbol in range(1, int(total_symbols) + 1):
    final_password_list += special_characters[random.randint(0,9)]    
secure_password = ''.join(random.sample(final_password_list, len(final_password_list)))
print(f"Your high security password is: {secure_password}")
