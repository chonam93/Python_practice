def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    low_rank = 0
    zero_count = 0
    for i in lottos:
        if i in win_nums:
            low_rank += 1 
            win_nums[win_nums.index(i)] = -1
        elif i == 0:
            zero_count += 1
    answer.append(rank[low_rank])

    high_rank= 0
    check_list = []
    for j in win_nums:
        if j != -1:
            check_list.append(j)
    if len(check_list) >= zero_count:
            high_rank = low_rank + zero_count
    else:
        high_rank = low_rank
    answer.append(rank[high_rank])
    answer.reverse()

    return answer

print(solution([0, 0,0, 0,0, 0], [31, 10, 45, 1, 6, 19]))

