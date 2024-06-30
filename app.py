import streamlit as st
from gooddata_component import gooddata_component

st.title("Custom Streamlit Component with React")

# Use your custom component
name = gooddata_component(name="Streamlit with React")
st.write(f"Hello, {name}!")