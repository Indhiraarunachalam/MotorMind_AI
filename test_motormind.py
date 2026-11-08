
from alert_history import create_alert
from maintenance_agent import run_maintenance_agent


def test_normal_alert():
    alert = create_alert("NORMAL", 40, 1.5, 0.05)

    assert alert["Severity"] == "Normal"
    assert "Time" in alert
    print("PASS: Normal condition alert")


def test_overheating_alert():
    alert = create_alert("OVERHEATING", 85, 1.5, 0.05)

    assert alert["Severity"] == "High"
    assert "temperature" in alert["Message"].lower()
    print("PASS: Overheating alert")


def test_overload_alert():
    alert = create_alert("OVERLOAD", 50, 4.0, 0.05)

    assert alert["Severity"] == "High"
    assert "current" in alert["Message"].lower()
    print("PASS: Overload alert")


def test_vibration_alert():
    alert = create_alert(
        "ABNORMAL VIBRATION", 40, 1.5, 0.5
    )

    assert alert["Severity"] == "Medium"
    assert "vibration" in alert["Message"].lower()
    print("PASS: Abnormal vibration alert")


def test_maintenance_assistant():
    report = run_maintenance_agent("OVERHEATING")

    assert report["predicted_fault"] == "OVERHEATING"
    assert len(report["possible_causes"]) > 0
    assert len(report["recommended_actions"]) > 0
    print("PASS: Maintenance assistant")


if __name__ == "__main__":
    test_normal_alert()
    test_overheating_alert()
    test_overload_alert()
    test_vibration_alert()
    test_maintenance_assistant()

    print("\nAll MotorMind AI tests passed!")
