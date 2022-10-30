from models.models import Plant, Employee, Saloon


class Control:

    def get_option(numbers, available_options, type_option):
        while True:
            num = 1
            print(f'Choose a {type_option}')

            for option in available_options:
                print(num, '.', option)
                num += 1

            print()
            user_option = int(input('Option: '))
            if user_option in numbers:
                return user_option
            else:
                print()
                print('Enter a valid option')

    @staticmethod
    def run():

        global defin
        print()
        nums1 = (1, 2, 3)
        classiz = ("Plants", "Employees", "Saloons")
        classz = Control.get_option(nums1, classiz, "data")

        nums2 = (1, 2, 3, 4)
        classf = ('Add', 'Get all', 'Get by Id', 'Delete')
        classif = Control.get_option(nums2, classf, "operation")

        if classz == 1:
            defit = Plant
            defin = 'plant'
            deftotake = {"id", "name", "location"}
        elif classz == 2:
            defit = Employee
            defin = 'employee'
            deftotake = {"id", "name", "email"}
        elif classz == 3:
            defit = Saloon
            defin = 'saloon'
            deftotake = {"id", "name", "location"}

        if classif == 1:
            if classz == 1 or classz == 3:
                name = input(f"Type name of new {defin} ")
                location = input(f"Type location of new {defin} ")
                defr = defit(name, location)
                defr.save()
            elif classz == 2:
                name = input(f"Type name of new {defin} ")
                email = input(f"Type email of new {defin} ")
                plant_id = input(f"Type id of plant of new {defin} ")
                saloon_name = input(f"Type name of saloon of new {defin} ")
                defr = defit(name, email, plant_id, saloon_name)
                defr.save()
        elif classif == 2:
            defs = defit.get_all()
            for defg in defs:
                for defn in deftotake:
                    print(defg[defn])
                # break
        elif classif == 3:
            id = int(input(f'Type id of {defin}: '))
            defi = defit.get_by_id(id)
            for defg in deftotake:
                print(defi[defg])
        elif classif == 4:
            id = int(input(f'Type id of {defin} which you want to delete: '))
            defit.delete(id)
