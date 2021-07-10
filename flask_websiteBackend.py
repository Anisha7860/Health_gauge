from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route('/HomePage')
def index():
    return render_template("index.html")

@app.route('/MentalHealth',methods = ["GET","POST"])
def MentalHealthpage():
    if (request.method == "GET"):
        return render_template("quizm.html")
    elif (request.method == "POST"):
        Age = int(request.form['Age'])
        Gender = str(request.form['Gender'])
        family_history = str(request.form['family_history'])
        benefits = str(request.form['benefits'])
        care_options = str(request.form['care_options'])
        anonymity = str(request.form['anonymity'])
        leave = str(request.form['leave'])
        work_interfere = str(request.form['work_interfere'])
        coworkers = str(request.form['coworkers'])
        

@app.route("/PhysicalHealth")
def physicalHealthpage():
    return "waiting"

if __name__ == "__main__":
    app.run(debug = True)