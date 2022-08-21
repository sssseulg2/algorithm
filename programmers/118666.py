def solution(survey, choices):
    answer = []

    character_type = dict({
        "R" : 0, "T" : 0,
        "C" : 0, "F" : 0,
        "J" : 0, "M" : 0,
        "A" : 0, "N" : 0,
    })

    for i in range(len(choices)):
        if choices[i] > 4:
            character_type[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            character_type[survey[i][0]] += 4 - choices[i]
    
    character_tuple =  [(k, v) for k, v in character_type.items()]

    for i in range(0,8,2):
        sorted_dict = sorted(character_tuple[i:i+2], key = lambda x : (-x[1], x[0]))
        answer.append(sorted_dict[0][0])

    return("".join(answer))


print(solution(["AN", "CF", "MJ", "RT", "NA"],[5,3,2,7,5]))
print(solution(["TR", "RT", "TR"],[7,1,3]))