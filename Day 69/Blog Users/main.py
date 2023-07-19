# Import necessary modules from Flask and extensions
from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import LoginForm, RegisterForm, CreatePostForm, CommentForm
from flask_gravatar import Gravatar
import os

# Create the Flask application instance
app = Flask(__name__)

# Configure the Flask app
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Secret key for security
ckeditor = CKEditor(app)  # Initialize the CKEditor for rich text editing
Bootstrap(app)  # Initialize Bootstrap for better UI
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False,
                    base_url=None)  # Configure Gravatar for user avatars

# Configure the database connection
database_directory = r''
# Check if the directory exists, if not, create it
if not os.path.exists(database_directory):
    os.makedirs(database_directory)
# Set the SQLite database URI with the specific location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(database_directory, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance
db = SQLAlchemy(app)  # Initialize SQLAlchemy for database handling

# Initialize the LoginManager for user authentication
login_manager = LoginManager()
login_manager.init_app(app)

# Define the function to load a user by its ID for authentication
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the User class for database table "users"
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

# Define the BlogPost class for database table "blog_posts"
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

# Define the Comment class for database table "comments"
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    comment_author = relationship("User", back_populates="comments")
    text = db.Column(db.Text, nullable=False)

# Create all the database tables within the app context
with app.app_context():
    db.create_all()

# Define a decorator for routes accessible only to admin users
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:  # Assuming the user with ID 1 is the admin user
            return abort(403)  # Forbidden status if the user is not the admin
        return f(*args, **kwargs)
    return decorated_function

# Define the route for the home page, showing all blog posts
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()  # Query all blog posts from the database
    return render_template("index.html", all_posts=posts, current_user=current_user)

# Define the route for user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()  # Initialize the registration form
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=form.email.data, name=form.name.data, password=hash_and_salted_password)
        db.session.add(new_user)  # Add the new user to the database
        db.session.commit()  # Commit the transaction
        login_user(new_user)  # Log in the new user
        return redirect(url_for("get_all_posts"))  # Redirect to the home page

    return render_template("register.html", form=form, current_user=current_user)

# Define the route for user login
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()  # Initialize the login form
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()  # Get the user by email
        if not user:
            # Email doesn't exist or password incorrect.
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)  # Log in the user
            return redirect(url_for('get_all_posts'))  # Redirect to the home page

    return render_template("login.html", form=form, current_user=current_user)

# Define the route for user logout
@app.route('/logout')
def logout():
    logout_user()  # Log out the user
    return redirect(url_for('get_all_posts'))  # Redirect to the home page

# Define the route for viewing a single blog post and adding comments
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()  # Initialize the comment form
    requested_post = BlogPost.query.get(post_id)  # Get the requested blog post

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(text=form.comment_text.data, comment_author=current_user, parent_post=requested_post)
        db.session.add(new_comment)  # Add the new comment to the database
        db.session.commit()  # Commit the transaction

    return render_template("post.html", post=requested_post, form=form, current_user=current_user)

# Define the route for the "About" page
@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)

# Define the route for the "Contact" page
@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)

# Define the route for adding a new blog post (admin-only route)
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()  # Initialize the blog post creation form
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)  # Add the new blog post to the database
        db.session.commit()  # Commit the transaction
        return redirect(url_for("get_all_posts"))  # Redirect to the home page

    return render_template("make-post.html", form=form, current_user=current_user)

# Define the route for editing an existing blog post (admin-only route)
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)  # Get the blog post by ID
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=current_user,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()  # Commit the transaction
        return redirect(url_for("show_post", post_id=post.id))  # Redirect to the edited post page

    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)

# Define the route for deleting a blog post (admin-only route)
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)  # Get the blog post by ID
    db.session.delete(post_to_delete)  # Delete the blog post from the database
    db.session.commit()  # Commit the transaction
    return redirect(url_for('get_all_posts'))  # Redirect to the home page

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run the app on all available network interfaces
