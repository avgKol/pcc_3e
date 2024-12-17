from pathlib import Path
import json

number =input("Input a number")
filename = Path("C:/Temp/pcc_3e/chapter_10/favorite_number.json")
contents = json.dumps(number)
filename.write_text(contents)

contents = filename.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}")

def get_stored_number():
    filename = Path("C:/Temp/pcc_3e/chapter_10/favorite_number.json")
    if filename.exists():
        contents = filename.read_text()
        number = json.loads(contents)
        return number
    else:
        return None
    
def prompt_for_new_number():
    number = input("What is your favorite number? ")
    filename = Path("C:/Temp/pcc_3e/chapter_10/favorite_number.json")
    contents = json.dumps(number)
    filename.write_text(contents)
    return number

def greet_user():
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It's {number}")
    else:
        number = prompt_for_new_number()
        print(f"We'll remember that your favorite number is {number}")
        
greet_user()