
def count(num1,num2):
    cnt = 0
    num = 0
    for num in range(num1):
        tmp = num
        add = 0
        while tmp:
            add += tmp%10            
            tmp //= 10

        if add == num2:
            cnt += 1
            print('cnt:{}'.format(cnt))
    return cnt

if __name__=='__main__':
    print(count(20,5))
