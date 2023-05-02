from flask import Flask,render_template 
import sqlite3


app =  Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", title = "hello world")

@app.route('/contact')
def contact():
    return render_template("contact.html", title = "contact")

@app.route('/about')
def about():
    return render_template("about.html", title = "about")

@app.route('/feels')
def feels():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM feel')
    results = cur.fetchall()
    print (results)
    return render_template('feels.html',results=results)

@app.route('/pizza/<int:id>')
def pizza(id):
    conn=sqlite3.connect('pizza.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM pizza WHERE id=?',(id,))
    pizza=cur.fetchone()
    return render_template ('pizza.html', pizza=pizza)

if __name__ == "__main__":
    app.run(debug=True)