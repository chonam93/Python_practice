#가위바위보
#사용자 입력 + 컴퓨터 결정을 함수로 설정
import random
print("가위바위보 게임 시작하겠습니다.")
print("컴퓨터의 수는 함수 실행 시 계속 변합니다.\n")
def rockpaperscissor(user):
    answer = False
    choice = ['가위', '바위', '보']
    com = random.choice(choice)

    if user == com:
        print('무승부, 함수를 다시 실행하세요.\n')
    elif user == '가위' and com == '보':
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
    elif user not in choice:
        print('잘못된 입력입니다. 다시 입력하세요\n')
    else:
        print('패배, 함수를 다시 실행하세요. 컴퓨터는 {}였습니다.\n'.format(com))

    return answer

while True:
    if rockpaperscissor(input('user: ')) == True:
        break
    
    