from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rohan:Fushimi#2112@localhost/trial_db'

app.config['MYSQL_USER'] = 'root' #root, epyqrev
app.config['MYSQL_PASSWORD'] = 'Fushimi@2112' #Fushimi@2112, epyq@pythontrial
app.config['MYSQL_HOST'] = '127.0.0.1' #127.0.0.1, epyqrev.mysql.pythonanywhere-services.com
app.config['MYSQL_DB'] = 'trial_db' #trial_db Tablename: trial_db.products, epyqrev$epyqdb
mysql = MySQL(app) 

all_entries = []
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM trial_db.products''')
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
        cursor.execute(''' INSERT INTO products (PName, Pcategory, Quantity, Price) VALUES(%s,%s,%s,%s)''',(pname,cat,qty,price))
        mysql.connection.commit()
        cursor.close()
    return redirect("/")
@app.route('/delete')
def delete_item():
    pid = request.args.get('pid')
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM products WHERE (PID = %s);''',[pid])
    mysql.connection.commit()
    cursor.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)