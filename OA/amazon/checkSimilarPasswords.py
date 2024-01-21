def checkSimilarPasswords(newPasswords,oldPasswords):
    res = []
    for i,pwd in enumerate(newPasswords):
        idx = 0
        source = 0
        start = 0
        flag = 0
        while idx < len(pwd):
            if start > len(oldPasswords):
                break
            elif ord(pwd[idx]) > ord(oldPasswords[i][start]):
                idx += 1
                continue
            if start == len(oldPasswords):
                res.append('YES')
                flag = 1
                break
            elif ord(oldPasswords[i][start]) - ord(pwd[idx]) <= 1:
                start += 1
                idx += 1
            
            else:
                start = 0
                source += 1
                idx = source
        if flag == 0:
            res.append('NO')
    return res
if __name__=="__main__":
    newPasswords = ["baacbb", "accdb", "baacba"]
    oldPasswords = ["abdbc", "ach", "abb"]
    print(checkSimilarPasswords(newPasswords,oldPasswords))
