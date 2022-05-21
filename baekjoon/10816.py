# 메모리 115904 시간 4852
import sys
input = sys.stdin.readline

def BinaryLowerBound(card_list, check):
    start_index = 0
    final_index = len(card_list)
    while start_index<final_index:
        mid_index = start_index + (final_index-start_index)//2
        if card_list[mid_index] >= check:
            final_index = mid_index
        elif card_list[mid_index] < check:
            start_index = mid_index + 1
    return start_index

def BinaryUpperBound(card_list, check):
    start_index = 0
    final_index = len(card_list)
    while start_index<final_index:
        mid_index = start_index + (final_index-start_index)//2
        if card_list[mid_index] > check:
            final_index = mid_index
        elif card_list[mid_index] <= check:
            start_index = mid_index + 1
    return start_index

def solution():
    n = int(input())
    card_list = list(map(int, input().split()))
    card_list.sort()

    m = int(input())
    check_list = list(map(int, input().split()))

    count_list = []

    for check in check_list:
        start_index = BinaryLowerBound(card_list, check)
        final_index = BinaryUpperBound(card_list, check)
        count_list.append(final_index-start_index)
    print(*count_list)

solution()

