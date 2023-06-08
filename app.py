from flask import Flask, render_template, request
import pyodbc

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

#ODBC Driver connection to Azure SQL Database
driver = '{ODBC Driver 18 for SQL Server}'
database = 'adb'
server = 'tcp:dbadb.database.windows.net,1433'
username = "kxs5434"
password = "kxs@root5434"
connection= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor() #cursor 

#Function to list all entries
@app.route('/all', methods=['POST','GET'])
def full_list():
    query="SELECT * FROM people"
    cursor.execute(query)
    rows=cursor.fetchall()
    return render_template("list.html",rows = rows)

#Function to update salary of a particular entry
@app.route('/update_salary',methods=['POST','GET'])
def updateSalary():
    if (request.method=='POST'):
        name= str(request.form['name'])
        keyword= str(request.form['sal'])
        query="UPDATE people SET salary = '"+keyword+"' WHERE Name ='"+name+"' "
        cursor.execute(query)
        connection.commit()
        query2="Select * from people"
        cursor.execute(query2)
        rows = cursor.fetchall()
    return render_template("list.html", rows = rows)

#Function to update descript of an entry
@app.route('/update_keyword',methods=['POST','GET'])
def updateKeyword():
    if (request.method=='POST'):
        name= str(request.form['name'])
        descript= str(request.form['descript'])
        query="UPDATE people SET descript = '"+descript+"'WHERE Name ='"+name+"' "
        cursor.execute(query)
        connection.commit()
        query2="Select * from people"
        cursor.execute(query2)
        rows = cursor.fetchall()
    return render_template("list.html",rows = rows)

#Function to add picture for an entry
@app.route('/addPicture',methods=['POST','GET'])
def addPicture():
    if (request.method=='POST'):
        name= str(request.form['name1'])
        pic= str(request.form['pic1'])
        query="UPDATE people SET Picture = '"+pic+"'   WHERE Name ='"+name+"' "
        cursor.execute(query)
        connection.commit()
        query2="Select * from people "
        cursor.execute(query2)
        rows = cursor.fetchall()
    return render_template("list.html",rows = rows)

#Function to list entries for room range
@app.route('/range_sal', methods=['GET', 'POST'])
def salaryRange():
    if (request.method=='POST'):
        stRange= (request.form['stRange'])
        endRange= (request.form['endRange'])
        query="Select * from people WHERE room BETWEEN '"+stRange+"' AND '"+endRange+"' "
        cursor.execute(query)
        rows = cursor.fetchall()
    return render_template("put_pic.html",rows = rows)

#Function to remove an entry
@app.route('/remove_person', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        name= str(request.form['name'])
        query="DELETE FROM people WHERE Name ='"+name+"' "
        cursor.execute(query)
        connection.commit()
        query2="Select * from people"
        cursor.execute(query2)
        rows = cursor.fetchall()
    return render_template("list.html",rows = rows)

#Function to list details of a particular entry
@app.route('/find_details', methods=['POST','GET'])
def findDetails():
    teln=(request.form['teln'])
    query="Select * from people WHERE teln ='"+teln+"' "
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template("put_pic.html",rows = rows)

if __name__ =="__main__":
    app.run(debug=True)
    