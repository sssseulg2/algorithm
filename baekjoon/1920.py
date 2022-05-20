import sys
input = sys.stdin.readline

def binary_search(x):
    start_index = 0
    final_index = n-1
    while final_index - start_index >= 0:
        if x == a[(final_index+start_index)//2]:
            print(1)
            return
        elif x < a[(final_index+start_index)//2]:
            final_index = (final_index+start_index)//2 - 1
        elif x > a[(final_index+start_index)//2]:
            start_index = (final_index+start_index)//2 + 1
    print(0)
    return

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
x_list = list(map(int, input().split()))

for x in x_list:
    binary_search(x)


