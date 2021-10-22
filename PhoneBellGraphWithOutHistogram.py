import csv
import plotly.figure_factory as px
import pandas as pd


Name=pd.read_csv('PhoneData.csv')

figure=px.create_distplot([Name['Avg Rating'].tolist()],['Bell Curve'],show_hist=False)

figure.show()
