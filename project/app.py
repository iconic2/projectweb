from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")




@app.route("/")
def index():
    return render_template("home.html")


#@app.route()
#def ():
#    return render_template("docenten.html","/docenten/templates")





if __name__ == "__main__":
    app.run(debug=True)
