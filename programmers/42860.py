def solution(name):
    alphabet_control = 0

    control = []
    reverse_control = []
    cnt, cnt2 = 0, 0
    for i in range(len(name)):
        j = len(name)-i-1
        if j != 0:
            if name[j] != "A":
                cnt2 += 1
                reverse_control.insert(0, cnt2)
                cnt2 = 0
            else:
                cnt2 += 1
        if i != 0:
            if name[i] != "A":
                cnt += 1
                control.append(cnt)
                cnt = 0
            else:
                cnt +=1

        asc = ord(name[i])
        if asc > 78:
            alphabet_control += (91-asc)
        else:
            alphabet_control += (asc-65)
        

    left1 = 0
    right1 = sum(reverse_control)
    left2 = 0
    right2 = sum(reverse_control) * 2
    
    answer = [right1]


    for i in range(len(control)):
        left1 += control[i]*2
        right1 -= reverse_control[i]

        left2 += control[i]
        right2 -= reverse_control[i]*2

        answer.append(left1+right1)
        answer.append(left2+right2)
    



    return min(answer)+alphabet_control

print(solution("BBAABB")) #8
print(solution("BBABAAAABBBAAAABABB")) #26
# print(solution("JEROEN"))
# print(solution("JAN"))


# "BBABAAAABBBAAAABABB" 26
# "BBAAAAAABBBAAAAAABB" 20
# "BBBAAAAAAAB" 8
# "ABAAAAAAAAABB" 7
# "BBAABB" 8
# "BBBAAAAABAAAAAAAAAAA" 12
# "BAAAAAAAAAABAAAAAABB" 13
# "AAABBAB" 7