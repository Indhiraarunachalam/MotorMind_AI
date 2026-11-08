
import random

print("================================")
print("          MotorMind AI")
print("     Motor Condition Demo")
print("================================")

print("\nSelect a motor condition:")
print("1. Normal")
print("2. Overheating")
print("3. Overload")
print("4. Abnormal Vibration")
print("5. Exit")

while True:
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        temperature = round(random.uniform(30, 45), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1400, 1500)
        condition = "Normal"

    elif choice == "2":
        temperature = round(random.uniform(75, 95), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1400, 1500)
        condition = "Overheating"

    elif choice == "3":
        temperature = round(random.uniform(40, 60), 2)
        current = round(random.uniform(3.0, 5.0), 2)
        vibration = round(random.uniform(0.01, 0.10), 3)
        rpm = random.randint(1300, 1450)
        condition = "Overload"

    elif choice == "4":
        temperature = round(random.uniform(30, 50), 2)
        current = round(random.uniform(1.0, 2.0), 2)
        vibration = round(random.uniform(0.30, 0.80), 3)
        rpm = random.randint(1350, 1500)
        condition = "Abnormal Vibration"

    elif choice == "5":
        print("MotorMind AI demo closed.")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")
        continue

    print("\n--- Simulated Motor Readings ---")
    print(f"Temperature : {temperature} °C")
    print(f"Current     : {current} A")
    print(f"Vibration   : {vibration} g")
    print(f"Speed       : {rpm} RPM")
    print(f"Selected Scenario: {condition}")
