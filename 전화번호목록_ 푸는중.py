
# # 1차 시도 정확성 통과 / 효율성 3번, 4번 실패
# def solution(phone_book):
#     answer = True
#     check = 0
#     phone_book.sort()
#     for i in phone_book:
#         for j in phone_book:
#             if i != j and i in j[0:len(i)]:
#                 answer = False
#                 check = 1
#                 break
#         if check == 1:
#             break
#     return answer

# # 2차 시도 정확성 통과 / 효율성 3번, 4번 실패
# # 반복문에서 검사를 했으면 다음 꺼 부터 하도록 설정
# def solution(phone_book):
#     answer = True
#     check = 0
#     phone_book.sort()
#     for i in phone_book:
#         for j in phone_book[phone_book.index(i)+1:]:
#             if i in j[0:len(i)]:
#                 answer = False
#                 check = 1
#                 break
#         if check == 1:
#             break
#     return answer
print(solution(["12", "123", "1235", "567", "88"]))
