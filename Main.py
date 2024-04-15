from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
#my database connection
local_server=True
app = Flask(__name__)
app.secret_key='sainadha'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms'
db=SQLAlchemy(app)

#Here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.string(100))
    email=db.column(db.string(100))

@app.route('/')
def hello_world():
    try:
        test.query.all()
        return 'My database is connected'
    except:
        return 'My db is not connected'

@app.route('/test')
def test():
    return render_template('test.html')
 
app.run(debug=True)