import logging

#Logging is a built-in module in Python so we do not need to download it


'''
Standard Logging Levels:

*Default logging level is Warning.

- DEBUG: Detailed information, typically of interest only when diagnosing problems.

- INFO: Confirmation that things are working as expected.

- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

- ERROR: Due to a more serious problem, the software has not been able to perform some function.

- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

'''

'''
As I said earlier, the default logging level is warning so, if we call the logging with debug it will return anything to us
Then we have to choice, either we use logging.warning or we change the logging level. 
Lets change the logging level
'''

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
#With this config we print the loggins to a file named test.log. Also we we change the logging printing format as time, levelname and message.

#Basic functions to test and learn the logging functions

def multiply(sayi1, sayi2):
    """Multiply function"""
    return sayi1 * sayi2

def divide(sayi1, sayi2):
    """Division function"""
    return sayi1/sayi2

def add(sayi1, sayi2):
    """Add function"""
    return sayi1+sayi2

def naming(name, surname):
    """Naming function"""
    return name + " " + surname


num1 = 20
num2 = 50
name = "Burak"
surname = "Zaifoğlu"

mul_result = multiply(num1,num2)
'''
Normally, we use the print function to check the result is true or not
print("Multiply: {} * {} = {}".format(num1, num2, mul_result))
'''
logging.debug("Multiply: {} * {} = {}".format(num1, num2, mul_result))

divide_result = divide(num1, num2)
logging.debug("Division: {} / {} = {}".format(num1, num2, divide_result))

add_result = add(num1, num2)
logging.debug("Adding: {} + {} = {}".format(num1, num2, add_result))

full_name = naming(name, surname)
logging.debug("Naming: {}".format(full_name))



