# Session
from flask import Flask, request, session

app = Flask(__name__)

app.secret_key="KK123"
@app.route("/session")
def session_set():
    session['ID'] = "Flask Test"
    return "Setting session"

@app.route("/session_out")
def session_out():
    del session["ID"]
    return "Session out"

if __name__=="__main__":
    app.run()
