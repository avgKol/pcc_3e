from pathlib import Path
import typing

path = Path("C:/Temp/pcc_3e/chapter_10/learning_python.txt")
contents = path.read_text()
if contents is not None:
    print(contents)
lines = contents.splitlines()
for line in lines:
    print(line)