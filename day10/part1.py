with open('input.txt') as home0:
    home = home0.read()

cycles = 0

while cycles <= 39:
    item = home[0]
    number = 1
    end = ''
    for i in (home+'x')[1:]:
        if item == i:
            number +=1
        else:
            end += str(number) + item
            item = i
            number = 1

    home = end

    cycles +=1

output = open('output1.txt', 'w')
output.write(str(len(end)))

output.close()
home0.close()



