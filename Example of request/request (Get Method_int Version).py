# request (Int Type Version)
from flask import Flask, request
app = Flask(__name__)

@app.route("/bbb")
def bbb():
    nameVal = request.args.get("name","100",int)
    return str(nameVal)

# The code was written to import only int-type,
# and it is necessary to convert the variable to str-type in order to import only int-type.

if __name__ == "__main__":
    app.run()

