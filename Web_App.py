import numpy as np
import pickle
import streamlit as st
import warnings 
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="Diabetes Prediction App - By Daivagna Parmar",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Beautiful Styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .developer-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        font-size: 1.8rem;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
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
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 3rem;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    .info-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 1rem 0;
        text-align: center;
        color: white;
    }
    .contact-info h4 {
        color: white;
        margin-bottom: 0.5rem;
    }
    .contact-info hr {
        border-color: rgba(255, 255, 255, 0.3);
        margin: 1rem 0;
    }
    .github-link {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        margin: 0.5rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .github-link:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .email-link {
        display: inline-block;
        background: rgba(234, 67, 53, 0.8);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        margin: 0.5rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(234, 67, 53, 0.5);
    }
    .email-link:hover {
        background: rgba(194, 51, 33, 0.9);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .footer {
        text-align: center;
        color: var(--text-color);
        padding: 2rem;
        border-top: 2px solid rgba(102, 126, 234, 0.3);
        margin-top: 3rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        border-radius: 15px;
    }
    .footer h3 {
        color: #667eea;
        margin-bottom: 1rem;
    }
    .footer p {
        color: var(--text-color);
        opacity: 0.8;
    }
    .parameter-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    /* Dark theme compatibility */
    @media (prefers-color-scheme: dark) {
        .footer {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-top: 2px solid rgba(102, 126, 234, 0.4);
        }
        .info-card {
            background: rgba(102, 126, 234, 0.1);
            border-left: 4px solid #667eea;
            color: var(--text-color);
        }
    }
</style>
""", unsafe_allow_html=True)

# Loading saved model and scaler
@st.cache_resource
def load_model_and_scaler():
    model = pickle.load(open('trained_model.sav', 'rb'))
    scaler = pickle.load(open('scaler.sav', 'rb'))
    return model, scaler

loaded_model, scaler = load_model_and_scaler()

# Creating a function for prediction
def diabetes_prediction(input_data):
    try:
        # Convert input to float and handle empty strings
        input_data_float = []
        for val in input_data:
            if val == '' or val is None:
                return "❌ Please fill in all fields with valid numbers."
            input_data_float.append(float(val))
        
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data_float)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        # ✅ Standardize the input data using saved scaler
        std_data = scaler.transform(input_data_reshaped)
        
        # Make prediction on standardized data
        prediction = loaded_model.predict(std_data)
        
        if (prediction[0] == 0):
            return '✅ Good News! The person is likely NOT diabetic'
        else:
            return '⚠️ Warning! The person shows HIGH RISK for diabetes'
    except ValueError:
        return "❌ Please enter valid numeric values for all fields."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"
    
def main():
    
    # Header Section
    st.markdown('<h1 class="main-header">🩺 Diabetes Risk Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced ML-Powered Health Assessment Tool</p>', unsafe_allow_html=True)
    
    
    # Sidebar Information
    with st.sidebar:
        st.markdown("### 📊 About This Application")
        st.info("""
        🤖 **Machine Learning Model**: Support Vector Machine (SVM)
        
        📈 **Dataset**: Pima Indians Diabetes Database
        
        🎯 **Accuracy**: High-precision classification
        
        ⚡ **Real-time**: Instant risk assessment
        """)
        
        st.markdown("### 📋 Input Parameter Guidelines")
        st.markdown("""
        - **Pregnancies**: 0-20 (number of times)
        - **Glucose**: 0-200 mg/dL
        - **Blood Pressure**: 0-200 mmHg  
        - **Skin Thickness**: 0-100 mm
        - **Insulin**: 0-500 μU/mL
        - **BMI**: 10.0-67.0 kg/m²
        - **Pedigree Function**: 0.078-2.420
        - **Age**: 1-120 years
        """)
        
        st.markdown("### 🏥 Health Disclaimer")
        st.warning("""
        ⚠️ This tool is for educational and screening purposes only. 
        
        Always consult healthcare professionals for medical advice.
        """)
    
    # Main Content Area
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        pass
    
    # Input Form in Two Columns
    st.markdown("### 🔍 Health Parameter Input (Enter Details Precisely)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏥 Medical History")
        Pregnancies = st.number_input(
            "👶 Number of Pregnancies", 
            min_value=0, max_value=20, value=None, step=1,
            help="Total number of pregnancies",
            placeholder="Enter number of pregnancies"
        )
        
        Glucose = st.number_input(
            "🍬 Glucose Level (mg/dL)", 
            min_value=0, max_value=300, value=None, step=1,
            help="Plasma glucose concentration (Normal: 70-100 mg/dL)",
            placeholder="Enter glucose level"
        )
        
        BloodPressure = st.number_input(
            "💓 Blood Pressure (mmHg)", 
            min_value=0, max_value=200, value=None, step=1,
            help="Diastolic blood pressure (Normal: 60-80 mmHg)",
            placeholder="Enter blood pressure"
        )
        
        SkinThickness = st.number_input(
            "📏 Skin Thickness (mm)", 
            min_value=0, max_value=100, value=None, step=1,
            help="Triceps skin fold thickness",
            placeholder="Enter skin thickness"
        )
    
    with col2:
        st.markdown("#### 🔬 Metabolic Markers")
        Insulin = st.number_input(
            "💉 Insulin Level (μU/mL)", 
            min_value=0, max_value=900, value=None, step=1,
            help="2-Hour serum insulin (Normal: 16-166 μU/mL)",
            placeholder="Enter insulin level"
        )
        
        BMI = st.number_input(
            "⚖️ BMI (kg/m²)", 
            min_value=10.0, max_value=70.0, value=None, step=0.1,
            help="Body Mass Index (Normal: 18.5-24.9)",
            placeholder="Enter BMI value"
        )
        
        DiabetesPedigreeFunction = st.number_input(
            "🧬 Diabetes Pedigree Function", 
            min_value=0.0, max_value=3.0, value=None, step=0.001, format="%.3f",
            help="Genetic diabetes likelihood score",
            placeholder="Enter pedigree function value"
        )
        
        Age = st.number_input(
            "🎂 Age (years)", 
            min_value=1, max_value=120, value=None, step=1,
            help="Age in years",
            placeholder="Enter age"
        )
    
    # Prediction Button
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        predict_button = st.button("🔮 Analyze Diabetes Risk", use_container_width=True)
    
    # Prediction Logic
    if predict_button:
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, 
                     Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        with st.spinner('🔄 Analyzing your health parameters...'):
            diagnosis = diabetes_prediction(input_data)
            
            if "NOT diabetic" in diagnosis:
                st.markdown(f"""
                <div class="prediction-box negative">
                    {diagnosis}
                    <br><small>Keep maintaining your healthy lifestyle! 🌟</small>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
                
                # Health Tips for Non-Diabetic
                st.markdown("### 💚 Maintain Your Health")
                st.success("""
                **Keep up the good work:**
                - 🥗 Continue balanced nutrition
                - 🏃‍♂️ Regular physical activity  
                - 💧 Stay hydrated
                - 😴 Get adequate sleep
                - 🔄 Regular health check-ups
                """)
                
            elif "HIGH RISK" in diagnosis:
                st.markdown(f"""
                <div class="prediction-box positive">
                    {diagnosis}
                    <br><small>Please consult a healthcare professional immediately! 🏥</small>
                </div>
                """, unsafe_allow_html=True)
                
                # Health Recommendations for High Risk
                st.markdown("### 🚨 Immediate Action Required")
                st.error("""
                **Important Steps to Take:**
                - 🏥 **Consult an endocrinologist or your doctor immediately**
                - 📋 Get comprehensive diabetes testing (HbA1c, fasting glucose)
                - 🥗 Start dietary modifications
                - 🏃‍♂️ Begin regular exercise routine
                - 📱 Monitor blood glucose levels regularly
                - 💊 Follow all medical recommendations
                """)
                
                st.markdown("### 📞 Emergency Contacts")
                st.info("""
                If you experience symptoms like excessive thirst, frequent urination, 
                blurred vision, or fatigue, seek immediate medical attention.
                """)
            
            else:
                st.error(diagnosis)
    
    # Footer with Contact Information
    st.markdown("""
    <div class="footer">
        <h3>👨‍💻 About the Developer</h3>
        <div class="contact-info">
            <h4>Daivagna Parmar</h4>
            <hr>
            <a href="https://github.com/daivagnaa" target="_blank" class="github-link">
                🔗 GitHub: @daivagnaa
            </a>
            <a href="mailto:devparmar1895@gmail.com" class="email-link">
                📧 devparmar1895@gmail.com
            </a>
        </div>
        <hr>
        <p><em>⚠️ Medical Disclaimer: This application is for educational and screening purposes only. 
        Always consult qualified healthcare professionals for medical diagnosis and treatment.</em></p>
        <p><small>© 2024 Daivagna Parmar | Built with ❤️ using Streamlit & Python</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()