from datetime import datetime
import csv
import json

with open("file.txt", "w") as f:
    f.write("some text")


# 1
class File:
    def __init__(self, file_name):
        self.name = file_name
        self.file = open(file_name)

    def __enter__(self):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()},{self.name} OPENED \n")
        return self.file

    def __exit__(self, typer, val, tb):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()},{self.name} CLOSED \n")
        self.file.close()


with File("file.txt") as f:
    f.read()


# 2
def trans(filetxt, filecsv):
    with open(filetxt, "r") as ftxt:
        with open(filecsv, "w") as fcsv:
            for line in ftxt:
                fcsv.write(line)


trans("logs.txt", "logs.csv")


# 3

word= "OPENED"
z=0
with open("logs.csv", "r") as fr:
        for line in fr:
            if word in line:
                m=line
                z+=1

ltm= "".join(m.split(",")[:-1])
tojs={"file.txt":{"count":z,"last_time_opened":ltm}}

with open("logs.json",'w') as fjs:
    json.dump(tojs,fjs, indent=4)
print(z)