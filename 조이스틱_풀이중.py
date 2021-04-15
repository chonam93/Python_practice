import string
#<JAN> 까지는 성공
def solution(name):
    answer = 0
    alpha = string.ascii_uppercase
#ABCDEFG HIJKLMNOP QRSTUVWXYZ
    for i in name:
        if i == 'A':
            answer += 1
        else:    
            to_a = abs(alpha.index(i)-alpha.index('A'))
            to_z = abs(alpha.index(i)-alpha.index('Z'))
            # d =alpha.index(name[name.index(i)-1])
            # c = name[name.index(i)-1]
            first = to_a - alpha.index(name[name.index(i)-1])
            second = to_z - alpha.index(name[name.index(i)-1])
            if name.index(i)==0:
               cnt = alpha.index(i)
               answer += cnt + 1
            elif first >= second:
                answer += abs(second)
            elif first < second:
                answer += abs(first) + 1

    return answer

print(solution("JAN"))