import streamlit as st
import pandas as pd
import mysql.connector

def app():
    conn = mysql.connector.connect( host="192.168.12.150",
                                    port="3306",
                                    user="root",
                                    passwd="",
                                    db="cubedb"
                                  )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms LIMIT 1,300")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['room_name',
                                     'room_status']
                      )
    df.to_csv("jantungg.csv")
    df = pd.read_csv('jantungg.csv')
    df.drop('Unnamed: 0', axis='columns', inplace=True)
    df['age']= df['age'].astype(int)

    st.subheader("Data diambil dari kaggle :")

    shwdata = st.multiselect('Pilih Kolom yang mau ditampilkan:', df.columns, default=[])
    st.write(df[shwdata])

   # st.text('F. Kyriakos)
