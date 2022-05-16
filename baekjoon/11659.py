import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
prefix_sum = [0]

for i in range(n):
    prefix_sum.append(prefix_sum[i] + number[i])

for a in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])

