from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin")
def render_signin(accountok=True):
    if accountok == True:
        return render_template("signin.html", message = "")
    else:
        return render_template("signin.html", message = "Username/Password is wrong")

@app.route("/login", methods = ['POST'])
def checkLogin():
    print("helllllllllo")
    email = request.form['email']
    pwd = request.form['password']
    if (email == "ab@ab.com" and pwd == "ab"):
        return render_template("dashboard.html", user="Pooja")
    else:
        return render_signin(False)

if __name__ == '__main__':
    app.debug = True
    app.run()