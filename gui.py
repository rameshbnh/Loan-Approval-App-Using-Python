import streamlit as st
st.title('My first app')
st.snow()
st.write('Hello all')
x=st.radio('Are you working',options=['yes','no'])
if x=='yes':
    st.write('Ok you can take our weekend batch')
else:
    st.write('Ok you can take our weekdays batch')
a=st.text_input('Enter you Branch')
b=st.number_input('Percentage')
c=st.sidebar.checkbox('Test cleared')
if c==True:
    st.sidebar.write('20% off')