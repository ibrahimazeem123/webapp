import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#  Setting the title of the page
st.title("*Exploratory Data Analysis*")

#  Importing the dataset

with st.sidebar.header("Upload your data (.csv)"):
    uploaded_file= st.sidebar.file_uploader("upload your file",type=['csv'])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)")

#  Profiling report for pandas
    
if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv=pd.read_csv(uploaded_file)
            return csv
        df=load_csv()
        pr=ProfileReport(df,explorative=True)
        st.header("Input df")
        st.write(df) 
        st.write('---')
        st.header("*Profiling report with pandas*")
        st_profile_report(pr)
else:
    st.info("Kindly upload your csv file")
    if st.button('Press to use example data'):
            @st.cache
            def load_data():
                a=pd.DataFrame(np.random.rand(100,5),
                       columns=['age','weight','height','state','code'])
                return a

            df=load_data()
            pr=ProfileReport(df,explorative=True)
            st.header("Input df")
            st.write(df)
            st.write('---')
            st.header("*Profiling report with pandas*")
            st_profile_report(pr)