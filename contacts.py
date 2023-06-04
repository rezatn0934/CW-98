from dataclasses import dataclass
import pickle


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
        contacts = [cls.load_from_pickle()]
        contact = Contact(name=name, email=email, phone=phone)
        contacts.append(contact)
        print(contacts)
        cls.save_to_pickle(contacts)


