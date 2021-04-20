def solution(n):
    answer = ''
    third = []
    while n:
        a =  n % 4
        if a == 1:
            third += str(1)
        elif a == 2:
            third += str(2)
        elif a == 0:
            third += str(4)
        n = n//4
    third.reverse()

    return third

print(solution(4))