import streamlit as st
from gooddata_component import gooddata_component

st.title("Streamlit with a React Component")

# Use your custom component
name = gooddata_component(name="GoodData User")
st.markdown("---")
st.write(f"Hello, {name}!")