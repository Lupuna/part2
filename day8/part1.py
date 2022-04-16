with open('input.txt') as home0:
    home = home0.read().split('\n')


velu1,velu2 = 0,0

velu1 = sum([len(string) for string in home])

for string in home:
    string = string[1:-1]
    string = string.replace('\\\"', ' ').replace('\\\\', ' ')
    velu2 += len(string) - 3*string.count('\\x')
    print(string)

output = open('output1.txt', 'w')
output.write(str(velu1-velu2))

output.close()
home0.close()











