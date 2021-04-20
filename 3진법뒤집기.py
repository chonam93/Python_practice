def solution(n):
    answer = 0
    third = []
    while n > 0:
        third.append(n%3)
        n = n//3
    third.reverse()
    for i in range(len(third)):
        answer += third[i]*(3**i)
    return answer

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(125))