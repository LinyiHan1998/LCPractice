from collections import defaultdict
def getDiscountPairs(x,prices):
    res = 0
    nums = defaultdict(int)
    for price in prices:
        p = abs(x - price%x)
        
        if price%x in nums:
            print(price,p)
            res += nums[price%x]
        else:
            nums[p] += 1
    #print(nums)
    return res
if __name__ == '__main__':
    x = 60
    prices = [31, 25, 85, 29, 35]
    print(getDiscountPairs(x,prices))