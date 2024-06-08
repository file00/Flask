from flask import Flask, request
app = Flask(__name__)

@app.route("/abab",methods=["GET","POST"])
def abab():
    return request.values.get("name",default="No Data!!")

if __name__ == "__main__":
    app.run()

