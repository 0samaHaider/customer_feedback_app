# feedback_classifier_app_v3.py
import streamlit as st
import pandas as pd
from transformers import pipeline
import io

# -------------------------------
# Load BERT sentiment model
# -------------------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")


sentiment_model = load_model()

# -------------------------------
# App UI
# -------------------------------
st.title("Customer Feedback Sentiment Classifier (BERT)")
st.write("Upload a CSV file with customer feedback and classify it into Positive, Negative, and Neutral categories.")

# -------------------------------
# Upload CSV
# -------------------------------
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'Feedback' not in df.columns:
        st.error("CSV must contain a column named 'Feedback'")
    else:
        feedback_texts = df['Feedback'].astype(str).tolist()

        # -------------------------------
        # Classify sentiment with loader
        # -------------------------------
        with st.spinner("Classifying feedback... Please wait."):
            results = sentiment_model(feedback_texts)

        # Add sentiment and confidence to DataFrame
        df['Sentiment'] = [res['label'] for res in results]
        df['Confidence'] = [res['score'] for res in results]

        # -------------------------------
        # Sort each sentiment by confidence descending
        # -------------------------------
        positive_df = df[df['Sentiment'] == 'POSITIVE'].sort_values(by='Confidence', ascending=False)
        negative_df = df[df['Sentiment'] == 'NEGATIVE'].sort_values(by='Confidence', ascending=False)
        neutral_df = df[df['Sentiment'] == 'NEUTRAL'].sort_values(by='Confidence', ascending=False)

        # -------------------------------
        # Display in tabs
        # -------------------------------
        tab1, tab2, tab3 = st.tabs(["Positive", "Negative", "Neutral"])

        with tab1:
            st.header("Positive Feedback")
            st.dataframe(positive_df)

        with tab2:
            st.header("Negative Feedback")
            st.dataframe(negative_df)

        with tab3:
            st.header("Neutral Feedback")
            st.dataframe(neutral_df)

        # -------------------------------
        # Download button for classified CSV
        # -------------------------------
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download Classified CSV",
            data=csv_buffer.getvalue(),
            file_name="classified_feedback.csv",
            mime="text/csv"
        )

        # -------------------------------
        # Bar chart at the end
        # -------------------------------
        st.subheader("Feedback Sentiment Counts")
        sentiment_counts = df['Sentiment'].value_counts()
        st.bar_chart(sentiment_counts)
