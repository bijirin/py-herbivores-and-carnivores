class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __print__(self):
        return f"{self.name} (Health: {self.health}, Hidden: {self.hidden})"

    def __repr__(self):
        message = (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )
        return message


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore):
        if other.hidden:
            return
        if other in self.alive and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                self.alive.remove(other)
