a = list()
while True:
    inp = int(input())
    if inp % 7 == 0:
        a.append(inp)
    else:
        break
        
a.reverse()
print(*a, sep=' ')


 # C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 1.py
# 7
# 7
# 14
# 21
# 15
# 21 14 7 7


# ИТОГ: отлично — 3/3
