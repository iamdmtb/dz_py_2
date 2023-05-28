x = int(input('Введите сумму двух чисел '))
y = int(input('Введите произведение этих чисел '))
for a in range(x):
    for b in range(y):
        if a + b == x and a * b == y:
            print(a, b)