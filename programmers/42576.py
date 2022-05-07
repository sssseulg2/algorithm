def solution(participant, completion):
    dic={}
    sum = 0

    for i in participant:
        dic[hash(i)] = i
        sum += hash(i)
    
    for i in completion:
        sum -= hash(i)
    
    answer = dic[sum]

    return answer

# print(solution(participant=["mislav", "stanko", "mislav", "ana"],completion=["stanko", "ana", "mislav"]))
