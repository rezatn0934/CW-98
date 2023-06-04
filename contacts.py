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
        with open("contacts.pickle","rb") as f:
            return pickle.load(f)

    @classmethod
    def add_contact(cls, name, email, phone):
        contact = Contact(name=name, email=email, phone=phone)
        if "contacts.pickle" in os.listdir():
            if isinstance(cls.load_from_pickle(), list):
                contacts = cls.load_from_pickle()
                contacts.append(contact)
            else:
                contacts = [cls.load_from_pickle(), contact]
        else:
            contacts = contact
        cls.save_to_pickle(contacts)

    @classmethod
    def edite_contact(cls, name, email=None, phone=None):
        contacts = cls.load_from_pickle()
        for num, contact in enumerate(contacts):
            if contact.name == name:
                if email:
                    contact.email = email
                if phone:
                    contact.phone = phone
                contacts[num]=contact
                cls.save_to_pickle(contacts)
                break


