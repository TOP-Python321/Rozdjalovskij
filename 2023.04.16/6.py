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


# g3
# f2
# да

# c6
# d4
# нет
