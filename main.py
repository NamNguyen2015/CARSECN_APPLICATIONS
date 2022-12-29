#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:16:07 2022

@author: namnguyen
"""

import streamlit as st
import webbrowser
import base64


st.write("***THIS IS THE MAIN PAGE***")
st.markdown("It is recommended to open this page in Firefox. Otherwise, if you use other webbrowser please click the following link to preview PDF.")
st.markdown("**Preview PDF:** [Manual CARSECN](https://github.com/NamNguyen2015/CARSECN_APPLICATIONS/blob/main/Input_files/carsecn.pdf)")


# Read the PDF file
with open('Input_files/carsecn.pdf', 'rb') as f:
    pdf = f.read()
    
# Encode the PDF file as a base64 string
base64_pdf = base64.b64encode(pdf).decode('utf-8')

# Encode the PDF file as a base64 string
base64_pdf = base64.b64encode(pdf).decode('utf-8')

# Write the PDF contents to a temporary HTML file
html = f"""
<html>
<head>
</head>
<body>
<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" />
</body>
</html>
"""

# Save the HTML file to a temporary location
temp_path = '/tmp/temp.html'
with open(temp_path, 'w') as f:
    f.write(html)

# Open the HTML file in the default web browser
webbrowser.open(temp_path)










