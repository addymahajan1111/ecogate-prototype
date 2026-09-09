import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="EcoGate - River Mouth Interceptor", layout="wide")

st.title("🌊 EcoGate: River-Estuary Debris & Effluent Interceptor")
st.caption("Central Telemetry & Edge-AI Waste Classifier System | SIH Prototype")

# Top KPI metrics
col1, col2, col3, col4 = st.columns(4)

np.random.seed(int(datetime.now().timestamp()) % 1000)
ph_val = round(np.random.uniform(6.8, 8.2), 2)
turbidity_val = int(np.random.uniform(40, 110))
bin_level = int(np.random.uniform(55, 85))
flow_speed = round(np.random.uniform(1.2, 2.2), 2)

is_alert = ph_val < 7.0 or turbidity_val > 95

with col1:
    st.metric("Water pH Level", f"{ph_val}", delta="-0.3 (Acidic Shift)" if ph_val < 7.0 else "Normal")
with col2:
    st.metric("Turbidity", f"{turbidity_val} NTU", delta="High Suspended Solids" if turbidity_val > 90 else "Clear")
with col3:
    st.metric("Collection Bay Fill", f"{bin_level}%", delta="Empty Soon" if bin_level > 75 else "Optimal")
with col4:
    st.metric("Flow Speed", f"{flow_speed} m/s", delta="Generating 120W Hydro")

if is_alert:
    st.error("⚠️ **CRITICAL ALERT:** Industrial effluent detected! CPCB alert ticket dispatched with GPS tag.")
else:
    st.success("✅ Water parameters within permissible CPCB standards.")

st.markdown("---")

left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.subheader("📊 24-Hour Estuary Telemetry Log")
    timestamps = pd.date_range(end=datetime.now(), periods=24, freq='h')
    df = pd.DataFrame({
        "Time": timestamps,
        "pH": np.random.normal(7.4, 0.3, 24),
        "Turbidity (NTU)": np.random.normal(65, 12, 24),
        "Trash Collected (kg)": np.cumsum(np.random.randint(15, 40, 24))
    })
    
    st.line_chart(df.set_index("Time")[["pH", "Turbidity (NTU)"]])
    st.subheader("♻️ Cumulative Waste Diverted (kg)")
    st.bar_chart(df.set_index("Time")["Trash Collected (kg)"])

with right_col:
    st.subheader("📷 Edge-AI River Surface Camera Feed")
    detection_mode = st.selectbox(
        "Demonstrate Detection Scenario to Judges:",
        ["Scenario 1: Plastic Bottles & Polythene", "Scenario 2: Factory Chemical Foam", "Scenario 3: Organic Driftwood (Safe)"]
    )
    
    if detection_mode == "Scenario 1: Plastic Bottles & Polythene":
        st.info("🎯 **Detected:** 14 PET Bottles (94% conf.), 3 Polythene Bags (89% conf.)")
        st.write("**Action:** Conveyor active. Diverted to Landfill Hopper #1.")
    elif detection_mode == "Scenario 2: Factory Chemical Foam":
        st.warning("⚠️ **Detected:** Heavy Industrial Surfactant Foam (96% conf.)")
        st.write("**Action:** Activated secondary barrier skirt + flagged upstream plant.")
    else:
        st.success("🌿 **Detected:** Organic Fallen Branches & Leaves")
        st.write("**Action:** Bypass open. Natural biomass allowed through for aquatic life.")
    
    st.markdown("---")
    st.subheader("⚡ Automated System Status")
    st.checkbox("Hydrokinetic Turbine (Self-Powering)", value=True, disabled=True)
    st.checkbox("Acoustic Fish Deterrent Beacon (400 Hz)", value=True, disabled=True)
    st.checkbox("Automated Trash Sluice Gate", value=True, disabled=True)

    if st.button("🔄 Refresh Live Sensor Packets"):
        st.rerun()
