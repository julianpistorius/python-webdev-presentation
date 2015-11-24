from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/bye')
def bye():
    return '<h1>See you later!</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=8888)
