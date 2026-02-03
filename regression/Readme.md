## 📘 Regression – End-to-End Demo (Training → Deployment)

This folder contains an end-to-end example of building and deploying a **house rent regression model**.

The goal is to show:

1. How to explore data and train a regression model in a notebook
2. How the trained model is saved
3. How the model is served using a simple API
4. How a basic UI can consume the model predictions


## 📂 Folder Structure

```
regression/
│
├── end_to_end_indian_house_rent_regression.ipynb
│
├── deployment_demo/
│   ├── app.py
│   └── index.html
│
└── artifacts/
    └── rent_model_pipeline_YYYYMMDD_HHMMSS.joblib
```


## 🧪 Step 1: Train the model (Notebook)

1. Open the notebook:

   ```
   end_to_end_indian_house_rent_regression.ipynb
   ```
2. Run the notebook end-to-end.
3. At the end, the trained **scikit-learn pipeline** is saved using `joblib`
   into the `artifacts/` folder.

> The deployment code automatically picks the **latest model** from the `artifacts` folder, so no filename changes are needed.


## 🚀 Step 2: Start the Prediction API (FastAPI)

1. Open a **new terminal / Git Bash**
2. Navigate to the deployment folder:

   ```bash
   cd deployment_demo
   ```
3. Run the FastAPI server:

   ```bash
   uv uvicorn app:app --reload
   ```
4. The API will start at:

   ```
   http://127.0.0.1:8000
   ```

---

## 🌐 Step 3: Open the UI and Predict

1. HTML Based approch. 
   Open the file:

   ```
   deployment_demo/index.html
   ```

   (Double-click or open with a browser)

   or 
   Run a python-based server (like Streamlit) to serve the UI:
   ```
   uv run streamlit run streamlit_app.py
   ```


2. Enter or modify the property details.

3. Click **Predict Rent**.

4. The predicted monthly rent will be displayed on the page.



## 🧠 What this demonstrates

* How a trained ML model moves from **notebook → production**
* How preprocessing lives inside a **pipeline**
* How a model can be exposed as a **REST API**
* How a simple frontend can consume model predictions

This setup is intentionally minimal and meant **only for learning and demonstration purposes**.


