import collections
def solution(grid, shots):
    row = len(grid)
    col = len(grid[0])
    res = []
    shiplength = collections.defaultdict(int)
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '.':
                continue
            shiplength[grid[i][j]] += 1
    
    for x,y in shots:
        if grid[x][y] == '.':
            res.append('Missed')
        elif grid[x][y] == '#':
            res.append('Already attacked')
        else:
            if shiplength[grid[x][y]] == 1:
                res.append('Ship {} sunk'.format(grid[x][y]))
            elif shiplength[grid[x][y]] > 1:
                res.append('Attacked ship {}'.format(grid[x][y]))
            
            shiplength[grid[x][y]] -= 1
            grid[x][y] = '#'
            print(shiplength)
    return res
