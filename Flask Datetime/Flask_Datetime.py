from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def userDateType(date_format):
    def changeFormat(date_string): 
        return datetime.strptime(date_string, date_format)
    return changeFormat

@app.route("/ccc",methods=["GET","POST"])
def ccc():
    print(request.values.get("date","2024-06-07",type=userDateType("%Y-%m-%d")))
    return "Check through the Console"

if __name__ == "__main__":
    app.run()


