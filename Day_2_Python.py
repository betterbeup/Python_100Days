#Day_2_Python
 #Subscripting (the last letter is -1, 0 is first letter)
# print("Hello"[-1])

# #Integer = whole numbers
# print(123 + 345)

# #Large integers readability 
# print(123_456_789)

# #Float = Floating point number
# print(3.14159)

# # Boolean
# print(True)
# print(False)

# # Check datatype of a variable
# print(type("Hello"))
# print(type(123))
# print(type(False))
# print(type(5.75))

# #Changing string to int for math
# print(int("123") + int("345"))

# #Fix this line
# print("Number of letters in your name: " + str(len(input("Enter your name "))))

# #Mathematical Operations (regular division is a float)
# print(123 + 456 - 10 * 3 / 2)
# #Division as integer
# print(4 // 2)
# #To the power of 
# print(4**4)

#PEMDAS (Parantheses, Exponents, Multiplication OR Division, Addition OR Subtraction) (LEFT TO RIGHT)

# bmi = 84 / 1.65 ** 2
# bmi2 = 84 / (1.65 * 1.65)

# #int rounds down(flooring), round is closest to the whole number
# print(int(bmi))
# print(round(bmi2))
# #Two decimal places if you want more specific (or money)
# print(round(bmi, 2))

# score = 0
# height = 1.8
# is_winning = True
# #user scores a point
# score += 2
# score *= 8
# print(score)

# # f-strings to insert all different variables into a string
# print(f"Your score is = {score}, your height is {height}, if you are winning is {is_winning}")


#Day Two(2) Project:
#  Tip Calculator
print("Welcome to the tip Calculator")
print("What was the total bill? ")
total_bill = float(input(("$")))
percentage_tip = int(input("How much of a tip would you like to give? 10%, 15%, 20%\n"))
total_people_splitting_bill = int(input("How many people are splitting the bill?\n"))
total_bill_with_tip = total_bill + (percentage_tip / 100 * total_bill)
final_pay_for_each_person = total_bill_with_tip / total_people_splitting_bill
print("Each person should pay: $" + str(final_pay_for_each_person))
