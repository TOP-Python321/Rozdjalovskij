n = int(input())
# ИСПОЛЬЗОВАТЬ: имена переменных, отличающееся от имён встроенных функций
primes_count = 0

# ПЕРЕИМЕНОВАТЬ: и снова: называйте вещи своими именами: что такое a, b?
# КОММЕНТАРИЙ: а вот диапазон определили правильно и оптимально
for a in range(10**(n-1), 10**n):
    b = 2
    # ИСПРАВИТЬ: этот цикл выполняет лишние итерации — подумайте, при каких значениях b остаток от деления никогда не сможет быть равным нулю
    while a % b != 0:
        b += 1
    if b == a:
        primes_count += 1
print(primes_count)


# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 4.py
# 3
# 143


# ИТОГ: нужно лучше, доработать — 2/5
