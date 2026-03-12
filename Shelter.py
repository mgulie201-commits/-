from animals import Dog, Cat, Parrot
from shelter import Shelter

shelter = Shelter()

while True:

    print("\n1 Добавить животное")
    print("2 Показать всех")
    print("3 Удалить")
    print("4 Сохранить")
    print("5 Выход")

    choice = input("Выбор: ")

    if choice == "1":
        name = input("Имя: ")
        age = int(input("Возраст: "))
        weight = float(input("Вес: "))

        animal = Dog(name, age, weight)
        shelter.add_animal(animal)

    elif choice == "2":
        shelter.show_all()

    elif choice == "3":
        name = input("Имя: ")
        shelter.remove_animal(name)

    elif choice == "4":
        shelter.save_to_file()

    elif choice == "5":
        break
