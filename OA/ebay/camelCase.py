def alter(s):
    res = ''
    i = 0
    while i < len(s):
        if s[i] == '_' and i+1<len(s):
            res += s[i+1].upper()
            i += 1
        else:
            res += s[i]
        i += 1
    #res = res.split('_')
    return res

if __name__=='__main__':
    s = 'res_wer_'
    print(alter(s))