from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/find-shelter")
def find_shelter():
    return render_template("find-shelter.html")

@app.route("/find-shelter/north")
def northabdn():
    return render_template("northabdn.html")

@app.route("/find-shelter/south")
def southabdn():
    return render_template("southabdn.html") #need to update this html file

@app.route("/submit-shelter")
def submit_shelter():
    return render_template("TEMPLATE") #merge with Sanni's work

#@app.route("/submit-shelter/form") not sure if this will be used

app.run(debug=True)
