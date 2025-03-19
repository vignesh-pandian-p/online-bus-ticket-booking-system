import os

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def extract_text_from_files(directory):
    extracted_data = {}
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            if filename.endswith((".php", ".html", ".css", ".js")):
                extracted_data[filename] = extract_text_from_txt(file_path)

    return extracted_data

# Example usage
directory_path = "C:\xampp\htdocs\bus-ticket-booking-system-cloud"
text_data = extract_text_from_files(directory_path)

# Print extracted text
for file, text in text_data.items():
    print(f"--- Text from {file} ---\n{text}\n")
