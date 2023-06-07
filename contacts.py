from dataclasses import dataclass
import pickle
import os
import csv
import re



@dataclass
class Contact:
    name: str
    email: str
    phone: str
    username: str
    categories: str = "All contact"

    @classmethod
    def save_to_pickle(cls, obj):
        with open("data/contacts.pickle", "wb") as f:
            pickle.dump(obj, f)

    @classmethod
    def load_from_pickle(cls, username):
        with open("data/contacts.pickle", "rb") as f:
            contacts = pickle.load(f)
        if isinstance(contacts, list):
            matching_contacts = [contact for contact in contacts if contact.username == username]
            if matching_contacts:
                return matching_contacts
        else:
            if contacts.username == username:
                return [contacts]

        print(f"No contacts found for the {username}.")
        return

    @classmethod
    def add_contact(cls, username, name, email, phone, categories="All contact"):
        if not cls.validate_email(email):
            print("Invalid email address")
            return
        if not cls.validate_phone(number):
            print("Invalid phone number format!!")
            return
        contact = Contact(name=name, email=email, phone=phone, username=username, categories=categories)
        if "contacts.pickle" in os.listdir("data/"):
            if isinstance(cls.load_from_pickle(username), list):
                result = cls.check_contact(username=username,in_contact=contact)
                contacts = cls.load_from_pickle(username)
                if result:
                    contacts.append(contact)
            else:
                contacts = [cls.load_from_pickle(username), contact]
        else:
            contacts = contact
        cls.save_to_pickle(contacts)

    @classmethod
    def edite_contact(cls,username, name, new_name=None, email=None, phone=None, categories=None):
        if not cls.validate_email(email):
            print("Invalid email address")
            return
        if not cls.validate_phone(number):
            print("Invalid phone number format!!")
            return
        contacts = cls.load_from_pickle(username)
        if isinstance(cls.load_from_pickle(username), list):
            for num, contact in enumerate(contacts):
                if contact.name == name:
                    if new_name:
                        contact.name = new_name
                    if email:
                        contact.email = email
                    if phone:
                        contact.phone = phone
                    if categories:
                        contact.categories = categories
                    contacts[num] = contact
                    cls.save_to_pickle(contacts)

                    break
        else:
            if contacts.name == name:
                if new_name:
                    contacts.name = new_name
                if email:
                    contacts.email = email
                if phone:
                    contact.phone = phone
                if categories:
                    contacts.categories = categories
            else:
                print("Contact doesn't exist!!!")

    @classmethod
    def check_contact(cls,username, in_contact):
        contacts = cls.load_from_pickle(username)
        for i, contact in enumerate(contacts):
            if contact.name == in_contact.name and contact.email == in_contact.email and contact.phone == in_contact.phone and contact.username == in_contact.username:
                print("Contact already exist!!")
                return False
        return True

    @classmethod
    def delete_contact(cls,username, contact_name):
        contacts = cls.load_from_pickle(username)
        if isinstance(contacts, list):
            for index,contact in enumerate(contacts):
                if contact.name == contact_name:
                    contacts.pop(index)
                    cls.save_to_pickle(contacts)
                    return
                else:
                    print("Contact doesn't exist!!")
        else:
            if contacts.name == contact_name:
                cls.save_to_pickle([])
            else:
                print("Contact doesn't exist!!")

    @classmethod
    def view_all_contacts(cls, username):
        contacts = cls.load_from_pickle(username)
        if contacts:
            if isinstance(cls.load_from_pickle(username), list):
                for i, contact in enumerate(contacts):
                    print(f"{i}, {contact}")
            else:
                print(contacts)

    @staticmethod
    def save_to_csv(list1, fpath):
        with open(fpath, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows([[item] for item in list1])

    @classmethod
    def save_contact_to_csv(cls, username, fpath="data/contact.csv"):
        contacts = cls.load_from_pickle(username)
        str_contacts = cls.obj_to_str(contacts)
        cls.save_to_csv(list1=str_contacts, fpath=fpath)

    @staticmethod
    def obj_to_str(contacts):
        lst = [];
        for contact in contacts:
            lst.append(f"{contact.name}//{contact.email}//{contact.phone}//{contact.username}//{contact.categories}")
        return lst

    @staticmethod
    def read_from_csv(fpath):
        list1 = []
        with open(fpath, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    list1.append(row)
        print(list1)
        return list1

    @classmethod
    def creat_contacts_from_csv(cls, username, fpath="data/contact.csv", categories="All contact"):
        contacts = cls.read_from_csv(fpath)
        for row in contacts:
            contact = row[0]
            name, email, phone = contact.split("//")
            contact = cls.add_contact(name=name, email=email, phone=phone, username=username, categories=categories)

    @classmethod
    def search_by_name(cls, username, contact_name):
        contacts = cls.load_from_pickle(username)
        if isinstance(contacts, list):
            for contact in contacts:
                if contact.name == contact_name:
                    print(contact)
                else:
                    print("Contact doesn't exist!!")
        else:
            if contacts.name == contact_name:
                print(contact)
            else:
                print("Contact doesn't exist!!")

    @classmethod
    def search_by_email(cls, username, contact_email):
        ontacts = cls.load_from_pickle(username)
        if isinstance(contacts, list):
            for contact in contacts:
                if contact.email == contact_email:
                    print(contact)
                else:
                    print("Contact doesn't exist!!")
        else:
            if contacts.email == contact_email:
                print(contact)
            else:
                print("Contact doesn't exist!!")

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phon_number):
        pattern = r'(?:\+98|0|0098)?9\d{2}-?\d{3}-?\d{4}'
        match = re.match(pattern, phone_number)
        return match is not None

