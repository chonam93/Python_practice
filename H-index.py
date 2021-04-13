def solution(citations):
    answer = 0
    for h in range(max(citations)):
        h_high = 0
        h_low = 0
        for num in citations:
            if h <= num:
                h_high += 1
            if h >= num:
                h_low += 1
        if h <= h_high and h >= h_low and h >= answer:
            answer = h
    return answer



print(solution([3, 0, 6, 1, 4, 7, 8]))