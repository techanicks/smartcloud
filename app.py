import streamlit as st
import os

st.set_page_config(page_title="SmartCloud", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: skyblue !important;
    }
    .stApp {
        background-color: skyblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("📁 SmartCloud: File Storage System")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "png", "jpg", "txt"])
if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

st.subheader("📂 Uploaded Files")
files = os.listdir(UPLOAD_FOLDER)

if files:
    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file)
        file_size_kb = os.path.getsize(path) / 1024

        col1, col2, col3 = st.columns([4, 2, 2])
        col1.markdown(f"📄 **{file}** ({file_size_kb:.1f} KB)")
        with open(path, "rb") as f:
            col2.download_button("Download", f, file_name=file)
        if col3.button("Delete", key=file):
            os.remove(path)
            st.warning(f"🗑️ {file} deleted.")
            st.experimental_rerun()
else:
    st.info("No files uploaded yet.")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-weight: bold;'>"
    "Created by Ayughtse Luper"
    "</div>",
    unsafe_allow_html=True
)
