from flask import Flask, render_template, request, redirect,session,escape, url_for
from datetime import timedelta
from DAL import *

app = Flask(__name__)

###세션키값(임의로 설정함)###
app.secret_key = 'session_key_set'

session_data = [1]

@app.before_request
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=24)
    ###세션 수명 24시간###


@app.route('/')
def main_page():
    global session_data

    if 'name' in session:
        session_data[0] = '%s' % escape(session['name'])
    else:
        session.pop('name', None)
        session_data[0] = 'temp'
    return render_template('index.html', name = session_data)


"""signin page"""
@app.route('/signin', methods=['GET'])
def sign_in():
    return render_template('signin.html')


"""sign up page"""
@app.route('/signup', methods=["GET"])
def sign_up():
    return render_template('signup.html')

@app.route('/signup',methods=["POST"])
def make_account():
    email = request.form['email']
    pwd = request.form['pwd1']
    name = request.form['fullname']
    sex = request.form['sex']
    birthday = request.form['birth']
    tel_num = request.form['tel']

    sign_up_query = 'INSERT INTO ACCOUNT VALUES ('
    sign_up_query += f"'{email}',"
    sign_up_query += f"'{pwd}',"
    sign_up_query += f"'{name}',"
    sign_up_query += f"'{sex}',"
    sign_up_query += f"'{birthday}',"
    sign_up_query += "'photo_path',"
    sign_up_query += f"'{tel_num}',"
    sign_up_query += "'C')"

    try:
        connection, cursor = db_connection('journer', 'traveler')
        print('DB Connnection complete')
    except:
        print('DB Connection failed')

    try:
        cursor.execute(sign_up_query)
        # 화면상 출력 필요
        print('회원가입에 성공했습니다.')
    except cx_Oracle.DatabaseError as e:
        # ORA-00001: 무결성 제약 조건(JOURNER.SYS_C009995)에 위배됩니다
        # 여기다가 이메일 중복 체크
        print(e)
        return "error_email"
    else:
        cursor.close()
        connection.commit()
        connection.close()

    return "success_signup"
    #return render_template('signin.html')


"""find id/pw"""
@app.route('/find', methods=['GET'])
def find():
    return render_template('find.html')


"""login information"""
@app.route('/login', methods=["POST"])
def login():
    global session_data
    email = request.form['id']
    pw = request.form['pw']

    login_query = "SELECT COUNT(*) FROM ACCOUNT "
    login_query += "WHERE 1 = 1 "
    login_query += f"AND EMAIL = '{email}' "
    login_query += f"AND PASSWORD = '{pw}'"

    try:
        connection, cursor = db_connection('journer', 'traveler')
        print('DB Connnection complete')
    except:
        print('DB Connection failed')

    try:
        cursor.execute(login_query)

        # 1개만 받아오는 법을 모르겠습니다 수정하겠습니다.
        for row in cursor:
            if row[0] == 1:
                print('login 성공!')
                # 임시로 로그인 성공시 index 페이지로 보내줍니다. 추후 수정이 필요합니다.
                session['name'] = '이름이당'  ###디비에서 이름 가져와서 넣어야함###
                session['email'] = email
                session['pw'] = pw
                print('%s' % escape(session['name']))
                if 'name' in session:
                    session_data[0] = '%s' % escape(session['name'])

                return redirect('/')
            else:
                print('이메일 또는 비밀번호를 다시 확인해 주십시오.')
                # 로그인 실패시 signin 페이지를 다시 렌더링 해주고, fail 파라미터를 보내줘서 문구를 띄워줍니다.
                return render_template('signin.html', fail=True)
    except:
        print('이메일 또는 비밀번호를 다시 확인해 주십시오.')
    else:
        cursor.close()
        connection.commit()
        connection.close()




"""review board"""
@app.route('/review', methods=['GET'])
def review_board():
    return render_template('review.html')


if __name__ == '__main__':
    app.run()
