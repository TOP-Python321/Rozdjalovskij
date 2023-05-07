n = int(input())
sum = 0
for a in range(10 ** (n - 1), 10 ** n):
    b = 2
    while a % b != 0:
        b += 1
    if b == a:
        sum += 1
print(sum)

# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 4.py
# 3
# 143