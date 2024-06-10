import streamlit as st

def loan_eligibility():
    st.title("Loan Eligibility and Interest Rate Calculator")
    st.sidebar.title("User Input")

    # Sidebar - User Input
    loan_amount = st.sidebar.number_input("Loan Amount (Rs)", min_value=1000, max_value=1000000, step=1000)
    Salary = st.sidebar.slider("Salary", min_value=10000,max_value=100000, step=10000)
    loan_term = st.sidebar.selectbox("Loan Term (years)", options=[1, 3, 5, 10, 15, 20, 25, 30])

    # Main panel
    st.subheader("Loan Details")

    # Calculate loan eligibility based on credit score
    if Salary >= 500000:
        st.write("Congratulations! You are eligible for the loan.")
        interest_rate = 5.0  # example interest rate for high credit score
    elif 100000 <= Salary < 500000:
        st.write("You are eligible for the loan, but with a higher interest rate.")
        interest_rate = 7.5  # example interest rate for medium credit score
    else:
        st.write("Sorry, you are not eligible for the loan.")
        return

    # Calculate monthly payment
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_payments)

    st.write(f"Interest Rate: {interest_rate}%")
    st.write(f"Monthly Payment: Rs {monthly_payment:.2f}")

if __name__ == "__main__":
    loan_eligibility()
