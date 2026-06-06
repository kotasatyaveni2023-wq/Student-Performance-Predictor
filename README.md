# Student-Performance-Predictor
# Student Performance Predictor

## Overview

Student Performance Predictor is a Machine Learning web application that predicts a student's final score based on academic and performance-related factors such as attendance, study hours, assignment scores, and internal marks.

The project uses a Linear Regression model trained on student data and provides predictions through a user-friendly web interface built with Flask.

## Features

* Predicts student final scores
* Simple and interactive web interface
* Machine Learning model using Linear Regression
* Real-time prediction based on user input
* Responsive and easy-to-use design

## Technologies Used

* Python
* Flask
* Scikit-Learn
* Pandas
* HTML
* CSS
* Joblib

## Project Structure

Student-Performance-Predictor/

├── app.py

├── train_model.py

├── student_data.csv

├── model.pkl

├── static/

│   └── style.css

└── templates/

```
└── index.html
```

## Input Parameters

* Attendance (%)
* Study Hours
* Assignment Score
* Internal Marks

## Output

* Predicted Final Score of the student

## How It Works

1. Student data is collected and stored in a CSV file.
2. A Linear Regression model is trained using Scikit-Learn.
3. The trained model is saved using Joblib.
4. Flask loads the saved model.
5. Users enter student details through the web interface.
6. The model predicts the final score and displays the result.

## Installation and Usage

### Clone the Repository

git clone https://github.com/kotasatyaveni2023-wq/Student-Performance-Predictor.git

### Navigate to Project Folder

cd Student-Performance-Predictor

### Install Dependencies

pip install flask pandas scikit-learn joblib

### Train the Model

python train_model.py

### Run the Application

python app.py

### Open in Browser

http://127.0.0.1:5000

## Future Enhancements

* Performance category classification
* Interactive charts and analytics
* Improved user interface
* Model accuracy evaluation
* Cloud deployment

## Author

Satyaveni Kota

B.Tech – CSE (AI & DS)

Passionate about Artificial Intelligence, Machine Learning, and Full Stack Development.
.
