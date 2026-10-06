# 🩺 Patient with Abnormal Blood Pressure — ML + RAG + Streamlit

## 📌 Project Overview

This project analyzes patient health data to identify and predict abnormal blood pressure conditions using **Machine Learning**. It combines a predictive ML model with a **Retrieval-Augmented Generation (RAG)** system and an interactive **Streamlit** application.

The application allows users to enter patient information, obtain a blood-pressure prediction, and interact with relevant information through a RAG-based question-answering system.

---

## 🎯 Objectives

- Analyze patient health and blood-pressure-related data.
- Perform data preprocessing and exploratory data analysis.
- Build a **Linear Regression** model for blood pressure prediction.
- Evaluate the performance of the ML model.
- Implement a **RAG-based question-answering system**.
- Build an interactive **Streamlit web application**.
- Combine traditional Machine Learning with Generative AI concepts.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **Linear Regression**
- **LangChain**
- **FAISS**
- **Embeddings**
- **RAG (Retrieval-Augmented Generation)**
- **Streamlit**
- **Jupyter Notebook**

---

## 📂 Dataset

**Dataset:** `Patient_with_abnormal_bloodpressure.csv`

The dataset contains patient-related attributes that can be used to analyze factors associated with abnormal blood pressure.

The dataset is used for:

- Data cleaning
- Exploratory Data Analysis
- Feature preparation
- Machine Learning
- Prediction

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Linear Regression Model
   ↓
Model Evaluation
   ↓
Knowledge/Data Preparation
   ↓
Embeddings
   ↓
FAISS Vector Database
   ↓
RAG Pipeline
   ↓
Streamlit Application
   ↓
User Interaction & Prediction
```

---

## 🤖 Machine Learning Model

### Linear Regression

Linear Regression is used to predict a continuous blood-pressure-related value based on the available patient features.

The basic relationship can be represented as:

```text
y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ
```

Where:

- `y` = predicted target value
- `β₀` = intercept
- `β₁ ... βₙ` = model coefficients
- `X₁ ... Xₙ` = input features

### Model Evaluation

The model can be evaluated using metrics such as:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

---

## 🧠 RAG System

The project also implements **Retrieval-Augmented Generation (RAG)**.

RAG combines information retrieval with a language model.

### RAG Workflow

```text
Knowledge Documents
       ↓
Document Processing
       ↓
Text Splitting
       ↓
Embeddings
       ↓
FAISS Vector Store
       ↓
Similarity Search
       ↓
Relevant Information
       ↓
Language Model
       ↓
Generated Response
```

The RAG system helps retrieve relevant information before generating an answer, making the application more useful for patient/blood-pressure-related queries.

---

## 📊 Streamlit Application

The project includes an interactive Streamlit interface.

The application allows users to:

- Enter patient information.
- Generate a prediction using the trained ML model.
- Ask questions related to blood pressure.
- Retrieve relevant information using the RAG system.
- View results through a simple web interface.

---

## 📁 Project Structure

```text
Patient_with_abnormal_bloodpressure/
│
├── app.py
│
├── Documents/
│   └── medical_information/
│
├── Dataset/
│   └── Patient_with_abnormal_bloodpressure.csv
│
├── Notebook/
│   └── Patient_with_abnormal_bloodpressure.ipynb
│
├── Model/
│   └── trained_model.pkl
│
├── README.md
│
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Patient_with_abnormal_bloodpressure.git
```

### 2. Navigate to the Project Directory

```bash
cd Patient_with_abnormal_bloodpressure
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

Example libraries used in the project:

```text
pandas
numpy
matplotlib
scikit-learn
streamlit
langchain
faiss-cpu
sentence-transformers
```

---

## 💡 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Train-Test Split
- Linear Regression
- Model Evaluation
- Model Serialization
- Embeddings
- Vector Databases
- FAISS
- Retrieval-Augmented Generation
- LangChain
- Streamlit
- Generative AI Integration

---

## 🚀 Future Improvements

- Add additional Machine Learning models such as Logistic Regression, Random Forest, and Decision Tree.
- Improve prediction performance through feature engineering.
- Add model comparison and visualization.
- Integrate a more advanced LLM.
- Add authentication to the Streamlit application.
- Deploy the application using Streamlit Cloud or another cloud platform.
- Expand the medical knowledge base used by the RAG system.

---

## ⚠️ Disclaimer

This project is created for **educational and demonstration purposes only**.

The predictions and information provided by this application should **not be considered medical advice or a medical diagnosis**. Users should consult qualified healthcare professionals for medical decisions.

---

## 👩‍💻 Author

**Shrushti Shelgave**

BSc Computer Science | Data Analytics & AI/ML Enthusiast

### Skills Demonstrated

`Python` `SQL` `Machine Learning` `Data Analytics` `Pandas` `Scikit-learn` `RAG` `LangChain` `FAISS` `Streamlit` `Generative AI`
