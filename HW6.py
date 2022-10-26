# 1
class FibonacciNumbers:
    fib1 = 0
    fib2 = 1
    count = 0

    def __init__(self, quantity):
        self.qty = quantity
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return 0
        if self.count < self.qty:
            self.number = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = self.number
            self.count += 1
            return self.number
        else:
            raise StopIteration


for elem in FibonacciNumbers(10):
    print(elem)


# 2
print('\n')
def FibonacciGen(quantity):
    number = 0
    fib1 = 0
    fib2 = 1
    count = 0
    while count < quantity:
        if count == 0:
            count +=1
            yield number
        else:
            number = fib1 + fib2
            fib1 = fib2
            fib2 = number
            count += 1
            yield number


FibGen = FibonacciGen(10)
for elem in FibGen:
    print(elem)

# 3
print('\n')
z={0, 1, 2, 3, 4 , 5 , 6, 7, 8, 9, 10}
g = (number*number for number in z)
for elem in g:
    print(elem)

# 4
print('\n')

from abc import abstractmethod, ABC

class Laptop(ABC):

    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError

class HPLaptop (Laptop):

    def Screen(self):
        print ('I will show you a wonderful world')

    def Keyboard(self):
        print ('I will write all you want')

    def Touchpad(self):
        print ('I will mark everything you want')

    def WebCam(self):
        print ('I will show you for everyone')

    def Ports(self):
        print('I will connect every USB devices (and not only them)')

    def Dynamics(self):
        print('I will tell you all you want to hear')

pavilion = HPLaptop()
pavilion.Ports()

# 5
print('\n')
class Car (ABC):

    def drive(self):
        print('I am speed')

    def stop(self):
        print('I am slowing down')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError


class Nissan(Car):

    def open_door(self):
        print('door is opened')

    def close_door(self):
        print ('door is closed')

    def turn_on_light(self):
        print('light on')

    def turn_off_light(self):
        print('light off')

    def enable_radio(self):
        print('Radio says hello')

    def disable_radio(self):
        print('Radio says bye')


skyline = Nissan()
skyline.drive()
skyline.enable_radio()