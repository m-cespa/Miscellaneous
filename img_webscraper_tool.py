# img webscraper tool

import bs4, requests, os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import re

# Insert total chapters
chapters = 200
title = 'SoloLevelling'

def natural_sort_key(s):
    """Generate a sort key that sorts numerically as well as alphabetically."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def images_to_pdf(folder_path, output_directory):
    """Creates merged pdf of all items in folder_path at the path specified by output_directory"""
    # Extract the directory name from the folder path
    directory_name = os.path.basename(os.path.normpath(folder_path))
    # Construct the output PDF file path using the specified output directory
    output_pdf = os.path.join(output_directory, f'{directory_name}.pdf')
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Loop through all files in specified folder path
    for file_name in sorted(os.listdir(folder_path), key=natural_sort_key):
        file_path = os.path.join(folder_path, file_name)
        # Only process image files
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img = Image.open(file_path)
            img_width, img_height = img.size
            # Create a new PDF page with the size of the image
            c.setPageSize((img_width, img_height))
            # Add image (maintaining its original size) to PDF
            c.drawImage(ImageReader(img), 0, 0, width=img_width, height=img_height)
            # Create a new PDF page
            c.showPage()
    
    c.save()

# Create base URLs
urls = ['https://w10.sololevelingmanga.org/manga/solo-leveling-chapter-' + f'{chap}/' for chap in range(1, chapters + 1)]
base_path = '/Users/michele/Desktop/Documents-Local/WebScraping/' + title
os.makedirs(base_path, exist_ok=True)

for chap, url in enumerate(urls):
    # Make directory for each chapter inside '<title>/dummy'
    path = '/Users/michele/Desktop/Documents-Local/WebScraping/' + title + '/dummy'
    chapter_dir = os.path.join(path, f'chapter_{chap + 1}')
    os.makedirs(chapter_dir, exist_ok=True)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.find_all('img')

    img_urls = []
    seen_urls = set()  # To keep track of URLs we have already seen

    for img in img_tags:
        # Prefer 'data-src' if available, otherwise fallback to 'src'
        img_url = img.get('data-src') or img.get('src')
        # Ensure it's a valid URL and not a duplicate
        if img_url and 'http' in img_url and img_url not in seen_urls:
            seen_urls.add(img_url)  # Mark this URL as seen
            img_urls.append(img_url)  # Use list to preserve order

    for page, ele in enumerate(img_urls):
        save_path = os.path.join(chapter_dir, 'page_' + f'{page + 1}' + '.png')
        res = requests.get(ele)
        res.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(res.content)

    # Create output directory for PDFs
    output_dir = base_path
    output_pdf = os.path.join(output_dir, f'chapter_{chap + 1}.pdf')
    images_to_pdf(chapter_dir, output_dir)





    

    




