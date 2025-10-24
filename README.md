# 🧠 Cement Strength Prediction – FastAPI App

This project is a **FastAPI-based web application** that predicts the **strength tendency of cement samples** using a pre-trained **Logistic Regression model**.
Users can input parameters like **temperature**, **ambient temperature**, and **sample type** to get instant predictions.

---

## 🚀 Features

* Web interface built with **Jinja2 templates**
* Backend powered by **FastAPI**
* Machine Learning model loaded via **joblib**
* Dynamic prediction endpoint (`/predict`)
* Lightweight and easily deployable

---

## 🧩 Project Structure

```
project/
│
├── app.py                  # Main FastAPI application
├── logistic_model.pkl      # Pre-trained logistic regression model
├── templates/
│   └── index.html          # Web form UI for input and results
├── static/                 # (Optional) CSS/JS assets
└── README.md               # Project documentation
```

---


## 🧠 How It Works

1. User opens the home page (`/`) and fills the form.
2. The app sends a POST request to `/predict` with:

   * `temperature`
   * `ambient_temperature`
   * `sample` (selected type)
3. The FastAPI backend:

   * Formats input into a DataFrame.
   * Sets one-hot encoding for the selected sample type.
   * Passes the data to the logistic regression model.
4. Model returns:

   * `"Tending to strong..."` if output = 1
   * `"Tending to weak..."` if output = 0

---

## ▶️ Running the App Locally

```bash
uvicorn app:app --reload
```

Then open in browser:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧾 Example Prediction

**Input:**

* Temperature: 32
* Ambient Temperature: 28
* Sample: `Sample_0.4 Nominal`

**Output:**

```
{
  "prediction": "Tending to strong..."
}
```

---

## 💡 Future Improvements

* Add data visualization on results page
* Integrate confidence score display
* Add user authentication (optional)
* Deploy to Render, Vercel, or AWS Lambda

---




