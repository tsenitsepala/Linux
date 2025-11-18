import streamlit as st
import pandas as pd
import mysql.connector
import altair as alt

db_config = {
    'host': 'localhost',
    'user': 'streamlit',
    'password': 'salasana',
    'database': 'motivaatio'
}

def load_data():
    conn = mysql.connector.connect(**db_config)
    query = "SELECT student_name AS Opiskelija, month AS Kuukausi, motivation_perc AS `Moti%` FROM moti_data;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("Onni Opiskelijan moti 2025")
st.write("huomaa linux-kurssin vaikutus loppuvuonna")

data = load_data()
st.dataframe(data)


chart = alt.Chart(data).mark_line(point=alt.OverlayMarkDef(size=150, filled=True), color='red').encode(
    x='Kuukausi',
    y='Moti%',
    tooltip=['Kuukausi', 'Moti%']
).properties(
    title='Motivaatio 2025'
)

st.altair_chart(chart, use_container_width=True)
