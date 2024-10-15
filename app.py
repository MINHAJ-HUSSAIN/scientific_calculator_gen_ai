# realistic_scientific_calculator_app.py

import streamlit as st
import math

# Initialize session state
if 'current_input' not in st.session_state:
    st.session_state.current_input = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Function Definitions
def calculate(expression):
    try:
        # Replace mathematical functions with math module equivalents
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', 'math.pi')
        expression = expression.replace('e', 'math.e')
        expression = expression.replace('factorial', 'math.factorial')
        
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

# Streamlit App
def main():
    st.set_page_config(page_title="🧮 Scientific Calculator", layout="centered")
    st.title("🧮 Scientific Calculator")

    # Display Area
    st.markdown("""
    <div style="background-color: #F0F0F0; padding: 10px; border-radius: 5px; text-align: right; font-size: 24px;">
        <div>{}</div>
        <div style="font-size: 32px;">{}</div>
    </div>
    """.format(st.session_state.current_input, st.session_state.result), unsafe_allow_html=True)

    # Define button labels
    buttons = [
        ['C', '⌫', '(', ')'],
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '^', '+'],
        ['sin', 'cos', 'tan', '='],
        ['log', 'ln', '√', 'factorial'],
        ['π', 'e']
    ]

    # Create buttons in grid
    for row in buttons:
        cols = st.columns(len(row))
        for idx, label in enumerate(row):
            with cols[idx]:
                if st.button(label):
                    if label == 'C':
                        st.session_state.current_input = ""
                        st.session_state.result = ""
                    elif label == '⌫':
                        st.session_state.current_input = st.session_state.current_input[:-1]
                    elif label == '=':
                        st.session_state.result = calculate(st.session_state.current_input)
                    elif label in ['sin', 'cos', 'tan', 'log', 'ln', '√', 'factorial']:
                        if label == '√':
                            st.session_state.current_input += '√('
                        else:
                            st.session_state.current_input += label + '('
                    elif label in ['π', 'e']:
                        st.session_state.current_input += label
                    else:
                        st.session_state.current_input += label

    # Additional Instructions or About Section
    st.markdown("---")
    st.write("### About")
    st.write("""
    This **Scientific Calculator** is built with [Streamlit](https://streamlit.io/). It supports various mathematical operations, including basic arithmetic, trigonometric functions, logarithms, square roots, exponentiation, and factorials.

    **Features:**
    - User-friendly interface resembling a real calculator.
    - Supports parentheses for complex expressions.
    - Handles scientific functions like sine, cosine, tangent, logarithms, and more.
    - Error handling for invalid inputs.
    """)

if __name__ == "__main__":
        main()
