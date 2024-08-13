import streamlit as st
import pickle


vectortest = pickle.load(open('Notebook/vector.pkl','rb'))
modeltest = pickle.load(open('Notebook/model2.pkl','rb'))

st.set_page_config(page_title="Email Spam Classifier")


st.markdown("<h1 style='text-align: center;'>Dr Harisingh Gour University</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Sagar, Madhya Pradesh, 470003</p>",unsafe_allow_html=True) 

logo_path = "logo/new-logo.png"

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(logo_path, width=250)

st.markdown("<p style='text-align: center;'><br>MCA<br><br><br><br></p>",unsafe_allow_html=True)


st.header("Email Spam Classifier")

input_sms = st.text_area("Enter your email message here and identify is it Spam or Ham")

if st.button('Predict'):

    # 1. vectorize
    vector_input = vectortest.transform([input_sms])
    # 2. predict
    result = modeltest.predict(vector_input)[0]
    # 3. Display Result
    if result == "spam":
        st.header("Spam")
    else:
        st.header("Not Spam")

st.markdown("<p style='text-align: right;'>by :- SYED REHAN GOHAR</p>", unsafe_allow_html=True)

