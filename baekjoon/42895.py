def solution(N, number):
    Ns = [0]
    Ns.append(N)
    for i in range(2, 9):
        Ns.append(N * (10 ** (i-1)) + Ns[i-1])

    dp = [0]
    dp.append(set([Ns[1]]))

    for i in range(2,9):
        dp.append(set([Ns[i]]))
        
        for j in range(1,i):
            #j의 모든 원소들, i-j의 모든 원소들의 조합 + - * /
            # j : 1,2,3,,  i-j: i-1,i-2,,,
            for k in dp[j]:
                dp[i].update(list(map(lambda x: x + k, dp[i-j])))
                dp[i].update(list(map(lambda x: x - k, dp[i-j])))
                dp[i].update(list(map(lambda x: x * k, dp[i-j])))
                dp[i].update(list(map(lambda x: k // x, filter(lambda z: z > 0, dp[i-j]))))

    for i in range(1,9):
        if number in dp[i]: return i
    
    return -1


print(solution(5,12))