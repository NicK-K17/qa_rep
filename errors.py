def calc (x, y):
    try:
        return x / y
    except (ZeroDivisionError, ValueError):
        print('Ожидаемая ощибка')

print(calc(int(input('number 1: ')), int(input('number 2: '))))