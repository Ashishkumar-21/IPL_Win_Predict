import streamlit as st
import pandas as pd
import pickle
from streamlit import runtime
runtime.exists()

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Gujarat Titans',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Rajkot', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
       'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai', 'Cape Town',
       'Port Elizabeth', 'Durban', 'Centurion', 'East London',
       'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
       'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali',
       'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL Wi Predictor')


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Seclect the Batting team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Seclet the bowling team',sorted(teams))

selected_city = st.selectbox('Seclet host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Over Completed')
with col5:
    wickets = st.number_input('Wickets over')

if st.button('Predicted Probablity'):
    runs_left = target-score
    balls_left = 120 - (overs*6)
    Wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/(balls_left)

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
