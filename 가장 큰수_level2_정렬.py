# def solution(numbers):
#     answer = ''
#     list_num =[]
#     for i in numbers:
#         i = list(str(i))
#         list_num.append(i)
#     list_num = sorted(list_num, key = lambda x : x[0], reverse=True)
    
#     for i in list_num
    
#     return list_num

def solution(numbers):
    list_num =[]
    for i in numbers:
        list_num.append(str(i))
        print(str(i)*5)
    list_num = sorted(list_num, key = lambda x : x*5, reverse=True)    
    print(list_num)
    answer = ''.join(list_num)
    return answer

# def solution(numbers):
#     answer = '' 
#     list_answer = []
#     for i in range(len(numbers), -1):
#         maxnum = -100
#         list_num = []
#         for num in numbers:
#             if len(num) > 1:
#                 list_num.append(num*(10**(i-))    
#             list_num.append(num*(10**i))
#         maxnum = max(list_num)
#         list_answer.append(str(maxnum))
            
#     return list_answer

print(solution([3, 320, 314, 5, 9]))

# a = ['1']
# print(a[-1])