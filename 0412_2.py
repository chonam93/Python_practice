def solution(arr):
    answer = []
    for num in range(len(arr)):
        if num >= 1 and arr[num] != arr[num-1]:
            answer.append(arr[num-1])
        if num == len(arr)-1 and answer and answer[len(answer)-1] != arr[num]:
            answer.append(arr[num])
    return answer

