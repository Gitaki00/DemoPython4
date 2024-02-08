from flask import Flask, render_template

new=Flask(__name__)

@new.route('/')
def index():
    return render_template('index.html')

@new.route('/templates/<username>')
def username(username):
    return render_template('profile.html',username=username,isActive=False)

@new.route('/books')
def book():
    book=[{'name':'book1','author':'abc1','cover':'https://images.thenile.io/r1000/9780007488353.jpg'},{'name':'book2','author':'abc2','cover':'https://images.thenile.io/r1000/9780007488353.jpg'},{'name':'book3','author':'abc3','cover':'https://images.thenile.io/r1000/9780007488353.jpg'}]
    return render_template('book.html',book=book)
new.run(debug=True)
