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
