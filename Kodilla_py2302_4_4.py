import sys
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="logfile.log"
)

CleverChoice = (input("Choose the best option: 1. Split, 2. Multiplication, \
3. Addition, 4. Subtraction: \n"))

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def Split (a, b):
    logging.debug(f'Splitting {a}, {b}')
    result = float(str(a)) / float(str(b))
    logging.debug(f'Result: {result}')
    return result 

def Substraction (a, b):
    logging.debug(f'Substracting {a}, {b}')
    result = float(str(a)) - float(str(b))
    logging.debug(f'Result: {result}')
    return result 

def Multiplication (a, b, c):
    logging.debug(f'Multiplication {a}, {b}, {c}')
    result = float(str(a)) * float(str(b)) * float(str(c))
    logging.debug(f'Result: {result}')
    return result

def Addition (a, b, c):
    logging.debug(f'Addition {a}, {b}')
    result = float(str(a)) + float(str(b)) + float(str(c))
    logging.debug(f'Result: {result}')
    return result 
    
if CleverChoice == '1':
    a = (input ('First number: '))
    logging.debug(f'Value is float: {isfloat(a)}')
    b = (input ('Second number: '))
    logging.debug(f'Value is float: {isfloat(b)}')
    print (Split(a, b))


    
if CleverChoice == '2':
    MoreMultiplication = (input ('Do you want to muliply three numbers? y/n \n'))
    if MoreMultiplication == 'y':
        a = (input ('First number: '))
        logging.debug(f'Value is float: {isfloat(a)}')
        b = (input ('Second nubmer: '))
        logging.debug(f'Value is float: {isfloat(b)}')
        c = (input ('Third number: '))
        logging.debug(f'Value is float: {isfloat(c)}')
        print (Multiplication(a, b, c))
    if MoreMultiplication == 'n':
        a = (input ('First number: '))
        logging.debug(f'Value is float: {isfloat(a)}')
        b = (input ('Second nubmer: '))
        logging.debug(f'Value is float: {isfloat(b)}')
        print (Multiplication(a, b, c = 1))

if CleverChoice == '3':
    MoreAdds = (input ('Do you want to add three numbers? y/n \n'))
    if MoreAdds == 'y':
        a = (input ('First number: '))
        logging.debug(f'Value is float: {isfloat(a)}')
        b = (input ('Second nubmer: '))
        logging.debug(f'Value is float: {isfloat(b)}')
        c = (input ('Third number: '))
        logging.debug(f'Value is float: {isfloat(c)}')
        print (Addition(a, b, c))
    if MoreAdds == 'n':
        a = (input ('First number: '))
        logging.debug(f'Value is float: {isfloat(a)}')
        b = (input ('Second nubmer: '))
        logging.debug(f'Value is float: {isfloat(b)}')
        print (Addition(a, b, c = 0))

if CleverChoice == '4':
    a = (input ('First number: '))
    logging.debug(f'Value is float: {isfloat(a)}')
    b = (input ('Second number: '))
    logging.debug(f'Value is float: {isfloat(b)}')
    print (Substraction(a, b))


    
    
