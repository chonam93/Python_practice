import pymysql
# u = input('계정명: ')
# p = input('패스워드: ')
def connect():
    connect = pymysql.connect(host = 'localhost', user= 'miniProject', password = 'project', db = 'project', charset = 'utf8')
    curs = connect.cursor(pymysql.cursors.DictCursor)
    result curs

def print_cus_result(result): #customer select구문 함수
    print("\n-----------------------------------------------------------")
    cnames = ['CUS_ID', 'PASSWD', 'GENDER','BIRTH']
    for c in cnames:
        print(c.center(11,' '), end='\t')
    print("\n-----------------------------------------------------------")
    for r in result:
        for c in cnames:
            if c == 'PASSWD': #비밀번호는 ***표시처리
                trans = list(r[c])
                for i in range(len(trans)):
                    trans[i] = '*'
                r[c] = ''.join(trans) 
                print(str(r[c]).center(11, ' '), end='\t')
            else:
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

def print_cntitem_result(result): #cnt item select구문 함수
    print("\n-------------------------------------------------------------------")
    inames = ['item_no', 'item_name', 'count(buy_no)']
    for c in inames:
        print(c.center(11,' '), end='\t')
    print("\n-------------------------------------------------------------------")
    for r in result:
        for c in inames:
            print(str(r[c]).center(11, ' '), end='\t')
        print()
    print("\n-------------------------------------------------------------------")

