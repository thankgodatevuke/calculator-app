w=input("what is your weight in kg\n")
w=float(w)
h=input("what is your height in metres\n")
h=float(h)
def BMI_calc (w,h):
    BMI = (w/(h**2))
    BMI = round(BMI)
    if BMI < 18.5: 
        print(f"Your BMI is: {BMI}\n Underweight")
    elif 18.4 < BMI < 25:
        print(f"Your BMI is: {BMI}\n Normal")
    elif 24.9< BMI < 30:
        print(f"Your BMI is: {BMI}\n Overweight")
    elif 29.9< BMI < 35:
        print(f"Your BMI is: {BMI}\n Class 1 Obesity")
    elif 34.9< BMI < 40:
        print(f"Your BMI is: {BMI}\n Class 2 Obesity")
    else: 
        print(f"Your BMI is: {BMI}\n Extreme Obesity")
        
BMI_calc (w,h)
