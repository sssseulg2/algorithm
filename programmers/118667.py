from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    if (sum1+sum2) % 2 == 1 or (sum1+sum2)//2 < max(max(q1),max(q2)) : return -1

    for i in range((len(q1) * 3) - 1):
        if sum1 == sum2:
            answer = i
            break
        elif sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
        elif sum2 > sum1:
            sum1 += q2[0]
            sum2 -= q2[0]
            q1.append(q2.popleft())

    return answer

print(solution([3,2,7,2],[4,6,5,1]))
print(solution([1,2,1,2],[1,10,1,2]))