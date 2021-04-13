import random

# 소지금 입력
# def interchange():
    
#     while True:
#         try:
#             deposit = int(input('소지금을 입력하세요: '))
#             break
#         except:
#             print('숫자만 입력하셔야 합니다.')
#     print()
#     return deposit

# 6개 숫자를 입력하세요
def userchoice():
    while True:
        ok = True
        guess = []
        guess_number = [int(x) for x in input('숫자를 입력하세요: ').split()]
        for i in guess_number:
            if i > 45 or i < 0:
                print('1부터 45까지의 정수를 입력하세요')
                print()
                ok = False
            if i not in guess:
                guess.append(i)
        if len(guess_number) != 6:
            print('6개의 숫자를 입력하셔야 합니다.')
            print()
            ok = False
        if len(guess) != 6:
            print('중복된 숫자가 있습니다. 천천히 입력하세요')
            print()
            ok = False

        if ok == True:
            break

    print()
    print('선택하신 번호는 {}입니다'.format(guess))
    print()

    return guess


# 당첨번호 생성
def winning_number():
    answer = []
    
    cnt = 0
    while cnt < 7:
        number = random.randint(1, 45)
        if number not in answer:
            answer.append(number)
            cnt += 1
    print('이번주 복권 번호는', answer,'입니다.')

    return answer


def check(guess, answer):
    cnt = 0
    
    for i in guess:
        if i in answer:
            cnt += 1
    print('겹치는 숫자는 {}개입니다'.format(cnt))
    return cnt
    
def prize(cnt):
    prize = 0
    if cnt < 3:
        prize += 0
    if cnt == 4:
        prize += 5000
        print('3등 당첨. 상금은 5,000원입니다')
    if cnt == 5:
        prize += 10000
        print('2등 당첨. 상금은 10,000원입니다')
    if cnt == 6:
        prize += 50000
        print('1등 당첨. 상금은 50,000원입니다')
    return prize
#게임 시작
print('복권 번호를 맞춰보세요!')
# print('복권 한장에 5,000원 입니다')
print()

# deposit = interchange()
total_prize = 0
while True:
    guess = userchoice()
#    deposit -= 5000
    answer = winning_number()
    cnt = check(guess, answer)
    total_prize += prize(cnt)

    retry = input('다시하시겠습니까? y / n ')
    if retry == 'n':
        print('총 상금은 {}입니다.'.format(total_prize))
        break
    else:
        continue