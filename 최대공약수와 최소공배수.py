def solution(n, m):
    answer = []
    lcm_n = []
    lcm_m = []
    lcm = []
    for num in range(1,n+1):
        if n % num == 0:
            lcm_n.append(num)
    for num in range(1,m+1):
        if m % num == 0:
            lcm_m.append(num)
    for check in lcm_n:
        if check in lcm_m:
            lcm.append(check)
    answer.append(max(lcm))
    answer.append((n*m)//max(lcm))


    return answer

print(solution(2, 5))