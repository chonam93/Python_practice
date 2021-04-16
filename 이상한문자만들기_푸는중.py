def solution(n):
    answer = ""
    new_a = n.split()
    for stri in new_a:
        new_str = list(stri)   
        for s in new_str:
            for i in new_str:
                if new_str.index(i) % 2 == 0:
                    answer += i.upper()
                    new_str[new_str.index(i)] = 0
                elif new_str.index(i) % 2 == 1:
                    answer += i.lower()
                    new_str[new_str.index(i)] = 0
            break
        if new_a.index(stri) < len(new_a)-1:
            y = n.index(new_a[new_a.index(stri)][len(new_str)-1])
            n = n.replace(n[:n.index(new_a[new_a.index(stri)][len(new_str)-1])+1], '1'*(y+1))
            h = n.index(new_a[new_a.index(stri)+1][0])
            answer += ' '*(h-y-1)
    return answer



print(solution("ttt ttttt tt tttt   "))

