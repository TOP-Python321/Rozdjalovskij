inp1 = input()
inp2 = input()
cell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6', '7', '8']
# проверка черных клеток
if ((inp1[0] in cell[0 : : 2] and inp1[1] in cell[0 : : 2]) or (inp1[0] in cell[1 : : 2] and inp1[1] in cell[1 : : 2])) and ((inp2[0] in cell[0 : : 2] and inp2[1] in cell[0 : : 2]) or (inp2[0] in cell[1 : : 2] and inp2[1] in cell[1 : : 2])):
    print('да')
# проверка белых клеток
elif ((inp1[0] in cell[1 : 7 : 2] and inp1[1] in cell[8 : : 2]) or (inp1[0] in cell[0 : 7 : 2] and inp1[1] in cell[9 : : 2])) and ((inp2[0] in cell[1 : 7 : 2] and inp1[1] in cell[8 : : 2]) or (inp2[0] in cell[0 : 7 : 2] and inp2[1] in cell[9 : : 2])):
    print('да')
    
# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.16>py 4.py
# a1
# b2
# да