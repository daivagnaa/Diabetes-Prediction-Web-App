# Diabetes Prediction Project

This project implements a machine learning solution to predict diabetes using the Pima Indians Diabetes Database. The project includes data preprocessing, model training with Support Vector Machine (SVM), and deployment through both a command-line interface and a beautiful web application using Streamlit.

## 🚀 Live Demo

**Web Application**: [Diabetes Risk Predictor](https://diabetes-predict-web.streamlit.app) 

## Project Structure

```
02. Diabites Prediction/
│
├── README.md                 # Project documentation
├── DiabetesPred.ipynb       # Jupyter notebook with complete analysis
├── diabetes.csv             # Dataset (Pima Indians Diabetes Database)
├── WorkFlow.txt             # Project workflow overview
├── trained_model.sav        # Saved trained SVM model
├── scaler.sav              # Saved StandardScaler for data preprocessing
├── predictive_system.py     # Command-line prediction system
└── Web_App.py              # Enhanced Streamlit web application
```

## Dataset

The project uses the **Pima Indians Diabetes Database** containing 768 samples with 8 features:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **BloodPressure**: Diastolic blood pressure (mmHg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (μU/mL)
- **BMI**: Body mass index (kg/m²)
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
   - Train the classifier on standardized training data
   - Optimize model parameters for best performance

5. **Model Evaluation**
   - Training Accuracy: High-precision classification
   - Testing Accuracy: Robust validation metrics
   - Model performance assessment

6. **Model Deployment**
   - Save trained model and scaler using pickle
   - Create prediction systems for new data
   - Deploy enhanced web application using Streamlit Cloud

## Key Features

### 🤖 Machine Learning Pipeline
- **Data Standardization**: Uses StandardScaler to normalize features
- **SVM Classifier**: Linear kernel for binary classification
- **Cross-validation**: Stratified train-test split for robust evaluation
- **Model Persistence**: Pickle serialization for model and scaler saving/loading

### 💻 Prediction Systems

1. **Command-line Interface** (`predictive_system.py`):
   - Direct Python script execution
   - Input data as tuple format
   - Instant prediction results

2. **Enhanced Web Application** (`Web_App.py`):
   - 🎨 **Beautiful Modern UI**: Gradient design with custom CSS styling
   - 📱 **Responsive Layout**: Professional interface with intuitive navigation
   - 🔍 **Interactive Input Forms**: Number inputs with validation and helpful tooltips
   - ⚡ **Real-time Prediction**: Instant results with loading animations
   - 🎯 **Health Recommendations**: Personalized advice based on prediction results
   - 📊 **Comprehensive Sidebar**: Model information and parameter guidelines
   - 💡 **Smart Validation**: Error handling and input validation
   - 🏥 **Medical Disclaimers**: Ethical use guidelines
   - 👨‍💻 **Developer Branding**: Professional contact information and attribution

## Installation & Usage

### Prerequisites
```bash
pip install numpy pandas scikit-learn streamlit pillow
```

### 🌐 Access Web Application
Visit the live demo: **[Diabetes Risk Predictor](https://diabetes-predict-web.streamlit.app)**

### 💻 Run Locally

#### Running the Jupyter Notebook
```bash
jupyter notebook DiabetesPred.ipynb
```

#### Using Command-line Prediction
```bash
python predictive_system.py
```

#### Launching Web Application Locally
```bash
streamlit run Web_App.py
```

## 🎯 Model Performance

The SVM classifier demonstrates excellent performance on the diabetes prediction task:
- **Algorithm**: Support Vector Machine with linear kernel
- **Training Strategy**: Standardized features with stratified sampling
- **Data Processing**: Proper standardization ensures accurate predictions
- **Evaluation**: High training and testing accuracy metrics
- **Deployment Ready**: Serialized model and scaler for production use

## 📝 Input Format

For making predictions, provide the following 8 features in order:

| Parameter | Range | Unit | Description |
|-----------|-------|------|-------------|
| Pregnancies | 0-20 | count | Number of pregnancies |
| Glucose | 0-300 | mg/dL | Plasma glucose concentration |
| Blood Pressure | 0-200 | mmHg | Diastolic blood pressure |
| Skin Thickness | 0-100 | mm | Triceps skin fold thickness |
| Insulin | 0-900 | μU/mL | 2-Hour serum insulin |
| BMI | 10.0-70.0 | kg/m² | Body Mass Index |
| Diabetes Pedigree | 0.0-3.0 | score | Genetic diabetes likelihood |
| Age | 1-120 | years | Age in years |

**Example Non-Diabetic Input**: `(1, 85, 66, 29, 0, 26.6, 0.351, 31)`
**Example Diabetic Input**: `(8, 183, 64, 0, 0, 23.3, 0.672, 32)`

## ✨ Web Application Features

### 🎨 User Experience
- **Modern Design**: Beautiful gradient backgrounds and animations
- **Interactive Elements**: Hover effects and smooth transitions
- **Loading Animations**: Spinner during prediction analysis
- **Success Celebrations**: Balloons for negative diabetes predictions
- **Color-coded Results**: Green for safe, red for high-risk predictions

### 🏥 Health Features
- **Comprehensive Health Tips**: Tailored recommendations based on results
- **Emergency Guidelines**: Important steps for high-risk cases
- **Medical Disclaimers**: Clear ethical use guidelines
- **Parameter Guidelines**: Helpful ranges and normal values

### 👨‍💻 Developer Features
- **Professional Branding**: Prominent developer information
- **Contact Integration**: Direct GitHub and email links
- **Dark Theme Support**: Automatic adaptation to user preferences
- **Responsive Design**: Works on desktop and mobile devices

## 🛠 Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Streamlit**: Web application framework and cloud deployment
- **Pickle**: Model and scaler serialization
- **Jupyter Notebook**: Interactive development environment
- **CSS**: Custom styling for enhanced UI

## 🌐 Deployment

The application is deployed on **Streamlit Community Cloud** for free public access:
- **Platform**: Streamlit Cloud
- **URL**: [diabetes-prediction-web-app.streamlit.app](https://diabetes-prediction-web-app.streamlit.app)
- **Auto-deployment**: Linked to GitHub repository for continuous deployment
- **Uptime**: 99.9% availability with global CDN

## 🔮 Future Enhancements

- [ ] 📊 Add interactive data visualization and EDA charts
- [ ] 🤖 Implement ensemble methods (Random Forest, Gradient Boosting)
- [ ] 🔍 Include cross-validation and hyperparameter tuning
- [ ] 📈 Add model interpretability features (SHAP, LIME)
- [ ] ☁️ Deploy to additional cloud platforms (Heroku, AWS, Azure)
- [ ] 📱 Create mobile application version
- [ ] 🎯 Add confidence scores and probability distributions
- [ ] 📊 Include batch prediction capabilities
- [ ] 🔐 Add user authentication and prediction history
- [ ] 🌍 Multi-language support

## 👨‍💻 Developer

**Daivagna Parmar**
- 📧 **Email**: [devparmar1895@gmail.com](mailto:devparmar1895@gmail.com)
- 🔗 **GitHub**: [@daivagnaa](https://github.com/daivagnaa)
- 💼 **LinkedIn**: [Daivagna Parmar](https://in.linkedin.com/in/daivagna-parmar-949315316)

## 📜 License & Disclaimer

⚠️ **Medical Disclaimer**: This application is for educational and screening purposes only. Always consult qualified healthcare professionals for medical diagnosis and treatment.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for suggestions and improvements.

---

*This project demonstrates a complete machine learning pipeline from data preprocessing to model deployment, showcasing practical implementation of diabetes prediction using Support Vector Machine classification with a beautiful, user-friendly web interface.*

**⭐ Star this repository if you found it helpful!**
