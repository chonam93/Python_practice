def solution(nums):
    from itertools import combinations as cb # combinations 사용
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))