
def get_maintenance_advice(fault):
    """Tool: Return maintenance guidance for a predicted condition."""

    advice = {
        "NORMAL": {
            "level": "Normal",
            "possible_causes": [
                "No abnormal pattern detected in the simulated readings."
            ],
            "recommended_actions": [
                "Continue monitoring sensor readings.",
                "Follow the motor manufacturer's maintenance schedule."
            ]
        },
        "OVERHEATING": {
            "level": "High Priority",
            "possible_causes": [
                "Insufficient ventilation or blocked cooling.",
                "Excessive load or a possible electrical issue."
            ],
            "recommended_actions": [
                "Check cooling airflow and ventilation.",
                "Inspect the motor load and temperature sensor.",
                "If a real motor is overheating, follow site safety procedures "
                "and ask a qualified technician to inspect it."
            ]
        },
        "OVERLOAD": {
            "level": "High Priority",
            "possible_causes": [
                "The motor may be drawing excessive current.",
                "The connected load may be too high.",
                "A supply or mechanical issue may need inspection."
            ],
            "recommended_actions": [
                "Check the connected load and current sensor.",
                "Compare current readings with the motor nameplate rating.",
                "Ask a qualified technician to inspect persistent high current."
            ]
        },
        "ABNORMAL VIBRATION": {
            "level": "Needs Inspection",
            "possible_causes": [
                "Possible mechanical looseness or imbalance.",
                "A bearing or mounting issue may need inspection."
            ],
            "recommended_actions": [
                "Check whether the vibration sensor is mounted securely.",
                "Inspect mounting and mechanical parts safely.",
                "Ask a qualified technician to investigate persistent vibration."
            ]
        }
    }

    return advice.get(
        fault,
        {
            "level": "Unknown",
            "possible_causes": ["The predicted condition is not recognised."],
            "recommended_actions": ["Check the sensor readings and model output."]
        }
    )


def run_maintenance_agent(fault):
    """Agent workflow: use the advice tool and prepare a report."""

    advice = get_maintenance_advice(fault)

    report = {
        "predicted_fault": fault,
        "priority": advice["level"],
        "possible_causes": advice["possible_causes"],
        "recommended_actions": advice["recommended_actions"]
    }

    return report
