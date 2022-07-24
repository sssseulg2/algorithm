def solution(s, n):
    alphabet=list(s)

    for i in range(len(alphabet)):
        o = ord(alphabet[i])
        # print(o)
        if o == 32:
            continue
        elif o >= 65 and o <=90:
            o += n
            if o > 90: o -= 26
        else:
            o += n
            if o > 122: o -= 26
        
        alphabet[i] = chr(o)

    answer = ''.join(alphabet)

    return answer


print(solution("a B z", 4))