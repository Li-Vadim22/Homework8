'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

'''


from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper

@type_logger
def calc_cube(*args):

    return list(map(lambda x: x ** 3, args))

a = calc_cube(5)
print(a)

