import streamlit as st

def show_developers_page():
    st.title("Developers Page")
    st.write("This page contains information about the developers of this project.")

    # Create a two-column layout
    col1, col2 = st.columns([5, 1])  # Adjust the column widths as needed

    with col1:
        st.write("""
        ### Arpit Sachin Kadam

        I'm currently a 3rd-year AIML student at Shivajrao S. Jondhale College of Engineering. Passionate about software development and artificial intelligence, I’ve been working on several projects that blend machine learning with real-world applications.

        **Skills:**
        - Python, Data Analysis
        - Machine learning frameworks: TensorFlow, Scikit-learn, and various machine learning libraries
        - Streamlit, yfinance, Prophet

        **Projects:**
        - **Software Developer Salary Prediction**: Developed a machine learning model that predicts salaries based on developer characteristics.
        - **Stock Forecast App**: Created a stock forecasting tool using Streamlit and Prophet.
        - **Breast-Cancer-Prediction-using-different-Machine-Learning-Algorithms**: Created a machine learning model that predicts whether a patient has breast cancer or not.
        - **Movie-Recommendation-System-using-Machine-Learning**: Created a movie recommendation system using machine learning.
        - **Facial-Recognition-with-Realtime-Database**: Created a facial recognition system using OpenCV, Dlib, Cmake, CVZone, Firebase-admin, and Python.
        - **Plant-Diseases-Prediction-Model**: Created a machine learning model that predicts whether a plant is healthy or not.

        **Hobbies:**
        - Listening to music
        - Exploring the latest advancements in AI
        - Gaming
        - Bike racing and Cruising
        - Car riding

        In the future, I aim to apply my knowledge and leadership skills to create innovative solutions for real-world problems.
        """)

    with col2:
        st.image("assets\my image.jpg", width=150)  


    st.write("### Contact Info")
    st.write("Email: arpitkadam922@example.com")
    st.write("Github: https://github.com/ArpitKadam")
    st.write("Phone: 8767375722")

    st.write("### Internship Certificates")
    st.image("assets/certificate-1.jpg", caption="Internship Certificate 1")
    st.image("assets/certificate-2.jpg", caption="Internship Certificate 2")
    st.image("assets/certificate-3.jpg", caption="Internship Certificate 3")
    




