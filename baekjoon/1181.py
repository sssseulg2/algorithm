# 메모리 36112 시간 868
import sys

n = int(sys.stdin.readline())
word_list = [input() for _ in range(n)]

word_list = sorted(set(word_list), key = lambda x: (len(x),x))


for word in word_list:
    print(word)