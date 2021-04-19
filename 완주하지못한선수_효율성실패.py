def solution(participant, completion):
    answer = ''
    parti_list = []

    for name in participant:
        if participant.count(name) > completion.count(name):
            parti_list.append(name)

    while True:
        cnt = len(parti_list)
        for name in parti_list:
            if name in completion:
                parti_list.remove(name)
                cnt -= 1
                completion.remove(name)
            if parti_list.count(name) >= 2:
                parti_list.remove(name)
                cnt -= 1
            cnt -= 1
        if cnt == 0:
            break
    answer = ", ".join(parti_list)
    return answer