import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Setup Page Configuration
st.set_page_config(page_title="My App", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Screen 1", "Screen 2", "Screen 3", "Screen 4"])

# 3. Helper Function to Load HTML
def load_stitch_screen(folder_name, html_file):
    # This looks inside your folders (like serene_heart/screen1.html)
    path = os.path.join(folder_name, html_file)
    try:
        with open(path, "r", encoding='utf-8') as f:
            html_content = f.read()
        # Height 1000 is usually plenty, but you can increase it if needed
        components.html(html_content, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error(f"File not found: {path}. Check your GitHub folder/file names!")

# 4. Routing Logic
# Make sure the folder names in quotes match your GitHub folders exactly!
if page == "Screen 1":
    load_stitch_screen("serene_heart", "screen1.html")

elif page == "Screen 2":
    # Replace 'folder2' with the actual name of your second folder
    load_stitch_screen("folder2", "screen2.html")

elif page == "Screen 3":
    # Replace 'folder3' with the actual name of your third folder
    load_stitch_screen("folder3", "screen3.html")

elif page == "Screen 4":
    # Replace 'folder4' with the actual name of your fourth folder
    load_stitch_screen("folder4", "screen4.html")
