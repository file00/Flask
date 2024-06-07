from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

class userDateType:
    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kw):
        return datetime.strptime(args[0], self.format)

@app.route("/ddd", methods=["GET","POST"])
def ddd():
    print(request.values.get("date","2024-06-07",type=userDateType("%Y-%m-%d")))
    return "Check through the Console"

if __name__ == "__main__":
    app.run()
