import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    st.info("                              ")
    a = st.number_input("Please input First Number")
    b = st.number_input("Please input Second Number")
    st.info("                              ")
    st.write("Enter Caculation type :")
    st.write("1) Addition ")
    st.write("2) Substraction ")
    st.write("3) Multiplication ")
    st.write("4) Division ")
 
    cal = st.number_input("") 
    st.info("                              ")
    st.text("The result is")
    if cal==1: 
        st.write(a+b)
    elif cal==2:
        if a>b: st.write(a-b)
        else: st.write(b-a)
    elif cal==3:
        st.write(a*b)
    elif cal==4:
        if a>b : st.write(a/b)
        else: st.write(b/a) 
    else:
        st.write(" INVALID  !")