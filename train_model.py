
import random
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# Make the experiment reproducible
random.seed(42)

print("====================================")
print("       MotorMind AI - ML Model")
print("====================================")

# Generate simulated training data
data = []
labels = []

for _ in range(1000):
    scenario = random.choice([
        "NORMAL",
        "OVERHEATING",
        "OVERLOAD",
        "ABNORMAL VIBRATION"
    ])

    if scenario == "NORMAL":
        temperature = random.uniform(30, 45)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1400, 1500)

    elif scenario == "OVERHEATING":
        temperature = random.uniform(75, 95)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1400, 1500)

    elif scenario == "OVERLOAD":
        temperature = random.uniform(40, 60)
        current = random.uniform(3.0, 5.0)
        vibration = random.uniform(0.01, 0.10)
        rpm = random.randint(1300, 1450)

    else:
        temperature = random.uniform(30, 50)
        current = random.uniform(1.0, 2.0)
        vibration = random.uniform(0.30, 0.80)
        rpm = random.randint(1350, 1500)

    data.append([
        temperature,
        current,
        vibration,
        rpm
    ])

    labels.append(scenario)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

# Create and train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\nModel training completed!")
print(f"Test accuracy on simulated data: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save the trained model
joblib.dump(model, "motor_fault_model.pkl")

print("Model saved as motor_fault_model.pkl")
