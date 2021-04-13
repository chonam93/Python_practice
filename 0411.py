def solution(numbers, hand):
    answer = ''
    dic = {1:'L', 4:'L', 7:'L', 3:'R', 6:'R', 9:'R'}
    check = [2, 5, 8, 0]
    find = [1, 3, 4, 6, 7, 9]
    for num in numbers:
        if num in find:
            answer += dic[num]
        if num in check:
            print()
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right")