# def solution(arr):
#     answer = []
#     for num in range(len(arr)):
#         if num >= 1 and arr[num] != arr[num-1]:
#             answer.append(arr[num-1])
#         if num == len(arr)-1 and answer and answer[len(answer)-1] != arr[num]:
#             answer.append(arr[num])
#     return answer

def solution(arr):
    answer = []
    for index in range(len(arr)):
        if index >= 1 and arr[index] != arr[index-1]:
            answer.append(arr[index-1])
        if index == len(arr)-1:
            if not answer:
                answer.append(arr[index])
            if answer[len(answer)-1] != arr[index]:
                answer.append(arr[index])

    return answer

# def solution(arr):
#     answer = []
#     for index in range(len(arr)):
#         if index >= 1 and arr[index] != arr[index-1]:
#             answer.append(arr[index-1])
#         if index == len(arr)-1:
#             if answer and answer[len(answer)-1] != arr[index]:
#                 answer.append(arr[index])
#             if not answer:
#                 answer.append(arr[index])
#     return answer

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(no_continuous([1,1,1,1,1,3,3,3,32,2]))
print(solution([1,1]))
