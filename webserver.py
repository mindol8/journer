from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/signup',methods=['POST'])
def sign_up():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
