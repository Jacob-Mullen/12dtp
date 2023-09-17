from flask import Flask,render_template 
import sqlite3


app =  Flask(__name__)

@app.route('/swing')
def home():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=1 ')
    results = cur.fetchall()
    print (results)
    return render_template("swing.html", title = "swing",results=results)

@app.route('/bossa')
def contact():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=2 ')
    results = cur.fetchall()
    print (results)
    return render_template("bossa.html", title = "bossa",results=results)

@app.route('/stand/<int:id>')
def stand(id):
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM info WHERE id=?',(id,))
    results = cur.fetchall()
    print (results)
    cur.execute('SELECT * FROM recordingimg WHERE id=?',(id,))
    image = cur.fetchone()
    print(image)
    cur.execute('SELECT * FROM recordingsaud WHERE id=?',(id,))
    link = cur.fetchone()
    print(link)
    return render_template("stand.html", title = "stand",results=results, image=image, link=link )

@app.route('/beebop')
def about():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=3 ')
    results = cur.fetchall()
    print (results)
    return render_template("beebop.html", title = "samba",results=results)

@app.route('/feels')
def feels():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=4 ')
    results = cur.fetchall()
    print (results)
    return render_template('feels.html',results=results)

@app.route('/landingpage')
def landingpage():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=4 ')
    results = cur.fetchone()
    print (results)
    return render_template('landingpage.html',results=results)


if __name__ == "__main__":
    app.run(debug=True)