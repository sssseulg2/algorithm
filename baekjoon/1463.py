n = int(input())

count = 0
dp = [0 for i in range(n+1)]

for level in range(2,n+1):
    dp[level] = dp[level-1] + 1
    if level%2 == 0:
        if dp[level] > dp[level//2] + 1:
            dp[level] = dp[level//2] + 1
    if level%3 == 0:
        if dp[level] > dp[level//3] + 1:
            dp[level] = dp[level//3] + 1

print(dp.pop())