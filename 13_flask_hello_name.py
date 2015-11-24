from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    user_name = request.args.get('name', 'Anonymous')
    return render_template('13_flask_hello_template.html', user_name=user_name)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
