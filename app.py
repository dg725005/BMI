import streamlit as slt

slt.title("BMI Calculator")

wt_entered = slt.number_input("Enter weight in kg")

height_unit = slt.radio("Height Unit",["cm",'m','feet'])

height_entered = slt.number_input("Enter height")

if height_unit == "cm":
    height_entered/=100.00 
elif height_unit=='feet':
    height_entered = (height_entered*12*2.54)/100.00
else:
    pass    

if (slt.button("Calculate BMI!")):
    slt.text("Your BMI is: "+str(round(wt_entered/(height_entered**2),1)))