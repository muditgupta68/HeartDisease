import streamlit as st
import joblib
import sklearn
from time import sleep

# python -m streamlit run healthPred.py


def main():
    url = 'https://www.kaggle.com/code/muditgupta1086/heart-disease'
    st.markdown("🔗[Source Code](%s)" % url)

    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:#232323;text-align:center">Heart Disease Forecasting</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('rf_heartForecastModel')
    st.divider()

    age = st.slider('Enter your age', 18, 100)
    # st.write(age, 'years old')

    gender = st.selectbox(
        'Enter your Age',
        ('Male', 'Female'))

    genderSwitcher = {
        "Male": 0,
        "Female": 1
    }
    gender = genderSwitcher.get(gender)
    # st.write(gender)

    cp = st.selectbox(
        'Chest Pain Type',
        ('Typical angina', 'Atypical agina', 'Non-anginal pain', 'Asymptomatic'))
    cpSwitcher = {
        'Typical angina': 0, 'Atypical agina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3
    }
    cp = cpSwitcher.get(cp)
    # st.write(cp)

    bps = st.slider('Resting blood pressure (mm Hg)', 94, 200)

    chol = st.slider('Chelostrol level (mg/dl)', 120, 600)

    fbs = st.selectbox(
        'fasting blood sugar > 120 mg/dl',
        ('Yes', 'No'))

    fbsSwitcher = {
        'Yes': 1,
        'No': 0
    }

    fbs = fbsSwitcher.get(fbs)
    # st.write(fbs)

    restecgSwitch = {
        'Normal': 0,
        'ST-T abnormality': 1,
        'Left Ventricular hypertrophy': 2
    }

    restecg = st.selectbox(
        'Resting Electro Cardiographic ',
        ('Normal', 'ST-T abnormality', 'Left Ventricular hypertrophy'))

    restecg = restecgSwitch.get(restecg)
    # st.write(restecg)

    thalach = st.slider('Maximum Heart rate achieved', 71, 202)

    exang = st.selectbox(
        'Exercise induced angina',
        ('Yes', 'No')
    )

    exangSwitch = {
        'Yes': 1,
        'No': 0
    }

    exang = exangSwitch.get(exang)
    # st.write(exang)

    oldpeak = st.number_input(
        'ST depression induced by exercise relative to rest', 0.00, 7.00)
    # st.write('The current number is ', oldpeak)

    slope = st.selectbox('Slope of the peak exercise ST segment',
                         ('Unsloping', 'Flat', 'Downsloping'))

    slopSwitcher = {
        'Unsloping': 1,
        'Flat': 2,
        "Downsloping": 3
    }

    slope = slopSwitcher.get(slope)
    # st.write(slope)

    ca = st.selectbox('Number of major vessels',
                      (0, 1, 2, 3))

    thal = st.selectbox('Thalassemia Status',
                        ('Normal', 'Fixed Defect', 'Reversable Defect'))

    thalSwitcher = ({
        'Normal': 1, 'Fixed Defect': 2, 'Reversable Defect': 3
    })

    thal = thalSwitcher.get(thal)
    # st.write(thal)

    if st.button('Predict Now'):
        
        with st.spinner('Model is predicting...'):
            sleep(5)
        
        prediction = model.predict(
            [[age, gender, cp, bps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        print(prediction[0])
        
        if(prediction[0]==0):
            st.balloons()
            st.success(f"You don't have heart disease 👍 Enjoy!")
        else:
            st.warning('You have heart disease‼ Consult doctor and opt for procedures 🥼🩺')
        


if __name__ == '__main__':
    main()
