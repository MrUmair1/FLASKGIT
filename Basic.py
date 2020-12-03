import pylint
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123@localhost/MYDB'

db = SQLAlchemy(app)


class blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    auther = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __rep__(self):
        return 'blogpost' + str(self.id)

all_posts=[
    {
     'title' : 'POST1',
     'content' : 'FIRST POSTS DISPLAY',
     'auther' : 'Umair'
     },
    {
     'title' : 'POST2',
     'content' : 'Second post',
     'auther' : 'OWAIS'
     }
  
]


@app.route('/form', methods=['GET', 'POST'])
def form1():
    return render_template('index.html')

@app.route('/posts', methods=['GET','POST'])
def posts():
    
    if request.method == 'POST':
        post_title= request.form['title']
        post_content = request.form['content']
        post_auther = request.form['auther']
        new_post = blogpost(title=post_title, content=post_content, auther=post_auther)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts= blogpost.query.order_by(blogpost.date_posted).all()
        return render_template('posts.html', posts = all_posts)


@app.route('/home/<string:name>')
def home(name):
    return "Hello ," + name


@app.route('/onlyget' , methods=['POST'])
def onlyget():
    return 'hey this your webpage'



if __name__ == '__main__':
    app.run()
