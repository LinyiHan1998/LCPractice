def getMaxRewardPoints(reward):
    res = 0
    idx = 0
    reward = sorted(reward,reverse=True)
    print(reward)
    for re in reward:
        if re - idx <= 0:
            break
        
        res += re - idx
        idx += 1
    return res
if __name__ == '__main__':
    #reward = [5, 2, 2, 3, 1]
    reward = [5,5,5]
    print(getMaxRewardPoints(reward))
