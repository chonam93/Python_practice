import random #절반성공
import sys
sys.setrecursionlimit(100000)

def solution(numbers):
    answer = []
    ran_nums = list(numbers)
    answer_listlist1 = []
    answer_listlist2 = []
    answer_listlist3 = []
    cnt = 0
    while cnt < 6:
        answer_list = []
        cnt2 = 0
        while cnt2 < 3:
            choice_num = random.choice(ran_nums)
            if choice_num not in answer_list:
                answer_list.append(choice_num)
                cnt2 += 1
        join_list = ''.join(answer_list)
        if join_list not in answer_listlist1:
            answer_listlist1.append(join_list)
            cnt += 1
    print(answer_listlist1)
    cnt = 0
    while cnt < 6:
        answer_list = []
        cnt2 = 0
        while cnt2 < 2:
            choice_num = random.choice(ran_nums)
            if choice_num not in answer_list:
                answer_list.append(choice_num)
                cnt2 += 1
        join_list = ''.join(answer_list)
        if join_list not in answer_listlist2:
            answer_listlist2.append(join_list)
            cnt += 1
    print(answer_listlist2)
    cnt = 0
    cnt2 = 0
    while cnt2 < 3:
        choice_num = random.choice(ran_nums)
        if choice_num not in answer_listlist3:
            answer_listlist3.append(choice_num)
            cnt2 += 1
        
    for check1 in answer_listlist2:
        if int(check1[0]) != 0 and int(check1)%2 != 0 and int(check1)%3 != 0 and int(check1)%5 != 0 and int(check1)%7 != 0:
            answer.append(check1)
    for check1 in answer_listlist3:
        if int(check1) != 1 and int(check1[0]) != 0 and int(check1)%2 != 0 and int(check1)%3 != 0 and int(check1)%5 != 0 and int(check1)%7 != 0:
            answer.append(check1)
        if int(check1) == 7 or int(check1) == 5 or int(check1) == 3 or int(check1) == 2:
            answer.append(check1)       


    print(answer_listlist3)
    print(answer)
    return answer



solution("189")