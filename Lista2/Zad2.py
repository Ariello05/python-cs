import sys
from colors import *


tablica = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
tablica = list(tablica)


def encoded_from_file(filename):
    result = ""

    with open(filename, "r") as f:
        rest = ""
        while True:
            byte = f.read(1)

            if byte:

                byte = ord(byte)
                # BINARY STRING of character
                byte = bin(byte)[2:].rjust(8, '0')

                sliceSize = 6-len(rest)  # determine slicingSize
                proccess = rest + byte[:sliceSize]  # rest + BINARY STRING

                rest = byte[sliceSize:]  # remeber the rest
                # repeat if rest is whole CHARACTER to encode (6 bits)
                if sliceSize == 0:
                    result += tablica[int(proccess, 2)]  # append
                    proccess = rest[:6]  # procces 6 bits of byte
                    rest = rest[6:]  # rest of byte

                result += tablica[int(proccess, 2)]  # append

            else:
                sliceSize = 6-len(rest)
                rest += '0' * sliceSize  # add 0`s from right
                result += tablica[int(rest, 2)]  # append

                break
    return result


def decoded_from_file(filename):
    binary_words = ""

    with open(filename, "r") as f:
        while True:
            character = f.read(1)
            if character:

                try:
                    code = tablica.index(character)  # code as INT
                except ValueError:
                    print(f"{OPENRED}FAILURE{CLOSECOLOR}")
                    print(f"{OPENRED}Unkown symbol: {character}{CLOSECOLOR}")
                    raise

                character = str(bin(code))[2:8]  # BINARY STRING from INT
                left = 6 - len(character)
                character = "0"*left + character  # BINARY of size 6 - we add 0`s from left
                binary_words += character  # append

            else:
                break

    result = ""
    for i in range(0, len(binary_words), 8):
        word = binary_words[i:i+8]  # get 8 BITS
        intWord = int(word, 2)  # convert to INT
        character = intWord.to_bytes(
            (intWord.bit_length() + 7) // 8, 'big').decode()  # decode using UTF-8
        result += character  # append

    return result


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print(f"{OPENRED}FAILURE{CLOSECOLOR}")
            print(
                f"{OPENRED}Expected:{OPENBLUE} --encode|--decode input output{CLOSECOLOR}")
            print(
                f"{OPENYELLOW}Got:\t {OPENBLUE}{' '.join(sys.argv[1:])}{CLOSECOLOR}")
        else:
            t = sys.argv[1]
            inp = sys.argv[2]
            out = sys.argv[3]

            if t == "--encode":
                result = encoded_from_file(inp)
                print(f"{OPENGREEN}SUCCESS{CLOSECOLOR}")
                with open(out, "w") as f:
                    f.write(result)
            elif t == "--decode":
                result = decoded_from_file(inp)
                print(f"{OPENGREEN}SUCCESS{CLOSECOLOR}")
                with open(out, "w") as f:
                    f.write(result)
            else:
                print(f"{OPENRED}FAILURE{CLOSECOLOR}")
                print(
                    f"{OPENRED}Expected:{OPENBLUE} --encode|--decode input output{CLOSECOLOR}")
                print(
                    f"{OPENYELLOW}Got:\t {OPENBLUE}{' '.join(sys.argv[1:])}{CLOSECOLOR}")
    except:
        print(f"{OPENRED}FAILURE{CLOSECOLOR}")
        raise
