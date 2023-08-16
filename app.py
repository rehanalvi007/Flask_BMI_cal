# Import required modules
from flask import Flask,render_template,request

# Instantiate the Flask module

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def BMI_calculate():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight,height)
        bmi_category = categorize_bmi(bmi)
        return render_template('result.html', bmi=bmi ,category=bmi_category)
    return render_template('index.html')

def calculate_bmi(weight,height):
    return weight/(height * height)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    

if __name__ == "__main__":
    app.run(debug=True)
