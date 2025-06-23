# 🩺 Diabetes Prediction System

A machine learning web application that predicts whether a person is likely to have diabetes or not, using the **Pima Indians Diabetes Dataset**.  
This project includes full data preprocessing, exploratory analysis, model training, and deployment with an interactive Streamlit interface.

🔗 **Live Web App:** [https://diabetes-predict-model.streamlit.app/](https://diabetes-predict-model.streamlit.app/) 

---
## **🔍 Dataset & EDA**  
### **Features**  
The dataset contains **9 medical features**:  
1. `Pregnancies`  
2. `Glucose`  
3. `BloodPressure`  
4. `SkinThickness`  
5. `Insulin`  
6. `BMI`  
7. `DiabetesPedigreeFunction`  
8. `Age`  
9. `Outcome` (Target: 0 = No Diabetes, 1 = Diabetes)  

### **Exploratory Data Analysis (EDA)**  
- **Data Cleaning:**  
  - Handled missing values (encoded as zeros) using `DataPreprocessing` class.  
  - Replaced zeros with `NaN` and imputed using mean/median (`fill_null` method).  
- **Visualizations:**  
  - **Univariate Analysis:** Histograms, boxplots (`UnivariateAnalysis` class).  
  - **Bivariate Analysis:** Scatter plots, correlation heatmaps (`BivariateAnalysis` class).  
  - **Key Insights:**  
    - Higher glucose levels and BMI correlate strongly with diabetes.  
    - Age and pregnancies are secondary risk factors.  

*(Full EDA implemented in `data.ipynb` classes.)*  

---

## **⚙️ Model Training & Results**  
### **Pipeline**  
1. **Data Splitting:** 80% training, 20% testing (`split_data` method in `Model` class).  
2. **Feature Scaling:** StandardScaler applied.  
3. **Model:** SVM with linear kernel (`SVC` from scikit-learn).  

### **Performance Metrics**  
| Metric          | Score  |  
|-----------------|--------|  
| **Accuracy**    | 75.3%  |  
| **Precision**   | 0.67   |  
| **Recall**      | 0.62   |  
| **F1-Score**    | 0.64   |  

### **Confusion Matrix**  
```python
[[82  17]  # True Negatives | False Positives  
 [21  34]] # False Negatives | True Positives  
```

---
---

## **🛠 Technologies Used**  
- **Language:** Python  
- **Libraries:**  
  - `pandas`, `numpy` (Data Manipulation)  
  - `matplotlib`, `seaborn` (EDA & Visualization)  
  - `scikit-learn` (Model Training: SVM)  
  - `streamlit` (Web Deployment)  
  - `pickle` (Model Serialization)  
- **Dataset:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  

---
---

## 🚀 How to Use This Project

### 🔗 Try It Online:
👉 [Launch Live App](https://diabetes-predict-model.streamlit.app/)

### 💻 Run Locally:
1. Clone the repository:
 ```bash
 git clone https://github.com/your-username/diabetes-predict-model
 cd diabetes-predict-model
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

4. Automtically a browser will open.
   

### **Deployment**  
- The app is deployed on **Streamlit Cloud** ([Live Link](https://diabetes-predict-model.streamlit.app/)).  


---

## 📁 Project Structure

```
diabetes-predict-model/
├── model/
│   └── diabetes_model.pkl       # Trained ML model
│
├── src/                         # Modular Streamlit components                   
│   ├── header.py                # App title and description
│   ├── sidebar.py               # Sidebar instructions
│   ├── prediction.py            # User input form logic                
│   └── result.py                # Output display
│
├── app.py                       # Streamlit main script
├── data.ipynb                   # Jupyter Notebook for EDA + Training
├── requirements.txt             # Python dependencies
├── diabetes.csv                 # Sample dataset
└── README.md                    # Project overview (this file)
```
---

## **📝 Key Components**  
### **1. Data Processing (`data.py`)**  
- **`DataLoading`:** Loads dataset and provides basic stats (`get_shape`, `get_columns`).  
- **`DataPreprocessing`:** Handles duplicates, null values, and zero imputation.  
- **`Graphs`:** Dynamic plotting (heatmaps, pairplots, histograms).  
- **`UnivariateAnalysis`/`BivariateAnalysis`:** Statistical and visual EDA.  
- **`Model` class:** Splits data, trains SVM, and evaluates performance.  
- **`PickleHandler`:** Saves/loads the trained model.  

### **3. Streamlit App**  
- **`Header`/`Sidebar`/`DisplayArea`:** UI components.  
- **`Prediction`:** Collects user input and predicts using the trained model.  
- **`Result`:** Displays prediction with color-coded alerts.  

---

## 👨‍💻 Developed By

**Aman Ali**

BS Artificial Intelligence – 2nd Semester

Superior University, Pakistan

---

### **Acknowledgments**  
- **Sir Ahmed Hassan** for project guidance.  
- Kaggle for the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).  
