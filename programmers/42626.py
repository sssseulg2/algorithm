import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
        answer += 1
        if len(scoville) < 2 and scoville[0]<K:
            return -1

    return answer


# print(solution([1, 2, 9, 3, 10, 12], 7))
# solution([0,0,0,0], 7)