import random
def solution(nums):
    numbers = set(range(2, max(nums)*3))
    for i in range(2, max(nums)):
        numbers -= set(range(2*i, max(nums)*3, i))
    check_list = []
    for j in range(len(nums)):
        for k in range(1, len(nums)):
            if j < k and j != k:
                for l in range(2, len(nums)):
                    if k != l and k < l and nums[j] + nums[k] + nums[l] not in check_list and nums[j] + nums[k] + nums[l] in numbers:
                        check_list.append(nums[j]+nums[k]+nums[l])
    return len(check_list)   
    
    # count = (len(nums)*(len(nums)-1)*(len(nums)-2))//6
    # cnt = 0
    # answer_list = []
    # answer_check = []
    # while cnt < count:
    #     new_numbers = []
    #     new_cnt = 0
    #     while new_cnt < 3:
    #         a = random.choice(nums)
    #         second_numbers = []
    #         if a not in second_numbers:
    #             second_numbers.append(a) 
    #             if second_numbers not in new_numbers and len(second_numbers)>3:
    #                 new_numbers.append(second_numbers)
    #                 b = sum(second_numbers)
    #                 new_cnt += 1
    #     if b not in answer_list and b in numbers:
    #         answer_list.append(b)
    #     if b not in answer_check:
    #         cnt += 1
    # answer = len(answer_list)
    

print(solution([1,2,7,6,4]))