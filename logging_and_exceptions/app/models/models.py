import logging

from app.framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id

        def check_email(self):
            data = self.get_all()
            for el in data:
                if self.email == el["email"]:
                    raise ValueError("This email already exist!")

        def check_email_format(self):
            if not "@" in self.email or not "." in self.email:
                raise ValueError("Not a valid email address!")
            position = self.email.find("@")
            position_of_dot = self.email.find(".")
            if position > position_of_dot:
                raise ValueError("Not a valid email address!")

        def CheckName(self):
            checker = 0
            word = self.name.split(" ")
            for i in word:
                if 'A' <= i[0] <= 'Z' or 'А' <= i[0] <= 'Я':
                    checker += 1
            if len(word) != 2 or checker != 2:
                print("write a correct name")
                raise ValueError("Name is not correct")

        def save(self):
            plant = Plant.get_by_id(self.plant_id)
            try:
                self.CheckName()
                self.check_email()
                self.check_email_format()
            except ValueError as e:
                logging.error(str(e) + " Email: " + self.email)
                print(e)
                return
            if not plant:
                raise ValueError("Plant not found!")
            super().save()
