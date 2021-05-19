import streamlit as st
from multiapp import MultiApp
from apps import calculator , Advanced_calculation, Trignometric_Calculation  # import your app modules here

app = MultiApp()

st.markdown("""
# Simple Calculator
""")

st.text("Use Drop Down menu below to navigate between Homepage and Calculator.")

# Add all your application here
app.add_app("Calculator", calculator.app)
app.add_app("Advanced_calculation",Advanced_calculation.app)
app.add_app("Trignometric-Calculation",Trignometric_Calculation.app)
# The main app
app.run()   