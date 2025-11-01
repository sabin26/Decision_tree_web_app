import pickle
import streamlit as st
with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('Iris-Species-Classifier')
    sl = st.number_input('SepalLength')
    sw = st.number_input('SepalWidth')
    pl = st.number_input('PetalLength')
    pw = st.number_input('PetalWidth')

    if st.button('Predict'):
        result = clf.predict([[sl,sw,pl,pw]])

        if result==0:
            st.success('Setosa')

        elif result == 1:
            st.success('Versicolor')

        else:
            st.success('Virginica')
if __name__=='__main__':
    main()
