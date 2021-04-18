def solution(phone_number):
    answer = ''
    answer += '*'*(len(phone_number)-4)
    answer += phone_number[-4:]
    return answer
print(solution("44444"))