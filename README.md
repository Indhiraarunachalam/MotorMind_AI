
# ⚙️ MotorMind AI

### AI-Powered Motor Health Monitoring and Maintenance Assistant

## 📌 Project Overview

MotorMind AI is an AI-powered motor health monitoring prototype
that uses simulated sensor readings and machine learning to
identify possible abnormal motor conditions.

The system analyses temperature, current, vibration, and motor
speed readings to predict possible motor faults. It also provides
general maintenance suggestions and records fault alerts.

This project is designed as a software-based educational
prototype without requiring physical motor hardware.

**Important:** All sensor readings and training data are
synthetic. The model has not been validated on real motor data.

## 🎯 Objectives

- Simulate motor sensor readings for different operating conditions.
- Use machine learning to classify possible motor faults.
- Provide maintenance suggestions based on predicted conditions.
- Display sensor history, predictions, and fault alerts.
- Allow users to download prediction and alert records as CSV files.

## ✨ Features

- Interactive Streamlit dashboard.
- Simulated normal and abnormal motor scenarios.
- Random Forest machine learning model.
- Possible fault classification.
- Maintenance recommendation assistant.
- Sensor history charts.
- Prediction history table.
- Fault alert history.
- CSV export for predictions and alerts.
- Automated tests for alert and maintenance functions.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Random Forest Classifier
- Git and GitHub

## 🔍 Monitored Parameters

| Parameter | Unit | Purpose |
|---|---|---|
| Temperature | °C | Identify simulated overheating conditions |
| Current | A | Identify simulated overload conditions |
| Vibration | g | Identify simulated abnormal vibration |
| Motor Speed | RPM | Provide additional simulated motor information |

## 🧠 Possible Fault Categories

1. NORMAL
2. OVERHEATING
3. OVERLOAD
4. ABNORMAL VIBRATION

The predictions indicate possible conditions in the simulation.
They are not confirmed diagnoses of physical motor faults.

## ⚙️ How It Works

1. The user selects a motor test scenario.
2. The simulator generates synthetic sensor readings.
3. The trained Random Forest model predicts a condition.
4. The maintenance assistant retrieves relevant guidance.
5. The dashboard displays sensor values, predictions, and charts.
6. Possible fault alerts are recorded during the current session.
7. Users can download prediction and alert history as CSV files.

## 📁 Project Structure

MotorMind_AI/
│
├── app.py
├── train_model.py
├── motor_fault_model.pkl
├── maintenance_agent.py
├── alert_history.py
├── test_motormind.py
├── sensor_simulator.py
├── sensor_scenarios.py
├── fault_detector.py
├── motor_monitor.py
├── requirements.txt
└── README.md

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Open the project folder

```bash
cd MotorMind_AI
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the machine learning model

```bash
python train_model.py
```

This creates the model file used by the dashboard.

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧪 Run Automated Tests

Run the alert and maintenance assistant tests:

```bash
python test_motormind.py
```

## 📊 Model Information

The prototype uses a Random Forest classifier trained on
synthetic sensor data.

The model's reported performance on synthetic test data does
not establish its accuracy on real motors. Further testing with
real sensor measurements and verified fault labels is required.

## 🔮 Future Enhancements

- Collect and validate real motor sensor datasets.
- Add persistent storage for alert history.
- Introduce sensor failure detection.
- Add live sensor integration.
- Improve model evaluation using real fault data.
- Explore remote notifications and deployment.

## ⚠️ Limitations

- Sensor readings are simulated.
- The training dataset is synthetic.
- Real-world prediction accuracy is not established.
- The prototype does not provide certified motor protection.
- Maintenance recommendations require appropriate technical verification.

## 👩‍💻 Author

Indhira A

Electronics and Communication Engineering

