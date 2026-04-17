"""
QML Project using Qiskit and Iris dataset
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from qiskit.circuit.library import ZZFeatureMap, TwoLocal
from qiskit_machine_learning.algorithms import VQC
from qiskit_algorithms.optimizers import COBYLA


def run_qml():
    """Run Quantum Machine Learning model"""

    print("Running QML Project...")

    # Load dataset (no CSV needed)
    data = load_iris()
    X = data.data
    y = data.target

    # Use only 2 classes (for binary classification)
    X = X[y != 2]
    y = y[y != 2]

    # Scale data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Quantum circuits
    feature_map = ZZFeatureMap(feature_dimension=4, reps=2)
    ansatz = TwoLocal(4, ["ry", "rz"], "cz", reps=2)

    # Model
    model = VQC(
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=COBYLA(maxiter=50),
    )

    # Train
    model.fit(X_train, y_train)

    # Test
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    run_qml()
