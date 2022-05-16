import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

for i in reversed(coin):
    count += k//i
    k = k%i

print(count)