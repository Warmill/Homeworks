import datetime
import json
import csv


class Human:
    def __init__(self, name, surname, age, birth_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = datetime.datetime.now() - datetime.timedelta(days=365*age)

class HumanSerializer:
    def serialize(self, hum, format):
        serializer = self._get_serializer(format)
        return serializer(hum)


    def _get_serializer(self,format):
        if format == 'json':
            return self._serialize_to_json
        elif format == 'csv':
            return self._serialize_to_csv

    def _serialize_to_json(self,hum):
        payload = {
            'name': hum.name,
            'surname': hum.surname,
            'birth_date': hum.birth_date.strftime("%d/%m/%Y")
        }
        return json.dumps(payload)

    def _serialize_to_csv(self,hum):
        fieldnames=['name','surname','birth_date']
        writer = csv.DictWriter(csvf,fieldnames=fieldnames)
        writer.writeheader()
        return writer.writerow({'name': hum.name,'surname': hum.surname,
                             'birth_date': hum.birth_date.strftime("%d/%m/%Y")})


if __name__=='__main__':

    obj = Human('Oleksii','Maksymiv',30, datetime.date(1992,11,22))
    print(obj.birth_date)
    serializer=HumanSerializer()

    with open ('file.csv','w',newline='') as csvf:
        serializer.serialize(obj,'csv') #1992-12-01=> 01-11-1992

    with open('file2.json', 'w', newline='') as jsnf:
        jsnf.write(serializer.serialize(obj,'json')) #1992-12-01=> 01-11-1992

