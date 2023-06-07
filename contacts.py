from dataclasses import dataclass
import pickle
import os


@dataclass
class Contact:
    name: str
    email: str
    phone: str
    username: str

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
        return None
    @classmethod
    def add_contact(cls, username, name, email, phone):
        contact = Contact(name=name, email=email, phone=phone, username=username)
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
    def edite_contact(cls,username, name, email=None, phone=None):
        contacts = cls.load_from_pickle(username)
        if isinstance(cls.load_from_pickle(username), list):
            for num, contact in enumerate(contacts):
                if contact.name == name:
                    if email:
                        contact.email = email
                    if phone:
                        contact.phone = phone
                    contacts[num] = contact
                    cls.save_to_pickle(contacts)

                    break
        else:
            if contacts.name == name:
                if email:
                    contacts.email = email
                if phone:
                    contacts.phone = phone
                cls.save_to_pickle(contacts)
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
                os.remove("data/contacts.pickle") # remove nashe
            else:
                print("Contact doesn't exist!!")

    @classmethod
    def viwe_all_contacts(cls, username):
        contacts = cls.load_from_pickle(username)
        for i, contact in enumerate(contacts):
            print(f"{i}, {contact}")