
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸"
)

st.title("Lab 8: Iris Flower Prediction")
st.write("Predict an Iris flower species using machine learning.")

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

st.subheader("Enter Flower Measurements")

sepal_length = st.slider(
    "Sepal length (cm)", 4.0, 8.0, 5.1
)
sepal_width = st.slider(
    "Sepal width (cm)", 2.0, 4.5, 3.5
)
petal_length = st.slider(
    "Petal length (cm)", 1.0, 7.0, 1.4
)
petal_width = st.slider(
    "Petal width (cm)", 0.1, 2.5, 0.2
)

if st.button("Predict Species"):
    sample = pd.DataFrame(
        [[sepal_length, sepal_width,
          petal_length, petal_width]],
        columns=iris.feature_names
    )

    prediction = model.predict(sample)[0]
    species = iris.target_names[prediction]

    st.success(f"Predicted species: {species.title()}")

    probabilities = model.predict_proba(sample)[0]

    probability_df = pd.DataFrame({
        "Species": iris.target_names,
        "Probability": probabilities
    })

    st.subheader("Prediction Probabilities")
    st.bar_chart(
        probability_df,
        x="Species",
        y="Probability"
    )