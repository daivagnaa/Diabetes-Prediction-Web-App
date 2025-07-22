import numpy as np
import pickle
import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .positive {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        border-left: 5px solid #ff6b6b;
        color: #d63031;
    }
    .negative {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-left: 5px solid #00b894;
        color: #00b894;
    }
    .footer {
        text-align: center;
        color: #666;
        padding: 2rem;
        border-top: 1px solid #eee;
        margin-top: 3rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Loading the saved model
@st.cache_resource
def load_model():
    return pickle.load(open('trained_model.sav', 'rb'))

loaded_model = load_model()

# Creating a Function for Prediction
def predict_diabetes(input_data):
    try:
        # Convert input to float
        input_data_float = [float(x) for x in input_data]
        input_data_as_numpy_array = np.asarray(input_data_float)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        
        prediction = loaded_model.predict(input_data_reshaped)
        probability = loaded_model.predict_proba(input_data_reshaped)
        
        return prediction[0], probability[0]
    except ValueError:
        return None, None

# Streamlit App
def main():
    # Header Section
    st.markdown('<h1 class="main-header">🏥 Diabetes Prediction System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced ML-powered health assessment tool</p>', unsafe_allow_html=True)
    
    # Create columns for layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>📋 Instructions</h4>
            <p>Please fill in all the medical parameters below. Our AI model will analyze your data and provide a diabetes risk assessment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sidebar for additional information
    with st.sidebar:
        st.markdown("### 📊 About This Tool")
        st.info("""
        This application uses a Support Vector Machine (SVM) model trained on the Pima Indians Diabetes Database to predict diabetes risk based on medical parameters.
        """)
        
        st.markdown("### 🎯 Model Performance")
        st.success("✅ High Accuracy Classification")
        st.success("✅ Clinically Validated Features")
        st.success("✅ Real-time Prediction")
        
        st.markdown("### 📋 Parameter Ranges")
        ranges = {
            "Pregnancies": "0-20",
            "Glucose": "0-200 mg/dL",
            "Blood Pressure": "0-200 mmHg",
            "Skin Thickness": "0-100 mm",
            "Insulin": "0-500 μU/mL",
            "BMI": "10.0-50.0 kg/m²",
            "Age": "18-100 years"
        }
        
        for param, range_val in ranges.items():
            st.text(f"{param}: {range_val}")
    
    # Main input form
    st.markdown("### 🔍 Medical Parameters")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.number_input(
            "👶 Number of Pregnancies", 
            min_value=0, max_value=20, value=0,
            help="Number of times pregnant"
        )
        
        Glucose = st.number_input(
            "🍬 Glucose Level (mg/dL)", 
            min_value=0, max_value=300, value=100,
            help="Plasma glucose concentration"
        )
        
        BloodPressure = st.number_input(
            "💓 Blood Pressure (mmHg)", 
            min_value=0, max_value=200, value=80,
            help="Diastolic blood pressure"
        )
        
        SkinThickness = st.number_input(
            "📏 Skin Thickness (mm)", 
            min_value=0, max_value=100, value=20,
            help="Triceps skin fold thickness"
        )
    
    with col2:
        Insulin = st.number_input(
            "💉 Insulin Level (μU/mL)", 
            min_value=0, max_value=900, value=80,
            help="2-Hour serum insulin"
        )
        
        BMI = st.number_input(
            "⚖️ BMI (kg/m²)", 
            min_value=10.0, max_value=70.0, value=25.0, step=0.1,
            help="Body Mass Index"
        )
        
        DiabetesPedigreeFunction = st.number_input(
            "🧬 Diabetes Pedigree Function", 
            min_value=0.0, max_value=3.0, value=0.5, step=0.001,
            help="Genetic diabetes likelihood"
        )
        
        Age = st.number_input(
            "🎂 Age (years)", 
            min_value=1, max_value=120, value=30,
            help="Age in years"
        )
    
    # Center the prediction button
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        predict_button = st.button("🔮 Predict Diabetes Risk", use_container_width=True)
    
    # Prediction logic
    if predict_button:
        input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, 
                     Insulin, BMI, DiabetesPedigreeFunction, Age)
        
        # Validate inputs
        if all(x >= 0 for x in input_data):
            with st.spinner('🔄 Analyzing your health parameters...'):
                prediction, probability = predict_diabetes(input_data)
                
                if prediction is not None:
                    # Display results
                    st.markdown("### 📋 Prediction Results")
                    
                    if prediction == 0:
                        st.markdown(f"""
                        <div class="prediction-box negative">
                            ✅ Low Diabetes Risk<br>
                            <small>Confidence: {probability[0]*100:.1f}%</small>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.balloons()
                        
                    else:
                        st.markdown(f"""
                        <div class="prediction-box positive">
                            ⚠️ High Diabetes Risk Detected<br>
                            <small>Confidence: {probability[1]*100:.1f}%</small>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.warning("⚠️ Please consult with a healthcare professional for proper medical advice.")
                    
                    # Show probability breakdown
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Non-Diabetic Probability", f"{probability[0]*100:.1f}%")
                    with col2:
                        st.metric("Diabetic Probability", f"{probability[1]*100:.1f}%")
                    
                    # Additional recommendations
                    st.markdown("### 💡 Health Recommendations")
                    if prediction == 1:
                        st.error("""
                        **Immediate Actions:**
                        - 🏥 Consult an endocrinologist or your primary care physician
                        - 📋 Get comprehensive diabetes testing (HbA1c, fasting glucose)
                        - 🥗 Consider dietary modifications
                        - 🏃‍♂️ Increase physical activity
                        - 📱 Monitor blood glucose regularly
                        """)
                    else:
                        st.success("""
                        **Maintain Healthy Lifestyle:**
                        - 🥗 Continue balanced diet
                        - 🏃‍♂️ Regular exercise routine
                        - ⚖️ Maintain healthy weight
                        - 🔄 Regular health check-ups
                        - 💧 Stay hydrated
                        """)
                
                else:
                    st.error("❌ Please ensure all values are valid numbers.")
        else:
            st.error("❌ Please ensure all values are positive numbers.")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <h4>🔬 About the Developer</h4>
        <p><strong>Daivagna Parmar</strong></p>
        <p>📧 Contact: devparmar1895@gmail.com | 🌐 <a href="https://github.com/daivagnaa">GitHub</a></p>
        <hr>
        <p><em>Disclaimer: This tool is for educational purposes only and should not replace professional medical advice.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()