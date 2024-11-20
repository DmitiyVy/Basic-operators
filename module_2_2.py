first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
thrid = int(input("Введите третье число: "))
if first == second and first == thrid:
    print("Одинаковых чисел: 3")
elif first == second or first == thrid:
    print("Одинаковых чисел: 2")
else:
    print("Одинаковых чисел: 0")