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
 
# Adding
add = lambda x,y: x + y
 
# Subtracting
subtract = lambda x,y: x - y
 
# Multiplying
multiply = lambda x,y: x * y
 
# Dividing
divide = lambda x,y: x/y
 
# Operations
operations = {'+': add, '-': subtract, '*': multiply, '/': divide,}
 
def Calculator():
    print(logo)
    
    num1 = float(input('What is the first number: '))
    for operation in operations.keys(): print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input('Pick an operation: ')
        try:
            num2 = float(input('What is the next number: '))
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # Handling a zero division error    
        except ZeroDivisionError:
            print("A ZeroDivisionError occurred.")
            break
        user_response = \
        (f"Type 'y' to continue calculating with {answer}, or type 'n' to clear: ") 
        
        if input(user_response) == 'y':
          num1 = answer
        else:
          Calculator()
                
Calculator()

