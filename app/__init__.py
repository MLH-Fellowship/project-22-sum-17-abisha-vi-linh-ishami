import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


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


pols = [
    Polaroid("Caption of polaroid 1", "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&poi=%5B1936%2C1296%5D&w=3872&h=1936&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F35%2F2019%2F08%2F05144705%2FGettyImages-96709750-1.jpg"),
    Polaroid("Caption of polaroid 2", ".\static\img\R.jpg"),
    Polaroid("Caption of polaroid 3",
             "https://www.success.com/wp-content/uploads/2016/09/therealreasontravelingmakesyouhappy.jpg")
]


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
        Exp("Experience 3", ["point 1", "point 2", "point 3"]),
        Exp("Experience 4", ["point 1", "point 2", "point 3"])
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=pols, experiences=exps)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), polaroids=pols)
