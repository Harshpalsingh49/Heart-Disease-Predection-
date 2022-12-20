from email import header
import numpy as np
from pandas import options
import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
scal=StandardScaler()
#from keras.models import load_model

header = st.container()
dataset = st.container()
# features = st.container()
# model_training = st.container()

# Loading pickled file.
with open(r'C:\Users\Harshpalsingh\Desktop\Heartapp.pkl','rb') as f:
      model = pickle.load(f)

def predict(age,sex,cp,oldpeak,thal,restecg,slope,exang,ca):
    
    if sex=="male":
        sex=1 
    else: sex=0
    
    
    if cp=="Typical angina":
        cp=0
    elif cp=="Atypical angina":
        cp=1
    elif cp=="Non-anginal pain":
        cp=2
    elif cp=="Asymptomatic":
        cp=2
    
    if exang=="Yes":
        exang=1
    elif exang=="No":
        exang=0

 
    if slope=="Upsloping: better heart rate with excercise(uncommon)":
        slope=0
    elif slope=="Flatsloping: minimal change(typical healthy heart)":
          slope=1
    elif slope=="Downsloping: signs of unhealthy heart":
        slope=2  
 
    if thal=="fixed defect: used to be defect but ok now":
        thal=6
    elif thal=="reversable defect: no proper blood movement when excercising":
        thal=7
    elif thal=="normal":
        thal=2.31

    if restecg=="Nothing to note":
        restecg=0
    elif restecg=="ST-T Wave abnormality":
        restecg=1
    elif restecg=="Possible or definite left ventricular hypertrophy":
        restecg=2
 
    user_input=[age,sex,cp,oldpeak,thal,restecg,slope,exang,ca]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    user_input=scal.fit_transform(user_input)
    prediction = model.predict(user_input)

    return prediction


with header:
    #Setting Title of App
    st.title("Heart Disease Prediction.")
    st.text("Predict if a person is having heart disease or not by letting them input a data.")
    
with dataset:
    def main():
        st.header("Data Input.")
        st.text("This data is used to predict.")
        html_temp = """
        <style>
            .reportview-container .main .block-container{{
                max-width: 90%;
                padding-top: 5rem;
                padding-right: 5rem;
                padding-left: 5rem;
                padding-bottom: 5rem;
            }}
            img{{
                max-width:40%;
                margin-bottom:40px;
            }}
        </style>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        
        age=st.number_input("Age",min_value=1, max_value=121,step=1, )
        sex = st.radio("Select Gender: ", ('male', 'female'))
        cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic"))
#trestbps=st.selectbox('Resting Blood Sugar',range(1,500,1))
        restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
#chol=st.selectbox('Serum Cholestoral in mg/dl',range(1,1000,1))
#fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
#thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
        exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
        oldpeak=st.number_input(label='oldpeak',step=1.,format="%.2f")
        slope = st.selectbox('Heart Rate Slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
        ca=st.selectbox('Number of Major Vessels Colored by Flourosopy',range(0,5,1))
        thal=st.selectbox('Thalium Stress Result',range(1,8,1))

        pred=predict(age,sex,cp,oldpeak,thal,restecg,slope,exang,ca)
        
        #result=""
        
        if st.button("Predict"):    
            if pred == 1:
                st.success('Warning! You have high risk of getting a heart attack!')
    
        else:
            st.success('You have lower risk of getting a heart disease!')
    

if __name__=='__main__':
    main()