def print_cntbuy_result(result): #cnt buy select구문 함수
    print("\n-------------------------------------------------------------------")
    inames = ['cus_id', 'count(buy_no)']
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
    print("r : 데이터 정보 변경(revise)")
    print("b : 제품 구매(buy)")
    print("q : 저장하고 나가기(quit)")
    print()
    cmd = input('command(명령어 입력): ')
    print()
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
            if what == '아이디':  # 고객 정보 전부
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
            print('무엇을 기준으로 검색하시겠습니까? (아이디, 구매 횟수)')
            what = input('> ')
            if what == '아이디' : # 사용자별 구매내역
                print('검색할 아이디를 입력하세요')
                id=input('> ')
                sql= 'select * from buy where cus_id= \'{}\''.format(id)
                curs.execute(sql)
                result = curs.fetchall()
                print_buy_result(result)
            
            elif what == '구매 횟수' : # 사용자별 구매횟수
                print('검색할 아이디를 입력하세요')
                id=input('> ')
                sql='select cus_id, count(buy_no) from buy where cus_id = \'{}\''.format(id)
                curs.execute(sql)
                result = curs.fetchall()
                print_cntbuy_result(result)    
            
        elif table == '제품리스트':  
            print('무엇을 기준으로 검색하시겠습니까?(판매량, 제품명, 가격, 카테고리)')
            what = input('> ')
            if what == '판매량': # 제품별 판매횟수 
                print('제품 번호를 입력하세요')
                no=input('>' )
                sql='select i.item_no, i.item_name, count(buy_no) from item i left join buy b using(item_no) where item_no=\'{}\''.format(no)
                curs.execute(sql)
                result = curs.fetchall()
                print_cntitem_result(result)

            elif what == '카테고리': # 카테고리별 제품
                cate= input('카테고리 명을 입력해주세요: ')
                sql = 'select * from item where category =  \'{}\' '.format(cate)
                curs.execute(sql)
                result = curs.fetchall()
                print_item_result(result)

            elif what == '제품명': # 제품정보
                cate = input('ipad, laptop, t_shirt, jeans, coffee, pizza, ring: ')
                sql = 'select * from item where category =  \'{}\''.format(cate)
                curs.execute(sql)
                result = curs.fetchall()
                print_item_result(result)
            
            elif what == '가격': # 가격순으로 정렬
                print('제품들이 가격 순으로 정렬됩니다.')
                updown = input('가격 높은 순으로 보기 (u) // 낮은 순으로 보기 (d) >>> ')
                if updown == 'u':
                    sql = 'select * from item order by price desc'
                    curs.execute(sql)
                    result = curs.fetchall()
                    print_item_result(result)
                if updown == 'd':
                    sql = 'select * from item order by price'
                    curs.execute(sql)
                    result = curs.fetchall()
                    print_item_result(result)

    elif cmd == 'b': # 구매 데이터 입력
        print('아이디를 입력하세요.')
        id=input('> ')
        sql = 'select * from item'
        curs.execute(sql)
        result = curs.fetchall()
        print_item_result(result)
        print('어떤 제품을 구매하시겠습니까?')
        no=input('제품 번호를 입력해주세요. > ')
        sql = 'insert buy(cus_id,item_no) values(\'{}\',\'{}\')'.format(id,no)
        curs.execute(sql)
        connect.commit()
        print('구매완료 되었습니다.')
    
    elif cmd == 'i': # 데이터 입력
        print('어떤 데이터를 입력하시겠습니까? (고객, 제품)')
        what=input('> ')
        while True: # !!! 제품을 입력해도 순서상으로 while문으로 들어가게 된다
            if what == '고객':
                print('고객 정보를 입력해주세요.')
                try:
                    id = input('아이디를 입력해주세요. > ')
                    pw = input('비밀번호를 입력해주세요. > ')
                    gen = input('성별을 입력해주세요. (F/M)> ')
                    bir = input('생년월일을 입력해주세요.(YYYY-MM-DD) > ')
                    sql = 'insert into customer values(%s, %s, %s, %s)'
                    curs.execute(sql,(id,pw,gen,bir))
                    connect.commit()
                    print('가입이 완료 되었습니다.')
                    break
                except:
                    print('이미 가입된 아이디입니다.')
            else: # !!! '고객'이 아니라면 탈출할 수 있도록
                break
                

        if what =='제품':
            print('제품 정보를 입력해주세요.')
            name = input('제품명을 입력해주세요. > ')
            pri= int(input('가격을 입력해주세요. > '))
            cat= input('카테고리를 입력해주세요. > ')
            sql = 'insert item(item_name, price, category) values(%s,%s,%s) '
            curs.execute(sql, (name, pri, cat))
            connect.commit()
            print('입력이 완료 되었습니다.')

    elif cmd == 'd': # 데이터 삭제하기
        print('어떤 데이터를 삭제하시겠습니까? (고객, 제품)')
        what=input('> ')
        if what == '고객':
            print('※ 고객정보 삭제는 ID로만 가능합니다.')
            id=input('> ')
            sql='delete from customer where cus_id = %s'
            curs.execute(sql, (id))
            connect.commit()
            print('탈퇴가 완료 되었습니다.')

        elif what=='제품': # !!! 삭제할 제품 리스트 보여주기
            sql = 'select * from item'
            curs.execute(sql)
            result = curs.fetchall()
            print_item_result(result)
            print('※ 제품정보 삭제는 제품번호로만 가능합니다.\n  삭제하실 제품을 선택해주세요.')
            no=input('> ')
            sql='delete from item where item_no = %s'
            curs.execute(sql, (no))
            connect.commit()
            print('제품 삭제가 완료 되었습니다.')

    elif cmd == 'r': # 데이터 변경하기
        print('어떤 데이터를 변경하시겠습니까? (고객, 제품)')
        what=input('> ')
        if what == '고객':
            print('※ 고객정보는 비밀번호만 변경 가능합니다.')
            id=input('아이디를 입력해주세요 >> ')
            pw=input('변경할 비밀번호를 입력해주세요 >> ')
            sql='update customer set passwd = %s where cus_id = %s'
            curs.execute(sql, (pw, id))
            connect.commit()
            print('비밀번호가 변경 되었습니다.')

        elif what=='제품':
            print('※ 제품 정보는 가격만 변경 가능합니다.')
            no=input('제품번호를 입력해주세요')
            pri =input('변경할 가격을 입력해주세요. > ')
            sql='update item set price = %s where Item_no = %s'
            curs.execute(sql, (pri, no))
            connect.commit()
            print('가격이 변경 되었습니다.')

    elif cmd == 'q':
        print('저장이 완료되었습니다. 프로그램을 종료합니다.')

    else:
        print('잘못된 명령어가 입력되었습니다. 다시 입력해주세요')

connect.close()

