def solution(answers): #리스트 안에 있는 순서로 문제풀고 몇 문제 맞췄는지, 1등을 출력 / 여럿이라면 오름차순으로 출력
    answer = []
    first_supo = [1, 2, 3, 4, 5]
    second_supo = [2, 1, 2, 3, 2, 4, 2, 5]
    third_supo = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_dic = {1:0, 2:0, 3:0}
    for ans in answers:
        a = answers.index(ans)
        if ans == first_supo[(answers.index(ans))%5]:
            check =(answers.index(ans))%5
            answer_dic[1] += 1
        if ans == second_supo[(answers.index(ans))%8]:
            check =(answers.index(ans))%5
            answer_dic[2] += 1
        if ans == third_supo[(answers.index(ans))%10]:
            check =(answers.index(ans))%5
            answer_dic[3] += 1
        answers[answers.index(ans)] = 0
    answer_sort = sorted(answer_dic.items(), key=lambda x:x[1], reverse=True)
    answer =[]
    for i in answer_sort:
        if i[1] == answer_sort[0][1]:
            answer.append(answer_sort[answer_sort.index(i)][0])
    
    return answer
print(solution([1,3,2,4,2,3,3]))
# ---------------다른 사람 풀이
#####사이클함수 사용 풀이

# from itertools import cycle

# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)

#     return [i + 1 for i, v in enumerate(scores) if v == highest]

# #####  enumerate 사용
# def solution(answers):
    # pattern1 = [1,2,3,4,5]
    # pattern2 = [2,1,2,3,2,4,2,5]
    # pattern3 = [3,3,1,1,2,2,4,4,5,5]
    # score = [0, 0, 0]
    # result = []

    # for idx, answer in enumerate(answers):
    #     if answer == pattern1[idx%len(pattern1)]:
    #         score[0] += 1
    #     if answer == pattern2[idx%len(pattern2)]:
    #         score[1] += 1
    #     if answer == pattern3[idx%len(pattern3)]:
    #         score[2] += 1

    # for idx, s in enumerate(score):
    #     if s == max(score):
    #         result.append(idx+1)

    # return result