def solution(progresses, speeds):

    answer = []
    while progresses:
        for progress_num in range(len(progresses)):
            if progresses[progress_num] < 100:
                progresses[progress_num] = progresses[progress_num] + speeds[progress_num]
        count = 0
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        if count != 0:
            answer.append(count)
    return answer

# 모범답안.......
# Q [걸리는 날짜][배포 되는 수]

# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1]) 
#         else: # 앞 순서 중 가장 늦은 프로그레스보다 빠르면 카운트만 올려줌
#             Q[-1][1]+=1
#     return [q[1] for q in Q]


print(solution([93, 30, 55], [1, 30, 5]))