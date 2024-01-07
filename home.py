import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings

st.markdown('<h2 style="color: maroon; text-align:center; background-color: #AEF359; font-family:Verdana; border: 3px black dashed ; border-radius:5px; margin-bottom: 20px; ">SPOTIFY SONGS DATA ANALYSIS AND VISUALIZATION</h2>', unsafe_allow_html=True)

st.markdown('''<p style="font-weight:bold; font-size: 20px; font-family:Cursive"> Imagine having access to a never-ending jukebox filled with millions
             of songs, podcasts, and playlists tailored just for you. Welcome to Spotify,
             the magical realm where music meets technology. It's your passport to a world 
            of tunes that can whisk you away to far-off places, stir your emotions,
             and keep you grooving through the highs and lows of life. With Spotify, 
            you're not just listening; you're embarking on a sonic adventure where your 
            favorite melodies are just a click away. </p>''', unsafe_allow_html=True)
st.image('Assets/Presentation1.jpg', use_column_width=True)

st.markdown('<h2 style="color: maroon; text-align:center; background-color: #AEF359; font-family:monospace; border: 3px solid black; border-radius:5px; margin-bottom: 20px; ">ABOUT THE PROJECT</h2>', unsafe_allow_html=True)
st.markdown('''<p style="font-weight:bold; font-size: 20px; font-family:Cursive">🎵Spotify is Swedish audio streaming and media services provider founded in April 2006.
            🎵 Here, We'll exploring and quantify data about music and drawing valuable insights.
            🎵 Perform an exploratory data analysis and data visualization project using data from spotify using python.
            🎵 Includes data collection script that scrapes audio features data from spotify.
            🎵 Problems skills. once the dataset has been analysed learners will opportunity to reorganise and restructure data to help them ans their question. </p>''', unsafe_allow_html=True)


st.markdown('<h2 style="color: maroon; text-align:center; background-color: #AEF359; font-family:Verdana; border: 3px solid black; border-radius:5px; margin-bottom: 20px; ">ABOUT THE DATASET</h2>', unsafe_allow_html=True)
st.markdown('''<p style="font-weight:bold; font-size: 20px; font-family:Cursive">The Spotify dataset provides insight into users
            data about whic songs they listen to, and not just the popularity of tracks they have in their libarary 
            recorded in their database.I plan on analysing user's listening profile to enable Spotify to suggest
            similar tracks on their platform to improve user experience.😊 </p>''', unsafe_allow_html=True)