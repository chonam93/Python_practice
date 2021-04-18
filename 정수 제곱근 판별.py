import math
def solution(n):
    answer = 0
    a= math.sqrt(n)
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = int(math.pow(math.sqrt(n)+1,2))
    else:
        answer = -1
    return answer