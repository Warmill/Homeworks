from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, plant_id,saloon_name):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        self.saloon_name = saloon_name


class Saloon(Model):
    file = "saloon.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location
