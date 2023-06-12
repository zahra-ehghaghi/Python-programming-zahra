import  streamlit as st
import  plotly.express as px
import  pandas
import sqlite3

connection = sqlite3.connect("temperature.db")
def read():
    curses = connection.cursor()
    sql =" select * from Temperatures"
    data = curses.execute(sql).fetchall()
    return data


data = read()
temperatures= [row[0]for row in data]
dates= [row[1]for row in data]

figure = px.line(x=dates, y=temperatures,labels={"x":"Date","y":"Temp"})

st.plotly_chart(figure)
