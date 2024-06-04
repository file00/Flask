from flask import Flask, render_template
app  = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template('Template Test.html', my_string="Template Test", my_list=[11,22,33,44,55,66,77])

if __name__ == "__main__":
    app.run()
