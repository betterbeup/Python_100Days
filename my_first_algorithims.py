#Factorials Basic
def iterative_factorial(number):
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    print(fact)

iterative_factorial(5)

def recur_factorial(number):
    if number == 1:
        return number
    else:
        temp = recur_factorial(number-1)
        temp = temp * number
    return temp

print(recur_factorial(5))