def seaBattle(grid,shots):
    res = []
    hitted = set()
    shoot = set()
    for shot in shots:
        hit = grid[shot[0]][shot[1]]
        if hit == '.':
            res.append('Missed')
        elif hit in hitted and shot in shoot:
            res.append('Already attacked')
        
