def solution(participant, completion):
    answer = ''
    new_dic = {i : participant[i] for i in range(len(participant))}
    
    for i in range(len(new_dic)):
        if new_dic[i] in completion:
            participant.remove(new_dic[i])
            completion.remove(new_dic[i])
    return participant

print(solution(["leo", "kiki", "eden", 'kiki'],["eden", "kiki", 'kiki']))