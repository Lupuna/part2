with open('input.txt') as home0:
    home=home0.read().split('\n')

def parse(line):
    return  [c == '#' for c in line]

def slove(lines):
    grid = [parse(line) for line in lines]

    for scroll in range(100):
        new_grid = []

        grid[0][0] = True
        grid[0][99] = True
        grid[99][0] = True
        grid[99][99] = True

        for string in range(len(grid)):
            new_row = []
            row = grid[string]
            for number in range(len(row)):
                c = grid[string][number]
                a = normal(grid, number, string)
                if c: # python понимает эту строку, как если правда (if True)
                    new_row.append(a == 2 or a == 3)
                else:
                    new_row.append(a == 3)
            new_grid.append(new_row)
        grid = new_grid

        grid[0][0] = True
        grid[0][99] = True
        grid[99][0] = True
        grid[99][99] = True

    return sum(sum(row) for row in grid)

def normal(grid, number, string):
    total = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if x==0 and y==0:
                continue
            if  number+x < 0 or number + x > 99:
                continue
            if y + string < 0 or y + string > 99:
                continue
            total += grid[y+string][number+x]
    return total

output = open('output2.txt', 'w')
output.write(str(slove(home)))

output.close()
home0.close()