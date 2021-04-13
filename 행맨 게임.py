import random

list = ['apple', 'banana', 'pineapple']

answer = random.choice(list)
print('정답: ' + answer)

print()
guess_list = ""  # 입력받을 값 저장소

while True:
    succeed = True
    for w in answer:
        if w in guess_list:
            print(w, end=" ")
        else:
            print('_', end=" ")
            succeed = False
    print()
    if succeed:
        print('success')
        break

    guess = input('알파벳 입력하세요: ')
    if guess not in guess_list:
        guess_list += guess
    if guess in answer:
        print('correct')

    else:
        print('wrong')

    print()

