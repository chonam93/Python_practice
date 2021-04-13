def solution(board, moves):
    answer = 0
    answer_list = []
    for pick_num in moves: #일단 뽑아야하니까 패스
        for select in range(0, len(board)): #
            if board[select][pick_num-1] != 0:
                answer_number = board[select][pick_num-1]
                answer_list.append(answer_number)
                board[select][pick_num-1] = 0
                break
        if len(answer_list) >= 2 and answer_list[-1] == answer_list[-2]:
            answer_list = answer_list[:-2]
            answer += 2
    return answer