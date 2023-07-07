from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_blogs = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_blogs)

@app.route('/post/<int:id>')
def get_post(id):
    return render_template('post.html', blog_posts=all_blogs, num=id)

if __name__ == "__main__":
    app.run(debug=True)
