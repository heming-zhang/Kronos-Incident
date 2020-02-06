from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = Flask)
    content = db.Column(db.Text, nullable = False)

db.create_all()

@app.route('/')
def hello_world():
    article1 = Article(title='aaa',content='bbb')
    db.session.add(article1)
    db.session.commit()
    return 'Hello!'


if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	