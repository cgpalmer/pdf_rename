import os
import pdfplumber

for file in os.listdir("submission_upload/"):
    with pdfplumber.open(f"submission_upload/{file}") as pdf:
        page_to_read = pdf.pages[0]
        extracted_text = page_to_read.extract_text()
        formatted_text = extracted_text.splitlines()
        name = formatted_text[1]
        os.rename(f"submission_upload/{file}", f"submission_upload/{name}_{file}.pdf")