import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    if degree == 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)':
        return 'Bachelor’s degree'
    if degree == 'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':
        return 'Master’s degree'
    if degree == 'Associate degree (A.A., A.S., etc.)':
        return 'Associate degree'
    else:
        return "Less than a Bachelor's Degree"
@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "YearsCodePro", "EdLevel", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df["YearsCodePro"] = df["YearsCodePro"].apply(experience)
    df["EdLevel"] = df["EdLevel"].apply(degree_status)
    country_map = country_cutoffs(df["Country"].value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 250000]
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Developer Salaries")
    st.write("""### Stack Overflows Developer Survey 2023""")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data,  autopct="%1.1f%%", shadow=True)
    ax1.legend(data.index, title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax1.axis("equal")
    st.pyplot(fig1)

    st.dataframe(df)

    st.write("""### Mean Salary Based on Country""")

    data = df["Salary"].groupby(df["Country"]).mean().sort_values(ascending=True)

    st.line_chart(data)

    st.write("""### Mean Salary Based on Experience""")

    data = df["Salary"].groupby(df["YearsCodePro"]).mean().sort_values(ascending=True)

    st.line_chart(data)

    st.write("""### Mean Salary Based on Education""")

    data = df["Salary"].groupby(df["EdLevel"]).mean().sort_values(ascending=True)

    st.line_chart(data)

    st.write("""### Mean Salary Based on Employment""")

    data = df["Salary"].groupby(df["Employment"]).mean().sort_values(ascending=True)

    st.line_chart(data)
    




