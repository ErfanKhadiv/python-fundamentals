import os
import json


def load_passwords():
    if os.path.exists("passwords.json"):
        try:
            with open("passwords.json", 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_passwords(passwords):
    with open("passwords.json", 'w') as file:
        json.dump(passwords, file, indent=4)


def add_account(website, username, password, passwords):
    account = {
        "Website": website,
        "Username": username,
        "Password": password
    }
    passwords.append(account)

def check_username(website, username, passwords):
    for account in passwords:
        if (account["Website"] == website
            and account["Username"] == username):

            return "invalid"
    return "valid"

def show_accounts(passwords):
    for i, account in enumerate(passwords, start=1):
        print(f"""{i}.Website: {account['Website']}\n  Username: {account['Username']}\n  Password: {account['Password']}\n""")

def search_account(search_input, method, passwords):
    search_result = []
    if method == 1:
        for account in passwords:
            if account["Website"] == search_input:
                search_result.append(account)
    elif method == 2:
        for account in passwords:
            if account["Username"] == search_input:
                search_result.append(account)
    else:
        print("INVALID INPUT!")
        return None
    return search_result

def delete_account(index, passwords):
    passwords.pop(index)

passwords = load_passwords()
while True:
    print("""
    ===== PASSWORD MANAGER =====

    1. Add Account
    2. Show Accounts
    3. Search Account
    4. Delete Account
    5. Exit
    """)

    while True:
        try:
            choose = int(input("Choose: "))
            if 1 <= choose <= 5:
                break
            else:
                print("ENTER A NUMBER BETWEEN 1 AND 5!")
        except ValueError:
            print("INVALID INPUT!")


    if choose == 1:
        print("****** ADD ACCOUNT ******")

        while True:
            website_name = input("Website: ").strip()
            if website_name:
                break
            else:
                print("INPUT CANNOT BE EMPTY!")

        while True:
            user_name = input("Username: ").strip()
            if user_name:
                checked = check_username(website_name, user_name, passwords)
                if checked == "invalid":
                    print("USERNAME ALREADY EXISTS FOR THIS WEBSITE!")
                    continue
                elif checked == "valid":
                    break
            else:
                print("INPUT CANNOT BE EMPTY!")

        while True:
            user_password = input("Password: ").strip()
            if user_password:
                break
            else:
                print("INPUT CANNOT BE EMPTY!")

        add_account(website_name, user_name, user_password, passwords)
        print("ACCOUNT ADDED!")
        print("*************************")
        save_passwords(passwords)


    elif choose == 2:
        if passwords:
            print("****** ACCOUNTS ******\n")
            show_accounts(passwords)
            print("**********************")
        else:
            print("YOU DON'T HAVE ANY ACCOUNTS YET!")

    elif choose == 3:
        if passwords:
            print("****** SEARCH ACCOUNT ******")
            print("""1. Search by website name\n2. Search by username""")
            while True:
                try:
                    search_method = int(input("Choose search method: "))
                    if 1 <= search_method <= 2:
                        break
                    else:
                        print("ENTER A NUMBER BETWEEN 1 AND 2!")
                except ValueError:
                    print("INVALID INPUT!")

            while True:
                try:
                    searched_name = input("name: ").strip()
                    if searched_name:
                        break
                    else:
                        print("INPUT CANNOT BE EMPTY!")
                except ValueError:
                    print("INVALID INPUT!")

            print("****** SEARCH RESULT ******")
            search_result = search_account(searched_name, search_method, passwords)
            if search_result:
                for i, account in enumerate(search_result, start=1):
                    print(f"""{i}.Website: {account['Website']}\n  Username: {account['Username']}\n  Password: {account['Password']}\n""")
            else:
                print("ACCOUNT NOT FOUND!")
            print("***************************")
        else:
            print("YOU DON'T HAVE ANY ACCOUNTS YET!")


    elif choose == 4:
        if passwords:
            print("****** DELETE ACCOUNT ******")
            show_accounts(passwords)
            while True:
                try:
                    choose_delete = int(input("Choose account to delete: "))
                    if 1 <= choose_delete <= len(passwords):
                        break
                    else:
                        print(f"ENTER A NUMBER BETWEEN 1 AND {len(passwords)}!")
                except ValueError:
                    print("INVALID INPUT!")
            delete_account(choose_delete - 1, passwords)
            save_passwords(passwords)
            print("ACCOUNT DELETED!")
            print("***************************")
        else:
            print("YOU DON'T HAVE ANY ACCOUNTS YET!")

    elif choose == 5:
        print("****** HAVE A NICE DAY! ******")
        break
    else:
        print("INVALID INPUT!")
