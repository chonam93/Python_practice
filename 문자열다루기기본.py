import string

def solution(s):
    alpha = string.ascii_letters
    if len(s) == 4 or len(s) == 6:
        cnt = 0
        for stri in s:
            if stri in alpha:
                cnt+=1
        if cnt == 0:
            return True
        else:
            return False
    return False

### try / except 사용법
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 


print(solution('123'))
