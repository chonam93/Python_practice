def solution(absolutes, signs):
    
    answer = 0

    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += absolutes[i]*(-1)

    return answer

print(solution([4,7,12],['true','false','true']))