import typing
from pathlib import Path

# Prompts the user for their name
name = input("What is your name? ")
filename = Path("C:/Temp/pcc_3e/chapter_10/guest.txt")
filename.write_text(name)

number1 = input("Please enter a number: ")
number2 = input("Please enter another number: ")
try:
    number1 = int(number1)
    number2 = int(number2)
    
except ValueError:
    print("Invalid imput .Please enter a valid number\n.")

else:
    try:
        result = number1/number2
    
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(result)

    finally:
        print("Thank you for using the program")
