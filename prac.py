from collections import Counter
import math
import os

# LOGIN SYSTEM

file_path = r"C:\Users\slikn\Desktop\users.txt"
users = {}

# Load users
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password

print("ϕ| Welcome to Informatics Calculator |ϕ")

# Ask if registered
while True:
    registered = input("Are you already registered? (yes/no): ").lower()
    if registered in ["yes", "no"]:
        break
    else:
        print("Please type only 'yes' or 'no'.")

# Login
if registered == "yes":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
    else:
        print("Login Failed!, Please check your username and password.")
        exit()

# Registration
else:
    print("ϕ| New User Registration |ϕ")
    new_username = input("Enter a new username: ")

    if new_username in users:
        print("Username already exists! Please restart and choose another.")
        exit()

    new_password = input("Enter a new password: ")
    users[new_username] = new_password

    with open(file_path, "a") as file:
        file.write(f"{new_username},{new_password}\n")

    print("Registration Successful!")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
    else:
        print("Login Failed!, Please check your username and password.")
        exit()

# --------------- MENU ----------------

print("\n------ Calculator Menu ------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square root")
print("6. Mode")
print("7. Multiples less than 50")
print("8. HCF or LCM")
print("9. Median value")
print("10. Mean value")
print("11. Conversion")

choice = input("Select option: ")

# 1 Addition
if choice == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Addition:", num1 + num2 )

# 2 Subtraction
elif choice == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Subtraction:", num1 - num2)

# 3 Multiplication
elif choice == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Multiplication:", num1 * num2)

# 4 Division
elif choice == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

# 5 Square root
elif choice == "5":
    num = float(input("Enter a number: "))
    if num >= 0:
        print("Square Root:", math.sqrt(num))
    else:
        print("Square root of negative number is not allowed!")

# 6 Mode
elif choice == "6":
    nums = input("Enter numbers separated by space: ").split()
    nums = [float(x) for x in nums]

    counts = Counter(nums)
    max_freq = max(counts.values())
    modes = [n for n, f in counts.items() if f == max_freq]

    if len(modes) == len(counts):
        print("All values occur equally. No mode.")
    else:
        print("Mode(s):", modes)

    # 7 Multiples less than 50
elif choice == "7":
    num = int(input("Enter a number: "))

    if num == 0:
        print("Invalid input — cannot find multiples of 0.")
    else:
        multiples = [i for i in range(1, 50) if i % num == 0]

        if len(multiples) == 0:
            print("No multiples of", num, "exist less than 50.")
        else:
            print("Multiples less than 50:", multiples)

# 8 HCF & LCM
elif choice == "8":
    option = input("HCF or LCM: ").upper()

    if option not in ("HCF" , "LCM"):
        print("Invalid choice!")
        exit()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    hcf = math.gcd(a, b)
    lcm = abs(a * b) // hcf
    if  option == "HCF":
        print("HCF:", hcf)
    else:
        print("LCM:", lcm)

# 9 Median
elif choice == "9":
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    nums.sort()

    length = len(nums)
    if length % 2 == 0:
        median = (nums[length//2 - 1] + nums[length//2]) / 2
    else:
        median = nums[length//2]

    print("Median:", median)

# 10 Mean
elif choice == "10":
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    print("Mean:", sum(nums) / len(nums))

 #11 Conversion
elif choice == "11":

    # ---------- Conversion Functions ----------
    # Function to convert  decimal numbeer to bin/hex/oct
    def decimal_to_base(num, base):
        try:
            # try converting  input to float handles integers and decimals
            num = float(num)
        except ValueError:
            return None

#seperate the whole nd the fractional part
        whole = int(num)
        frac = num - whole

        if base == 2:
            result = bin(whole)[2:]
        elif base == 8:
            result = oct(whole)[2:]
        elif base == 16:
            result = hex(whole)[2:].upper()
        else:
            return None

        if frac == 0:
            return result

        result += "."
        for _ in range(20):
            frac *= base
            digit = int(frac)
            frac -= digit

# handles digits above 9 for hexadeimal
            if digit < 10:
                result += str(digit)
            else:
                result += chr(ord('A') + digit - 10)
#stops if fraction becomes zero
            if frac == 0:
                break

        return result

#function convert bin/oct/hex to decimal
    def base_to_decimal(num, base):
        try:
            #split into whole and fractional part
            if "." in num:
                whole, frac = num.split(".")
            else:
                whole, frac = num, ""

            value = 0
            power = 0

#process whole number part (Right to left)
            for d in reversed(whole):
                if d.isdigit():
                    v = int(d)
                elif d.isalpha():
                    v = ord(d.upper()) - ord('A') + 10
                else:
                    return None

#check if digit is valid for the base
                if v >= base:
                    return None

                value += v * (base ** power)
                power += 1

            power = -1
            for d in frac:
                if d.isdigit():
                    v = int(d)
                elif d.isalpha():
                    v = ord(d.upper()) - ord('A') + 10
                else:
                    return None
#process fractional part (left to right)
                if v >= base:
                    return None

                value += v * (base ** power)
                power -= 1

            return value
        except:
            return None


    # ---------- Conversion Menu Loop ----------
    while True:
        print("\n--- Conversion Menu ---")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Octal to Decimal")
        print("6. Hexadecimal to Decimal")

        conv_choice = input("Select option (1-6): ")

        # Validate menu choice
        if not conv_choice.isdigit() or int(conv_choice) < 1 or int(conv_choice) > 6:
            print("Invalid choice! Enter a number between 1 and 6.")
            continue # Restart conversion menu

        number = input("Enter number: ")

        # Perform conversion
        if conv_choice == "1":
            result = decimal_to_base(number, 2)
        elif conv_choice == "2":
            result = decimal_to_base(number, 8)
        elif conv_choice == "3":
            result = decimal_to_base(number, 16)
        elif conv_choice == "4":
            result = base_to_decimal(number, 2)
        elif conv_choice == "5":
            result = base_to_decimal(number, 8)
        elif conv_choice == "6":
            result = base_to_decimal(number, 16)

        #Invalid number
        if result is None:
            print("Invalid number please enter an integer. Try again.")
            continue

        print("Result:", result)
else:
    print("Invalid choice! Try again.")
