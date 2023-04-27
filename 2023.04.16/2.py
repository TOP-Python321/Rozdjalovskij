num1 = int(input())
num2 = int(input())
if num1 % num2:
    print(f"{num1} не делится на {num2} нацело \nнеполное частное: {int(num1 // num2)} \nостаток: {num1 % num2}")
else:  
    print(f"{num1} делится на {num2} нацело \nчастное: {int(num1 / num2)}")
    
# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.16>py 2.py
# 8
# 2
# 8 делится на 2 нацело
# частное: 4

# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.16>py 2.py
# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1