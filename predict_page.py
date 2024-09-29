import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
def country_cutoffs(country, cutoff):
    map = {}
    for i in range(len(country)):
        if country.values[i] >= cutoff:
            map[country.index[i]] = country.index[i]
        else:
            map[country.index[i]] = 'Others'
    return map

def experience(Years):
    if Years == 'More than 50 years':
        return 50
    if Years == 'Less than 1 year':
        return 0.5
    return float(Years)
    
def degree_status(degree):
    if degree == "Bachelorâ€™s degree (B.A., B.S., B.Eng., etc.)":
        return "Bachelor degree"
    if degree == "Masterâ€™s degree (M.A., M.S., M.Eng., MBA, etc.)":
        return "Master degree"
    if degree == "Associate degree (A.A., A.S., etc.)":
        return "Associate degree"
    else:
        return "Less than a Bachelor Degree"


data = pd.read_excel("Book1.xlsx")
df = data[['Country', 'EdLevel', 'YearsCodePro', 'DevType', 'Employment', 'ConvertedCompYearly']]
df = df[df['ConvertedCompYearly'].notnull()]
df = df.dropna()
df["YearsCodePro"] = df["YearsCodePro"].apply(experience)
df["EdLevel"] = df["EdLevel"].apply(degree_status)
country_map = country_cutoffs(df["Country"].value_counts(), 400)
df["Country"] = df["Country"].map(country_map)
df = df[df["ConvertedCompYearly"] <= 150000]
df = df[df['Country'] != 'Others']
df = df[df['DevType'] != 'Other (please specify):']

x = df.drop('ConvertedCompYearly', axis =1)
y = df['ConvertedCompYearly']

le_country = LabelEncoder().fit(x['Country'])
le_devtype = LabelEncoder().fit(x['DevType'])
le_employment = LabelEncoder().fit(x['Employment'])
le_education = LabelEncoder().fit(x['EdLevel'])

x['Country'] = le_country.transform(x['Country'])
x['DevType'] = le_devtype.transform(x['DevType'])
x['Employment'] = le_employment.transform(x['Employment'])
x['EdLevel'] = le_education.transform(x['EdLevel'])

regressor = DecisionTreeRegressor(max_depth=9, random_state=0)
regressor.fit(x, y)

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the software developer salary""")

    #st.write(data.tail())

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
        "Less than a Bachelor Degree",
        "Bachelor degree",
        "Master degree",
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


        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
