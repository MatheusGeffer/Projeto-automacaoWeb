from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("cadastro"))
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro_produtos.html")

#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)



