first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
thrid = int(input("Введите третье число: "))
if len(set([first, second, thrid])) == 1: #if first == second == thrid:
    print("Одинаковых чисел: 3")
elif len(set([first, second, thrid])) == 2: #elif first == second or first == thrid or second == thrid:
    print("Одинаковых чисел: 2")
else:
    print("Одинаковых чисел: 0") # в комментариях указан старый код
