import streamlit as st
import time

st.set_page_config(page_title="Package Delivery Status", page_icon="📦")

# Title and description
st.title("📦 Package Delivery Status Tracker")
st.write("Enter your tracking ID below to simulate the delivery progress of your package.")

# Input for tracking ID
tracking_id = st.text_input("🔍 Enter Tracking ID", "")

# Simulated delivery stages
delivery_stages = [
    "Order Placed",
    "Dispatched from Warehouse",
    "In Transit",
    "Arrived at Destination City",
    "Out for Delivery",
    "Delivered"
]

# Button to start tracking
if st.button("Track Package"):
    if tracking_id.strip() == "":
        st.warning("Please enter a valid tracking ID.")
    else:
        st.success(f"Tracking Package ID: {tracking_id}")
        st.write("📦 Simulating delivery status...")

        # Simulate the delivery process
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i, stage in enumerate(delivery_stages):
            time.sleep(1.5)  # Simulate delay
            progress = int(((i + 1) / len(delivery_stages)) * 100)
            progress_bar.progress(progress)
            status_text.markdown(f"**Current Status:** `{stage}`")

        st.balloons()
        st.success("🎉 Package Delivered Successfully!")
