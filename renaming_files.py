import os
import pdfplumber
import time
start_time = time.time()
x = 1
for item in os.listdir("submission_upload/"):
      
#     # with pdfplumber.open(f"submission_upload/{file}") as pdf:
#     #     page_to_read = pdf.pages[0]
#     #     extracted_text = page_to_read.extract_text()
#     #     formatted_text = extracted_text.splitlines()
#     #     name = formatted_text[1]
    os.rename(f"submission_upload/{item}", f"submission_upload/{x}.jpg")
    x = x + 1

# import os
# os.getcwd()
# collection = "submission_upload"
# for i, filename in enumerate(os.listdir(collection)):
#     os.rename("submission_upload" + filename, "C:/darth_vader/" + str(i) + ".jpg")

# print("My program took", time.time() - start_time, "to run")