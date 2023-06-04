from dataclasses import dataclass
import pickle


@dataclass
class Contact:
    name: str
    email: str
    phone: str
    def save_to_pickle(self, obj):
        with open("contacts.pickle","rb") as f:
            pickle.dump(obj, f)

