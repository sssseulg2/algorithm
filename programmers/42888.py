def solution(record):
    answer = []
    end_index = 0
    id = {}
    
    for end_index in range(len(record)):
        command = record[end_index].split()
        if command[0] == "Enter" or command[0] == "Change":
            id[command[1]] = command[2]

    for i in range(len(record)):
        command = record[i].split()
        if command[0] == "Enter":
            answer.append(id[command[1]] + "님이 들어왔습니다.")
        elif command[0] == "Leave":
            answer.append(id[command[1]] + "님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])