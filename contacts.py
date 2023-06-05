from dataclasses import dataclass
import pickle
import os


@dataclass
class Contact:
    name: str
    email: str
    phone: str

    @classmethod
    def save_to_pickle(cls, obj):
        with open("contacts.pickle", "wb") as f:
            pickle.dump(obj, f)

    @classmethod
    def load_from_pickle(cls):
        with open("contacts.pickle", "rb") as f:
            return pickle.load(f)

    @classmethod
    def add_contact(cls, name, email, phone):
        contact = Contact(name=name, email=email, phone=phone)
        if "contacts.pickle" in os.listdir():
            if isinstance(cls.load_from_pickle(), list):
                result = cls.check_contact(contact)
                contacts = cls.load_from_pickle()
                if result:
                    contacts.append(contact)
            else:
                contacts = [cls.load_from_pickle(), contact]
        else:
            contacts = contact
        cls.save_to_pickle(contacts)

    @classmethod
    def edite_contact(cls, name, email=None, phone=None):
        contacts = cls.load_from_pickle()
        if isinstance(cls.load_from_pickle(), list):
            for num, contact in enumerate(contacts):
                if contact.name == name:
                    if email:
                        contact.email = email
                    if phone:
                        contact.phone = phone
                    contacts[num]=contact
                    break
        else:
            if contacts.name == name:
                if email:
                    contacts.email = email
                if phone:
                    contacts.phone = phone
            else:
                print("Contact doesn't exist!!!")

        cls.save_to_pickle(contacts)


    @classmethod
    def check_contact(cls, in_contact):
        contacts = cls.load_from_pickle()
        for i, contact in enumerate(contacts):
            if contact.name == in_contact.name and contact.email == in_contact.email and contact.phone == in_contact.phone:
                print("Contact already exist!!")
                return False
        return True

    @classmethod
    def delete_contact(cls, contact_name):
        contacts = cls.load_from_pickle()
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
                os.remove("contacts.pickle")
            else:
                print("Contact doesn't exist!!")


