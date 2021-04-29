# a = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# print(a)
# print('ㅡ'*20)

# print(*a, sep='\n')
# print('ㅡ'*20)

# a = list(zip(*a))
# print(a, sep='\n')
# for i in a:
#     for j in i:
#         print(i, j)
# print('ㅡ'*20)
# a = list(zip(*a))
# print(a, sep='\n')
# print('ㅡ'*20)
def solution(arr1, arr2):
    answer = []
    # arr1 = list(zip(*arr1))
    # arr1 = list(zip(*arr1))
    # arr2 = list(zip(*arr2))
    # for row_num in range(len(arr1)):
    #     for col_num in range(len(arr1[0])):
    #         answer[row_num] = arr1[row_num][col_num]*arr2[col_num][col_num]
       
    
    for i in range(len(arr1)):
        example = []
        check = 0

        for j in range(len(arr2)):
            for k in range(len(arr2[0])):
                check += arr1[i][j]*arr2[j][k]
                example.append(check)
            if len(example) == len(arr2[0]):
                answer += example
    return answer


# import numpy as np

# def solution(arr1, arr2):
#     answer = []
#     a = np.array(arr1)
#     b = np.array(arr2)

#     c= np.dot(a, b)
#     return c


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))