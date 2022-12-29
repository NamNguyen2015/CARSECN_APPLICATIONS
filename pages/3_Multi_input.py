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
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

#%%# Create a None Database

# =============================================================================
# DB['secc']=str
# DB['unid']=str
# DB['norm']=str
# DB['coef_horm']= float
# DB['coef_arma']= float
# DB['coef_pret']= float
# DB['punt_contorno']=[0:{'punt':1, 'X':0,'Y':0},'punt':2, 'X':2,'Y':0},...] # pandasDataFrame.to_dict('records')
# DB['horm']=float
# DB['contorno_Poligonal']=[0:{'Punto_1':1,'Punto_2':2,'Punto_3':3,'Punto_4':4,...}]
# DB['hc']=[0:{'Punto_Central':5,'Radio':0.3}]
# DB['arma']=float
# DB['punt_armadura']=[0:{'Punto_Inicial':6,'Punto_Final':7,'No_Armadura':10, 'Area':0.000314}]
# DB['LC']=[0:{"Axil":-10, 'monento_X':5, 'monento_Y':2}]
# 
# =============================================================================

#%%# 


st.subheader('Preview data')

st.write('**In this template file we organize our :blue[_dataset_] as an excel file with :blue[6] Speadsheets:**')
st.write("***Properties:*** defines all the coefficients of materials.")
st.write("***Geometries:*** indicates all set-up points")
st.write("***hp:*** shows the points which make the poligonal shape.")
st.write("***hc:*** indicates the central point and the radial of steel which located in that position")
st.write("***Caracteristics:*** defines the area of material's distibuition.")
st.write("***LC:*** Load Case")


input_DB = pd.read_excel(
    r'/app/carsecn_applications/Input_files/CARSEC_excel.xlsx',
    sheet_name=None, header=0, index_col=None)


#Show all tables in excel
list_tables=list(input_DB.keys())
#st.markdown("Data's Preview")
#for k in list_tables:  
 #   st.write(k)
  #  st.write(input_DB[k].head(10))
    
    
# Create the interactive tables

for k in list_tables: 
	df=input_DB[k]
	
	# always check if the key exist in session state: 
	if df not in st.session_state:	
		st.write(k)	
		st.session_state.df=pd.DataFrame(df, columns=df.columns)
		#st.dataframe(df)
		AgGrid(df)
	
		
		# Add a clear button to clear the table data
		if st.button("Clear table - "+str(k), key='unique_button_key' +str(k)):
			 # update dataframe state
			st.session_state.df = pd.DataFrame('',index=range(len(df)), columns=df.columns)
						   
			
			
			
			#['ID','secc','unid','norm','coef_horm','coef_arma','coef_pret','horm','arma'])

		
	
	
    
 

#if 'df_Properties' not in st.session_state:
#	_df = {'ID': ['A', 'B'], 'secc','unid','norm','coef_horm','coef_arma','coef_pret','horm','arma'}
#	st.session_state.df_punt_contorno= pd.DataFrame(_df,columns=['punt', 'X', 'Y'])   
 
#if st.button("Clear table"):
 #   # update dataframe state
#	st.session_state.df_Properties= pd.DataFrame('',index=range(2), columns=['ID','secc','unid','norm','coef_horm','coef_arma','coef_pret','horm','arma'])

#if st.button("Add rows"):
    # update dataframe state
#	additional_rows= pd.DataFrame('',index=range(5), columns=['punt', 'X', 'Y'])
#	st.session_state.df_punt_contorno=pd.concat([st.session_state.df_punt_contorno,additional_rows])
	
#_df=st.session_state.df_punt_contorno.copy()
  
#with st.form('test') as f:
#	response = AgGrid(_df, editable=True, fit_columns_on_grid_load=True,data_return_mode=DataReturnMode.AS_INPUT,update_mode=GridUpdateMode.MODEL_CHANGED,reload_data=False,
 #   wrap_text=True,resizeable=True)
#	st.form_submit_button('Confirm')


#st.session_state.df_punt_contorno=response['data'].dropna(axis='rows', how='any')
#st.write(st.session_state.df_punt_contorno)
#DB['punt_contorno'] = response['data'].dropna(axis='rows', how='any').to_dict('records')   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#Create a multi database where each Database equivalents to one unique ID
 
#ID_list = (input_DB['Properties']['ID'].unique()).tolist()


#multi_DB={}

#for i in ID_list:
  #  multi_DB[i]={}
 
  #  for k in list_tables:
 #       multi_DB[i][k] = input_DB[k][input_DB[k]['ID'] == i]
  #      if k=='Properties':
  #          multi_DB[i]['secc']=multi_DB[i][k]['secc'].tolist()[0]
  #          multi_DB[i]['unid']=multi_DB[i][k]['unid'].tolist()[0]
  #          multi_DB[i]['norm']=multi_DB[i][k]['norm'].tolist()[0]
  #          multi_DB[i]['coef_horm']=multi_DB[i][k]['coef_horm'].tolist()[0]
  #          multi_DB[i]['coef_arma']=multi_DB[i][k]['coef_arma'].tolist()[0]
   #         multi_DB[i]['coef_pret']=multi_DB[i][k]['coef_pret'].tolist()[0]
  #          multi_DB[i]['horm']=multi_DB[i][k]['horm'].tolist()[0]
  #          multi_DB[i]['arma']=multi_DB[i][k]['arma'].tolist()[0]
            
 #       elif k=="Geometries":
  #          multi_DB[i]['punt_contorno']=multi_DB[i][k].iloc[:,1:10].dropna(axis=1).to_dict('record')
            
  #      elif k=="hp":
  #          multi_DB[i]['contorno_Poligonal']=multi_DB[i][k].iloc[:,1:11].dropna(axis=1).to_dict('records')
            
  #      elif k=="hc":
  #          multi_DB[i]['hc']=multi_DB[i][k].iloc[:,1:3].to_dict('record')
            
  #      elif k=="Caracteristicas":
  #          multi_DB[i]['punt_armadura']=multi_DB[i][k].iloc[:,1:10].to_dict('record')
            
  #      elif k=="LC":
   #         multi_DB[i]['LC']=multi_DB[i][k].iloc[:,1:5].to_dict('record')
            
           
#import CARSEC as CS


#CS.CARSEC_Writer(DB=multi_DB['A'], name="CS_Multi")

#def multi_CARSEC_writer(multi_DB,export_path='CS_Multi_'):
#	for i_d in multi_DB:
#		CARSEC_Writer(multi_DB[i_d], export_path=export_path+str(i_d))


            
#def multi_CARSEC_Writer(multi_DB):
#    for i_d in multi_DB:
        
#        CS.CARSEC_Writer(multi_DB[i_d], name='CS_Multi_'+str(i_d))
    
    
#multi_CARSEC_Writer(multi_DB)
        
            
#CS.CARSEC_Writer(DB=DB, export_path="Output_files/Multi_Output")")          
            
            
            
 
