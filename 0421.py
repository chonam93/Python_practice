# import random
# def solution(nums):
#     numbers = set(range(2, sum(nums)+1))
#     for i in range(2, sum(nums)+1):
#         if i in numbers:
#             numbers -= set(range(2*i, sum(nums)+1, i))
#     count = len(nums)*(len(nums)-1)
#     cnt = 0
#     answer_list = []
#     answer_check = []
#     while cnt < count:
#         new_numbers = []
#         new_cnt = 0
#         while new_cnt < 3:
#             a = random.choice(nums)
#             if a not in new_numbers:
#                 new_numbers.append(a) 
#                 new_cnt += 1
#         b = sum(new_numbers)
#         if b not in answer_list and b in numbers:
#             answer_list.append(b)
#         if b not in answer_check:
#             cnt += 1
#     answer = len(answer_list)
    
#     return answer

# print(solution([1,2,7,6,4]))
import random
def solution(nums):
    numbers = set(range(2, sum(nums)+1))
    for i in range(2, sum(nums)+1):
        if i in numbers:
            numbers -= set(range(2*i, sum(nums)+1, i))
    count = len(nums)*(len(nums)-1)
    cnt = 0
    answer_list = []
    answer_check = []
    while cnt < count:
        new_numbers = []
        new_cnt = 0
        while new_cnt < 3:
            for new_cnt in range(3):
                for i in range(3):
                    for j in range(3):
                        if new_cnt != i or new_cnt != j:


        b = sum(new_numbers)
        if b not in answer_list and b in numbers:
            answer_list.append(b)
        if b not in answer_check:
            cnt += 1
    answer = len(answer_list)
    
    return answer

print(solution([1,2,7,6,4]))