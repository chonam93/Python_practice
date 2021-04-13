import random
import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 

def solution(numbers):
    answer = ''
    range_num = factorial(len(numbers))
    list2 = []
    while True:
        list = []
        while True:
            num = random.choice(numbers)
            if str(num) not in list:
                list.append(str(num))
            
            if list[0] == 0:
                list.remove(0)      

            if len(list) == len(numbers):
                break
        new_num =''.join(list)
        if new_num not in list2:
            list2.append(new_num)

        if len(list2) == range_num:
            break
    
    for j in list2:
        if j > str(answer):
            answer = j
    return answer

print(solution([3, 30, 34, 5, 9]))