from flask import Flask

from Common.Result import Result

app = Flask(__name__)


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
    return Result(data='Hello Python', msg='Fail Demo').fail()


if __name__ == '__main__':
    app.run()
