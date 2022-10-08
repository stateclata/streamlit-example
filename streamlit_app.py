# streamlit_app.py

import streamlit as st
import pandas as pd
import mysql.connector


@st.experimental_singleton
def init_connection():
    conn = mysql.connector.connect(host=’192.168.12.150’, database=’cubedb’, user=’arduino’, password=’1234’)
    cursor = conn.cursor()

    conn = init_connection()
    query = “SELECT * FROM rooms”
    cursor.execute(query)

def main():
    st.title("Cube Rooms")
    
    col1,col2 = st.columns(2)
    
    with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("SQL Code Here")
            submit_code = st.form_submit_button("execute")
            
        #Table
    #Results Layouts
    with col2:
        if submit_code:
            st.info("Query Submitted")
            st.write(raw_code)
    
if __name__ == '__main__':
    main()
    

# Initialize connection.
# Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
 #   return mysql.connector.connect(**st.secrets["mysql"])

#conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
 #   with conn.cursor() as cur:
  #      cur.execute(query)
   #     return cur.fetchall()

#rows = run_query("SELECT * from cubedb.rooms;")

# Print results.
#for row in rows:
 #   st.write(f"{row[0]} has a :{row[1]}:")
