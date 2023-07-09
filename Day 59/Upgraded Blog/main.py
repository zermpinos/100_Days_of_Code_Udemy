from flask import Flask, render_template
import requests
from datetime import datetime

current_year = datetime.now().year
posts = requests.get("https://api.npoint.io/321041d25aaaa6c91040").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts, current_year=current_year)

@app.route("/about")
def about():
    return render_template("about.html", current_year=current_year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=current_year)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
