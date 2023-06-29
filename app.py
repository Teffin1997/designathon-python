from flask import Flask,render_template,request
import mysql.connector
user_dic={'teffin97':'098765','rajeev90':'098765'}
conn=mysql.connector.connect(host='localhost',user='root',password='',database='sole')
mycursor=conn.cursor()

app= Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/make')
def make():
    return render_template("newaccount.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/admin',methods=['post'])
def admin_login():
    adm=request.form['usertype']
    userr= request.form['user']
    pwd=request.form['password']
    if adm=="ve":
        if userr not in user_dic:
         return render_template('login.html',msg='invalid userid or password')
        elif user_dic[userr] != pwd:
         return render_template('login.html',msg='invalid userid or password')
        else:
         return render_template('admin.html')
    else:
       return render_template('login.html')
    
@app.route('/costumer')
def view():
    
    query="select * from details"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('costumer.html',sqldata=data)

@app.route('/BACKADMIN')
def backadmin():
   return render_template('admin.html')

@app.route('/update',methods=['post'])
def update():
   name=request.form['name']
   cons=request.form['cons']
   city=request.form['city']
   phone=request.form['phone']
   dct=request.form['dct']
   pin=request.form['pin']
   eml=request.form['eml']
   query="insert into details values(%s,%s,%s,%s,%s,%s,%s)"
   values=(name,phone,cons,dct,city,pin,eml)
   mycursor.execute(query,values)
   conn.commit()
   return render_template('login.html')
  








   
   
   


if __name__ == '__main__':
   app.run(debug = True)
