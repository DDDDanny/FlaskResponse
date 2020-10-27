from flask import Flask, abort

from Common import bp
from Common.Result import Result
from Common.Error import error_response, handle_404_error, handle_500_error

app = Flask(__name__)

# 注册异常处理方法
app.register_error_handler(404, handle_404_error)
app.register_error_handler(500, handle_500_error)


@app.route('/')
def hello_world():
    return 'Hello World!'


# Success Demo
@app.route('/success')
def success():
    return Result(data='Hello Flask', msg='Success Demo').success()


# Fail Demo
@app.route('/fail')
def fail():
    abort(500)
    return Result(data='Hello Python', msg='Fail Demo').fail()


if __name__ == '__main__':
    app.run()
