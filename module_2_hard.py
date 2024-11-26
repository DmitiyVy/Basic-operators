import random
x = random.randint(3, 20)

def password_2():
    correct_number = []
    a = 1
    b = 2
    while a < b:
        for i in range(1, x):
            a = i
            for j in range(2, x):
                b = j
                if i >= j:
                    continue
                if i + j == x or x % (i + j) == 0:
                    correct_number.append(i)
                    correct_number.append(j)

        continue
    return correct_number

print("Число из первой вставки - ", x)
print("Пароль: ", *password_2())