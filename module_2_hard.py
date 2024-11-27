import random
x = random.randint(3, 20)
def password_2():
    correct_number = []
    a = 1
    b = 2
    while a < b:
        for a in range(1, x):
            for b in range(2, x):
                if a >= b:
                    continue
                if a + b == x or x % (a + b) == 0:
                    correct_number.append(a)
                    correct_number.append(b)
        continue
    return correct_number
print("Число из первой вставки - ", x)
print("Пароль: ", *password_2())
