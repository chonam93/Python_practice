def solution(clothes):
    dic_answer = {}
    for i in clothes:
        if i[1] in dic_answer:
            dic_answer[i[1]] += ','+i[0]
        else:
            dic_answer[i[1]] = i[0]
    countlist = []
    for j in dic_answer.values():
        if ',' in j:
            countlist.append(j.count(',')+1)
        else:
            countlist.append(1)
        
    if sum(countlist) != len(countlist) and len(countlist) != 1:
        answer = countlist[0]
        for k in countlist[1:]:
            answer = answer*k

        return answer+sum(countlist)
    else:
        return sum(countlist)


print(solution([["yellowhat", "headgear"], 
["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
