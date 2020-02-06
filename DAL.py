import cx_Oracle

def db_connection(account = 'journer', password = 'traveler', ip = '127.0.0.1:1521', sid = 'orcl'):
    '''
    :param account: Database account
    :param password: Database password
    :param ip: Database server ip address (format - ip:port)
    :param sid: Database system identifier
    :return: Connection , Cursor of Connected Database
    '''

    con = cx_Oracle.connect(f'{account}/{password}@{ip}/{sid}')
    cur = con.cursor()

    return con , cur



#default 값으로 연결
#connection, cursor = db_connection()


try:
    # 인자 지정 연결
    connection, cursor = db_connection('journer','traveler')
except:
    print('DB Connection failed')
else:
    # 사용후 close
    cursor.close()
    connection.commit()
    connection.close()


#아래와 같은 방법으로도 DB 사용 가능
# sql = "INSERT INTO TEST_ACCOUNT VALUES(:1,:2)"
# data = ('TEST003','4123')
#
# cursor.execute(sql,data)