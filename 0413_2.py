# 함수로 계속돌린다
# 어떻게?
DEF CONNECT()
DEF CLOSE()

def connect():
    connect = pymysql.connect(host = 'localhost', user= 'miniProject', password = 'project', db = 'project', charset = 'utf8')
    curs = connect.cursor(pymysql.cursors.DictCursor)
    return curs

def close_conn():
    connect.close()

print('환영합니다. SQL에 접속하였습니다.')
print('ID와 PW를 입력해주세요.')
ID = input('ID >> ')
PW = input('PW >> ')

if ID == 'root' and PW == 


while True:
    try:
        sql = 'select cus_id, passwd from customer where cus_id = {} and passwd = {}'.format(id, pw)
        curs.execute(sql)
        result = curs.fetchall()
        
    except:
        print('잘못입력하셨습니다.')
    else: 
        

# 환영합니다. SQL에 접속하였습니다.
# ID와 PW를 입력해주세요
# IF ID == ROOT AND PW == ROOT:
ㄱ
# ELSE:
#     'ID'님 환영합니다.
#     사용하실 서비스를 선택하세요.
      WHILE INPUT != QUIT
#     DEF 고객옵션()
#     PRINT 선택가능한옵션들 출력
#     INPUT 옵션선택
#     IF INPUT == ?
#         DEF ??
#     IF INPUT == ?
#         DEF ??
#     IF INPUT == ?
#         DEF ??
#     IF INPUT == ?
#         DEF ??
      IF INPUT == QUIT:
          BREAK



뭘하시겠ㅅ브니가?
로그인 1 회원가입 2

if input 1
f로그인으로 고


if input 2
회원가입 고

i 아이디 