from flask import Flask,request
from flask import render_template

app = Flask(__name__)
Genderl = ['female', 'male', 'trans']
family_historyl = ['No', 'Yes']
treatmentl = ['No', 'Yes']
benefitsl =  ["Don't know", 'No', 'Yes']
care_optionsl = ['No', 'Not sure', 'Yes']
anonymityl = ["Don't know", 'No', 'Yes']
leavel = ["Don't know", 'Somewhat difficult', 'Somewhat easy', 'Very difficult', 'Very easy']
work_interferel = ["Don't know", 'Never', 'Often', 'Rarely', 'Sometimes']
coworkersl =  ['No', 'Some of them', 'Yes'] 

def CheckPositionNumber(string,lists):
    for no,data in enumerate(lists):
        if string == data:
            return no

@app.route('/HomePage')
def index():
    return render_template("index.html")

@app.route('/MentalHealth',methods = ["GET","POST"])
def MentalHealthpage():
    if (request.method == "GET"):
        return render_template("quizm.html")
    elif (request.method == "POST"):
        Age = int(request.form['Age'])
        Gender = CheckPositionNumber(str(request.form['Gender']),Genderl)
        family_history = CheckPositionNumber(str(request.form['family_history']),family_historyl)
        benefits = CheckPositionNumber(str(request.form['benefits']),benefitsl)
        care_options = CheckPositionNumber(str(request.form['care_options']),care_optionsl)
        anonymity = CheckPositionNumber(str(request.form['anonymity']),anonymityl)
        leave = CheckPositionNumber(str(request.form['leave']),leavel)
        work_interfere = CheckPositionNumber(str(request.form['work_interfere']),work_interferel)
        coworkers = CheckPositionNumber(str(request.form['coworkers']),coworkersl)
       


        

@app.route("/PhysicalHealth")
def physicalHealthpage():
    return "waiting"

if __name__ == "__main__":
    app.run(debug = True)