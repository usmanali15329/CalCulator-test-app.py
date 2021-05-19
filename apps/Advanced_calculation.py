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
    st.write("1) Factorial ")
    st.write("2) Square ")
    st.write("3) Root ")

    cal = st.number_input("") 
    st.info("                              ")
    
    if cal==1:
        a = int(a)
        f1 = 1
        for aa in range(1,a+1,1):
            f1 = f1*aa
        st.write("Factorial of " ,a, " is ",f1 )
    elif cal==2:
        st.write("Square Root of ", a ,"is" ,np.square(int(a)))
    elif cal==3:
        b = st.number_input("Please Enter the Power of Root ")
        c = a ** (1/b)
        st.write("Square Root of is ", c)
    else:
        st.write(" INVALID  !")
