class Rectangle:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle : {self.x, self.y, self.a, self.b}'

    def getArea(self):
        return self.a *self.b

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб"'

    def getClientList(self):
        return f'{self.name} {self.surname} {self.city}'
