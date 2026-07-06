import os
import math

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("""Select one: 
1. Encode
2. Decode""")
    try:
        choice = int(input(">> "))
    except:
        clear_console()
        input("Invalid input. Try again.")
        clear_console()
        main()
    if(choice == 1):
        clear_console()
        msg = input("Enter your message >> ")
        print()
        input(f"Output >> {encode(msg)}")
        clear_console()
        main()
    elif(choice == 2):
        clear_console()
        msg = input("Enter your encoded message >> ")
        print()
        input(f"Output >> {decode(msg)}")
        clear_console()
        main()
    else:
        clear_console()
        input("Invalid input. Try again.")
        clear_console()
        main()


def encode(msg):
    encoded_msg = ""

    for c in msg:
        ascii = ord(c)
        encoded_ascii = f"{((pow(ascii, 2) * 6) + 69):05d}"
        encoded_msg += encoded_ascii
    
    return encoded_msg

def decode(msg):
    decoded_msg = ""

    try:
        for _ in range(int(len(msg)/5)):
            num = int(msg[:5])
            decoded_ascii = int(math.sqrt((num-69)/6))
            decoded_msg += chr(decoded_ascii)
            msg = msg[5:]
    except:
        clear_console()
        input("Failed to decode message. Try again.")
        clear_console()
        main()

    return decoded_msg

main()