def solution(answers):
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

print(solution([3,3,1,1,2,2]))
