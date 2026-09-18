
import streamlit as st
from datetime import datetime
import requests

st.title("Plastic Waste Classifier")
st.write("Upload a plastic waste image")

BACKEND_URL = "http://127.0.0.1:8000/classify"

if "history" not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader(
    "Upload Plastic Waste Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

    category = st.selectbox(
        "Select Plastic Category",
        [
            "PET (Plastic Bottle)",
            "HDPE",
            "PVC",
            "LDPE",
            "Other Plastic"
        ]
    )

    if st.button("Classify Image"):

        data = {
            "image_name": uploaded_file.name,
            "category": category
        }

        try:
            response = requests.post(
                BACKEND_URL,
                json=data
            )

            if response.status_code == 200:
                result = response.json()

                st.session_state.history.append({
                    "Image": result["image"],
                    "Category": result["category"],
                    "Time": datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    )
                })

                st.success(result["status"])
                st.write("Predicted Category:", result["category"])

            else:
                st.error("Backend error occurred")

        except requests.exceptions.ConnectionError:
            st.error("Please start the FastAPI Backend first")

st.subheader("Classification History")

if st.session_state.history:
    st.table(st.session_state.history)

    st.subheader("Result Visualization")

    category_count = {}

    for item in st.session_state.history:
        category = item["Category"]
        category_count[category] = category_count.get(category, 0) + 1

    st.bar_chart(category_count)

else:
    st.info("No classification history yet.")