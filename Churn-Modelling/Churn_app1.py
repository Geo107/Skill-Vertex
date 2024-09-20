import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('Churn_Model1.pkl', 'rb'))


def run():
    st.title("Churn Prediction using Machine Learning for Telecom Sector")

    state = st.text_input('State')

    ar_cd = st.text_input('Area Code')

    plan_display = ('Yes', 'No')
    plan_options = list(range(len(plan_display)))
    plan = st.selectbox("International Plan", plan_options, format_func=lambda x: plan_display[x])

    intl_min = st.slider('International Minutes Spent',0.0,20.0,5.0)
    intl_call= st.slider('International Call Attended',0.0,20.0,1.0)
    intl_charge = st.slider('international Charge',0.0,6.0,5.0)        
    

    voice_display = ('No', 'Yes')
    voice_options = list(range(len(voice_display)))
    voice = st.selectbox("Voice Mail Plan", voice_options, format_func=lambda x: voice_display[x])

    vmail = st.number_input("Number of Vmail Messages", value=10)

    ncsc = st.slider('Customer Service Calls',0,10,1)

    def user_input():
        td_min = st.slider('Total Day Minutes Spent',0.0,52.0,5.0)
        td_call = st.slider('Total Day Calls',0,165,5)
        td_charge = st.slider('Total Day Charge',0.00,0.20,0.10)
        eve_min = st.slider('Total Evening Minutes Spent',0.0,365.0,5.0)
        eve_call = st.slider('Total Evening Calls',0,170,5)
        eve_charge = st.slider('Total Evening Charge',0.0,1.0,0.5)
        nyt_min = st.slider('Total Night Minutes Spent',0.0,400.0,5.0)
        nyt_call = st.slider('Total Night Calls',0,175,5)
        nyt_charge = st.slider('Total Night Charge',0.0,2.0,1.2)
        
        data = [   
            td_min,
            td_call,
            td_charge,
            eve_min,
            eve_call,
            eve_charge,
            nyt_min,
            nyt_call,
            nyt_charge,
        ]

        return data
    
    features = [[plan,voice,vmail]]
    second = [[intl_min,intl_call,intl_charge,ncsc]]
    for i in user_input():
        features[0].append(i)
    for i in second[0]:
        features[0].append(i)
    print(features)
    for i in features[0]: print(type(i))

    if st.button("Submit"):
        print(type(features))
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Customer from Area Code: " + ar_cd + " || "
                                 "State: " + state + ' || '
                                                                   'Will not leave'
            )
        else:
            st.success(
                "Customer from Area Code: " + ar_cd + " || "
                                 "State: " + state + ' || '
                                                                   'will leave'
            )


run()
