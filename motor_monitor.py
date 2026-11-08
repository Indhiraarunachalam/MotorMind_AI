
import random
import time
from datetime import datetime


def generate_sensor_readings():
    scenario = random.choice([
        "Normal",
        "Normal",
        "Overheating",
        "Overload",
        "Abnormal Vibration"
    ])

    if scenario == "Normal":
        temperature = round(random.uniform(30, 45), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1400, 1500)

    elif scenario == "Overheating":
        temperature = round(random.uniform(75, 95), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1400, 1500)

    elif scenario == "Overload":
        temperature = round(random.uniform(40, 60), 2)
        current = round(random.uniform(3.0, 5.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1300, 1450)

    else:
        temperature = round(random.uniform(30, 50), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.30, 0.80), 3)
        rpm = random.randint(1350, 1500)

    return temperature, current, vibration, rpm


def detect_motor_fault(temperature, current, vibration):
    if temperature > 70:
        return "OVERHEATING"

    elif current > 3.0:
        return "OVERLOAD"

    elif vibration > 0.20:
        return "ABNORMAL VIBRATION"

    else:
        return "NORMAL"


print("======================================")
print("            MotorMind AI")
print("      Real-Time Motor Simulation")
print("======================================")
print("Press Ctrl+C to stop the program.")

try:
    while True:
        temperature, current, vibration, rpm = (
            generate_sensor_readings()
        )

        condition = detect_motor_fault(
            temperature, current, vibration
        )

        print("\nTime:", datetime.now().strftime("%H:%M:%S"))
        print("--------------------------------------")
        print(f"Temperature : {temperature} °C")
        print(f"Current     : {current} A")
        print(f"Vibration   : {vibration} g")
        print(f"Speed       : {rpm} RPM")
        print("--------------------------------------")

        if condition == "NORMAL":
            print("Status: NORMAL")
        else:
            print("ALERT:", condition, "detected!")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nMotorMind AI simulation stopped.")
