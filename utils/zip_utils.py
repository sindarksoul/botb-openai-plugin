import zipfile
import os

def extract_zip(path: str, dest: str):
    if not zipfile.is_zipfile(path):
        return {"error": "Invalid ZIP"}
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(dest)
    return {"status": "extracted", "to": dest}
