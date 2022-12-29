#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:16:07 2022

@author: namnguyen
"""

import streamlit as st
import webbrowser
import base64

# Read the PDF file
with open('file.pdf', 'rb') as f:
    pdf = f.read()

# Write the PDF contents to a temporary HTML file
html = f"""
<html>
<head>
</head>
<body>
<embed src="data:application/pdf;base64,{pdf.encode('base64')}" type="application/pdf" />
</body>
</html>
"""

# Save the HTML file to a temporary location
temp_path = '/tmp/temp.html'
with open(temp_path, 'w') as f:
    f.write(html)

# Open the HTML file in the default web browser
webbrowser.open(temp_path)











