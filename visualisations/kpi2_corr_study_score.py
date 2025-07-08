import altair as alt
import pandas as pd

def plot_kpi2(con, where_clause):
    base_query = "SELECT study_hours, exam_score FROM students {where_clause}"
    if where_clause:
        base_query = base_query.replace("{where_clause}", f"WHERE {where_clause}")
    else:
        base_query = base_query.replace("{where_clause}", "")

    df = con.execute(base_query).fetchdf()

    chart = alt.Chart(df).mark_circle(size=60, opacity=0.6).encode(
        x=alt.X("study_hours:Q", title="Heures d'étude par semaine"),
        y=alt.Y("exam_score:Q", title="Score à l'examen"),
        tooltip=["study_hours", "exam_score"],
        color=alt.value("#4e79a7")
    ).properties(height=300)

    return chart
