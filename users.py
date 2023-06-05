from dataclasses import dataclass
import pickle

@dataclass
class User:
    username: str
    password: str

    @classmethod
    def save_to_pickle(cls, obj):
        with open("User.pickle", "wb") as f:
            pickle.dump(obj, f)

    @classmethod
    def load_from_pickle(cls):
        with open("User.pickle", "rb") as f:
            return pickle.load(f)
