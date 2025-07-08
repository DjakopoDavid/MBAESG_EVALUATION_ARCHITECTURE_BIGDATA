import altair as alt
import pandas as pd

def plot_kpi1(con, where_clause):
    query = open("queries/kpi1_avg_score_by_parent_edu.sql").read()
    if where_clause:
        query = query.replace("{where_clause}", f"WHERE {where_clause}")
    else:
        query = query.replace("{where_clause}", "")

    df = con.execute(query).fetchdf()

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("avg_score:Q", title="Score moyen"),
        y=alt.Y("parental_education_level:N", sort='-x', title="Niveau d'éducation des parents"),
        color=alt.Color("avg_score:Q", scale=alt.Scale(scheme="blues"), legend=None)
    ).properties(height=300)

    return chart
