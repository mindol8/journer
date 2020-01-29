from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

"""
    signin page
"""
@app.route('/signin',methods=['GET'])
def sign_in():
    return render_template('signin.html')

"""
    login information
"""
@app.route('/main',methods = ["POST"])
def login():
    id = request.form['id']
    pw = request.form['pw']
   # print(id)
   # print(pw)
    """
        로그인 끝나면 다시 메인 화면으로 이동
    """
    return render_template('main.html')

if __name__ == '__main__':
    app.run()
