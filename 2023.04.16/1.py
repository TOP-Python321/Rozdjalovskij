inp1 = float(input())
inp2 = float(input())
inp3 = float(input())
if inp1 > 0:
    num1 = inp1
else:
    num1 = 0 
if inp2 > 0:
    num2 = inp2
else:
    num2 = 0 
if inp3 > 0:
    num3 = inp3
else:
    num3 = 0

# КОММЕНТАРИЙ: вы создаёте дополнительные переменные, куда в зависимости от выполнения условия записываете либо значение исходной переменной, либо ноль — это работает, и в ряде ситуаций так можно поступать, но при текущей постановке задачи это решение не слишком оптимально, зато слишком длинно
# СДЕЛАТЬ: перепишите код так, чтобы использовать только одну дополнительную переменную для суммы и не использовать блоки else в условных конструкциях

print(num1 + num2 + num3)


# 4
# -22
# 1.5
# 5.5


# ИТОГ: нужно лучше — 2/4
