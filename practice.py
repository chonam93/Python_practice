def solution(arr, divisor):
    answer = []
    for number in arr:
        if number % divisor == 0:
            answer += [number]
    answer.sort()
    if answer == []:
        answer += [-1]
    return answer   
print(solution([2, 3 ,4, 6], 5))