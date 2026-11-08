
def detect_motor_fault(temperature, current, vibration):
    if temperature > 70:
        return "OVERHEATING", "Warning: Motor temperature is too high!"

    elif current > 3.0:
        return "OVERLOAD", "Warning: Motor current is too high!"

    elif vibration > 0.20:
        return "ABNORMAL VIBRATION", "Warning: Unusual motor vibration detected!"

    else:
        return "NORMAL", "Motor readings appear normal."


# Test the fault detection function
print("================================")
print("       MotorMind AI")
print("    Automatic Fault Detection")
print("================================")

temperature = float(input("Enter temperature (°C): "))
current = float(input("Enter current (A): "))
vibration = float(input("Enter vibration (g): "))

condition, message = detect_motor_fault(
    temperature, current, vibration
)

print("\n--- Fault Detection Result ---")
print("Temperature:", temperature, "°C")
print("Current:", current, "A")
print("Vibration:", vibration, "g")
print("Detected Condition:", condition)
print("Message:", message)
