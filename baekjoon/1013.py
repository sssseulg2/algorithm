import re

def solution(n):
    reg = re.compile('(100+1+|01)+')
    case_list = [input() for _ in range(n)]
    for case in case_list:
        if reg.fullmatch(case):
            print("YES")
        else:
            print("NO")


solution(int(input()))


# (100+1+ | 01)+