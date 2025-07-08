import altair as alt
import pandas as pd

def plot_kpi4(con, where_clause):
    query = """
        SELECT extracurricular_activities, AVG(exam_score) AS avg_score
        FROM students
        {where_clause}
        GROUP BY extracurricular_activities
        ORDER BY avg_score DESC
    """
    if where_clause:
        query = query.replace("{where_clause}", f"WHERE {where_clause}")
    else:
        query = query.replace("{where_clause}", "")

    df = con.execute(query).fetchdf()

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("extracurricular_activities:N", title="Activités extrascolaires"),
        y=alt.Y("avg_score:Q", title="Score moyen"),
        color=alt.Color("avg_score:Q", scale=alt.Scale(scheme="purples"), legend=None)
    ).properties(height=300)

    return chart
