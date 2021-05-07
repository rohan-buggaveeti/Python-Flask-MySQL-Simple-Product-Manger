from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)


app.config['MYSQL_USER'] = 'mysql_username' 
app.config['MYSQL_PASSWORD'] = 'mysql_pwd'
app.config['MYSQL_HOST'] = 'mysql_host_url'
app.config['MYSQL_DB'] = 'mysql_db'
mysql = MySQL(app) 

#table schema -> PID (Primary Key, Integer, Auto-Increment - starts from 1000), PName (varchar), PCategory (varchar), Quantity (Integer), Price (Integer)

all_entries = []
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM mysql_db.table_name''')
    all_entries = cursor.fetchall()
    cursor.close()
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
        pname = request.form['pname']
        cat = request.form['cat']
        qty = request.form['qty']
        price = request.form['price']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO table_name (PName, Pcategory, Quantity, Price) VALUES(%s,%s,%s,%s)''',(pname,cat,qty,price))
        mysql.connection.commit()
        cursor.close()
    return redirect("/")
@app.route('/delete')
def delete_item():
    pid = request.args.get('pid')
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM table_name WHERE (PID = %s);''',[pid])
    mysql.connection.commit()
    cursor.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
