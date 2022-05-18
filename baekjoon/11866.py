import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = list(range(1, n+1))
answer = []
popindex = k-1

while queue:
    for i in range(k-1):
        queue.append(queue.pop(0))
    answer.append(queue.pop(0))

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")