# redirect_to Option

from flask import Flask

app = Flask(__name__)

@app.route("/aaa",redirect_to="/new_aaa")
def aaa():
    return "Page called /aaa"

@app.route("/new_aaa")
def new_aaa():
    return "/Page called /aaa"

if __name__== "__main__":
    app.run()
