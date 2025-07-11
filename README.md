## Projet de Groupe 7 – Analyse des Habitudes Étudiantes et Performance Académique

##  Objectif du Projet

Développer une application web interactive avec *Streamlit* qui :

- Permet le *téléversement d’un fichier CSV* sur les habitudes des étudiants.
- Stocke et interroge les données via *DuckDB*.
- Affiche *4 KPIs* (indicateurs clés de performance) avec *visualisations* interactives.
- Offre des *filtres dynamiques* pour explorer les résultats par genre, réseau social, alimentation, ou participation extrascolaire.

##  Technologies Utilisées

- *Python 3.11*
- *DuckDB* pour le moteur de requête SQL léger
- *Streamlit* pour l’interface utilisateur
- *Pandas* pour la manipulation des données
- *Altair / Plotly  pour les visualisations
- *GitHub* pour la gestion du code en équipe

---
##  Jeu de Données

- *Nom* : Student Habits vs Academic Performance
- *Source* : [Kaggle](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)
- *Colonnes principales* :
  - gender
  - study_hours
  - social_media_hours
  - diet_quality
  - mental_health_rating
  - exam_score
  - extracurricular_participation

---

## Fonctionnalités de l’Application

1. *Import de CSV*  
   Interface conviviale pour uploader le fichier Student_Habits.csv.

2. *Base de données DuckDB*  
   - Création automatique de la base à chaque chargement.
   - Nettoyage et normalisation des colonnes.

3. *Visualisation des 4 KPIs*

   | KPI                                                |        Description                                                    |Visualisation    |
   |----------------------------------------------------|-----------------------------------------------------------------------|-----------------|
   | Score moyen par niveau d'éducation parentale*      |  Évaluer l'influence du niveau scolaire des parents sur les résultats | BarChart        |
   | Corrélation : Heures d'étude vs Score*             |Analyser si plus d'heures d’étude influencent les notes obtenues       | ScatterPlot     |
   | Score moyen par qualité de régime alimentaire*     | Engagement social des étudiants                                       | Pie Chart       |
   | Impact des activités extrascolaires*               | Mesurer l’effet de l'engagement social sur les résultats scolaires    | Boxplot         |

4. *Filtres dynamiques*  
   - Par genre (gender)
   - Par job
   - Par niveau d'étude parental

5. Installation
Cloner le dépôt :
git clone https://github.com/DjakopoDavid/MBAESG_EVALUATION_ARCHITECTURE_BIGDATA

Créer un environnement virtuel :
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows

Installer les dépendances :
pip install -r requirements.txt

Lancer l’application Streamlit :
streamlit run app.py

Répartition des Tâches
Membre	Rôle
Mariska Djomo	Intégration DuckDB, filtres
David Djakopo	Visualisations et indicateurs
Yannick MOKTO	README, support GitHub

✅ Problèmes rencontrés & Solutions
Problème	             Solution
Données manquantes	     Remplacement par médianes ou filtrage
Visualisation vide	     Gestion via if not df.empty:
Mismatch types DuckDB	 Casting des colonnes avant requêtes