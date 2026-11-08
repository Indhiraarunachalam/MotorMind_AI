
import random
import time

print("================================")
print("       MotorMind AI")
print("   Virtual Motor Simulator")
print("================================")

while True:
    temperature = round(random.uniform(30, 45), 2)
    current = round(random.uniform(1.0, 2.0), 2)
    vibration = round(random.uniform(0.01, 0.10), 3)
    rpm = random.randint(1400, 1500)

    print("\nMotor Sensor Readings")
    print("---------------------")
    print(f"Temperature : {temperature} °C")
    print(f"Current     : {current} A")
    print(f"Vibration   : {vibration} g")
    print(f"Speed       : {rpm} RPM")

    time.sleep(2)


