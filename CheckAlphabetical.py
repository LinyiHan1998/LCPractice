def CheckAlphabetical(str1):
    for i in range(len(str1)-1):
        if str1[i] <= str1[i+1]:
            continue
        return i+1
    return 0

if __name__ == '__main__':
    str1 = 'asd'
    print(CheckAlphabetical(str1))