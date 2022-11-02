from datetime import datetime


def timer(func_name):
    def real_decor(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            print(
                "function execution time of {z} is: {time.seconds}s, {time.microseconds}ms".format(
                    z = func_name, time=end - start
                )
            )
            return result
        return wrapper
    return real_decor