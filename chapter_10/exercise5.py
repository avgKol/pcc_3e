from pathlib import Path
import typing

#book.txt.Write a program that counts how many times the word "the" appears in the file.Compare the counts when using 'the' and 'the ' (with a space).

filename = Path("C:/Temp/pcc_3e/chapter_10/book.txt")
contents = filename.read_text()
words = contents.split()
count = words.count("the")
count2 = words.count("the ")
print(f"The word 'the' appears {count} times in the file.")
print(f"The word 'the ' appears {count2} times in the file.")