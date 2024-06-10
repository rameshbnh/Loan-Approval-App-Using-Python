import streamlit as st
st.title('Loan approval app')
st.write('Welcome to check your eligibility for loan')

c=st.number_input('Enter your credit score')
s=st.number_input('Enter your Salary')
st.button('Check')

if 50000<=s<=150000 and 500<=c<=650:
    st.write('Congratulations you are eligible for loan but with higher interest rate of 7.5%')
elif s>150000 and c>650:
    st.write('Congratulations you are eligible for loan with interest rate of 5.5%')
else:
    st.write('sorry you are not eligible')