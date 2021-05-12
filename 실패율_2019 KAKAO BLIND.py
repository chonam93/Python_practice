## 실패율 = 스테이지 도달했으나 클리어 못한 플레이어 수 / 스테이지 도달한 플레이어 수

# N은 전체 스테이지의 개수
# stages에는 1부터 N+1 사이의 숫자
# stages의 길이가 사용자의 수
# - 각 사용자가 현재 도전 중인 스테이지 번호를 나타냄
# - N+1은 마지막 스테이지 (N번째 스테이지) 까지 클리어 한 사람을 타나낸다
# 만약 실패율이 같은 스테이지가 있다면 / 작은 번호의 스테이지가 앞으로
# 스테이지에 도달한 유저가 없는 경우 (앞에서 다 실패) 해당 스테이지 실패율은 0

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호를 출력하라

def solution(N, stages):
    fail_list = {}
    cal = len(stages)
    for i in range(1, N+1):
        count_loser = stages.count(i)
        if count_loser != 0:
            fail_list[i] = count_loser / cal
            cal -= count_loser
        if count_loser == 0:
            fail_list[i] = 0

    fail_list = sorted(fail_list.items(), key =  lambda x : x[1], reverse = True)
    answer = [ i[0] for i in fail_list ]

    return fail_list

##한희님 코드 푸는중...
# def solution(N, stages):
    stages=sorted(stages)
    players=len(stages)
    answer=[]
    result=[]
    for i in range(len(stages)):
        if stages[i] > N:
            del stages[i]
    for j in range(1,N+1):
        try:
            if j in stages:
                answer.append(stages.count(j)/players)
                players=players-stages.count(j)
            else:
                answer.append(0.0)
        except:
            continue
    answer=dict(zip(range(1,N+1),answer))
    answer=sorted(answer.items(), key=lambda x:x[1], reverse=True) 
    for i in answer:
        result.append(i[0])
    return result

##프로그래머스 다른 풀이
#def solution(N, stages):
    fail = {}
    for i in range(1,N+1): 
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i]) # LIST COMPREHENSION 에다가 IF문 적용 실패율 계산한 내용
        except:
            fail_ = 0 # TRY에서 실패할 경우 (탈락한 사람이 없을 경우 분자가 0이 되어 계산이 불가) EXCEPT 예외 처리로 0을 넣어 준다
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True) # key = lambda x : x[1] 이 아닌 다른 방법
    # 위 처럼 해결하면 리스트 형식으로 바로 키 값이 나온다

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
