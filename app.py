import streamlit as st
import pickle

model1 = pickle.load(open("height.pkl","rb"))


st.title("Human Weight Prediction APP")
height= st.slider("Height", 0.0,100.0,.10)



if st.button("Submit"):
    pred = model1.predict([[height]])
    st.write("predicted weight is ", pred)
