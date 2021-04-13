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
        i = len(answer_list)
        if i >= 2 and answer_list[i-1] == answer_list[i-2]:
            answer += 2
            answer_list.remove(answer_list[i-1])
            answer_list.remove(answer_list[i-2])
            break
                
    print(answer_list)
    print(answer)
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])