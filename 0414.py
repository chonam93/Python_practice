def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    str_n = list(n)
    print(str_n)
    return answer

n = 123
a = 0
str_n = list(str(n))
for i in str_n:
    a += int(i)
print(str_n)
print(a)