from dataclasses import dataclass


@dataclass
class Contacts:
    name: str
    email: str
    phone: str
    Contacts: dict= field(default_factory=dict)
