#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:15:55 2022
@author: namnguyen
"""
import numpy as np
import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import CARSEC as CS
from zipfile import ZipFile
import tempfile




#%%%%%%%%%%%%%%%%%%
st.subheader('Download Excel Template input')
with open("Input_files/CARSEC_excel.xlsx", "rb") as fp:
	btn = st.download_button(label="Download Excel Template",data=fp,file_name="CARSEC_Excel_Input.xlsx",mime="application/xlsx")
#%%%%%%%%%%%%%%%%%%%	
st.subheader('Upload your own Excel file')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_tables=pd.read_excel(uploaded_file,sheet_name=None)
	for k in _tables:  
		st.write(_tables[k])
#%%%%%%%%%%%%%%%%%%%
st.subheader('Download Muti CARSEC files')

# if uploaded_file is not None:
# 	multi_name_file = tempfile.gettempdir()
# 	#CS.CARSEC_Writer(DB=DB, export_path=name_file)
# 	CS.excel_to_CARSEC(load_path=uploaded_file,export_path=multi_name_file+'/CS_Multi_')	


# Create a temporary directory
temp_dir = tempfile.TemporaryDirectory()

# Print the path to the temporary directory
print(temp_dir.name)

# Write some files to the temporary directory
if uploaded_file is not None:
	CS.excel_to_CARSEC(load_path=uploaded_file,export_path={temp_dir.name}/CS_Multi_)	



# Zip the temporary directory
import shutil
shutil.make_archive(temp_dir.name, 'zip', temp_dir.name)

zip_path = f"{temp_dir.name}.zip"
st.file_downloader("Download zip file", zip_path)
