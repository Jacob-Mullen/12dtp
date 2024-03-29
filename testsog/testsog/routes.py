from flask import Flask,render_template 
import sqlite3


app =  Flask(__name__)




#this is the route to the home page/landing page
@app.route('/')
def landingpage():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=4 ')
    results = cur.fetchone()
    print (results)
    return render_template('landingpage.html',results=results)

#this is the route to the standerds page whitch will display magority of the information in the database
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

#this is the route to the swing page witch will display all the songs that are in the catagry of swing
@app.route('/swing')
def home():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=1 ')
    results = cur.fetchall()
    print (results)
    return render_template("swing.html", title = "swing",results=results)

#this is the route to the bossa page witch will display all the songs in the catagry of bossa nova
@app.route('/bossa')
def contact():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=2 ')
    results = cur.fetchall()
    print (results)
    return render_template("bossa.html", title = "bossa",results=results)

#this is the route to the bebop page it is used to display all the bebop catagry songs
@app.route('/bebop')
def about():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=3 ')
    results = cur.fetchall()
    print (results)
    return render_template("bebop.html", title = "samba",results=results)

#this i the others route it is used to diplay the songs that dont fit in the other three category 
@app.route('/other')
def feels():
    conn = sqlite3.connect('song.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM song WHERE feel=4 ')
    results = cur.fetchall()
    print (results)
    return render_template('other.html',results=results)




if __name__ == "__main__":
    app.run(debug=True)