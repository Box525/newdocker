from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return u"今天是11月10日，这是一个Nginx+Apache 负载均衡的运维环境的部署"


@app.route('/login/')
def login():

    """数据库的操作"""
    return u"登录成功!!!"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6001)

