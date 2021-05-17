import datetime #datetime 함수이용
def solution(a, b):

    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    day = days[datetime.date(2016,a,b).weekday()]
    return day

print(solution(5,24))

def solution(a, b): #일반 풀이
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    day = days[(sum(months[:a-1])+b-4)%7]
    return day

print(solution(5,24))
