import streamlit as st
import requests

# ---- Config ----
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Rental Price Prediction Demo",
    layout="wide"
)

# ---- Simple CSS to make it look similar to the HTML page ----
st.markdown(
    """
    <style>
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .title {
        text-align: center;
        font-size: 36px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .result {
        text-align: center;
        font-size: 26px;
        font-weight: 800;
        color: #0f766e;
        margin-top: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Rental Price Prediction Demo</div>', unsafe_allow_html=True)

# ---- Default values (same as your sample row) ----
default_house_type = "2 BHK Flat"
default_locality = "Powai"
default_city = "Mumbai"
default_furnishing = "Semi-Furnished"

# From your sample data
city_options = ["Mumbai", "Pune", "Bangalore", "New Delhi", "Nagpur"]
furnishing_options = ["Semi-Furnished", "Unfurnished", "Fully Furnished"]

# ---- Inputs ----
st.markdown('<div class="section-title">Property Details</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    house_type = st.text_input("House Type", value=default_house_type)
with c2:
    locality = st.text_input("Locality", value=default_locality)
with c3:
    city = st.selectbox("City", options=city_options, index=city_options.index(default_city))
with c4:
    furnishing = st.selectbox("Furnishing", options=furnishing_options, index=furnishing_options.index(default_furnishing))

st.markdown('<div class="section-title">Numerical Features</div>', unsafe_allow_html=True)

# Use 5 columns; Streamlit wraps nicely based on screen width.
n1, n2, n3, n4, n5 = st.columns(5)
with n1:
    area = st.number_input("Area (sqft)", value=897.0, min_value=0.0, step=1.0)
with n2:
    beds = st.number_input("Beds", value=2, min_value=0, step=1)
with n3:
    bathrooms = st.number_input("Bathrooms", value=2, min_value=0, step=1)
with n4:
    balconies = st.number_input("Balconies", value=0, min_value=0, step=1)
with n5:
    area_rate = st.number_input("Area Rate", value=134.0, min_value=0.0, step=1.0)

st.write("")  # spacing

# ---- Predict ----
predict_clicked = st.button("Predict Rent", use_container_width=True)

if predict_clicked:
    payload = {
        "house_type": house_type,
        "locality": locality,
        "city": city,
        "area": float(area),
        "beds": int(beds),
        "bathrooms": int(bathrooms),
        "balconies": int(balconies),
        "furnishing": furnishing,
        "area_rate": float(area_rate),
    }

    try:
        resp = requests.post(API_URL, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        st.markdown(f'<div class="result">Predicted Monthly Rent: {result["predicted_rent"]}</div>',
                    unsafe_allow_html=True)
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it is running at http://127.0.0.1:8000")
    except requests.exceptions.HTTPError:
        st.error(f"FastAPI returned an error: {resp.status_code} - {resp.text}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
