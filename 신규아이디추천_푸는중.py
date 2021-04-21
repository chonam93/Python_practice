# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.




def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    special = ['-', '.', '_']
    for i in new_id:
        if i.isalpha() == True or i.isdigit() == True or i in special:
            answer += i    
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.strip('.')
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer


print(solution("z-+.^."))
# print( 'i' == string.ascii_uppercase)

    # for i, val in enumerate(real_new):
    #     dic_id[i] = val
    # cnt_1 = 0
    # for i in range(len(dic_id)):
    #     if dic_id[i] in string.ascii_uppercase:
    #         dic_id[i] = dic_id[i].lower()
    #     if dic_id[i] == '.' and dic_id[i+1] == '.':
    #         cnt_1 += 2
    #     if dic_id[i] == '.' and dic_id[i+1] == '.' and cnt_1 > 1:
    #         dic_id[i]=' '
    #         cnt_1 -= 2
    #     if dic_id[i] == '.' and dic_id[i+1] != '.' and cnt_1 > 1:
    #         dic_id[i] = ' '
    #         cnt_1 = 0
    # join_id =dic_id.values()
    # join_s = ''.join(join_id)
    # split_id = join_s.split()
    # answer =split_id
    # if answer[0][0] == '.':
    #     answer.remove(answer[0][0])
    # return answer



# a = 'abcd'
# print(a[1].upper())