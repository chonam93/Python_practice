def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):                  # 1의 로우길이
        answer_list = []
        for j in range(len(arr2[0])):           # 2의 컬럼길이
            for m in range(len(arr2)):          # 2의 
                a= arr1[i][j]*arr2[j][m]
                print(a)
                answer_list.append(arr1[i][j]*arr2[j][m])
            answer.append(sum(answer_list))
    return answer