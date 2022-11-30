from functools import wraps

print("\n#1 \n")
def double_result(func):
    def inner(*args):
        res= (args[0]+args[1]) * 2
        return res
    return inner

def add(a, b):
    return a + b

print(add(5, 5))  # 10

@double_result
def add(a, b):
    return a + b

print(add(5, 5))  # 20

print("\n#2 \n")
def only_odd_parameters(func):
    def inner(*args):
        a=0
        for elem in args:
            if elem%2==0:
                a=1
        if a==1:
            print("Please use only odd numbers!")
        else:
             print(func(*args))
        return func
    return inner

@only_odd_parameters
def add(a, b):
    return a + b

add(5, 5)  # 10
add(4, 4)  # "Please use only odd numbers!"

@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e

multiply(1,2,3,4,5)

print("\n#3 \n")

def logged(func):
    @wraps(func)
    def decor_func(*args,**kwargs):
        
        with open("logs.txt", "a") as file:
            file.write(
                f"{datetime.datetime.now()} args {args}, kwargs {kwargs} res = {func(*args, **kwargs )}\n"
            )
        return func(*args,**kwargs)
    return decor_func

@logged
def func(*args):
    return 3 + len(args)+len(kwargs)


func(4, 4, 4)


print("\n#4 \n")

def type_check(correct_type):
    def decoration(function):
        def wrapped(*args):
            try:
                for el in args:
                    if not isinstance(el,correct_type):
                        print(f'Wrong Type: {type(el)}')
            finally:
                return function(*args)
        return wrapped
    return decoration


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function Footer
