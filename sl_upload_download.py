import streamlit as sl
import os

# Let's get rid of the "Made with Streamlit" at the bottom of the page
sl.markdown("""
<style>
.css-cio0dv.ea3mdgi1
{
            visibility: hidden;
}            
</style>
""", unsafe_allow_html= True
)
# to get things going, write streamlit run main.py in the terminal and hit enter

sl.title("Uploading Files")
sl.markdown("---")

sl.subheader("Upload Shapefiles")
shapefiles = sl.file_uploader("Please upload your shapefile", type=["shp","shx","dbf","prj","xml","sbn","sbx","cpg"], accept_multiple_files=True,)
if shapefiles is not None:
    for file in shapefiles:
        file_details = {"FileName": file.name, "FileType": file.type}
        sl.write(file_details) 
        # Saving
        with open(os.path.join("/Users/israelgolden/Documents/GitHub/StreamlitDev/DownloadFolder",file.name), "wb") as f:
            f.write(file.getbuffer())
        sl.success("File saved")