import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict 

load_dotenv()
app = Flask(__name__)

#connect to MySQL db
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

class Proj:
    def __init__(self, name, descrip, git, demo) -> None:
        self.name = name
        self.descrip = descrip
        self.git = git
        self.demo = demo

class Polaroid:
    def __init__(self, caption, pic):
        self.caption = caption
        self.pic = pic

class Exp:
    def __init__(self, name, descrip) -> None:
        self.name = name
        self.descrip = descrip

class Post:
    def __init__(self, name, email, content) -> None:
        self.name = name
        self.email = email
        self.content = content

@app.route('/')
def index():

    projs = [
        Proj("Proj 1", "Description of my proj 1!",
             "https://google.com/", "https://github.com/"),
        Proj("Proj 2", "This is my proj 2!!",
             "https://github.com/", "https://github.com/"),
        Proj("Proj 3", "Description of my proj 3",
             "https://github.com/", "https://github.com/"),
        Proj("Proj 4", "Description of my proj 4",
             "https://github.com/", "https://github.com/")
    ]

    exps = [
        Exp("Experience 1", ["point 1", "point 2", "point 3"]),
        Exp("Experience 2", ["point 1", "point 2", "point 3"]),
        Exp("Experience 3", ["point 1", "point 2", "point 3"])
    ]

    pols = [
        Polaroid("Caption of polaroid 1", "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&poi=%5B1936%2C1296%5D&w=3872&h=1936&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F35%2F2019%2F08%2F05144705%2FGettyImages-96709750-1.jpg"),
        Polaroid("Caption of polaroid 2", ".\static\img\R.jpg"),
        Polaroid("Caption of polaroid 3",
                "https://www.success.com/wp-content/uploads/2016/09/therealreasontravelingmakesyouhappy.jpg")
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=pols, experiences=exps)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), polaroids=pols)

# create timeline post page
@app.route('/timeline')
def timeline():
    posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), posts=posts)

# create db timeline_post
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

# create a GET endpoint that retrieves all timeline posts ordered by created_at descending 
# so the newest timeline posts are returned at the top
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {'timeline_posts': [
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


