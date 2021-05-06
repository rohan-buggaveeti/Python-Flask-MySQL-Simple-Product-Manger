from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rohan:Fushimi#2112@localhost/trial_db'

app.config['MYSQL_USER'] = 'epyqrev' #root
app.config['MYSQL_PASSWORD'] = 'epyq@pythontrial' #Fushimi@2112
app.config['MYSQL_HOST'] = 'epyqrev.mysql.pythonanywhere-services.com' #127.0.0.1
app.config['MYSQL_DB'] = 'epyqrev$epyqdb' #trial_db Tablename: trial_db.products
mysql = MySQL(app) 


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM trial_db.products''')
    all_entries = cursor.fetchall()
    return render_template("index.html",list = all_entries)
@app.route('/home')
def home():
    return redirect('/')
@app.route('/add')
def add():
    return render_template("form.html")
@app.route('/add_item', methods = ['POST', 'GET'])
def add_item():
    if request.method == "POST":
        pid = request.form['pid']
        pname = request.form['pname']
        cat = request.form['cat']
        qty = request.form['qty']
        price = request.form['price']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO products VALUES(%s,%s,%s,%s,%s)''',(pid,pname,cat,qty,price))
        mysql.connection.commit()
        cursor.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)