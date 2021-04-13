def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    
    answer.sort()

    return answer

print(solution([5,0,2,7]))


def solution2(numbers): #set함수사용. set은 중복값 삭제해준다
    answer = [] # not in 사용할 필요가 없는 것. 계산값 그대로 받고 set으로 중복값 삭제
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))