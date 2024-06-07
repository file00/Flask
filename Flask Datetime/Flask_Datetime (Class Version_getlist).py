# If multiple values are added to the same variable, return to -> list Type. (Use getlist -> No default)

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

class userDateType:
    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kw):
        return datetime.strptime(args[0], self.format)

@app.route("/eee", methods=["GET","POST"])
def eee():
    print(request.values.getlist("dates",type=userDateType("%Y-%m-%d")))
    return "Check through the Console"

if __name__ == "__main__":
    app.run()

