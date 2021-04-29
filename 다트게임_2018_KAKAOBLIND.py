#다트 게임은 총 3번의 기회로 구성된다.
#각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.

#점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 
##각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.

#옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 
##아차상(#) 당첨 시 해당 점수는 마이너스된다.

#스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
#스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
#스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
#Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
#스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
#0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

##############################################
#점수는 0에서 10 사이의 정수이다.
#보너스는 S, D, T 중 하나이다.
#옵선은 *이나 # 중 하나이며, 없을 수도 있다.
##############################################


# 예제  dartResult	    answer	설명
# 1	    1S2D*3T	        37	    1^1 * 2 + 2^2 * 2 + 3^3
# 2	    1D2S#10S	    9	    1^2 + 2^1 * (-1) + 10^1
# 3	    1D2S0T	        3	    1^2 + 2^1 + 0^3
# 4	    1S*2T*3S	    23	    1^1 * 2 * 2 + 2^3 * 2 + 3^1
# 5	    1D#2S*3S	    5	    1^2 * (-1) * 2 + 2^1 * 2 + 3^1
# 6	    1T2D3D#	        -4	    1^3 + 2^2 + 3^2 * (-1)
# 7	    1D2S3T*	        59	    1^2 + 2^1 * 2 + 3^3 * 2


# def solution(dartResult):
#     answer = 0
#     answer_list = []
#     len_dart = len(dartResult)
#     i = 0
#     while i < len_dart:
#         for text in dartResult:
#             if text ==  'S':
#                 slice_dart = dartResult[:dartResult.index(text)]
#                 answer_list.append(int(slice_dart))
#                 dartResult = dartResult[dartResult.index(text)+1:]
#             elif text == 'D':
#                 slice_dart = dartResult[:dartResult.index(text)]
#                 answer_list.append(int(slice_dart)**2)
#                 dartResult = dartResult[dartResult.index(text)+1:]
#             elif text == 'T':
#                 slice_dart = dartResult[:dartResult.index(text)]
#                 answer_list.append(int(slice_dart)**3)
#                 dartResult = dartResult[dartResult.index(text)+1:]
#             elif text == '*':
#                 dartResult = dartResult[dartResult.index(text)+1:]
#                 if len(answer_list) == 1:
#                     answer_list[0] = answer_list[0]*2
#                 elif len(answer_list) == 2:
#                     answer_list[0] = answer_list[0]*2
#                     answer_list[1] = answer_list[1]*2
#                 elif len(answer_list) == 3:
#                     answer_list[1] = answer_list[1]*2
#                     answer_list[2] = answer_list[2]*2
#             elif text == '#':
#                 dartResult = dartResult[dartResult.index(text)+1:]
#                 if len(answer_list) == 1:
#                     answer_list[0] = answer_list[0]*-1
#                 elif len(answer_list) == 2:

#                     answer_list[1] = answer_list[1]*-1
#                 elif len(answer_list) == 3:

#                     answer_list[2] = answer_list[2]*-1
#             i += 1
#     answer = sum(answer_list)
                

                

            
#     return answer

import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    a = p.findall(dartResult)
    print(a)



print(solution('1D2S#10S'))



# ## re / compile 사용
# import re

# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer



# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k') ##문자열을 리스트로 만들 때, 두글자인채로 변환하고 싶을 때 먼저 치환해주고,
#     point = ['10' if i == 'k' else i for i in dartResult] ##list comprehension의 IF문으로 다시 바꿔주면 된다. HONEY TIP
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)


