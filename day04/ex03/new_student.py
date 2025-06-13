import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character string consisting \
        of lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:

    name: str = field(init=True)
    surname: str = field(init=True)  # marche sans rien
    active: str = True
    login: str = field(init=False)
    # field avec default_factory pour générer un ID a chaque nouvelle instance :
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}"
