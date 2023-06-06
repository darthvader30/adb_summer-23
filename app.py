from multiprocessing import connection
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/range_sal')
def range_sal():
   return render_template('range_sal.html')

@app.route('/updatesalary')
def updatesalary():
   return render_template('updatesalary.html')

@app.route('/remove')
def remove():
   return render_template('remove.html')

@app.route('/find')
def find():
   return render_template('find.html')

@app.route('/put_pic')
def put_pic():
   return render_template('put_pic.html')

@app.route('/updatekey')
def updatekey():
   return render_template('updatekey.html')

@app.route('/add_pic')
def addpic():
   return render_template('add_pic.html')

@app.route('/all', methods=['POST','GET'])
def full_list():
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    querry="Select * from people "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("list.html",rows = rows)

@app.route('/update_sal',methods=['POST','GET'])
def update_sal():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['sal'])
        querry="UPDATE people SET salary = '"+keyword+"'   WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/update_key',methods=['POST','GET'])
def updatek():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        querry="UPDATE people SET keywords = '"+keyword+"'   WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/addpic',methods=['POST','GET'])
def addpicture():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        currsor = connection.cursor()
        name= str(request.form['name1'])
        pic= str(request.form['pic1'])
        querry="UPDATE people SET Picture = '"+pic+"'   WHERE Name ='"+name+"' "
        currsor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        currsor.execute(querry2)
        rows = currsor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)



@app.route('/range_sal', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        salrange= (request.form['range'])
        querry="select * from people WHERE Salary  <"+salrange+""
        cursor.execute(querry)
        rows = cursor.fetchall()
        connection.close()
    return render_template("put_pic.html",rows = rows)

@app.route('/remove_person', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        querry="DELETE FROM people WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/find_deets', methods=['POST','GET'])
def list():
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    field=str(request.form['name'])
    querry="Select * from people WHERE Name =  '"+field+"' "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("put_pic.html",rows = rows)

if __name__ =="__main__":
    app.run(debug=True)
    