N = int(input())

list = list(map(int,input().split()))

max = list[0]
min = list[0]
for i in range(1, N):
    # 1234
    if max < list[i]:
        max = list[i]

    if min > list[i]:
        min = list[i]

print(min, max)