import random
n = int(input())
cnt = 0
num_list = []
while cnt < n:
    rnum = random.randint(1, n)
    if rnum not in num_list:
        num_list.append(rnum)
        cnt += 1
# 랜덤변수 가진 리스트 생성
# min 사용한 내 풀이
'''for i in range(len(num_list)-2): # n-1번 실행
    a = min(num_list[i+1:]) # i번 자리 이후 최솟값
    b = num_list[i]
    c = num_list.index(min(num_list[i+1:]))
    if num_list[i] < min(num_list[i+1:]):
        continue
    if num_list[i] > min(num_list[i+1:]):
        num_list[i] = a
        num_list[c] = b

print(num_list)
'''
# 자리 비교해가는 풀이
for i in range(0, len(num_list)-1):
    minV = i

    for j in range(i+1, len(num_list)):
        if num_list[j] < num_list[minV]:
            minV = j

    temp = num_list[i]
    num_list[i] = num_list[minV]
    num_list[minV] = temp
    
print(num_list)
        