def solution(participant, completion):
    answer = ''
    p_dict = { i : name for i, name in enumerate(participant)}
    c_dict = { i : name for i, name in enumerate(completion)}
    for i in range(len(c_dict)):
        if c_dict[i] in participant:
            p_dict = p_dict.remove(c_dict[i])

    return p_dict, c_dict

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))