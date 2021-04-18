def solution(x):
    sum_x = 0
    for num in list(str(x)):
        sum_x += int(num)
    if x % sum_x == 0:
        return True
    else:
        return False

print(solution(11))

###다른 사람 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0