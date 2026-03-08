# Student Score Prediction 📊

## Overview
This is my **first Machine Learning project**, built with Python and scikit-learn.  
The goal is to predict student exam scores based on the number of study hours using **Linear Regression**.

It demonstrates:
- Setting up a Python virtual environment (`ai_env`)
- Installing core AI/ML libraries (NumPy, Pandas, Matplotlib, scikit-learn)
- Organizing datasets and scripts
- Training a regression model
- Visualizing predictions with a regression line

---

## Project Structure
score_prediction/
│
├── score_predict.py   # Main ML script
├── Datasets/
│   └── students_scores.csv        # Dataset file
├── Notebooks/
│   └── student_score_prediction.ipynb (optional Jupyter version)
|
└── README.md                     # Project documentation

---

## Dataset
The dataset contains study hours and corresponding exam scores:

```csv
Hours,Scores
2,22
3,34
4,40
5,50
6,60
7,62
8,70
9,80
10,85

Installation & Setup
Clone the repository:


git clone https://github.com/<your-username>/student-score-prediction.git
cd student-score-prediction
Create and activate a virtual environment:


python -m venv ai_env
ai_env\Scripts\activate   # Windows
Install dependencies:


pip install -r requirements.txt
Usage
Run the script:


python student_score_prediction.py
Expected output:

Code
Predicted score for 8.5 hours of study: ~75.14
A graph will also appear showing:

Blue dots → actual scores

Red line → regression prediction

Results
The model successfully predicts exam scores based on study hours.

Example: For 8.5 hours of study, the predicted score is ~75.14.

Visualization confirms the regression line fits the dataset.

Future Work
Add more datasets with real-world student data.

Experiment with other ML models (Decision Trees, Random Forests).

Convert to a Jupyter Notebook for interactive exploration.

Deploy as a simple web app using Flask or Streamlit.

Author
👩‍💻 Chittaveni Manasa  
B.Tech CSE (3rd Year), aspiring AI Android App Developer