import pickle
import streamlit as st

# Load the pre-trained classifier from a pickle file
with open('iris_classifier.pickle', 'rb') as f:
    classifier = pickle.load(f)

def main():
    # Set page configuration
    st.set_page_config(page_title="Iris Species Classifier Using Decision Tree Algorithm", layout="wide")

    # Custom CSS to change background color and style input fields
    st.markdown("""
        <style>
        .reportview-container {
            background-color: #f0f8ff; /* Light blue background */
        }
        .css-1l02u2i {
            border-radius: 50%; /* Make input fields circular */
            padding: 10px;
            text-align: center;
        }
        .css-1l02u2i input {
            border-radius: 50%; /* Ensure the input itself is circular */
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title('Iris Species Classifier Using Decision Tree Algorithm')
    st.markdown("""
        This application predicts the species of an Iris flower based on its measurements. 
        Enter the sepal and petal dimensions to get the prediction.
    """)

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
        sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, step=0.1, format="%.1f")

    with col2:
        petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
        petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, step=0.1, format="%.1f")

    # Prediction button
    if st.button('Predict'):
        # Make a prediction using the classifier
        prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # Display the prediction result
        species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        st.success(f'The predicted species is {species[prediction[0]]}.')

    # Footer
    st.markdown("""
        ---
        Made with Softwarica College of IT and E-commerce by [Shrawan Thakur](https://shrawanthakur.com)
    """)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
