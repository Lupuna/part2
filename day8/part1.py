with open('input.txt') as home0:
    home = home0.read().split('\n')


velu1,velu2 = 0,0

velu1 = sum([len(string) for string in home])

for string in home:
    velu2+=len(eval((string)))

output = open('output1.txt', 'w')
output.write(str(velu1-velu2))

output.close()
home0.close()











