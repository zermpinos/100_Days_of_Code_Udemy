from flask import Blueprint, render_template, request, redirect, url_for
from .models import Book
from . import db

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    all_books = Book.query.order_by(Book.title).all()
    return render_template('index.html', books=all_books)

@main_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template("add.html")

@main_blueprint.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get_or_404(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('main.home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get_or_404(book_id)
    return render_template("edit_rating.html", book=book_selected)

@main_blueprint.route('/delete', methods=['POST'])
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get_or_404(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('main.home'))
