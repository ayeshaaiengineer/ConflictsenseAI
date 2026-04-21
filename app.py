import streamlit as st
from utils import get_news, clean_text, detect_conflict

from utils import get_news

st.title("ConflictSense AI")
st.write("AI-based Conflict & Misinformation Detection System")

# ---------- USER INPUT ----------
text = st.text_area("Enter News Text")

if st.button("Analyze"):
    if text == "":
        st.warning("Please enter some text first ⚠")
    else:
        cleaned = clean_text(text)
        result = detect_conflict(cleaned)

        st.success("Analysis Complete ✅")
        st.write("Original:", text)
        st.write("Cleaned:", cleaned)

        if "Conflict" in result:
            st.error(result)
        else:
            st.success(result)
