fizz = int(input('Введите первое число: '))
buzz= int(input('Введитие второе число: '))
tazz = int(input('Введите тупиковое число: '))


for i in range(1, tazz):
    if i % fizz and i % buzz:
        print('FB')
    elif i % buzz:
        print('B')
    elif i % fizz:
        print ('F')
    else:
        print(i)