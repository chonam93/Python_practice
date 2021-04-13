def solution(n):
    answer = []
    list_str_n = list(str(n))
    list_str_n.reverse()
    for a in list_str_n:
        answer.append(int(a))
    return answer

def digit_reverse(n): #map을 이용한 풀이
    return list(map(int, reversed(str(n))))


def solution2(n):
    answer = [int(i) for i in str(n)][::-1]
    return answer
