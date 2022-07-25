def solution(s):
    result = []
    result.append(len(s))
    for i in range(1, len(s)//2 + 1):
        s2 = ''
        count = 1
        temp = s[0:i]
        for j in range(i, len(s), i):
            print(temp)
            if temp == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    s2 = s2 + temp
                else:
                    s2 = s2 + str(count) + temp
                temp = s[j:j+i]
                count = 1
        if count == 1:
            s2 = s2 + temp    
        else:
            s2 = s2 + str(count) + temp
        result.append(len(s2))
            
            
    answer = min(result)
    return answer


print(solution("aabbaccc"))