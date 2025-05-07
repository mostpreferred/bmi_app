#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing our streamlit library
import streamlit as st


# In[2]:


#bmi calculator------ creating a function called bmi calculator

def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi


st.title("BMI calculator")


    
weight = st.number_input("enter your weight in Kg.",min_value=1.0)
height = st.number_input("enter your height in m.",min_value=0.5,format="%.2f") 

if st.button("Calculate BMI"):
     bmi = calculate_bmi(weight,height)
     st.write(f"Your BMI is:, **{bmi:.2f}**")
   
     if  bmi < 18.5:
        st.warning( "you are underweight. Improve your nutrition and exercise regularly.")
     elif 18.5 <= bmi < 25:
        st.success (" you are normal. keep being fit and eating healthy.")
     elif 25 <= bmi <30:
        st.info( "you are overweight. give attention to your diet and improve your exercise and rest.")
     else:
        st.error( "you are obese. please consult a nutritionist and physical therapist.")

 


# In[ ]:





# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




