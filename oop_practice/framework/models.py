import json
from abc import ABC


class Model(ABC):
    file = "default.json"

    @staticmethod
    def get_data(path):
        file = open(path, "r")
        data = json.loads(file.read())
        file.close()
        return data

    def save(self):
        data = self.get_data("database/" + self.file)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance["id"] = data[-1]["id"] + 1
        else:
            new_instance["id"] = 1
        data.append(new_instance)
        self.save_data_to_file(data, "database/" + self.file)

    @staticmethod
    def save_data_to_file(data, path):
        file = open(path, "w")
        file.write(json.dumps(data))
        file.close()

    @classmethod
    def get_all(cls):
        instances = cls.get_data("database/" + cls.file)
        return instances

    @classmethod
    def get_by_id(cls, id):
        instances = cls.get_data("database/" + cls.file)
        for instance in instances:
            if instance["id"] == id:
                return instance

    @classmethod
    def delete(cls, id):
        instances = cls.get_data("database/" + cls.file)
        for i in range(len(instances)):
            if instances[i]["id"] == id:
                del instances[i]
                break
        cls.save_data_to_file(instances, "database/" + cls.file)