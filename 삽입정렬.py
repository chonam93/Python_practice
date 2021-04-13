import random
cnt = 0
num_list = []
while cnt < 10:
    rnum = random.randint(1, 10)
    if rnum not in num_list:
        num_list.append(rnum)
        cnt += 1


for j in range(1, len(num_list)): # 1부터 끝까지 비교 시작
    key = num_list[j]  # 비교하고자 하는 key의 자리
    i = j - 1  # key의 자리보다 앞
    while i >= 0 and num_list[i] > key: # i가 0보다 크거나 같고 / i자리의 값이 키보다 크면 계속 반복
        num_list[i+1] = num_list[i] #바꿔준다 앞뒤를
        i = i - 1 
    num_list[i+1] = key 

print(num_list)
