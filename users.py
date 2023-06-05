from dataclasses import dataclass
import pickle
import os

@dataclass
class User:
    username: str
    password: str

    @classmethod
    def save_to_pickle(cls, obj):
        with open("users.pickle", "wb") as f:
            pickle.dump(obj, f)

    @classmethod
    def load_from_pickle(cls):
        with open("users.pickle", "rb") as f:
            return pickle.load(f)

    @classmethod
    def add_user(cls, name, password):
        user = User(username=name, password=password)
        if "users.pickle" in os.listdir():
            if isinstance(cls.load_from_pickle(), list):
                result = cls.check_user(user)
                users = cls.load_from_pickle()
                if result:
                    users.append(user)
            else:
                users = [cls.load_from_pickle(), user]
        else:
            users = user
        cls.save_to_pickle(users)