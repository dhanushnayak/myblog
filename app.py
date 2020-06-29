from flask  import *
import sqlite3 as sql
import os



app = Flask(__name__,template_folder='template')

def db():
   con = sql.connect("./myblog.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   return cur   

@app.route('/')
def home():
   cur = db()
   cur.execute('SELECT * FROM blog limit 1;')
   rows = cur.fetchone()
   return render_template('index.html',row=rows)


@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact",methods = ["POST","GET"])
def contact():
       msg = "No QUERY"  
       if request.method == "POST":  
          try:  
                  name = request.form["name"]  
                  email = request.form["email"] 
                  subject = request.form['subject'] 
                  message = request.form["message"]  
                  cur= db() 
                  cur.execute("INSERT into contact (Name, Email, Subject, Message) values (?,?,?,?)",(name,email,subject,message))  
                  con.commit()  
                  msg = "QUERY Submitted"  
          except:  
                  con.rollback()  
                  msg = "Query not Added"  
          finally:  
                  return render_template("contact.html",msg = msg) 
       return render_template("contact.html",msg = msg)
       
  
@app.route("/project")
def project():
       return render_template("portfolio.html")
 
if __name__ == '__main__':
   app.run()