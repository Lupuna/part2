with open('input.txt') as home0:
    home = home0.read().split('\n')

velu1,velu2 = 0,0

velu1 = sum([len(string) for string in home])
velu2= sum([len(string.replace('\\','\\\\').replace('\"','\\\"'))+2 for string in home])

output = open('output2.txt', 'w')
output.write(str(velu2-velu1))

output.close()
home0.close()