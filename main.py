from contacts import Contact
from users import User
import getpass


def main_menu():

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
1. Add contacts
2. Edite an existing contact
3. Delete a contact
4. View all contact
5. Save contact to a csv file
6. Back
7. Quit   
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
            Contact.delete_contact(username=username,contact_name=name)
            print("Contact has been deleted!!")
            sub_menu1(username)
        case 4:
            Contact.viwe_all_contacts(username)
        case 5:
            fpath = input("Enter your file path or pass( Default path: data/): ")
            if fpath:
                Contact.save_contact_to_csv(username=username,fpath=fpath)
            else:
                Contact.save_contact_to_csv(username=username)
        case 6:
            main_menu()
        case 7:
            quit()
        case _:
            print("Wrong input!!")
            sub_menu1()

def sub_menu2(username):
    text = """
1. Add contact
2. Import from csv file
3. Back
4. Quit
"""
    print(text)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            Contact.add_contact(name=name, email=email, phone=phone, username=username)
        case 2:
            fpath = input("Enter your file path or pass( Default path: data/): ")
            if fpath:
                Contact.creat_contacts_from_csv(username=username, fpath=fpath)
            else:
                Contact.creat_contacts_from_csv(username=username)
        case 3:
            sub_menu1(username)
        case 4:
            quit()
        case _:
            print("Wrong input!!!")
            sub_menu2(username)

if __name__ == "__main__":
    main_menu()
