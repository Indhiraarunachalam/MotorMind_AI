
from datetime import datetime


def create_alert(prediction, temperature, current, vibration):
    """Create an alert when a possible motor fault is predicted."""

    if prediction == "NORMAL":
        severity = "Normal"
        message = "No abnormal condition detected in this simulation."

    elif prediction == "OVERHEATING":
        severity = "High"
        message = (
            f"High temperature detected: {temperature} °C. "
            "Check cooling and ventilation."
        )

    elif prediction == "OVERLOAD":
        severity = "High"
        message = (
            f"High current detected: {current} A. "
            "Check the motor load and current sensor."
        )

    elif prediction == "ABNORMAL VIBRATION":
        severity = "Medium"
        message = (
            f"Abnormal vibration detected: {vibration} g. "
            "Check sensor mounting and arrange a mechanical inspection."
        )

    else:
        severity = "Unknown"
        message = "Unrecognised prediction. Check the model output."

    return {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Prediction": prediction,
        "Severity": severity,
        "Message": message
    }
