import os
from pdf2image import convert_from_path
from concurrent.futures import ProcessPoolExecutor

# Path to the folder containing the PDF files
pdf_folder = "pdfs"

# Path to the folder where you want to save the images
output_folder = "output"

# Get a list of all PDF files in the folder
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]


# Function to convert a PDF file to images
def convert_pdf_to_images(pdf_file):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    images = convert_from_path(pdf_path)

    # Create a folder for each PDF file
    folder_name = os.path.splitext(pdf_file)[0]
    folder_path = os.path.join(output_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Save each page as an image in the corresponding folder
    for i, image in enumerate(images):
        image_path = os.path.join(folder_path, f"{pdf_file}_page{i+1}.jpg")
        image.save(image_path)
        print(f"Saved {image_path}")

    # Delete the PDF file
    os.remove(pdf_path)
    print(f"Deleted {pdf_path}")


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        executor.map(convert_pdf_to_images, pdf_files)
