import os
from colors import OPENGREEN, CLOSECOLOR

file = open("./tekst.txt", "r")

lineCount = 0
wordCount = 0
maxLine = 0
for line in file:
    counter = 0
    for e in line:
        counter += 1

    if counter > maxLine:
        maxLine = counter

    txt = line.split()
    wordCount += len(txt)
    lineCount += 1
    print(line, end="")

print("\n")
print(f"Bytes Count: {OPENGREEN}{os.path.getsize('./tekst.txt')}{CLOSECOLOR}")
print(f"Line Count: {OPENGREEN}{lineCount}{CLOSECOLOR}")
print(f"Word Count: {OPENGREEN}{wordCount}{CLOSECOLOR}")
print(f"Max Line Length: {OPENGREEN}{maxLine}{CLOSECOLOR}")
