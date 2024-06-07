from flask import Flask

app = Flask(__name__)

@app.route("/aaa",defaults={ "bbs_id":100 })
@app.route("/aaa/<bbs_id>")
def aaa(bbs_id):
    return "This is {} from 'aaa'.".format(bbs_id)

if __name__ == "__main__":
    app.run()

# Even if the positions of Line 5 and Line 6 are changed, the results are the same.
