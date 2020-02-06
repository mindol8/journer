from flask import Flask, render_template, request
#from DAL import *

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


"""signin page"""


@app.route('/signin', methods=['GET'])
def sign_in():
    return render_template('signin.html')


"""sign up"""


@app.route('/signup', methods=["GET"])
def sign_up():
    return render_template('signup.html')


"""find id/pw"""


@app.route('/find', methods=['GET'])
def find():
    return render_template('find.html')


"""login information"""


@app.route('/main', methods = ["POST"])
def login():
    email = request.form['id']
    pw = request.form['pw']

    login_query  = "SELECT COUNT(*) FROM ACCOUNT "
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
            else:
                print('이메일 또는 비밀번호를 다시 확인해 주십시오.')

    except:
        print('이메일 또는 비밀번호를 다시 확인해 주십시오.')

    else:
        cursor.close()
        connection.commit()
        connection.close()





    return render_template('main.html')


if __name__ == '__main__':
    app.run()
