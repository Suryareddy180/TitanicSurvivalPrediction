# 🚢 Titanic Survival Prediction

This project is a simple machine learning web app built using **Streamlit**. It predicts whether a passenger survived the Titanic disaster based on selected features like age, gender, passenger class, and more.

---

## 📁 Project Structure
```base
titanic-streamlit-app/
│
├── titanic_app.ipynb # Jupyter notebook to train and save the model (recommended to run in Colab)
├── titanic_model.pkl # Trained ML model saved with pickle
├── app.py # Streamlit web app for making predictions
├── requirements.txt # Required Python packages
└── README.md # Project overview and setup guide
```
## 📸 Preview
![App Screenshot](https://github.com/Suryareddy180/TitanicSurvivalPrediction/blob/main/preview.png)

---

## 🚀 Features
- Passenger class (`pclass`)
- Sex (`sex`)
- Age (`age`)
- Siblings/Spouses aboard (`sibsp`)
- Fare paid (`fare`)


---
## 🛠 Tech Stack

- **Python**
- **Scikit-learn**
- **Streamlit**
- **NumPy**
- **Pickle**
---

## 🛠️ Installation & Setup

### 1. Clone the repository:
```bash
git clone https://github.com/Suryareddy180/TitanicSurvivalPrediction.git
cd TitanicSurvivalPrediction
```
### 2. (Optional) Create a virtual environment:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies:
``` bash
pip install -r requirements.txt
```
### ▶️ Run the App
``` bash
streamlit run app.py
```
Then open the local URL provided in your browser (usually http://localhost:8501).
---

## 🧠 Model Training
To retrain the model:
- Open titanic_app.ipynb in Google Colab or Jupyter Notebook.
- Run all cells.
- Save the generated titanic_model.pkl.
- Replace the existing one in the repo.
---

## 📄 License
This project is for educational/demo purposes. Free to use and modify.
---

## 🤝 Acknowledgements
- Titanic dataset from Kaggle
- Streamlit for easy web app deployment.



  

