from flask import Flask, request, render_template, g, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'cafes.db'


# Function to get a database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Route to display the list of cafes
@app.route('/', methods=['GET'])
def get_cafes():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cafe")
    cafes = cur.fetchall()
    cur.close()
    return render_template('cafes.html', cafes=cafes)


# Route to add a new cafe
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        conn = get_db()
        cur = conn.cursor()

        # Get cafe data from the form
        name = request.form['name']
        map_url = request.form['map_url']
        img_url = request.form['img_url']
        location = request.form['location']
        has_sockets = request.form.get('has_sockets', 0)
        has_toilet = request.form.get('has_toilet', 0)
        has_wifi = request.form.get('has_wifi', 0)
        can_take_calls = request.form.get('can_take_calls', 0)
        seats = request.form['seats']
        coffee_price = request.form['coffee_price']

        # Insert new cafe into the database
        cur.execute(
            "INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price))
        conn.commit()
        cur.close()
        return redirect('/')

    return render_template('add_cafe.html')


# Route to remove a cafe
@app.route('/remove/<int:cafe_id>', methods=['GET'])
def remove_cafe(cafe_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM cafe WHERE id = ?", (cafe_id,))
    conn.commit()
    cur.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
