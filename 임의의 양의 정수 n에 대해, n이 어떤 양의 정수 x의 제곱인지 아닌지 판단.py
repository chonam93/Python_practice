import math

def solution(n):
    answer = 0 
    a =math.sqrt(n)
    if int(a) == a :
        answer = (math.sqrt(n) + 1)*(math.sqrt(n) + 1)
    else:
        answer = -1
    return answer

print(solution(12))