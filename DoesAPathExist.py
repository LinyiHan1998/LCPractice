import math
import collections
def isSquare(x):
    sqrt = int(math.sqrt(x))
    if sqrt **2 == x:
        return True
    else:
        return False
    
def canReach(c,x1,y1,x2,y2):
    if isSquare(x1 + y1):
        return "No"
    if isSquare(x2 + y2):
        return "No"
    
    pair = (x1,y1)
    deque = collections.deque()
    deque.append(pair)

    visited = set()
    visited.add(pair)

    while deque:
        tmp = deque.popleft()
        x=tmp[0]
        y=tmp[1]

        if (x==x2) & (y == y2):
            return "Yes"
        if(x+y,y) not in visited:
            if((x+y)==x2) & (y == y2):
                return "Yes"
            deque.append((x+y,y))
            visited.add((x+y,y))
        
        if (x+y<=y2) & (not isSquare(x+x+y)):
            if (x,x+y) not in visited:
                if (x ==x2) &((x+y)==y2):
                    return "Yes"
                deque.append((x,x+y))
                visited.add((x,x+y))
        if(x + c <= x2) & (y + c <= y2) & (not isSquare(x+c+y)):
            if(x+c,y+c) not in visited:
                if((x+c)==x2)&((y+c)==y2):
                    return "Yes"
                deque.append((x+c,y+c))
                visited.add((x+c,y+c))
    return "No"

if __name__=='__main__':
    print(canReach(1,1,4,7,6))