def solution(participant, completion):
    answer = ''
    parti_dic = {}
    compl_dic = {}

    for i in range(0, len(participant)):
        parti_dic[i] = participant[i]
    for j in range(0, len(completion)):
        compl_dic[i] = completion[j]

    

    return answer


solution(["mislav", "stanko", "mislav", "ana", "cho"], ["stanko", "ana", "mislav"])
