import random
def solution(nums):
    numbers = set(range(2, sum(nums)+1))
    for i in nums:
        if i != 1:
            numbers -= set(range(2*i, sum(nums)+1, i))
    count = (len(nums)*(len(nums)-1)*(len(nums)-2))//6
    cnt = 0
    answer_list = []
    answer_check = []
    while cnt < count:
        new_numbers = []
        new_cnt = 0
        while new_cnt < 3:
            a = random.choice(nums)
            second_numbers = []
            if a not in second_numbers:
                second_numbers.append(a) 
                if second_numbers not in new_numbers and len(second_numbers)>3:
                    new_numbers.append(second_numbers)
                    b = sum(second_numbers)
                    new_cnt += 1
        if b not in answer_list and b in numbers:
            answer_list.append(b)
        if b not in answer_check:
            cnt += 1
    answer = len(answer_list)
    
    return answer

print(solution([1,2,3,4]))