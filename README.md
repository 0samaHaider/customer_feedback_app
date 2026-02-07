# Customer Feedback Sentiment Classifier (BERT + Streamlit)

## 📄 Overview

This project is a **web-based application** that classifies customer feedback into **Positive, Negative, and Neutral sentiments** using **BERT**. It provides an interactive interface with **Streamlit** where users can:

* Upload a CSV file of customer feedback.
* Automatically classify each feedback into **Positive, Negative, or Neutral**.
* View the results in **separate tabs** sorted by confidence.
* Download the **classified CSV** for further analysis.
* Visualize overall feedback distribution with a **bar chart**.

This app is ideal for **businesses and organizations** to quickly analyze customer feedback, detect issues, and monitor sentiment trends.

---

## ⚡ Features

1. **Upload CSV**: Easily upload feedback from surveys, reviews, or support tickets.
2. **Sentiment Analysis with BERT**: Uses a pretrained BERT model for accurate classification.
3. **Confidence Scores**: Displays confidence of each sentiment prediction.
4. **Tabs by Sentiment**: Positive, Negative, and Neutral feedback displayed separately.
5. **Sorted Tables**: Most confident predictions appear at the top.
6. **Bar Chart**: Visual summary of sentiment counts at the end.
7. **Download Classified CSV**: Export results for further reporting or analysis.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/0samaHaider/customer_feedback_app
cd customer_feedback_app
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
streamlit run feedback_classifier_app_v3.py
```

* A browser window will open with the Streamlit app.
* Upload your **CSV file** containing a column named `Feedback`.
* The app will classify all feedback and display the results.

---

## 📁 CSV Format

Your CSV file should have a **column named `Feedback`** containing the customer feedback texts. Example:

| Feedback                                             |
| ---------------------------------------------------- |
| "I love the new app update, very smooth!"            |
| "The product broke after a week, very disappointed." |
| "Delivery was okay, nothing special."                |

---
