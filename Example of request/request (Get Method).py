from flask import Flask, request
app = Flask(__name__)

# Get variable values from Get Method
@app.route("/aaa")
def aaa():
    return "The variable name value using the request object is {}.".format(request.args.get("name"))

if __name__ == "__main__":
    app.run()

# In request.args, the args is accessible only to the data delivered in the Get method.
