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

@app.route('/')
def index():

    projs = [
        Proj("Proj 1", "Description of my proj 1!",
             "https://google.com/", "https://github.com/"),
        Proj("Proj 2", "This is my proj 2!!",
             "https://github.com/", "https://github.com/"),
        Proj("Proj 3", "Description of my proj 3",
             "https://github.com/", "https://github.com/")
    ]

    pols = [
        Polaroid("Caption of polaroid 1", ".\static\img\R.jpg"),
        Polaroid("Caption of polaroid 2", ".\static\img\R.jpg"),
        Polaroid("Caption of polaroid 3",
                 ".\static\img\Screenshot 2022-06-04 163820.png")
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=pols)
