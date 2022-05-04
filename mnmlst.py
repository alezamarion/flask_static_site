
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/zen")
def zen():
    return render_template("zen.html")

@app.route("/not_mnmlst_list")
def not_mnmlst_list():
    return render_template("not_mnmlst_list.html")

@app.route("/mscncptns")
def mscncptns():
    return render_template("mscncptns.html")

@app.route("/breathe")
def breathe():
    return render_template("breathe.html")


if __name__ == "__main__":
    app.run(debug=True)
