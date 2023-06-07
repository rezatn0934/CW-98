from dataclasses import dataclass
import pickle
import os
import csv



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
        contact = Contact(name=name, email=email, phone=phone, username=username, categories=categories)
        if "contacts.pickle" in os.listdir("data/"):
            if isinstance(cls.load_from_pickle(username), list):
                result = cls.check_contact(contact)
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
            if contact.name == in_contact.name and contact.email == in_contact.email and contact.phone == in_contact.phone:
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
    def viwe_all_contacts(cls, username):
        contacts = cls.load_from_pickle(username)
        for i, contact in enumerate(contacts):
            print(f"{i}, {contact}")

    @staticmethod
    def save_to_csv(list1, fpath):
        with open(fpath, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(list1)

    @classmethod
    def save_contact_to_csv(cls, username, fpath="data/"):
        contacts = cls.load_from_pickle(username)
        cls.save_to_csv(list1=contacts, fpath=fpath)

    @staticmethod
    def read_from_csv(fpath):
        list1 = []
        with open(fpath, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    list1.append(row)
        return list1

    @classmethod
    def creat_contacts_from_csv(cls, username, fpath="data/", categories="All contact"):
        contacts = cls.read_from_csv(fpath)
        for contact in contacts:
            name, email, phone= contact
            Contact(name=name, email=email, phone=phone, username=username, categories=categories)
