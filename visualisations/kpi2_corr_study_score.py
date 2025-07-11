import altair as alt
import pandas as pd

def plot_kpi2(con, where_clause):
    # ✅ Correction 1 : bon nom de colonne + bon nom de table (etudiants)
    base_query = "SELECT study_hours_per_day, exam_score FROM etudiants {where_clause}"
    
    if where_clause:
        base_query = base_query.replace("{where_clause}", f"WHERE {where_clause}")
    else:
        base_query = base_query.replace("{where_clause}", "")

    df = con.execute(base_query).fetchdf()

    # ✅ Correction 2 : utiliser les bons noms de colonnes dans Altair
    chart = alt.Chart(df).mark_circle(size=60, opacity=0.6).encode(
        x=alt.X("study_hours_per_day:Q", title="Heures d'étude par jour"),
        y=alt.Y("exam_score:Q", title="Score à l'examen"),
        tooltip=["study_hours_per_day", "exam_score"],
        color=alt.value("#4e79a7")
    ).properties(height=300)

    return chart
