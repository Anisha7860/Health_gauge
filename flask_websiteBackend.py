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
    BMI =  round(BMI, 2)
    if BMI <= 17:
        return "Severe Thinnees"
    elif BMI > 17 and BMI <= 18.5:
        return "Moderate Thinnees",BMI
    elif BMI > 18.5 and BMI <= 25:
        return "Normal",BMI
    elif BMI > 25 and BMI <= 30:
        return "Overweight",BMI
    elif BMI > 30 and BMI <= 35:
        return "Obese class 1",BMI
    else:
        return "Obese class 2",BMI


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
    print(prediction[0])
    if prediction[0] == 0:
        return render_template("MentalHeslthRecomend.html", mental_status = "YOU ARE MENTALLY FIT!! CONGRATS",heading = "Here are some strategy that'll help you maintain a good Mental Health:")
    else:
        return render_template("MentalHeslthRecomend.html", mental_status = "You dont seem to be mentally fit ",heading = "Here are some strategy that'll help you out:")
    

@app.route("/PhysicalHealth",methods = ["GET","POST"])
def physicalHealthpage():
    if (request.method == "GET"):
        return render_template("physical.html")
    else:
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        weightClass,BMI = BMIcalculate(weight, height)
        if weightClass == "Severe Thinnees":
            return render_template("PhyHealthrecommendation.html", excercise_heading = "The Workout Plan All Skinny Guys Have Been Waiting For", excercise_link = "https://www.menshealth.com/fitness/a19540601/skinny-man-transformation-plan/",deit_heading = "The Skinny Guy’s Guide: Eating To Gain Muscle",deit_link = "https://breakingmuscle.com/healthy-eating/the-skinny-guy-s-guide-eating-to-gain-muscle",weight_class = weightClass, BMI = BMI)
        elif weightClass == "Moderate Thinnees":
            return render_template("PhyHealthrecommendation.html", excercise_heading = "How to Gain Weight Fast and Safely", excercise_link = "https://www.healthline.com/nutrition/how-to-gain-weight",deit_heading = "Underweight? see How to Add weight healthfully",deit_link = "https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429",weight_class = weightClass, BMI = BMI)
        elif weightClass == "Normal":
            return render_template("PhyHealthrecommendation.html", excercise_heading = "The 7 Best Exercises for a Full-Body Workout", excercise_link = "https://www.active.com/fitness/articles/the-7-best-exercises-for-a-full-body-workout",deit_heading = "How to Maintain Weight",deit_link = "https://www.openfit.com/how-to-maintain-weight",weight_class = weightClass, BMI = BMI)
        elif weightClass == "Overweight":
            return render_template("PhyHealthrecommendation.html", excercise_heading = "The 8 Best Exercises for Weight Loss", excercise_link = "https://www.healthline.com/nutrition/best-exercise-for-weight-loss#TOC_TITLE_HDR_3",deit_heading = "Best Indian Diet Plan for Weight Loss",deit_link = "https://www.healthifyme.com/blog/best-indian-diet-plan-weight-loss/",weight_class = weightClass, BMI = BMI)
        elif weightClass == "Obese class 1":
            return render_template("PhyHealthrecommendation.html", excercise_heading = "Morbidly Obese: Tips for Losing 100 Pounds or More", excercise_link = "https://www.onhealth.com/content/1/morbidly_obese_tips_for_losing_100_pounds_or_more",deit_heading = "Obesity Diet: What To Eat And Avoid To Manage Obesity",deit_link = "https://food.ndtv.com/food-drinks/obesity-diet-what-to-eat-and-avoid-to-manage-obesity-181546",weight_class = weightClass, BMI = BMI)
        else:
            return render_template("PhyHealthrecommendation.html", excercise_heading = "How Sedentary Obese People Can Ease Into Regular Exercise", excercise_link = "https://www.healthline.com/health/fitness-exercise/exercise-for-obese-people",deit_heading = "Morbidly Obese Weight Loss Plan Without Surgery",deit_link = "https://flabfix.com/morbidly-obese-weight-loss-plan-without-surgery/",weight_class = weightClass, BMI = BMI)     

@app.route("/MentalHealthBooks",methods = ["GET","POST"])
def MentalHealthBooks():
    return render_template("book.html")


@app.route("/Meditations",methods = ["GET","POST"])
def Meditations():
    return "meditations"


@app.route("/LandingPage",methods = ["GET","POST"])
def Landingpage():
    return render_template("crawler.html")




if __name__ == "__main__":
    app.run(debug = True)