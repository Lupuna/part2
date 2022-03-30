with open('input.txt') as home0:
    home=home0.read().split("\n")

gridX = [[0]*1000 for i in range(1000)]
count = 0

for line in home:
    lamps = line.split(' ')
    start = [int(x) for x in lamps[-3].split(',')]
    end = [int(x) for x in lamps[-1].split(',')]
    dool = ' '.join(lamps[0:-3])


    for y in range(start[0],end[0]+1):
        x1,x2 = start[1],end[1]+1

        if dool == 'turn off':
            for i in range(x1,x2):
                gridX[y][i] += -1
                if gridX[y][i] <= 0:
                    gridX[y][i] = 0

        elif dool == 'turn on':
            for i in range(x1, x2):
                gridX[y][i] += 1

        elif dool == 'toggle':
            for i in range(x1,x2):
                gridX[y][i] += 2

for y in gridX:
    for i in y:
        count += i

output = open('output2.txt', 'w')
output.write(str(count))

output.close()
home0.close()
