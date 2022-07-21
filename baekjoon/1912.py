n = int(input())
answer = sequence = list(map(int, input().split()))
reverse = list(reversed(sequence))

for i in range(n):
    if i >= 1 and reverse[i-1]>0:
        reverse[i] += reverse[i-1]

    if i >= 1 and answer[i-1] > 0:
        answer[i] += answer[i-1]

for i in range(n):
    answer[i] = answer[i] + reverse[n-1-i] - sequence[i]


print(max(answer))