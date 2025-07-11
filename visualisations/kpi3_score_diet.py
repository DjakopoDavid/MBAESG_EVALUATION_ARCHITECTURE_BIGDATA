import altair as alt
import pandas as pd

def plot_kpi3(con, where_clause):
    query = """
        SELECT diet_quality, AVG(exam_score) AS avg_score
        FROM etudiants
        {where_clause}
        GROUP BY diet_quality
        ORDER BY avg_score DESC
    """
    if where_clause:
        query = query.replace("{where_clause}", f"WHERE {where_clause}")
    else:
        query = query.replace("{where_clause}", "")

    df = con.execute(query).fetchdf()

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("diet_quality:N", title="Qualité de l'alimentation"),
        y=alt.Y("avg_score:Q", title="Score moyen"),
        color=alt.Color("avg_score:Q", scale=alt.Scale(scheme="greens"), legend=None)
    ).properties(height=300)

    return chart
