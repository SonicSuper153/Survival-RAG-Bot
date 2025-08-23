# import fitz
# import os

# class FileReader:
#     def __init__(self):
#         self.output_dir = r"C:\Users\Ishmeet\OpenAI\tools\texts"

#     def pdf_to_txt(self, url: str):
#         document = fitz.open(url)
#         pdf_text = {}

#         for page_number in range(document.page_count):
#             page = document.load_page(page_number)
#             text = page.get_text()
#             pdf_text[page_number + 1] = text

#         document.close()

#         base_name = os.path.basename(url)
#         name_without_ext = os.path.splitext(base_name)[0]

#         output_dir = self.output_dir
#         os.makedirs(output_dir, exist_ok=True)

#         output_file = os.path.join(output_dir, f"{name_without_ext}.txt")
#         output_file += 

#         with open(output_file, "w", encoding="utf-8") as f:
#             for page, text in pdf_text.items():
#                 f.write(f"Text from page {page}:\n{text}\n\n")

#         print(f"Extracted text saved to {output_file}")
#         return output_file
    
#     def convert_pdfs_to_txt(self, pdf_folder):
#         if not os.path.exists(pdf_folder):
#             raise FileNotFoundError(f"[ERROR] PDF folder {pdf_folder} does not exist.")

#         pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
#         if not pdf_files:
#             raise FileNotFoundError("[ERROR] No PDF files found in the folder.")

#         print(f"[INFO] Found {len(pdf_files)} PDF files.")
#         for pdf_file in pdf_files:
#             self._pdf_to_txt(os.path.join(pdf_folder, pdf_file))

#     def _pdf_to_txt(self, pdf_path):
#         doc = fitz.open(pdf_path)
#         pdf_text = {}

#         for page_number in range(doc.page_count):
#             page = doc.load_page(page_number)
#             text = page.get_text()
#             pdf_text[page_number + 1] = text

#         doc.close()

#         base_name = os.path.basename(pdf_path)
#         name_without_ext = os.path.splitext(base_name)[0]
#         output_file = os.path.join(self.output_dir, f"{name_without_ext}.txt")

#         with open(output_file, "w", encoding="utf-8") as f:
#             for page, text in pdf_text.items():
#                 f.write(f"Text from page {page}:\n{text}\n\n")

#         print(f"[INFO] Extracted text saved to {output_file}")

import fitz
import os

class FileReader:
    def __init__(self):
        self.output_dir = r"C:\Users\Ishmeet\OpenAI\tools\texts"

    def pdf_to_txt(self, pdf_path: str):
        # Open PDF
        document = fitz.open(pdf_path)

        # Extract PDF metadata (title if available)
        pdf_metadata = document.metadata
        pdf_title = pdf_metadata.get("title") or os.path.basename(pdf_path)
        pdf_text = f"Document Title: {pdf_title}\n\n"  # Add title at the top

        # Extract text from all pages
        for page_number in range(document.page_count):
            page = document.load_page(page_number)
            text = page.get_text()
            pdf_text += f"\n\n--- Page {page_number + 1} ---\n{text}"
        # Prepare output file
        base_name = os.path.basename(pdf_path)
        name_without_ext = os.path.splitext(base_name)[0]
        output_file = os.path.join(self.output_dir, f"{name_without_ext}.txt")

        # Write text to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(pdf_text)

        print(f"[INFO] Extracted text saved to {output_file}")
        return output_file

    def convert_folder_pdfs(self, pdf_folder: str):
        if not os.path.exists(pdf_folder):
            raise FileNotFoundError(f"[ERROR] Folder {pdf_folder} does not exist.")

        pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]
        if not pdf_files:
            raise FileNotFoundError("[ERROR] No PDF files found in the folder.")

        print(f"[INFO] Found {len(pdf_files)} PDF files.")
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            self.pdf_to_txt(pdf_path)
