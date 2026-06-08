import streamlit as st
import math

# Configure page title and browser tab icon
st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("Web Calculator")
st.write("___")

# Getting numbers and operators
with st.form(key="calculator_form"):
    num1 = st.number_input("Enter the First Number : ", value=0.0, format="%f")
    
    # Dropdown menu to select a mathematical operation-
    operation = st.selectbox(
        "Choose an operation :", 
        ["Addition(+)",
        "Subtraction(-)",
        "Multiplication(*)",
        "Division(/)",
        "Power(**)",
        "Percent(%)",
        "Sin", "Cos"])

    if operation not in ["Cos", "Sin"]:
        num2 = st.number_input("Enter the Second Number : ", value=0.0, format="%f")
    
    # Submit button to perform the calculation
    submit_button = st.form_submit_button(label="Calculator")

# Execute calculation
if submit_button:
    st.write("### Result : ")
    try:
        # Calculate sin ، cos
        if operation == "Sin":
                result = math.sin(math.radians(num1))
                st.success(f"**{num1} = {result}**")
        elif operation == "Cos":
                result = math.cos(math.radians(num1))
                st.success(f"**{num1} = {result}**")
        
        # Handle all other operations
        else:
            match operation:
                case "Addition(+)":
                    result = num1 + num2
                    st.success(f"**{num1} + {num2} = {result}**")

                case "Subtraction(-)":
                    result = num1 - num2
                    st.success(f"**{num1} - {num2} = {result}**")

                case "Multiplication(*)":
                    result = num1 * num2
                    st.success(f"**{num1} * {num2} = {result}**")

                case "Division(/)":
                    result = num1 / num2
                    st.success(f"**{num1} / {num2} = {result}**")
                
                case "Power(**)":
                    result = num1 ** num2
                    st.success(f"**{num1} ** {num2} = {result}**")

                case "Percent(%)":
                    result = num1 % num2
                    st.success(f"**{num1} % {num2} = {result}**")
    
    # Handle any runtime errors (e.g., division by zero)
    except Exception as e:
        st.error(f"Calculated{e}")

