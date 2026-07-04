import os
import secrets as sc
import string


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def password(length):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += sc.choice(char_pool)

    return password

def main():
    try:
        pass_length = int(input("Enter the length of password: "))
        input(f"Password: {password(pass_length)}")
        clear_console()
        main()

    except:
        input("Invalid length of password.")
        clear_console()
        main()

main()