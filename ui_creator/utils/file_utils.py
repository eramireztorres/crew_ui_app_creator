import os
from ui_creator.utils.code_extractor import PythonCodeExtractor

def txt_to_py(files_map):
    extractor = PythonCodeExtractor()
    for txt_file, py_file in files_map.items():
        if not os.path.exists(txt_file):
            print(f"Warning: '{txt_file}' does not exist. Skipping conversion.")
            continue
        with open(txt_file, "r", encoding="utf-8") as infile:
            content = infile.read()
        extracted_code = extractor.extract_code(content)
        if extracted_code:
            with open(py_file, "w", encoding="utf-8") as outfile:
                outfile.write(extracted_code + "\n")
            print(f"Converted '{txt_file}' to '{py_file}' successfully.")
        else:
            with open(py_file, "w", encoding="utf-8") as outfile:
                outfile.write(content)
            print(f"Warning: No valid code blocks in '{txt_file}'. Entire content saved to '{py_file}'.")
