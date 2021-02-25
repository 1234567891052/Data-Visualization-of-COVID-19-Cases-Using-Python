import pandas as pd
import plotly_express as px

dataFrame = pd.read_csv('data.csv')

scatterGraph = px.scatter(data_frame=dataFrame,
                          x='date', y='cases', color='country', title='The amount of COVID-19 cases per day in some countries')
lineGraph = px.line(data_frame=dataFrame, x='date', y='cases', color='country',
                    title='The amount of COVID-19 cases per day in some countries')

scatterGraph.show()
lineGraph.show()
