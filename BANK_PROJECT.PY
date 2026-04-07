# Bank Operation Project--------
# Create Account
# Login
# Deposit 
# Withdraw
# Check Balance
# Logout

import random
import json
import os

print(".......Welcome to Bank of India.......")

FILE_NAME = "bank_data.json"

# for Loading data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# ------ Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

users = load_data()
current_user = None

def Create_Account():
    global users

    name = input("Enter Name: ")
    pan = input("Enter PAN No.: ")
    mobile = input("Enter Mobile No.: ")
    address = input("Enter Address: ")
    balance = int(input("Enter Initial Balance: "))

    acc_no = str(random.randint(100000000000, 999999999999))
    pin = input("Set 4-digit PIN: ")

    users[acc_no] = {
        "name": name,
        "pan": pan,
        "mobile": mobile,
        "address": address,
        "balance": balance,
        "pin": pin
    }

    save_data(users)

    print("\n✅ Account Created Successfully!")
    print("Account Number:", acc_no)


def Login():
    global current_user

    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in users and users[acc_no]["pin"] == pin:
        current_user = acc_no
        print(f"Welcome {users[acc_no]['name']}")
    else:
        print("Invalid credentials")


def Deposit():
    global current_user

    if not current_user:
        print("Please login first")
        return

    amount = int(input("Enter amount: "))
    users[current_user]["balance"] += amount

    save_data(users)
    print("✅ Deposit successful")


def Withdraw():
    global current_user

    if not current_user:
        print("Please login first")
        return

    amount = int(input("Enter amount: "))

    if amount > users[current_user]["balance"]:
        print("Insufficient balance")
    else:
        users[current_user]["balance"] -= amount
        save_data(users)
        print("✅ Withdraw successful")


def CheckBalance():
    if not current_user:
        print("Please login first")
        return

    print("Balance:", users[current_user]["balance"])


def Logout():
    global current_user
    current_user = None
    print("Logged out...")

while True:

    if current_user:  # User is logged in
        print(f"\nLogged in as: {users[current_user]['name']}")
        print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Logout\n5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            Deposit()

        elif choice == "2":
            Withdraw()

        elif choice == "3":
            CheckBalance()

        elif choice == "4":
            Logout()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice...")

    else:  # User NOT logged in
        print("\n1.Create Account\n2.Login\n3.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            Create_Account()

        elif choice == "2":
            Login()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice...")
