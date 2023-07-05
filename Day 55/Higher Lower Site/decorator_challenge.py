def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


from flask import Flask
app = Flask(__name__)


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug='on', host='0.0.0.0', port=5000)
