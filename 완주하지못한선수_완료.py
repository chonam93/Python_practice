def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)
    b.append('')
    for i in range(len(b)):
        if a[i] != b[i]:
            answer = a[i]
            break

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

##해시 이용한 풀이
def solution(participant, completion):
    dic={}
    num_k=0
    for p in participant:
        dic[hash(p)]=p 
        num_k=num_k+int(hash(p))
    for c in completion:
        num_k=num_k-hash(c)
    answer=dic[num_k]
    return answer