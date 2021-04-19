import string
def solution(new_id):
    dic_id = {}
    real_new = []
    selection = list(string.ascii_letters)
    selection += ('-', '_', '.')
    for letters in new_id:
        if letters in selection:
            real_new.append(letters)

    for i, val in enumerate(real_new):
        dic_id[i] = val
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
    return answer

print(solution(".........!@BaT#*...y....abcdefghijklm"))

# a = 'abcd'
# print(a[1].upper())