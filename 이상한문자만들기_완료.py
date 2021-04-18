def solution(n):
    answer = ""
    split_n = n.split(" ")
    for i in range(len(split_n)):
        new_alpha = list(split_n[i])
        for k in range(len(new_alpha)):
            if k % 2 == 0:
                new_alpha[k] = new_alpha[k].upper()
            else:
                new_alpha[k] = new_alpha[k].lower()
        split_n[i] = ''.join(new_alpha)
    answer = ' '.join(split_n)    
    return answer

print(solution("try print hello world"))