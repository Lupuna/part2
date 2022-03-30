with open('input.txt') as home0:
    home=home0.read().split("\n")

gridX = [[0]*1000 for i in range(1000)]


for line in home:
    lamps = line.split(' ')
    start = [int(x) for x in lamps[-3].split(',')]
    end = [int(x) for x in lamps[-1].split(',')]
    dool = ' '.join(lamps[0:-3])


    for y in range(start[0],end[0]+1):
        x1,x2 = start[1],end[1]+1

        if dool == 'turn off':
            gridX[y][x1:x2] = [0]*(x2-x1)

        elif dool == 'turn on':
            gridX[y][x1:x2] = [1]*(x2-x1)

        elif dool == 'toggle':
            for i in range(x1, x2):
                if gridX[y][i] == 1:
                    gridX[y][i] = 0
                else:
                    gridX[y][i] = 1


count = 0

for y in gridX:
    count += y.count(1)

output = open('output1.txt', 'w')
output.write(str(count))

output.close()
home0.close()




