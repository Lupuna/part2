with open('input.txt') as home0:
    home = home0.read().split('\n')

win = []

for i in home:
    name,_,_,km,_,_,sec,_,_,_,_,_,_,ot,_, = i.split(' ')
    amount, rest = divmod(2503, int(ot)+int(sec))
    kmm = int(km) * int(sec) * amount

    if rest > int(sec):
        kmm += int(km) * int(sec)
    else:
        kmm += int(km) * rest

    win.append(kmm)

output = open('output1.txt', 'w')
output.write(str(max(win)))

output.close()
home0.close()
