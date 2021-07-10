from flask import Flask,request
from flask import render_template
import pickle
import sklearn

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

        if string.lower() == data.lower():
            print("yessssssss")
            return no
        
def checkAgeRange(age):
    
    if age >= 0 and age <= 20:
        return 0
    elif age >= 21 and age<=30:
        return 1
    elif age >= 31 and age <= 65:
        return 2
    else:
        return 3

def BMIcalculate(weight, height):
    height = height*0.01
    height = height*height
    BMI = weight/height
    print(BMI)
    if BMI <= 17:
        return "Severe Thinnees"
    elif BMI > 17 and BMI <= 18.5:
        return "Moderate Thinnes Thinnees"
    elif BMI > 18.5 and BMI <= 25:
        return "Normal"
    elif BMI > 25 and BMI <= 30:
        return "Overweight"
    elif BMI > 30 and BMI <= 35:
        return "Obese class 1"
    else:
        return "Obese class 2"


@app.route('/HomePage')
def index():
    return render_template("index.html")

@app.route('/MentalHealth',methods = ["GET","POST"])
def MentalHealthpage():
    if (request.method == "GET"):
        return render_template("quizm.html")


@app.route('/Recomendations',methods = ["GET","POST"])
def Recomendation():
    Age = int(request.form['Age'])
    gender = request.form['label_Gender']
    Gender = CheckPositionNumber(request.form['label_Gender'],Genderl)
    family_history = CheckPositionNumber(request.form['label_family_history'],family_historyl)
    fam = request.form['label_family_history']
    print(fam)
    benefits = CheckPositionNumber(str(request.form['label_benefits']),benefitsl)
    care_options = CheckPositionNumber(str(request.form['label_care_options']),care_optionsl)
    anonymity = CheckPositionNumber(str(request.form['label_anonymity']),anonymityl)
    leave = CheckPositionNumber(str(request.form['label_leave']),leavel)
    work_interfere = CheckPositionNumber(str(request.form['label_work_interfere']),work_interferel)
    coworkers = CheckPositionNumber(str(request.form['label_coworkers']),coworkersl)

    age_range = checkAgeRange(Age)

    print(Age,"++",Gender,"++", family_history,"++", benefits,"++", care_options,"++", anonymity,"++", leave,"++", work_interfere,"++", age_range,"++", coworkers)

    model = pickle.load(open('finalized_model', 'rb'))
    print("hereeee")
    prediction = model.predict([[Age, Gender, family_history, benefits, care_options, anonymity, leave, work_interfere, age_range, coworkers]])
    print("fddddddddddddddddddddddddddddddddddddd")
    print(prediction)
    return "recomends"

@app.route("/PhysicalHealth")
def physicalHealthpage():
    return render_template("physical.html")

if __name__ == "__main__":
    app.run(debug = True)