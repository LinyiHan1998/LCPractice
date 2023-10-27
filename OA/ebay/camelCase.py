def solution(docstring):
    res = ''
    i = 0
    cnt = 0
    while i < len(docstring):

        if docstring[i] == "'":
            cnt += 1
        if cnt %2 == 0:
            res += docstring[i]
            i += 1
            continue
        # if docstring[i] == '_' and i+1<len(docstring):
        if docstring[i] == '_':
            if i+1 >= len(docstring):
                break
            if docstring[i+1] == "'":
                
                i += 1
                continue
            if docstring[i+1] == docstring[i+1].upper():
                while docstring[i] != "'" and i<len(docstring):
                    res += docstring[i]
                    i+=1
                continue
            res += docstring[i+1].upper()
            i += 1

        else:
            res += docstring[i]
        i += 1

    return res
# def alter(s):
#     res = ''
#     for i in range(len(s)):
#         if s[i] == '_':
#             if i+1 < len(s):
#                 res += (s[i+1])
#         else:
#             res += s[i]
# def solution(sentence):
#     name = sentence.split("'")
#     print(name)
#     for i in range(len(name)):
#         if '_' in name[i]:
#             name[i] = alter(name[i])
#     return "'".join(name)

if __name__=='__main__':
    s = "not_to_be_changed Function 'some_function' has two arguments 'shoet_arg very_long_argument_'. The 'very_LONG_argument_'"
    #print(alter(s))
    print(solution(s))