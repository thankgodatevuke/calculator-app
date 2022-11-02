import streamlit as st
w=st.number_input("what is your weight in kg\n", step=1)
h=st.number_input("what is your height in metres\n")
st.selectbox('select gender', ['male', 'female'])

if st.button('check'):
    BMI = (w/(h**2))
    BMI = round(BMI)
    if BMI < 18.5: 
        st.write(f"Your BMI is: {BMI}\n Underweight")
    elif 18.4 < BMI < 25:
        st.write(f"Your BMI is: {BMI}\n Normal")
    elif 24.9< BMI < 30:
        st.write(f"Your BMI is: {BMI}\n Overweight")
    elif 29.9< BMI < 35:
        st.write(f"Your BMI is: {BMI}\n Class 1 Obesity")
        st.image('USDT.png')
    elif 34.9< BMI < 40:
        st.write(f"Your BMI is: {BMI}\n Class 2 Obesity")
        st.image('USDT.png')
    else: 
        st.write(f"Your BMI is: {BMI}\n Extreme Obesity")
        st.image('USDT.png')
