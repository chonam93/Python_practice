def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    for num in arr1:
        new_list = []
        for i in range(n-1,-1, -1):
            if num >= 2**i:
                new_list.append('#')
                num -= 2**i
            else:
                new_list.append(' ')
        new_arr1.append(new_list)
    
    new_arr2 = []
    for num in arr2:
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
        for j in range(n):
            if new_arr1[i][j] == '#' or new_arr2[i][j] =='#':
                preanswer.append('#')
            else:
                preanswer.append(' ')
        answer.append(''.join(preanswer))
    return answer



def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))