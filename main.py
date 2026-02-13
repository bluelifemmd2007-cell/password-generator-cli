from generator.generator import generate_password, generate_multiple
from utils.colors import Color
import os

def save_to_file(passwords):
    os.makedirs("output", exist_ok=True)
    with open("output/passwords.txt", "a") as f:
        for p in passwords:
            f.write(p + "\n")

def main():
    print(Color.OKCYAN + "=== Advanced Password Generator ===" + Color.ENDC)

    mode = input("1) Single password\n2) Multiple passwords\nChoose mode: ")

    length = int(input("Password length: "))
    digits = input("Include digits? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    if mode == "1":
        password = generate_password(length, digits, symbols)
        print(Color.OKGREEN + "\nGenerated Password: " + password + Color.ENDC)
        save_to_file([password])

    elif mode == "2":
        count = int(input("How many passwords? "))
        passwords = generate_multiple(count, length, digits, symbols)
        print(Color.OKGREEN + "\nGenerated Passwords:" + Color.ENDC)
        for p in passwords:
            print(" -", p)
        save_to_file(passwords)

    else:
        print(Color.FAIL + "Invalid option!" + Color.ENDC)

if __name__ == "__main__":
    main()
