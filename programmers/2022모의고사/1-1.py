def solution(X, Y):
    answer = []
    count = {"0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0
        }

    for i in range(len(X)):
        count[X[i]] += 1
    for i in range(len(Y)):
        if count[Y[i]] > 0:
            answer.append(Y[i])
            count[Y[i]] -= 1
    
    if len(answer) == 0:
        return "-1"

    countZero = 0
    for i in answer:
        if i == "0":
            countZero += 1
    if countZero == len(answer):
        return "0"


    answer.sort(reverse=True)
    answer = ''.join(answer)
    return answer