import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    st.info("                              ")
    a = st.number_input("Please input Number")
   
    st.info("                              ")
    st.write("Enter Caculation type :")
    st.write("1) sin \u03B8 ")
    st.write("2) cos \u03B8")
    st.write("3) tan \u03B8")
    st.write("4) cosec \u03B8")
    st.write("5) sec \u03B8")
    st.write("6) cot \u03B8")
    
    cal = st.number_input("") 
    st.info("                              ")
    
    if cal==1:
        st.write("Value of Sin " ,a, " is ", math.sin(a))
    elif cal==2:
        st.write("Value of Cos " ,a, " is ", math.cos(a))
    elif cal==3:
        st.write("Value of Tan " ,a, " is ", math.tan(a))
    elif cal==4:
        st.write("Value of Cosec " ,a, " is ", math.asin(a))
    elif cal==5:
        st.write("Value of Sec " ,a, " is ", math.acos(a))
    elif cal==6:
        st.write("Value of Cot " ,a, " is ", math.atan(a))
    else:
        st.write(" INVALID  !")
