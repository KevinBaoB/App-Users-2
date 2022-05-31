# your improved User class goes here

class User:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def __str__(self):
        return f"My name is {self.name}, I'm {self.age} years old and I am {self.nationality}!"