def solution(d, budget):
    answer = 0
    d.sort()
    sum_d = 0
    for demand in d:
        if (sum_d + demand) <= budget:
            sum_d += demand
            answer += 1
        else:
            break

    return answer

print(solution([2,2, 3, 3],	10))