inp1 = input()
inp2 = input()
cell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
if (
        cell.index(inp1[0]) - cell.index(inp2[0]) == 1
        or cell.index(inp1[0]) - cell.index(inp2[0]) == -1
    ) and (
        int(inp1[1]) - int(inp2[1]) == 1
        or int(inp1[1]) - int(inp2[1]) == -1
):
    print('да')
else:
    print('нет')


# СДЕЛАТЬ: есть такая классная штука, как (двойные) неравенства — подумайте какие у вас получаются результаты при вычитаниях и как это намного удобнее и проще записать с помощью неравенств (подсказка: список cell в этом случае вам просто не понадобится)


# g3
# f2
# да

# c6
# d4
# нет


# ИТОГ: хорошо — 3/4
