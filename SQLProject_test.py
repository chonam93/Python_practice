import pymysql
# u = input('계정명: ')
# p = input('패스워드: ')
connect = pymysql.connect(host = 'localhost', user= 'miniProject', password = 'project', db = 'project', charset = 'utf8')
#host : 컴퓨터에 설치된 DB에 접속하기 때문에 localhost
#유저아이디 / 패스워드 / 사용할 DB / 한글이 안깨지도록 charset 설정
curs = connect.cursor(pymysql.cursors.DictCursor)

def print_cus_result(result): #customer select구문 함수
    print("\n-----------------------------------------------------------")
    cnames = result['']
    for c in cnames:
        print(c.center(11,' '), end='\t')
    print("\n-----------------------------------------------------------")
    for r in result:
        for c in cnames:
            print(str(r[c]).center(11, ' '), end='\t')
        print()
    print("\n-----------------------------------------------------------")

def print_buy_result(result): #buy select구문 함수
    print("\n-------------------------------------------------------------------")
    bnames = ['BUY_NO', 'CUS_ID', 'ITEM_NO', 'BUY_DATE']
    for c in bnames:
        print(c.center(11,' '), end='\t')
    print("\n-------------------------------------------------------------------")
    for r in result:
        for c in bnames:
            print(str(r[c]).center(11, ' '), end='\t')
        print()
    print("\n-------------------------------------------------------------------")

def print_item_result(result): #item select구문 함수
    print("\n-------------------------------------------------------------------")
    inames = ['ITEM_NO', 'ITEM_NAME', 'PRICE', 'CATEGORY']
    for c in inames:
        print(c.center(11,' '), end='\t')
    print("\n-------------------------------------------------------------------")
    for r in result:
        for c in inames:
            print(str(r[c]).center(11, ' '), end='\t')
        print()
    print("\n-------------------------------------------------------------------")

cmd = 'na'
while cmd != 'q': #검색 옵션 출력
    print("")
    print("***사용 가능한 명령어 리스트***")
    print("a : 모든 데이터 조회(all)")
    print("f : 조건에 맞는 데이터만 조회(find)")
    print("i : 데이터 추가(insert)")
    print("d : 데이터 삭제(delete)")
    print("r : 데이터 변경(revise)")
    print("q : 저장하고 나가기(quit)")
    print()
    cmd = input('command(명령어 입력): ')
    print()

    # def all_search(cmd):
    if cmd == 'a': # 전체 테이블 출력
        print('어떤 테이블을 출력하시겠습니까? (고객리스트, 구매리스트, 제품리스트)')
        what = input('> ')
        if what == '고객리스트':
            sql = 'select * from customer'
            curs.execute(sql)
            result = curs.fetchall()
            print_cus_result(result)
            # for r in result:
            #     print(r)
        elif what == '구매리스트':
            sql = 'select * from buy'
            curs.execute(sql)
            result = curs.fetchall()
            print_buy_result(result)
        elif what == '제품리스트':
            sql = 'select * from item'
            curs.execute(sql)
            result = curs.fetchall()
            print_item_result(result)

    elif cmd == 'f': #조건에 맞는 데이터만 조회
        print('어떤 테이블을 검색하시겠습니까? (고객리스트, 구매리스트, 제품리스트)')
        table = input('> ')
        
        if table == '고객리스트': #고객리스트 검색
            print('무엇을 기준으로 검색하시겠습니까? (아이디, 성별, 생일)')
            what = input('> ')
            if what == '아이디':
                print('검색할 아이디를 입력하세요')
                id = input('> ')
                sql = 'select * from customer where cus_id = \'{}\''.format(id)
                curs.execute(sql)
                result = curs.fetchall()
                print_cus_result(result)
            elif what == '성별':
                print('검색하실 성별을 입력하세요. (m/f)')
                gender = input('> ')
                sql = 'select * from customer where gender = \'{}\''.format(gender)
                curs.execute(sql)
                result = curs.fetchall()
                print_cus_result(result)
            elif what == '생일':
                print('숫자만 입력해주세요')
                input_date1 = int(input('검색 시작연도'))
                input_date2 = int(input('검색 끝 연도'))
                sql = 'select * from customer where left(birth, 4) between  \'{}\' and \'{}\''.format(input_date1, input_date2)
                curs.execute(sql)
                result = curs.fetchall()
                print_cus_result(result)
            else:
                print('다시 입력해주세요') 
        elif table == '구매리스트':
            print('무엇을 기준으로 검색하시겠습니까? (구매 번호, 아이디, 제품 번호, 구매 날짜, 사용자 검색)')
            what = input('> ')
            if what == '사용자 검색':
                sql = input('> ')
                curs.execute(sql)
                result = curs.fetchall()
                print_buy_result(result)
            # elif what == '구매 번호':
            #     sql = 'select * from '
        elif table == '제품리스트':
            print('무엇을 기준으로 검색하시겠습니까? (가격, 제품번호)')
            what = input('> ')
            if what == '가격': #f, 제품리스트
                print('제품들이 가격 순으로 정렬됩니다.')
                sql = 'select * from item order by price desc'
                curs.execute(sql)
                result = curs.fetchall()
                print_item_result(result)
            elif what == '제품 번호':
                print('검색할 제품 번호을 입력하세요. 해당 제품을 구매한 사람들이 출력됩니다.')
                id = input('> ')
                sql = 'select * from customer c'
            
    elif cmd == 'i':
        print('i')
    elif cmd == 'd':
        print('d')
    elif cmd == 'r':
        print('r')
    elif cmd == 'q':
        print('저장이 완료되었습니다. 프로그램을 종료합니다.')
    else:
        print('잘못된 명령어가 입력되었습니다. 다시 입력해주세요')

connect.close()
