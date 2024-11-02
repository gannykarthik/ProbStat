import streamlit as st
import os
import base64

# Define path to study materials
MATERIALS_PATH = "materials"

# App Title
st.title("Probability and Statistics")
st.title("-Ganapathi Karthik V")

# Sidebar Navigation
st.sidebar.title("Modules")
modules = [f"Module {i + 1}" for i in range(7)]
selected_module = st.sidebar.selectbox("Select a Module", modules)

# Content for each module
content_directory = {
    "Module 1": [
        "Statistics and data analysis", 
        "Measures of central tendency", 
        "Measure of Dispersion",
        "Moments-Skewness-Kurtosis (Concepts only)"
    ],
    "Module 2": [
        "Random variables", 
        "Probability mass function, distribution and density functions",
        "Joint probability distribution and Joint density functions",
        "Marginal, Conditional distribution and Density functions",
        "Mathematical expectation and its properties- Covariance, Moment generating function"
    ],
    "Module 3": [
        "Correlation - Rank Correlation; Partial and Multiple correlation",
        "Regression and Multiple regression"
    ],
    "Module 4": [
        "Binomial distribution", 
        "Poisson distributions", 
        "Normal distribution", 
        "Gamma distribution",
        "Exponential distribution", 
        "Weibull distribution"
    ],
    "Module 5": [
        "Testing of hypothesis - Types of errors - Critical region, Procedure for testing of hypothesis",
        "Large sample tests- Z test for Single Proportion- Difference of Proportion- Mean and difference of means"
    ],
    "Module 6": [
        "Small sample tests- Student's t-test, F-test- chi-square test", 
        "Goodness of fit - independence of attributes",
        "Design of Experiments - Analysis of variance – One way-Two way-Three way classifications",
        "Classifications - CRD-RBD- LSD"
    ],
    "Module 7": [
        "Basic concepts- Hazard function-Reliabilities of series and parallel systems- System Reliability - Maintainability",
        "Preventive and repair maintenance- Availability"
    ]
}

# Display Module Content
st.header(selected_module)

# Subsection for Module Topics
st.subheader("Module Topics")
topics = content_directory.get(selected_module, [])
for topic in topics:
    st.markdown(f"- {topic}")

# Study Materials Section
st.subheader("Study Materials Directory")
module_path = os.path.join(MATERIALS_PATH, selected_module.replace(" ", ""))
if os.path.exists(module_path):
    files = os.listdir(module_path)
    if files:
        for file_name in files:
            file_path = os.path.join(module_path, file_name)
            
            # Display file name with preview
            st.write(f"📄 {file_name}")
            
            # Preview the content based on file type
            if file_name.endswith((".png", ".jpg", ".jpeg")):  # Image files
                st.image(file_path)
            elif file_name.endswith(".txt"):  # Text files
                with open(file_path, "r") as text_file:
                    st.text(text_file.read())
            elif file_name.endswith(".pdf"):  # PDF files
                # Display PDF in the app
                with open(file_path, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                    # Encode PDF bytes to base64 for rendering
                    b64 = base64.b64encode(PDFbyte).decode()
                    st.markdown(f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="500"></iframe>', unsafe_allow_html=True)
                    st.download_button(label="Download PDF", data=PDFbyte, file_name=file_name)
            else:
                st.write("Unsupported file type.")
    else:
        st.write("No study materials available in this module.")
else:
    st.write("This module is not yet available.")

# Tutorial Sheets Section
st.subheader("Tutorial Sheets")
tutorial_sheets_path = os.path.join(MATERIALS_PATH, "Tutorial Sheets")
if os.path.exists(tutorial_sheets_path):
    files = os.listdir(tutorial_sheets_path)
    if files:
        for file_name in files:
            file_path = os.path.join(tutorial_sheets_path, file_name)
            
            # Display file name with preview
            st.write(f"📄 {file_name}")
            
            # Preview the content based on file type
            if file_name.endswith((".png", ".jpg", ".jpeg")):  # Image files
                st.image(file_path)
            elif file_name.endswith(".txt"):  # Text files
                with open(file_path, "r") as text_file:
                    st.text(text_file.read())
            elif file_name.endswith(".pdf"):  # PDF files
                # Display PDF in the app
                with open(file_path, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                    # Encode PDF bytes to base64 for rendering
                    b64 = base64.b64encode(PDFbyte).decode()
                    st.markdown(f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="500"></iframe>', unsafe_allow_html=True)
                    st.download_button(label="Download PDF", data=PDFbyte, file_name=file_name)
            else:
                st.write("Unsupported file type.")
    else:
        st.write("No tutorial sheets available.")
else:
    st.write("Tutorial sheets directory does not exist.")

# Admin Upload Section (Hidden in Sidebar)
st.sidebar.subheader("Admin: Upload Materials")
upload_file = st.sidebar.file_uploader("Choose a file to upload", type=['pdf', 'txt', 'jpg', 'jpeg', 'png'])
upload_module = st.sidebar.selectbox("Select module to upload", modules)
upload_button = st.sidebar.button("Upload File")

# Handle the upload
if upload_button and upload_file is not None:
    # Define the upload path
    upload_path = os.path.join(MATERIALS_PATH, upload_module.replace(" ", ""))
    os.makedirs(upload_path, exist_ok=True)  # Create module folder if it doesn't exist
    file_path = os.path.join(upload_path, upload_file.name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(upload_file.getbuffer())
    
    st.sidebar.success(f"File '{upload_file.name}' uploaded successfully to {upload_module}.")

# Placeholder for bookmarks and search functionality
st.sidebar.write("🔖 Bookmark your favorite topics")
st.sidebar.write("🔍 Search within modules")

# Footer with interactive learning suggestions
st.markdown("---")
st.markdown("### Interactive Learning")
st.markdown("Explore exercises and quizzes to test your knowledge (coming soon!)")

