from flask import Flask
import platform, pymysql

app = Flask(__name__)


@app.route('/')
def index():

    return u"欢迎登陆首页!!!!!%s" % platform.python_version()


@app.route('/user/')
def create_user_table():
    connection = pymysql.connect(host='192.168.3.243', port=3308, user='root', passwd='123456', db='py112db',
                                 charset='utf8')
    '''2.获取游标'''
    cursor = connection.cursor()
    '''3.执行SQL语句'''
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS ebuser")

    # 使用预处理语句创建表
    sql_string = """CREATE TABLE ebuser (
                     FIRST_NAME  CHAR(20) NOT NULL,
                     LAST_NAME  CHAR(20),
                     AGE INT,  
                     SEX CHAR(1),
                     INCOME FLOAT )"""

    cursor.execute(sql_string)

    cursor.close()
    connection.close()

    return u"创建成功!!!!!"




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
