def solution(nums):
    answer = 0
    expect = len(nums) // 2
    new_nums = []
    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
    if len(new_nums) >= expect:
        answer = expect
    else:
        answer = len(new_nums)
    return answer

print(solution([3,1,2,3]))