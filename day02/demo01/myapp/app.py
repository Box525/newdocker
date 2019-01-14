from flask import Flask

app = Flask(__name__)

# TODO:主页路由
@app.route('/')
def home_page():
    return u'今天是11月6日'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6000)

