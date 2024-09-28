import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_devtype = data["le_devtype"]
le_education = data["le_education"]
le_employment = data["le_employment"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the software developer salary""")

    countries = (
        "Australia",
        "Austria",
        "Belgium",
        "Brazil",
        "Canada",
        "Czech Republic",
        "Denmark",
        "Finland",
        "France",
        "Germany",
        "India",
        "Israel",
        "Italy",
        "Netherlands",
        "New Zealand",
        "Norway",
        "Poland",
        "Portugal",
        "Romania",
        "Russian Federation",
        "Spain",
        "Sweden",
        "Switzerland",
        "Turkey",
        "Ukraine",
        "United Kingdom of Great Britain and Northern Ireland",
        "United States of America",
    )

    education = (
        "Less than a Bachelor's Degree",
        "Bachelor’s degree",
        "Master’s degree",
        "Associate degree",
    )

    employment = (
        'Employed, full-time',
        'Independent contractor, freelancer, or self-employed',
        'Employed, part-time',
        'Employed, full-time;Independent contractor, freelancer, or self-employed',
        'Employed, full-time;Employed, part-time',
        'Independent contractor, freelancer, or self-employed;Employed, part-time',
        'Employed, full-time;Independent contractor, freelancer, or self-employed;Employed, part-time',
        'Independent contractor, freelancer, or self-employed;Retired',
        'Employed, full-time;Retired', 'Employed, part-time;Retired'
    )

    DevType = (
        'Developer, back-end', 'Developer, full-stack',
        'System administrator', 'Developer, QA or test',
        'Developer, front-end',
        'Data scientist or machine learning specialist',
        'Data or business analyst', 'Research & Development role',
        'Database administrator',
        'Developer, desktop or enterprise applications', 'Engineer, data',
        'Security professional', 'Product manager',
        'Cloud infrastructure engineer',
        'Developer, embedded applications or devices',
        'Developer Experience', 'Engineering manager', 'Developer, mobile',
        'DevOps specialist', 'Senior Executive (C-Suite, VP, etc.)',
        'Engineer, site reliability', 'Project manager',
        'Academic researcher', 'Blockchain', 'Developer, game or graphics',
        'Hardware Engineer', 'Educator', 'Scientist', 'Developer Advocate',
        'Designer', 'Student', 'Marketing or sales professional'
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    employment = st.selectbox("Employment", employment)
    DevType = st.selectbox("DevType", DevType)
    yearsExperience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, employment, DevType, yearsExperience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X[:, 2] = le_employment.transform(X[:, 2])
        X[:, 3] = le_devtype.transform(X[:, 3])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
