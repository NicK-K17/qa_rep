# Так выглядит декоратор
def add_text(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper
# Применение декоратора
@add_text
def print_name():
    return print('Name')

print_name()