SELECT
    parental_education_level,
    AVG(exam_score) AS avg_score
FROM
    students
{where_clause}
GROUP BY
    parental_education_level
ORDER BY
    avg_score DESC;