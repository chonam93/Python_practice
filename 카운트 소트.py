import random

length = int(input('리스트의 길이를 입력하세요: '))
listA = []
cntA = 0
while cntA < length: # 입력한 길이만큼 랜덤값을 가진 리스트생성 (길이가 7인 리스트여도 최대값이 5일 수도 있음)
    data = random.randint(1, length)
    listA.append(data)
    cntA += 1
print(listA, end=' ')

maxA = max(listA) # 최대 최소값 변수 지정
minA = min(listA)

listC = []
cntC = 0 
while cntC < maxA: # 0으로 최대값만큼 채운 리스트 생성
    listC.append(0)
    cntC += 1

print(listC)

for i in range(1, maxA+1): # listA의 랜덤값을 0부터 최대값까지 찾아서 카운트 / 카운트수를 값과 동일한 인덱스자리에 채움
    search = listA.count(i)
    listC[i-1] = search

print(listA, end=' ')
print(listC)
print()
print('카운트 리스트 완성')
listB = []
while listC.count(0) < len(listC): # listC가 0으로 가득차면 while문 탈출
    for i in listC: 
        if i != 0: #listC의 값들 중 0이 아니면 
            for j in range(i): # 해당 값의 크기만큼 listB에 추가
                index_value = listC.index(i)
                listB.append(index_value+1)
            listC[index_value] = 0
            print(listA, listC, listB)
