import streamlit as st
import tarfile
import io
import gzip

# Create a Streamlit app
st.title("Tar.gz File Explorer")

# Upload file
uploaded_file = st.file_uploader("Upload a .tar.gz file", type=["tar.gz"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.tar.gz'):
        with st.spinner("Extracting and listing files..."):
            # Read the uploaded .tar.gz file
            file_buffer = io.BytesIO(uploaded_file.read())
            
            # Extract the files
            try:
                with tarfile.open(fileobj=gzip.GzipFile(fileobj=file_buffer, mode='rb')) as archive:
                    file_list = archive.getnames()
                    st.success(f"File {uploaded_file.name} was successfully extracted.")
                    
                    # List the files in the archive
                    st.subheader("Files in the Archive:")
                    for file in file_list:
                        st.write(file)
            except tarfile.TarError:
                st.error("Error extracting the .tar.gz file.")
    else:
        st.error("Invalid file format. Please upload a .tar.gz file.")

