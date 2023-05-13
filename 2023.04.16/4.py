inp1 = input()
inp2 = input()
cell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6', '7', '8']
# проверка черных клеток
# ИСПОЛЬЗОВАТЬ: если всё-таки очень нужно составить такое сложное выражение, то помимо линейно записи, использованной вами, есть два пути для упрощения восприятия этого выражения:
#   1) вычислить части сложного выражения по отдельности
#   2) грамотно записать выражение на нескольких строках
inp1_odd = inp1[0] in cell[0::2] and inp1[1] in cell[0::2]
inp1_even = inp1[0] in cell[1::2] and inp1[1] in cell[1::2]
inp2_odd = inp2[0] in cell[0::2] and inp2[1] in cell[0::2]
inp2_even = inp2[0] in cell[1::2] and inp2[1] in cell[1::2]
if (inp1_odd or inp1_even) and (inp2_odd or inp2_even):
    print('да')
# проверка белых клеток
elif ((
          inp1[0] in cell[1:7:2] and inp1[1] in cell[8::2]
          or inp1[0] in cell[0:7:2] and inp1[1] in cell[9::2]
      ) and (
          inp2[0] in cell[1:7:2] and inp1[1] in cell[8::2]
          or inp2[0] in cell[0:7:2] and inp2[1] in cell[9::2]
)):
    print('да')


# a1
# b2
# да
