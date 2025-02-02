import streamlit as st
import seaborn as sa 
import numpy as np
import pandas as pd
import matplotlib as mt 


def main():
    st.title("This is first programme")   
    st.sidebar.title("This is side bar")

    uploadfile = st.sidebar.file_uploader("Upload file",type=["csv","xlsx"])

    if uploadfile is not None:
        if uploadfile.name.endswith(".csv"):
           data=  pd.read_csv(uploadfile)
        elif uploadfile.name.endswith(".xlsx"):
          data =  pd.read_excel(uploadfile)
         
        st.subheader("file data")
        st.dataframe(data.head())      


    else:
        print("Ouside Not a valid file")
        
if __name__ == "__main__":
    main()