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


@app.route('/')
def index():
    projs = [Proj("Proj 1", "Description of my proj 1!", "https://google.com/", "https://github.com/"), Proj("Proj 2", "This is my proj 2!!",
                                                                                                             "https://github.com/", "https://github.com/"),  Proj("Proj 3", "Description of my proj 3", "https://github.com/", "https://github.com/")]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs)
