class Animal:
    def _init_(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__health = "good"

    def speak(self):
        return "..."

    def eat(self, food):
        return f"{self.name} ест {food}"

    def info(self):
        return f"Имя: {self.name}, возраст: {self.age}, вес: {self.weight}"

    def _str_(self):
        return self.info()


class Dog(Animal):
    def speak(self):
        return "Гав!"

    def fetch(self):
        return f"{self.name} принес палку"


class Cat(Animal):
    def speak(self):
        return "Мяу!"

    def purr(self):
        return f"{self.name} мурлычет"


class Parrot(Animal):
    def speak(self):
        return "Привет!"

    def repeat(self, phrase):
        return phrase
