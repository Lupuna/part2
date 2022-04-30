with open('input.txt') as home0:
    home = home0.read().split('\n')

def win(time, name : list, km : list, sec : list , ot : list):

    win =[]
    for i,j,l,k in zip(name,km,sec,ot):
        amount, rest = divmod(time, int(k) + int(l))
        kmm = int(j) * int(l) * amount

        if rest > int(l):
            kmm += int(j) * int(l)
        else:
            kmm += int(j) * rest

        win.append(kmm)

    return win

Name = list()
KM = list()
Sec = list()
Ot = list()

for i in home:
    name,_,_,km,_,_,sec,_,_,_,_,_,_,ot,_, = i.split(' ')
    Name.append(name)
    KM.append(km)
    Sec.append(sec)
    Ot.append(ot)

pyp = dict()
for i in Name:
    pyp[i] = 0

for time in range(1,2504):
    winer = win(time,Name,KM,Sec,Ot)
    maximum = max(winer)
    for i,j in enumerate(Name):
        if winer[i] == maximum:
            pyp[j] += 1
F = []
for i,f in pyp.items():
    F.append(f)

winner = max(F)

output = open('output2.txt', 'w')
output.write(str(winner))

output.close()
home0.close()










