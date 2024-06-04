# Jinja2 Template Engine

# Flask 설치시 같이 설치되기 때문에 추가 설치 X
# Flask의 Template Files은 기본적으로 Templates Folder에 저장함.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world!!</h1>"

@app.route("/user/<username>")
def get_user(username):
    return render_template("user.html",name=username)

if __name__ == "__main__":
    app.run()

