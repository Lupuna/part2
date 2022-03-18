with open('input.txt') as home0:
    home=home0.read()


coords = [(0,0), (0,0)]
help_0 = set([(0,0)])


for n,i in enumerate(home):
    x,y = coords[n%2]
    if i == "^":
        coords[n%2] =(x,y+1)
    elif i == "v":
        coords[n%2] =(x,y-1)
    if i == ">":
        coords[n%2] =(x+1,y)
    elif i == "<":
        coords[n%2] =(x-1,y)

    help_0.add(coords[n%2])

output = open('output2.txt', 'w')
output.write(str((len(help_0))))

output.close()
home0.close()
