import sys
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="logfile.log"
)

clever_choice = input("Choose the best option: 1. Split, 2. Multiplication, \
3. Addition, 4. Subtraction: \n")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def divide (a, b):
    logging.debug(f'Dividing {a}, {b}')
    result = float(str(a)) / float(str(b))
    logging.debug(f'Result: {result}')
    return result 

def substraction (a, b):
    logging.debug(f'Substracting {a}, {b}')
    result = float(str(a)) - float(str(b))
    logging.debug(f'Result: {result}')
    return result 


def multiplication(numbers):
    logging.debug(f'Multiplication {numbers}')
    result = 1
    for num in numbers:
        result *= float(str(num))
    logging.debug(f'Result: {result}')
    return result

def addition (numbers):
    logging.debug(f'Addition {numbers}')
    result = 1
    for num in numbers:
        result += float(str(num))
    logging.debug(f'Result: {result}')
    return result 
    
if clever_choice == '1':
    a = (input ('First number: '))
    logging.debug(f'Value is float: {isfloat(a)}')
    b = (input ('Second number: '))
    logging.debug(f'Value is float: {isfloat(b)}')
    print (divide(a, b))


    
if clever_choice == '2':
    user_input = input("Enter numbers separated by commas: ")
    numbers = user_input.split(',')
    print(multiplication(numbers))


if clever_choice == '3':
    user_input = input("Enter numbers separated by commas: ")
    numbers = user_input.split(',')
    print(addition(numbers))

if clever_choice == '4':
    a = (input ('First number: '))
    logging.debug(f'Value is float: {isfloat(a)}')
    b = (input ('Second number: '))
    logging.debug(f'Value is float: {isfloat(b)}')
    print (substraction(a, b))


    
    
