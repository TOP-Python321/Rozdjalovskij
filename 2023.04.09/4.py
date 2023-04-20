num = int(input())
n1 = num // 100
n2 = num  // 10 % 10 
n3 = num %10 
print(f"Сумма цифр = {n1 + n2 + n3}")
print(f"Произведение цифр = {n1 * n2 * n3}")

# C:\Python_HW>py 1.4.py
# 333
# Сумма цифр = 9
# Произведение цифр = 27