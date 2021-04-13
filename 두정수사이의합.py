def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a):
            answer += i
        answer += a
    if a < b:
        for i in range(a, b):
            answer += i
        answer += b
    if a == b:
        answer = a
    return answer


solution(3,6)