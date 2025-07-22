# Diabetes Prediction Project

This project implements a machine learning solution to predict diabetes using the Pima Indians Diabetes Database. The project includes data preprocessing, model training with Support Vector Machine (SVM), and deployment through both a command-line interface and a web application using Streamlit.

## Project Structure

```
02. Diabites Prediction/
│
├── README.md                 # Project documentatio
├── DiabetesPred.ipynb       # Jupyter notebook with complete analysis
├── diabetes.csv             # Dataset (Pima Indians Diabetes Database)
├── WorkFlow.txt             # Project workflow overview
├── trained_model.sav        # Saved trained SVM model
├── predictive_system.py     # Command-line prediction system
└── Web_App.py              # Streamlit web application
```

## Dataset

The project uses the **Pima Indians Diabetes Database** containing 768 samples with 8 features:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function
- **Age**: Age (years)
- **Outcome**: Target variable (0: Non-diabetic, 1: Diabetic)

## Workflow

1. **Data Collection and Analysis**
   - Load and explore the diabetes dataset
   - Analyze data distribution and statistics
   - Check for missing values and data quality

2. **Data Preprocessing**
   - Feature standardization using StandardScaler
   - Separate features (X) and target (Y)
   - Handle data normalization for better model performance

3. **Train-Test Split**
   - Split data into training (80%) and testing (20%) sets
   - Use stratified sampling to maintain class balance
   - Random state = 2 for reproducibility

4. **Model Training**
   - Support Vector Machine (SVM) with linear kernel
   - Train the classifier on preprocessed training data
   - Optimize model parameters for best performance

5. **Model Evaluation**
   - Training Accuracy: Evaluated on training set
   - Testing Accuracy: Evaluated on test set
   - Model performance metrics assessment

6. **Model Deployment**
   - Save trained model using pickle
   - Create prediction systems for new data
   - Deploy web application using Streamlit

## Key Features

### Machine Learning Pipeline
- **Data Standardization**: Uses StandardScaler to normalize features
- **SVM Classifier**: Linear kernel for binary classification
- **Cross-validation**: Stratified train-test split for robust evaluation
- **Model Persistence**: Pickle serialization for model saving/loading

### Prediction Systems
1. **Command-line Interface** (`predictive_system.py`):
   - Direct Python script execution
   - Input data as tuple format
   - Instant prediction results

2. **Web Application** (`Web_App.py`):
   - Interactive Streamlit interface
   - User-friendly input forms with placeholders
   - Real-time prediction with visual feedback
   - Professional UI with developer attribution

## Installation & Usage

### Prerequisites
```bash
pip install numpy pandas scikit-learn streamlit pickle-mixin
```

### Running the Jupyter Notebook
```bash
jupyter notebook DiabetesPred.ipynb
```

### Using Command-line Prediction
```bash
python predictive_system.py
```

### Launching Web Application
```bash
streamlit run Web_App.py
```

## Model Performance

The SVM classifier demonstrates good performance on the diabetes prediction task:
- **Algorithm**: Support Vector Machine with linear kernel
- **Training Strategy**: Standardized features with stratified sampling
- **Evaluation**: Training and testing accuracy metrics
- **Deployment Ready**: Serialized model for production use

## Input Format

For making predictions, provide the following 8 features in order:
1. Pregnancies (0-20)
2. Glucose Level (0-200)
3. Blood Pressure (0-200)  
4. Skin Thickness (0-100)
5. Insulin Level (0-500)
6. BMI (0.0-50.0)
7. Diabetes Pedigree Function (0.0-2.5)
8. Age (0-120)

**Example Input**: `(5, 166, 72, 19, 175, 25.8, 0.587, 51)`

## Web Application Features

- **Interactive Interface**: Easy-to-use input fields with helpful placeholders
- **Real-time Prediction**: Instant results with button click
- **Input Validation**: Guided input ranges for each parameter
- **Professional Design**: Clean UI with success/error messaging
- **Developer Attribution**: Credit and contact information

## Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Streamlit**: Web application framework
- **Pickle**: Model serialization
- **Jupyter Notebook**: Interactive development environment

## Future Enhancements

- [ ] Add more sophisticated feature engineering
- [ ] Implement ensemble methods (Random Forest, Gradient Boosting)
- [ ] Include cross-validation and hyperparameter tuning
- [ ] Add data visualization and EDA charts
- [ ] Implement model interpretability features
- [ ] Deploy to cloud platforms (Heroku, AWS, etc.)
- [ ] Add batch prediction capabilities
- [ ] Include confidence scores for predictions

## Developer

**Daivagna Parmar**

---

*This project demonstrates a complete machine learning pipeline from data preprocessing to model deployment, showcasing practical implementation of diabetes prediction using Support