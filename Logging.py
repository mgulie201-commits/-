import json
import logging

logging.basicConfig(filename='shelter.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


class Shelter:

    def _init_(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        logging.info(f"Добавлено животное {animal.name}")

    def remove_animal(self, name):
        for a in self.animals:
            if a.name == name:
                self.animals.remove(a)
                logging.info(f"Удалено животное {name}")
                return
        print("Животное не найдено")

    def find_by_name(self, name):
        for a in self.animals:
            if a.name == name:
                return a
        return None

    def show_all(self):
        for a in self.animals:
            print(a)

    def save_to_file(self):
        data = []

        for a in self.animals:
            data.append({
                "name": a.name,
                "age": a.age,
                "weight": a.weight
            })

        with open("shelter.json", "w") as f:
            json.dump(data, f)

        logging.info("Данные сохранены")

    def load_from_file(self):
        try:
            with open("shelter.json", "r") as f:
                data = json.load(f)
            print(data)
            logging.info("Данные загружены")
        except:
            print("Файл не найден")
