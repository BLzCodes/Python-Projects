RED = '\033[31m'
GRN = '\033[32m'
CYN = '\033[36m'
YLW = '\033[33m'
MGN = '\033[35m'
RST = '\033[0m'

def addition():
    try:
        result = float(input(f"{CYN}Number to add to: {RST}"))
    except:
        print(f"\n{RED}Provided input is not a number.{RST}\n")
        addition()
    print("")
    while True:
        raw_input = input(f"{CYN}Type a number to add or press {YLW}[ENTER]{CYN} for final result: {RST}")
        if not raw_input:
            print(f"\n{GRN}Final Result: {result}{RST}\n")
            input(f"Press {YLW}[ENTER]{RST} to return...\n")
            break
        try:
            num_input = float(raw_input)
        except:
            print(f"\n{RED}Provided input is not a number.{RST}\n")
            main_function()
        result += num_input
        print(f"{GRN}Addition result: {result}{RST}")
    main_function()
    

def subtraction():
    try:
        result = float(input(f"{CYN}Number to subtract from: {RST}"))
    except:
        print(f"\n{RED}Provided input is not a number.{RST}\n")
        subtraction()
    print("")
    while True:
        raw_input = input(f"{CYN}Type a number to subtract or press {YLW}[ENTER]{CYN} for final result: {RST}")
        if not raw_input:
            print(f"\n{GRN}Final Result: {result}{RST}\n")
            input(f"Press {YLW}[ENTER]{RST} to return...\n")
            break
        try:
            num_input = float(raw_input)
        except:
            print(f"\n{RED}Provided input is not a number.{RST}\n")
            main_function()
        result -= num_input
        print(f"{GRN}Subtraction result: {result}{RST}")
    main_function()

def multiplication():
    try:
        result = float(input(f"{CYN}Number to be multiplied: {RST}"))
    except:
        print(f"\n{RED}Provided input is not a number.{RST}\n")
        multiplication()
    print("")
    while True:
        raw_input = input(f"{CYN}Type a number to multiply by or press {YLW}[ENTER]{CYN} for final result: {RST}")
        if not raw_input:
            print(f"\n{GRN}Final Result: {result}{RST}\n")
            input(f"Press {YLW}[ENTER]{RST} to return...\n")
            break
        try:
            num_input = float(raw_input)
        except:
            print(f"\n{RED}Provided input is not a number.{RST}\n")
            main_function()
        result *= num_input
        print(f"{GRN}Multiplication result: {result}{RST}")
    main_function()

def division():
    try:
        result = float(input(f"{CYN}Number to be divided: {RST}"))
    except:
        print(f"\n{RED}Provide a number.{RST}\n")
        division()
    print("")
    while True:
        raw_input = input(f"{CYN}Type a number to divide by or press {YLW}[ENTER]{CYN} for final result: {RST}")
        if not raw_input:
            print(f"\n{GRN}Final Result: {result}{RST}\n")
            input(f"Press {YLW}[ENTER]{RST} to return...\n")
            break
        try:
            num_input = float(raw_input)
        except:
            print(f"\n{RED}Provided input is not a number.{RST}\n")
            main_function()
        try:
            result /= num_input
        except ZeroDivisionError:
            print(f"\n{RED}INFINITY!{RST}\n")
            division()
        print(f"{GRN}Division result: {result}{RST}")
    main_function()




def main_function():
    print(f"""   
{CYN}[ Type a number corresponding to a function ]{RST}\n
{MGN}1. Addition
2. Subtraction
3. Multiplication
4. Division{RST}
""") 
    try:
        choice = int(input("Choose a function >>> "))
    except:
        print(f"\n{RED}Provided input is not a number.{RST}")
        main_function()

    if choice == 1:
        print("")
        addition()
    elif choice == 2:
        print("")
        subtraction()
    elif choice == 3:
        print("")
        multiplication()
    elif choice == 4:
        print("")
        division()
    else:
        print(f"\n{RED}Chose a number between 1 & 4.{RST}")
        main_function()

main_function()