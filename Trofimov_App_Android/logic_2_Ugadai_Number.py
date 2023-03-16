print("""Назовите число,которое
не меньше 80 и не больше 150 и 
не меньше 90 или равно 150.

Таких чисел может быть больше десятка.
Найдите хотя бы одно""")

try:
    x = int(input("Введите предполагаемое число: "))
    res = (not (x < 80) and not (x > 150) and not (x < 90) or (x == 150))
    if (res):
        print("Вы угадали!")
    else:
        print("К сожалению, не то . . .")

    input("Нажмите Enter для выхода . . .")
    quit()
except (ZeroDivisionError, ValueError):
    print("Error Please Enter number:")
