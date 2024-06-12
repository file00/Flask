# test_request_context(): Method for testing HTTP requests on Flask
# Use url_for() Method 

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/Hello/")
def hello():
    return "<h1>Hello World!!</h1>"

@app.route("/user/<username>")
def get_user():
    return "user:"+username

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("hello"))
        print(url_for("get_user",username = "Git"))
    


