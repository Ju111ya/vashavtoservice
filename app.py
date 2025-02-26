from flask import Flask, render_template, redirect, request



app = Flask(__name__)



@app.route("/")
def home(): 
  return render_template("index.html")


@app.route("/contacts")
def contacts(): 
  return render_template("contacts.html")

@app.route("/services")
def services(): 
  return render_template("services.html")

if __name__ == "__main__":
  app.run(port=8080, debug=True)
