class Player:
    def __init__(self, id, name, carType, carNumber):
        self.id = id.int()
        self.name = name.str()

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}"