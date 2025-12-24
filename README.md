# Student Academic Risk Analytics
Educational institutions often identify struggling students too late—after grades have already declined. This project builds a data-driven academic risk analytics model that identifies at-risk students early, explains why they are at risk, and evaluates targeted interventions to improve outcomes.

The system integrates data preprocessing, machine learning, explainability, and deployment-ready APIs to support evidence-based academic decision-making.

## Objectives
At the end of the project, we aim to
- identify students at academic risk using performance, behavioral and socioeconomic data
- explain the key drivers behind academic underperformance
- analyse educational inequality across demogragraphic and access factors
- deploy a REST API for real-time risk scoring

## Dataset Source and Description
The dataset was sourced from Hugging-Face and it includes demographic, academic, socioeconomic and behavioral variables

### Dataset Schema

| Column Name          | Description |
|----------------------|-------------|
| Age                  | Student’s age in years (14–18). |
| Grade                | Grade level (9–12), derived from age. |
| Gender               | Student gender (Female, Male). |
| Race                 | Race/ethnicity (White, Hispanic, Black, Asian, Two-or-more, Other). |
| SES_Quartile         | Socioeconomic status quartile (1 = lowest, 4 = highest). |
| ParentalEducation    | Highest education of parent/guardian (<HS, HS, SomeCollege, Bachelors+). |
| SchoolType           | Type of school attended (Public, Private). |
| Locale               | School location (Suburban, City, Rural, Town). |
| TestScore_Math       | Math achievement score (0–100). |
| TestScore_Reading    | Reading achievement score (0–100). |
| TestScore_Science    | Science achievement score (0–100). |
| GPA                  | Cumulative Grade Point Average on a 0.0–4.0 scale. |
| AttendanceRate       | Fraction of school days attended (0.70–1.00). |
| StudyHours           | Average self-reported homework/study hours per day (0–4). |
| InternetAccess       | Home internet access (1 = yes, 0 = no). |
| Extracurricular      | Participation in clubs/sports (1 = yes, 0 = no). |
| PartTimeJob          | Holds a part-time job (1 = yes, 0 = no). |
| ParentSupport        | Regular parental help with homework (1 = yes, 0 = no). |
| Romantic             | Currently in a romantic relationship (1 = yes, 0 = no). |
| FreeTime             | Amount of free time after school on a scale from 1 (low) to 5 (high). |
| GoOut                | Frequency of going out with friends on a scale from 1 (low) to 5 (high). |


## Methodology
1. EDA & Data Preprocessing
2. Feature Engineering & Scaling
3. Model Training and Performance Tracking
4. Model Evaluation & Selection


## Deployment Architecture
The best-performing model, selected based on evaluation metrics and tracked via MLflow, is deployed as a RESTful API using FastAPI.

- Airflow schedules and manages the ML pipeline
- MLflow tracks experiments, metrics, artifacts, and model versions
- FastAPI serves the selected production model
- Docker ensures consistent deployment across environments
- Grafana supports monitoring and visualization

Sample API Response
```
{
  "risk_score": 0.82,
  "risk_level": "High",
  "top_risk_factors": [
    "Low Attendance",
    "Low Study Hours",
    "Low Parent Support"
  ]
}
```

## Tools & Technologies

Python, Pandas, NumPy, Scikit-learn, MLflow, Apache Airflow, SHAP, FastAPI, Docker, Grafana, Data Visualization, Machine Learning Algorithms, Machine Learning Pipelines


## Repository Structure

- student-academic-risk-analytics/
  - data/
    - raw/
    - processed/
  - notebooks/
    - 01_eda.ipynb
  - src/
    - preprocessing.py
    - features.py
    - train.py
    - evaluate.py
  - api/
    - app.py
  - models/
    - model.pkl
  - requirements.txt
  - Dockerfile
  - README.md