"""1"""
from operator import truediv

print(len(input("what is your name")))
$


'''2'''
number_in = input( " what is a number in your mind? ")
number_in = int(number_in)
number_1 = int(number_in/10)
number_2 = number_in%10
number_final = number_1 + number_2
print(number_final)
$

'''3'''
number1 = int(input("type your number."))
if number1 % 2 == 1:
   print("your number is odd")
else:
   print("your number is even")
$

'''4'''
weight = float(input("enter your weight in kg."))
height = float(input("enter your height in M."))
final = weight / (height ** 2)
if final <= 18.5:
    print("under weight")
    print(final)
elif final <= 25:
    print("normal weight")
    print(final)
elif final <= 30:
    print("over weight")
    print(final)
elif final <= 35:
    print("obese")
    print(final)
else:
    print("clinically obese")
    print(final)
$


'''5'''
year = int(input("write your year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400==0:
            print(year," is  leap")
        else:
            print(year, " is not  leap")
    else:
        print(year, " is not  leap")
else:
    print(year, " is not  leap")
$


'''6'''
import random
ny = random.randint (0, 1)
if ny == 0:
    print("tail")
else:
    print("head")
$
'''7'''
row1 = ["y", "y", "y"]
row2 = ["y", "y", "y"]
row3 = ["y", "y", "y"]
map = [row1 ,row2 ,row3]
print(f"{row1}\n{row2}\n{row3}")
p = input("where you want ?")
horizon = int(p[0])
vertical = int(p[1])
a = map[vertical-1]
b = a[horizon-1] = "x"
print(f"{row1}\n{row2}\n{row3}")
$
'''8'''
import random
select = int(input("select from 0 = rock ,1 = paper ,2 = scissors:"))
number1 = "rock"
number2 = "paper"
number3 = "scissors"
random_number = random.randint(0, 2)
if random_number == select:
    print("equal")
elif random_number == 1 and select == 0:
    print("you lose")
elif random_number == 2 and select == 0:
    print("you win")
elif random_number == 0 and select == 1:
    print("you win")
elif random_number == 2 and select == 1:
    print("you lose")
elif random_number == 0 and select == 2:
    print("you lose")
elif random_number == 1 and select == 2:
    print("you win")
$
'''9'''
import random
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a' , 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i']
symbols = ['!','@','#','$','%','^','&','*']
nr_letters = int(input("how many letters you like?\n"))
nr_number = int(input("how many number you like?\n"))
nr_symbols = int(input("how many symbols you like?\n"))
password = ""
for i in range(1,nr_letters + 1):
    password += random.choice(letters)
for i in range(1,nr_number + 1):
    password += random.choice(number)
for i in range(1,nr_symbols + 1):
    password += random.choice(symbols)
print(password)
$
'''10'''
import random
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a' , 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i']
symbols = ['!','@','#','$','%','^','&','*']
nr_letters = int(input("how many letters you like?\n"))
nr_number = int(input("how many number you like?\n"))
nr_symbols = int(input("how many symbols you like?\n"))
password = ""
for i in range(1,nr_letters + 1):
    password += random.choice(letters)
for i in range(1,nr_number + 1):
    password += random.choice(number)
for i in range(1,nr_symbols + 1):
    password += random.choice(symbols)
print(password)
$
'''11'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1 = int(input("what is your first number?"))
num2 = int(input("what is your second number?"))
for symbol in operations:
    print(symbol)
operation_symbol = input("select one of symbol from the line above:")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
$
'''12'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1 = int(input("what is your first number?"))
num2 = int(input("what is your second number?"))
for symbol in operations:
    print(symbol)
operation_symbol = input("select one of symbol from the line above:")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")
operation_symbol = input("select another symbol:")
num3 = int(input("what is your another number?"))
second_answer = calculation_function(calculation_function(num1, num2), num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
$
'''13'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1 = int(input("what is your first number?"))
for symbol in operations:
    print(symbol)
should_continue = True
while should_continue:
    operation_symbol = input("select one symbol :")
    calculation_function = operations[operation_symbol]
    num2 = int(input("what is your next number?"))
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"type 'y' for continue whit {answer},or type 'n' for end") == "y" :
        num1 = answer
    else:
        should_continue = False
$
'''14'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator() :
    num1 = int(input("what is your first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("select one symbol :")
        calculation_function = operations[operation_symbol]
        num2 = int(input("what is your next number?"))
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' for continue whit {answer},or type 'n' to start new calculation ") == "y" :
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
$
'''15'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator() :
    num1 = float(input("what is your first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("select one symbol :")
        calculation_function = operations[operation_symbol]
        num2 = float(input("what is your next number?"))
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' for continue whit {answer},or type 'n' to start new calculation ") == "y" :
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
$
'''16'''