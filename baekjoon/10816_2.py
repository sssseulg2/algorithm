# 메모리 136584 시간 672
import sys
from collections import Counter
input = sys.stdin.readline

_ = int(input())
n_list = list(map(int, input().split()))
_ = int(input())
m_list = list(map(int, input().split()))

C = Counter(n_list)
print(' '.join(f'{C[m]}' if m in C else '0' for m in m_list))