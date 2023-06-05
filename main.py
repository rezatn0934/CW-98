from contacts import Contact
from users import User
import getpass



def main_menu():
    users = []

    while True:
        print("1. Create a new account")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user = User.add_user(username=username, password=password)
                print("Account created successfully.")
                sub_menu1(username)
            case 2:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                status = User.login(username=username, password=password)
                if status:
                    print("Authenticated successfully. Access granted.")
                    sub_menu1(username)
                else:
                    print("Authentication failed. Invalid username or password.")
            case 3:
                quit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
