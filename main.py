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


def sub_menu1(username):
    text = """
1. Add a new contact
2. Edite an existing contact
3. Delete a contact
4. View all contact
5. Back
6. Quit   
"""
    print(text)
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            Contact.add_contact(name=name, email=email, phone=phone,username=username)
            sub_menu1(username)
        case 2:
            name = input("Enter contact name: ")
            text = """Choose what property you want to change: 
1. Email
2. Phone
3. Both            
4. Back
5. Quit           
"""
            print(text)
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    email = input("Enter contact email: ")
                    Contact.edite_contact(username=username, name=name, email=email)
                    sub_menu1(username)
                case 2:
                    phone = input("Enter contact phone: ")
                    Contact.edite_contact(username=username, name=name, phone=phone)
                    sub_menu1(username)
                case 3:
                    email = input("Enter contact email: ")
                    phone = input("Enter contact phone: ")
                    Contact.edite_contact(username=username, name=name,email=email, phone=phone)
                    sub_menu1(username)
                case 4:
                    sub_menu1(username)
                case 5:
                    quit()
                case _:
                    print("wrong input")
        case 3:
            name = input("Enter contact name: ")
            Contact.delete_contact(name)
            print("Contact has been deleted!!")
            sub_menu1(username)
        case 4:
            ...
        case 5:
            ...
        case 6:
            quit()


if __name__ == "__main__":
    main_menu()
