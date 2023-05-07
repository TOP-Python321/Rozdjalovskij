n = int(input())
a = [ ]
for i in range(n):
    a.append(input())
    
sum = 0
for i in range(n):
    if int(a[i]) >= 0:
        sum += int(a[i])
print(sum)

# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 2.py
# 6
# 3
# -5
# 1
# 10
# -1
# 8
# 22    