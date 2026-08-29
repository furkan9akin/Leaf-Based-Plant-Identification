# Leaf-Based Plant Identification

A web-based machine learning application that identifies plants from **leaf images** using Python, Flask, and a trained Keras image classification model.

The project was developed as my final project during the **Kodland Python Pro** program and helped me explore how machine learning models can be integrated into a real web application.

---

## 🌿 Project Overview

The goal of this project is to identify a plant by analyzing an image of its leaf.

A user uploads a leaf image through the web interface. The application processes the image, sends it to a trained image classification model, and returns the predicted plant class.

This project combines:

- image classification
- machine learning
- web development
- image preprocessing
- model inference

The project focuses on **plant identification from leaf images**.

---

## 🔄 How It Works

The application follows a simple prediction pipeline:

```text
Leaf Image
    ↓
Image Upload
    ↓
Image Preprocessing
    ↓
Resize to 128 × 128
    ↓
Normalization
    ↓
Keras Classification Model
    ↓
Predicted Plant Class
    ↓
Result Displayed in Flask Web Application
```

### Step 1 — Upload

The user uploads an image of a plant leaf through the Flask-based web interface.

### Step 2 — Preprocessing

Before the image is sent to the model, it is prepared for prediction.

The image is:

- loaded from the uploaded file
- resized to **128 × 128 pixels**
- converted into an array
- normalized for model input

### Step 3 — Prediction

The processed image is passed to a trained Keras image classification model.

The model produces prediction scores for the plant classes it was trained to recognize.

### Step 4 — Result

The application selects the most likely class and displays the predicted plant identification to the user.

---

## 🧠 Machine Learning Model

The application uses a trained **Keras image classification model**.

The model is loaded from:

```text
plant_village_model.h5
```


The prediction logic is implemented in Python and connects the trained model to the Flask application.

---

## 📊 Dataset

The project uses leaf images from the **PlantVillage dataset**.

PlantVillage provides a large collection of plant leaf images that can be used for computer vision and image classification research.

Dataset:

[PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)

Although PlantVillage contains images that are commonly used in plant disease research, **this project uses leaf images for plant classification and identification rather than disease diagnosis**.

---

## 🖼️ Image Processing

Before classification, uploaded images are converted into the format expected by the model.

The main preprocessing steps include:

1. Loading the uploaded image
2. Resizing the image to **128 × 128 pixels**
3. Converting the image into a numerical array
4. Normalizing pixel values
5. Preparing the image as a batch for model inference

This ensures that images uploaded by users have the same input format as the images used by the classification model.

---

## 🌱 Plant Classification

The model was trained to classify leaf images into **nine plant categories**:

- Apple
- Bell Pepper
- Cherry
- Corn
- Grape
- Peach
- Potato
- Strawberry
- Tomato

During training, Keras automatically assigns class indices based on the dataset directory structure.

The application uses these prediction scores to identify the plant class associated with an uploaded leaf image.

---

## 🌐 Web Application

The machine learning model is connected to a web interface using **Flask**.

The application allows users to:

- upload leaf images
- send images to the classification model
- receive plant predictions
- interact with the project through a browser-based interface

The project also includes HTML templates and static resources used to build the user interface.

---

## 💻 Technologies

### Programming

- Python
- HTML
- CSS

### Web Development

- Flask
- Flask-SQLAlchemy

### Machine Learning

- TensorFlow
- Keras
- NumPy
- Pillow

### Database

- SQLite

### Development Tools

- Git
- GitHub
- Visual Studio Code

---

## 📁 Repository Structure

The repository contains the main components required for the web application and machine learning prediction pipeline.

```text
Leaf-Based-Plant-Identification/
│
├── README.md
├── app.py
├── tarim.py
├── requirements.txt
├── .gitignore
│
├── training/
│   └── train_model.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
└── static/
    ├── css/
    └── img/
```

> The exact repository structure may vary depending on where the trained model files are stored.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/furkan9akin/Leaf-Based-Plant-Identification.git
```

Move into the project directory:

```bash
cd Leaf-Based-Plant-Identification
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The application uses libraries including:

```text
Flask
Flask-SQLAlchemy
tensorflow
keras
numpy
Pillow
```

The exact versions used by the project should be listed in:

```text
requirements.txt
```

---

## ▶️ Running the Application

After installing the required dependencies, start the Flask application:

```bash
python app.py
```

Then open the local address shown by Flask in your web browser.

A typical local address is:

```text
http://127.0.0.1:5000
```

Upload a leaf image through the interface to generate a plant prediction.

---

## ⚠️ Model Files

The application requires the trained model and label files:

```text
plant_village_model.h5
labels.txt
```

These files must be placed in the location expected by the Python prediction code.

If the model file is not included in the repository because of its file size, it must be downloaded or generated separately before the application can perform predictions.

---

## 🎓 What I Learned

This project was one of my first opportunities to combine **machine learning with a complete software application**.

Instead of only running a machine learning model inside a notebook, I learned how to connect a trained model to a web interface that another person could actually use.

Some of the main concepts I explored include:

- how images can be represented as numerical data
- how images need to be resized and normalized before model inference
- how an image classification model generates predictions
- how model outputs can be mapped to meaningful class labels
- how Python machine learning code can be integrated into Flask
- how files uploaded through a website can be processed by a backend application
- how application logic, templates, static files, and machine learning components work together

The project helped me better understand the connection between **computer vision, machine learning, and software development**.

---

## 🚀 Future Improvements

There are several ways I would like to improve the project.

### Improve Model Evaluation

Add a more complete evaluation of the trained model using:

- validation accuracy
- confusion matrix
- precision
- recall
- F1 score

### Display Prediction Confidence

Show the confidence score together with the predicted plant class.

For example:

```text
Predicted Plant: Tomato
Confidence: 94.2%
```

### Display Top Predictions

Instead of showing only one result, display the top three predictions and their confidence scores.

### Improve the User Interface

Create a cleaner and more responsive interface for uploading images and viewing predictions.

### Add More Plant Classes

Expand the training dataset so that the system can recognize a larger variety of plants.

### Improve Model Generalization

Test the model with leaf photographs taken outside the original dataset to understand how well it performs on real-world images.

### Deploy the Application

Deploy the Flask application so that the model can be tested through a public web interface.

---

## 🔬 Limitations

This project is an educational machine learning application and has several limitations.

The model's predictions depend heavily on:

- the quality of the training dataset
- lighting conditions
- image background
- leaf orientation
- similarity between plant species
- image quality

Because the model was trained using a specific dataset, its performance on photographs taken in different real-world environments may vary.

The application should therefore be considered a **plant image classification project**, not a professional botanical identification system.

---

## 🎓 Project Context

This project was developed as my final project during the:

**Kodland Python Pro Program**

The project gave me the opportunity to apply concepts from Python programming, web development, and machine learning in a single application.

---

## 👤 Author

### Furkan Akın

High school senior and aspiring Computer Science major interested in:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Robotics
- Computer Architecture
- Software Development

GitHub: [furkan9akin](https://github.com/furkan9akin)

---

## 📌 Why This Project Matters to Me

This project was an important step in my transition from learning Python syntax to building applications that combine multiple areas of computer science.

I had to think about more than just writing code. The project required me to understand how a machine learning model receives data, how an image needs to be prepared for prediction, how the model communicates its result, and how that result can be presented to a user through a web application.

It increased my interest in **machine learning and computer vision** and motivated me to continue building projects where software can interpret and learn from real-world data.
