import streamlit as st
import duckdb
import pandas as pd
import os
from visualisations.kpi1_score_parent_edu import plot_kpi1
from visualisations.kpi2_corr_study_score import plot_kpi2
from visualisations.kpi3_score_diet import plot_kpi3
from visualisations.kpi4_score_extra import plot_kpi4

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("Student Habits & Performance Dashboard")

# Initialisation de la DB
con = duckdb.connect(database=':memory:')

DATA_PATH = os.path.join("DATA_PROJET", "student_habits_performance.csv")

def upload_and_store():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        con.execute("DROP TABLE IF EXISTS etudiants")
        con.execute("CREATE TABLE etudiants AS SELECT * FROM df")
        st.success("Données chargées automatiquement depuis DATA_PROJET !")
        return True
    else:
        st.error("Fichier introuvable dans DATA_PROJET. Veuillez vérifier le chemin.")
        return False

def show_filters():
    with st.sidebar:
        st.header("Filtres")
        genders = con.execute("SELECT DISTINCT gender FROM etudiants").fetchall()
        jobs = con.execute("SELECT DISTINCT part_time_job FROM etudiants").fetchall()
        education_levels = con.execute("SELECT DISTINCT parental_education_level FROM etudiants").fetchall()

        selected_gender = st.selectbox("Genre", [g[0] for g in genders] + ["All"])
        selected_job = st.selectbox("Job etudiant", [j[0] for j in jobs] + ["All"])
        selected_edu = st.selectbox("parental education level", [e[0] for e in education_levels] + ["All"])

    filters = []
    if selected_gender != "All":
        filters.append(f"gender = '{selected_gender}'")
    if selected_job != "All":
        filters.append(f"part_time_job = '{selected_job}'")
    if selected_edu != "All":
        filters.append(f"parental_education_level = '{selected_edu}'")

    where_clause = " AND ".join(filters)
    return where_clause

if upload_and_store():
    where = show_filters()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Score moyen par niveau d'éducation parentale")
        st.altair_chart(plot_kpi1(con, where), use_container_width=True)

    with col2:
        st.subheader("Corrélation : Heures d'étude vs Score")
        st.altair_chart(plot_kpi2(con, where), use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Score moyen par qualité de régime")
        st.altair_chart(plot_kpi3(con, where), use_container_width=True)

    with col4:
        st.subheader("Impact des activités extrascolaires")
        st.altair_chart(plot_kpi4(con, where), use_container_width=True)
else:
    st.info("Veuillez placer le fichier CSV dans le dossier 'DATA_PROJET' pour commencer.")
