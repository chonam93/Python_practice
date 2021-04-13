import random

def com():
    choice = ['가위', '바위', '보']
    select = random.choice(choice)
    return select

def user():
    what = input('무엇을 내겠습니까? ')
    return what

def win(user, com):
    answer = True

    if user == com:
        print('무승부, 함수를 다시 실행하세요.\n')
    if user == '가위' and com == '보':
        print('승리하셨습니다. 컴퓨터는 {}, 당신은 {}\n'.format(com, user))
        answer = True
        return answer
    elif user == '바위' and com == '가위':
        print('승리하셨습니다. 컴퓨터는 {}, 당신은 {}\n'.format(com, user))
        answer = True
        return answer
    elif user == '보' and com == '바위':
        print('승리하셨습니다. 컴퓨터는 {}, 당신은 {}\n'.format(com, user))
        answer = True
        return answer
    else:
        print('패배, 함수를 다시 실행하세요. 컴퓨터는 {}였습니다.\n'.format(com))
        answer = False

    return answer

print('가위바위보 게임합시다')
while True:
    what = user()
    select = com()
    answer = win(what, select)
    if answer == True:
        break