from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

todos = []

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete():
    todo = request.form.get('todo')
    todos.remove(todo)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
