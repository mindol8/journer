'''
삭제할 주석입니다.
DB 연결을 임시로 모듈화한 코드입니다.
DB서버 계정 테이블 모두 임시로 만들어졌으며 추후 수정될 예정입니다.

DB : ORACLE
DB_SERVER : 127.0.0.1 localhost
DB_ACCOUNT : journer
DB_PASSWORD : traveler

ACCOUNT_TABLE_NAME : TEST_ACCOUNT
ID VARCHAR2(20)
PASSWORD VARCHAR2(20)
'''

import cx_Oracle

def db_connection(account = 'journer', password = 'traveler', ip = '127.0.0.1:1521', sid = 'orcl'):

    con = cx_Oracle.connect(f'{account}/{password}@{ip}/{sid}')
    cur = con.cursor()

    return con , cur

#default 값으로 연결
#a , b = db_connection()

#인자 지정 연결
connection, cursor = db_connection('journer','traveler')


cursor.execute('SELECT * FROM TEST_ACCOUNT')


for result in cursor:
    print(result)

