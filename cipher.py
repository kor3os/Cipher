# System calls
import sys


class DispStr:
    # Final string when function returns True
    ENDT = "Encryption finished.\nExiting..."
    # Final string when function returns False
    ENDF = "Something went wrong. Refer to the error above.\nExiting..."
    # String when "increment" is negative
    INCNEG = "Please a number above or equal to zero. Negative numbers are not supported yet."
    # String when no arguments are passed
    NOARG = "Please specify a cipher or use -h for help and infos."
    # Help string
    HELP = """HELP:
    This program allows you to pass a string through the implemented ciphers.
    
    1. Caesar Cipher: increments each character by the given integer.
    Used """


# Caesar Cipher
def caesar(increment, string):
    # Init vars
    ciphstring = ""
    # If the passed increment cannot be converted to integer, exit
    try:
        increment = int(increment)
    except ValueError:
        print("Please use a valid integer!")
        return False
    if increment < 0:
        print(DispStr.INCNEG)
        return False
    # String change for loop
    for c in string:
        ciphc = ord(c) + increment
        # if "overload" (aka overstepping z or Z), come back to a
        if 90 < ciphc < 97:
            ciphc = ciphc - 26
            pass
        elif ciphc > 122:
            ciphc = ciphc - 26
            pass
        # Concat char to final string
        ciphstring = ciphstring + chr(ciphc)
    print("Here is your ciphered string: " + ciphstring)
    return True
    pass


def main(argv):
    if len(argv) > 1:
        if argv[1] == "-h":
            print(DispStr.HELP)
            pass
        # Caesar cipher
        elif argv[1] == "-ca":
            check = caesar(argv[2], argv[3])
            print(DispStr.ENDT) if check else print(DispStr.ENDF)
            pass
    else:
        print(DispStr.NOARG)
        pass
    pass


if __name__ == "__main__":
    # For caesar => cipher.py -ca <how much to increment or decrement> <string>
    main(sys.argv)
    pass
