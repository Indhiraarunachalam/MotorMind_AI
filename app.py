
import random
import joblib
import pandas as pd
import streamlit as st
from datetime import datetime

from maintenance_agent import run_maintenance_agent
from alert_history import create_alert


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="MotorMind AI",
    page_icon="⚙️",
    layout="wide"
)


# -------------------------------
# LOAD MACHINE LEARNING MODEL
# -------------------------------

try:
    model = joblib.load("motor_fault_model.pkl")
except FileNotFoundError:
    st.error("Model file not found. Please run train_model.py first.")
    st.stop()


# -------------------------------
# SIMULATE MOTOR SENSOR READINGS
# -------------------------------

def generate_readings(scenario):

    if scenario == "Normal":
        temperature = random.uniform(30, 45)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1400, 1500)

    elif scenario == "Overheating":
        temperature = random.uniform(75, 95)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1400, 1500)

    elif scenario == "Overload":
        temperature = random.uniform(40, 60)
        current = random.uniform(3.0, 5.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1300, 1450)

    else:
        temperature = random.uniform(30, 50)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.30, 0.80)
        rpm = random.randint(1350, 1500)

    return {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Temperature": round(temperature, 2),
        "Current": round(current, 2),
        "Vibration": round(vibration, 3),
        "RPM": rpm
    }


# -------------------------------
# SESSION HISTORY
# -------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "alerts" not in st.session_state:
    st.session_state.alerts = []


# -------------------------------
# DASHBOARD HEADER
# -------------------------------

st.title("⚙️ MotorMind AI")

st.subheader(
    "AI-Powered Motor Health Monitoring "
    "and Maintenance Assistant"
)

st.info(
    "Educational simulation: sensor readings and ML training "
    "data are synthetic. No physical motor is connected."
)


# -------------------------------
# SCENARIO SELECTION
# -------------------------------

scenario = st.selectbox(
    "Select a motor test scenario",
    [
        "Normal",
        "Overheating",
        "Overload",
        "Abnormal Vibration"
    ]
)


# -------------------------------
# GENERATE READING AND PREDICT
# -------------------------------

if st.button("Generate Reading & Predict", type="primary"):

    reading = generate_readings(scenario)

    features = [[
        reading["Temperature"],
        reading["Current"],
        reading["Vibration"],
        reading["RPM"]
    ]]

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]
    confidence = max(probabilities) * 100

    reading["Prediction"] = prediction
    reading["Confidence"] = round(confidence, 2)

    # Save prediction history
    st.session_state.history.append(reading)
    st.session_state.history = st.session_state.history[-30:]

    # Create an alert for the predicted condition
    alert = create_alert(
        prediction,
        reading["Temperature"],
        reading["Current"],
        reading["Vibration"]
    )

    # Store fault alerts only
    if prediction != "NORMAL":
        st.session_state.alerts.append(alert)
        st.session_state.alerts = st.session_state.alerts[-50:]


# -------------------------------
# DISPLAY RESULTS
# -------------------------------

if st.session_state.history:

    latest = st.session_state.history[-1]

    st.divider()
    st.subheader("📊 Motor Sensor Readings")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f'{latest["Temperature"]} °C'
    )

    col2.metric(
        "Current",
        f'{latest["Current"]} A'
    )

    col3.metric(
        "Vibration",
        f'{latest["Vibration"]} g'
    )

    col4.metric(
        "Motor Speed",
        f'{latest["RPM"]} RPM'
    )


    # -------------------------------
    # ML PREDICTION
    # -------------------------------

    st.divider()
    st.subheader("🤖 Machine Learning Fault Prediction")

    if latest["Prediction"] == "NORMAL":
        st.success("Predicted Condition: NORMAL")
    else:
        st.error(
            f'Possible Condition: {latest["Prediction"]}'
        )

    st.metric(
        "Model Confidence",
        f'{latest["Confidence"]:.2f}%'
    )

    st.caption(
        "Confidence is the model's estimated probability. "
        "It does not guarantee real-world accuracy."
    )


    # -------------------------------
    # MAINTENANCE ASSISTANT
    # -------------------------------

    st.divider()
    st.subheader("🛠️ MotorMind AI Maintenance Assistant")

    report = run_maintenance_agent(latest["Prediction"])

    st.write(
        "**Predicted Condition:**",
        report["predicted_fault"]
    )

    st.write(
        "**Inspection Priority:**",
        report["priority"]
    )

    st.write("**Possible Causes:**")

    for cause in report["possible_causes"]:
        st.write(f"- {cause}")

    st.write("**Recommended Actions:**")

    for action in report["recommended_actions"]:
        st.write(f"- {action}")

    st.caption(
        "Maintenance suggestions are general guidance based on "
        "simulated predictions, not a confirmed diagnosis."
    )


    # -------------------------------
    # SENSOR HISTORY CHARTS
    # -------------------------------

    df = pd.DataFrame(st.session_state.history)

    st.divider()
    st.subheader("📈 Sensor History")

    st.write("Temperature (°C)")
    st.line_chart(
        df.set_index("Time")[["Temperature"]]
    )

    st.write("Current (A)")
    st.line_chart(
        df.set_index("Time")[["Current"]]
    )

    st.write("Vibration (g)")
    st.line_chart(
        df.set_index("Time")[["Vibration"]]
    )

    st.write("Motor Speed (RPM)")
    st.line_chart(
        df.set_index("Time")[["RPM"]]
    )


    # -------------------------------
    # PREDICTION HISTORY TABLE
    # -------------------------------

    st.divider()
    st.subheader("📋 Recent Prediction History")

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )

    st.download_button(
        label="Download Prediction History (CSV)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="motormind_predictions.csv",
        mime="text/csv"
    )


    # -------------------------------
    # FAULT ALERT HISTORY
    # -------------------------------

    st.divider()
    st.subheader("🚨 Motor Fault Alert History")

    if st.session_state.alerts:

        alert_df = pd.DataFrame(st.session_state.alerts)

        st.dataframe(
            alert_df,
            use_container_width=True
        )

        st.download_button(
            label="Download Alert History (CSV)",
            data=alert_df.to_csv(index=False).encode("utf-8"),
            file_name="motormind_alerts.csv",
            mime="text/csv"
        )

    else:
        st.success(
            "No fault alerts generated in this session."
        )

else:
    st.warning(
        "Select a scenario and click "
        "'Generate Reading & Predict' to start."
    )


# -------------------------------
# FOOTER
# -------------------------------

st.divider()

st.caption(
    "MotorMind AI | Educational prototype using synthetic data. "
    "Not validated for real motor diagnosis or automatic protection."
)
