from pathlib import Path
#Create two text files: cats.txt and dogs.txt. Write at least three names of cats and dogs in their respective files.
cats = Path("C:/Temp/pcc_3e/chapter_10/cats.txt")
dogs = Path("C:/Temp/pcc_3e/chapter_10/dogs.txt")
try:
    cats.write_text("Tom\nMax\nSam")
    dogs.write_text("Rex\nBuddy\nMax")
    print(cats.read_text())
    print(dogs.read_text())
    print("Files created successfully")
    
except Exception as e:
    print(f"An error occurred: {e}")