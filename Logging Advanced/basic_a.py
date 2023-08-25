import logging
import Friendship_a
"""
When we import a module with a logging, it will occupy the root logger. So if we do not create another variable
or logger to the our main file, it can not overwrite to root logger. So our logging do not work as we want.
"""

#To get rid of the above problem, we are create another logger other than root.
logger = logging.getLogger(__name__)
#We set our new logger level to DEBUG
logger.setLevel(logging.DEBUG)

#We create a new formatter varibale to use it at the file handler
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

#Create a file_handler variable to use it on the new logger
file_handler = logging.FileHandler("test_a.log")
#I want to filter the logging which goes to file as hierarchy, so I set the file logging's level
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

#If you want to show the logging on the internal terminal, we can use the stream handler addition to file handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

#We add new handler to the logger which as file_handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def multiply(sayi1, sayi2):
    """Multiply function"""
    return sayi1 * sayi2

def divide(sayi1, sayi2):
    """Division function"""
    try:
        result = sayi1 / sayi2
    except ZeroDivisionError:
        #If you want to write just the logging message
        #logger.error("Tried to divide a number with zero.")

        #If you want to also write the traceback with the error, you can use the exception instead of the error
        logger.exception("Tried to divide a number with zero.")
    else:
        return result

def add(sayi1, sayi2):
    """Add function"""
    return sayi1+sayi2

def naming(name, surname):
    """Naming function"""
    return name + " " + surname


num1 = 20
num2 = 0
name = "Burak"
surname = "Zaifoğlu"

mul_result = multiply(num1,num2)
logger.debug("Multiply: {} * {} = {}".format(num1, num2, mul_result))

divide_result = divide(num1, num2)
logger.debug("Division: {} / {} = {}".format(num1, num2, divide_result))

add_result = add(num1, num2)
logger.debug("Adding: {} + {} = {}".format(num1, num2, add_result))

full_name = naming(name, surname)
logger.debug("Naming: {}".format(full_name))



