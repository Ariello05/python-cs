import os
import sys
from colors import OPENRED, OPENBLUE, OPENGREEN, CLOSECOLOR


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(f"{OPENRED}FAILURE{CLOSECOLOR}")
            print(
                f"Expected: {OPENBLUE}filename{CLOSECOLOR}")
            print(
                f"Got:\t  {' '.join(sys.argv[1:])}")
        else:
            filename = sys.argv[1]
            file = open(filename, "r")

            lineCount = 0
            wordCount = 0
            maxLine = 0
            for line in file:
                counter = len(line)

                if counter > maxLine:
                    maxLine = counter

                txt = line.split()
                wordCount += len(txt)
                lineCount += 1
                #print(line, end="")

            print("\n")
            print(
                f"Bytes Count: {OPENGREEN}{os.path.getsize('./tekst.txt')}{CLOSECOLOR}")
            print(f"Line Count: {OPENGREEN}{lineCount}{CLOSECOLOR}")
            print(f"Word Count: {OPENGREEN}{wordCount}{CLOSECOLOR}")
            print(f"Max Line Length: {OPENGREEN}{maxLine}{CLOSECOLOR}")
    except:
        print(f"{OPENRED}FAILURE{CLOSECOLOR}")
        raise
