n = int(input())
sum = 0
for i in range(n + 1):
    if i != 0 and n % i == 0:
        sum += i
print(sum)

# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 3.py
# 50
# 93