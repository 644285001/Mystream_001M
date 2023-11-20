import streamlit as st

st.title('การทำนายการลาออกของพนักงาน')
st.header('นาย ชินวัฒน์ ภูไชยแสง')
st.subheader('สาขาวิชาวิทยาการข้อมูล')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/Resignation.png')
with col2:
    st.image('./pic/Resignation2.png')

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูลของพนักงาน</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

raw_data=pd.read_csv('./data/Employee.csv')
st.write(raw_data.head(10))


import matplotlib.pyplot as plt
import seaborn as sns

features = ['Education', 'City', 'Gender', 'EverBenched']


for f in features:
    plt.figure()
    ax = sns.countplot(x=f, data=raw_data, hue = 'LeaveOrNot', palette="Set1")

if st.button("show bar chart"):
    st.bar_chart(raw_data)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 
