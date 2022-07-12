N = int(input())

cost_rgb = []
for i in range(N):
    cost_rgb.append(list(map(int, input().split())))

for i in range(1,N):
    cost_rgb[i][0] = min(cost_rgb[i-1][1], cost_rgb[i-1][2]) + cost_rgb[i][0]
    cost_rgb[i][1] = min(cost_rgb[i-1][0], cost_rgb[i-1][2]) + cost_rgb[i][1]
    cost_rgb[i][2] = min(cost_rgb[i-1][0], cost_rgb[i-1][1]) + cost_rgb[i][2]

print(min(cost_rgb[N-1]))