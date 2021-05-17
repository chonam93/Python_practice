def solution(left, right):
    answer = 0
    for num in range(left, right+1): # left부터 right까지 변수 생성
        cnt = 0 # 약수 갯수 카운트
        for div in range(1, num+1): 
            if num % div == 0: # div가 num의 약수이면 카운트 업
                cnt += 1
        if cnt % 2 == 0: # 약수의 갯수가 짝수면 +
            answer += num
        else:
            answer -= num # 홀수라면 -
    return answer

print(solution(13, 17))