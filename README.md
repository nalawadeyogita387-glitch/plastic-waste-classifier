# Plastic Waste Classifier Using Computer Vision

## Problem Statement

Plastic waste is increasing day by day. Proper classification of plastic waste helps in better waste management and recycling. This project provides a prototype for classifying plastic waste into different categories.

## Features

- Upload plastic waste image
- Plastic category classification prototype
- Display classification result
- Maintain classification history
- Result visualization using bar chart

## Technologies Used

- Python
- Streamlit
- FastAPI
- Pillow
- Uvicorn
- GitHub

## AI Tools Used

- ChatGPT for project planning and coding guidance
- ChatGPT for debugging and documentation
- Visual Studio Code for development

## Important AI Prompts Used

1. Create a Streamlit application for plastic waste classification.
2. Add image upload functionality.
3. Display classification history and result visualization.
4. Create a FastAPI backend for classification.
5. Prepare README documentation, algorithm and flowchart.

## Project Modules

### Frontend

The Streamlit frontend allows users to upload images, select plastic categories and view classification results.

### Backend

The FastAPI backend provides an API endpoint for classification requests.

## Algorithm

1. Start the application.
2. Upload a plastic waste image.
3. Select the plastic category.
4. Click the Classify Image button.
5. Display the classification result.
6. Store the result in classification history.
7. Display the result visualization.
8. Stop.

## How to Run

### Run Backend

```bash
python -m uvicorn backend:app --reload
```

Backend URL:

http://127.0.0.1:8000

### Run Frontend

Open another terminal and run:

```bash
streamlit run main.py
```

Frontend URL:

http://localhost:8501

## Limitation

This version is a prototype. The plastic category is selected manually. A trained computer vision model can be integrated in the future for automatic prediction.

## Future Scope

- Train a real computer vision model
- Automatic plastic category prediction
- Improve classification accuracy
- Add more plastic categories
- Connect the frontend with the backend API

## Conclusion

The Plastic Waste Classifier project demonstrates image upload, classification result display, history management and visualization for plastic waste management.
