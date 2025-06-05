#Calculator App Second try
def calculator():
    first_number = float(input('What is the first number you want to calculate with?'))
    type_of_calculation = input('\n+\n-\n*\n/\n')
    print('Pick an operation! ')
    second_number = float(input("What's the next number you want to calculate with?"))
    if type_of_calculation == '+':
        first_number += second_number
        continue_calculation = input("Would you like to calculate again? 'y' for yes 'n' for no. ")
        while continue_calculation == 'y':
                print('Total is ' + str(first_number))
                float(first_number)
                type_of_calculation = input('\n+\n-\n*\n/\n')
                second_number = int(input("What's the next number you want to calculate with?"))
                if type_of_calculation == '+':
                    first_number+= second_number
                    second_number /= float(first_number)
                elif type_of_calculation == '-':
                    first_number -= second_number
                elif type_of_calculation == '*':
                    first_number *= second_number
                elif type_of_calculation == '/':
                    second_number /= float(first_number)
        else:
            print('Total is ' + str(first_number))
calculator()

#ChatGPT Calculator
#def calculator():
#     print("Basic Calculator")
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             result = num1 + num2
#             print("Result:", result)
#         elif choice == '2':
#             result = num1 - num2
#             print("Result:", result)
#         elif choice == '3':
#             result = num1 * num2
#             print("Result:", result)
#         elif choice == '4':
#             if num2 != 0:
#                 result = num1 / num2
#                 print("Result:", result)
#             else:
#                 print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid input")

# calculator()