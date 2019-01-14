from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return u"今天是11月7日!!马上到双11！！！！"


@app.route('/home/<name>/')
def home(name):
    return u"<h1>Welcome %s !!!!</h1>" % name


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6000)