import streamlit as st
import pandas as pd
import os
import zipfile
import gdown

# download all the necesary files for the project 

zip_url = 'https://drive.google.com/file/d/11KFS8Kiyivn0vvaOJwHiNo42CAduzLuV/view?usp=drive_link'
file_id = zip_url.split('/d/')[1].split('/')[0]
download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
folder_storage = '../data_files'

st.header("Title")


def download_extract_zip(gdrive_url, out_dir):
    """
    Download a google drive Zip archive and extract it to wanted folder

    Args:
        gdrive_url (str): Google Drive url of the download zip archive.
        out_dir (str): Path where to extract the zip files.
    """
    # create output path if not existing
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    try:
        # Download zip file
        local_zip_path = os.path.join(out_dir, "data.zip")
        gdown.download(gdrive_url, local_zip_path, quiet=False)

        # Extract zip file
        with zipfile.ZipFile(local_zip_path, 'r') as zipf:
            zipf.extractall(out_dir)
            print(' -- Extraction terminée --')
        
        # Remove zip file
        os.remove(local_zip_path)
    except Exception as e:
        print("*** ERREUR ***", e)



if __name__ == "__main__":
    
    if not os.path.exists('../data_files/RAW_interactions.csv') : 
        download_extract_zip(download_url, folder_storage)


    # Initialize session state for login status and clean_df
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

   
