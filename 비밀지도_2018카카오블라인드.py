def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    for num in arr1:
        new_list = []
        for i in range(n-1,-1, -1): # 인덱스 크기에서 1씩 작아진다
            if num >= 2**i: # 2진법 계산 / 2의 i승 보다 크다면 #더해주고 그 만큼 빼준다
                new_list.append('#')
                num -= 2**i
            else: # 아니라면 공백 추가
                new_list.append(' ')
        new_arr1.append(new_list)
    
    new_arr2 = []
    for num in arr2: # 동일
        new_list = []
        for i in range(n-1,-1, -1):
            if num >= 2**i:
                new_list.append('#')
                num -= 2**i
            else:
                new_list.append(' ')
        new_arr2.append(new_list)

    for i in range(n):
        preanswer = []
        for j in range(n): # 같은 인덱스 자리 비교
            if new_arr1[i][j] == '#' or new_arr2[i][j] =='#': #둘 중 하나라도 #이면 # 추가
                preanswer.append('#')
            else: # 둘 다 #이 없다면 공백 추가
                preanswer.append(' ')
        answer.append(''.join(preanswer)) # 마지막으로 join 사용하여 ''없애준다
    return answer



# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))