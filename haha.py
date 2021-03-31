def solution(x, n):
    answer = []
    for i in range(n):
        int_ans = x + x*i
        answer += str(int_ans)

    answer = list(map(int, answer))

    return answer

print(solution(2, 5))