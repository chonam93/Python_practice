def solution(n, lost, reserve):
    answer = 0
    answer += n - len(lost)
    for lost_student in lost:
        if lost_student in reserve:
            answer += 1
            reserve.remove(lost_student)    
        elif lost_student - 1 in reserve and lost_student - 1 not in lost:
            answer += 1
            reserve.remove(lost_student-1)
        elif lost_student + 1 in reserve and lost_student + 1 not in lost:
            answer += 1
            reserve.remove(lost_student+1)        
    return answer


print(solution(30, [2,3,4,5,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11]))