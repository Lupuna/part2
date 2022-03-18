with open('input.txt') as home0:
    home=home0.read()


coords = (0,0)
help_0 = set([coords])


for i in home:
    x,y = coords
    if i == "^":
        coords =(x,y+1)
    elif i == "v":
        coords =(x,y-1)
    if i == ">":
        coords =(x+1,y)
    elif i == "<":
        coords =(x-1,y)

    help_0.add(coords)


output = open('output1.txt', 'w')
output.write(str((len(help_0))))

output.close()
home0.close()

























# def con(i,b,c):
#     i = []
#     for a in home:
#         if a==c and i[-1]==1:
#             i.pop()
#         elif a == b:
#             i.append(1)
#
#         elif a==b and i[-1]==0:
#             i.pop()
#         elif a == c:
#             i.append(0)
#         # if a == b:
#         #     i.append(1)
#         # elif a != b and i[-1] == -1:
#         #     i.pop()
#         # elif a != b:
#         #     i.append(0)
#         # if a == c and i[-1] == 1:
#         #     i.pop()
#         # elif a==c and i[-1] == 0:
#         #     i.append(-1)
#
#     return i
#
#
# position1 = []
# position2 = []
#
#
# a=con(position1, '>','<')
# d=con(position2,'^','v')
# print(a)
# print(d)
#
#
#
#
# print(a)
# print(d)





