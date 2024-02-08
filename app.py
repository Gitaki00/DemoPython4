from flask import Flask
app=Flask(__name__)

@app.route('/')
def helo():
    return '<h1>helo</h1>'

@app.route('/new/<username>')
def username(username):
    return '<h1> my name is %s</h1>'% username

@app.route('/new/<int:id>')
def int(id):
    return '<h1>my num is %d</h1>'% id

app.run()