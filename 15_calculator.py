logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
#Add
def add(n1, n2):
  return n1 + n2
 
 #Subtract
def subtract(n1, n2):
  return n1 - n2
 
 #Multiply
def multiply(n1, n2):
  return n1 * n2
 
 #Divide
def divide(n1, n2):
  return n1 / n2

operators={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("What's the first number?\n"))

for symbols in operators:
    print(symbols)

should_continue = True
while should_continue:
    operator_symbols=input("Pick an operation from the above line?\n")

    num2 = int(input("What's the second number?\n"))

    calculation_function=operators[operator_symbols]

    answer = calculation_function(num1,num2)

    print(f"{num1} {operator_symbols} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:") == 'y':
        num1 = answer
    else:
        should_continue = False