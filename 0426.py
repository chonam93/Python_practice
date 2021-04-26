# def solution(people, limit):
#     answer = 0
#     new_list = dict(enumerate(people))
#     keep = []
#     for i in range(len(people)):
#         if new_list[i] <= limit or new_list[i] + min(people) > limit:
#             del new_list[i]
#             answer += 1
        
#         elif len(new_list) == 1 :
#             answer += 1
#         else:
#             keep.append(new_list[i])
#             if len(keep) > 1 and sum(keep) <= limit:
#                 keep = []
#                 answer += 1


#     return answer

def solution(people, limit):
    answer = 0
    new_list = dict(enumerate(people))
    keep = 0
    while keep < len(people):
    for i in range(len(people)):
        if len(new_list) == 1 :
            answer += 1
            break
        for j in range(i + 1, len(people)):
            if new_list[i] + min(people) > limit:
                del new_list[i]
                answer += 1
                break
            elif new_list[i] + new_list[j] <= limit:
                del new_list[i]
                del new_list[j]
                answer += 1


    return answer


print(solution([70, 50, 80, 50],100))