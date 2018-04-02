from flask import Flask, render_template, flash

app = Flask(__name__)

#We need this for flashing errors
app.secret_key = 'some_secret'

@app.route('/')
def page1():
    return render_template("page1.html")

@app.route('/2')
def page2():
    return render_template("page2.html")

@app.route('/3')
def page3():
    flash("You can alert the user to an error like this.")
    return render_template("page3.html")

if __name__ == '__main__':
    app.run()