def solution(s, n):
    answer = ''
    str_s = list(s)
    alp1 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alp2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in str_s:
        if i in alp1:
            i = alp1[alp1.index(i)+n]
            answer += i
        if i in alp2:
            i = alp2[alp2.index(i)+n]
            answer += i
        if i == ' ':
            answer += ' '
        answer = ''.join(answer)
    return answer

print(solution('a  b', 1))

