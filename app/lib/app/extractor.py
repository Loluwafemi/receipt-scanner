from lib.utils.mytypes import *
from typing import Union
from fastapi import UploadFile
from cv2 import imread, imdecode, IMREAD_COLOR, imshow, waitKey, destroyAllWindows, resize, INTER_AREA, selectROI, cvtColor, COLOR_BGR2GRAY, GaussianBlur, createCLAHE, MORPH_RECT, getStructuringElement, MORPH_OPEN, morphologyEx, filter2D, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, MORPH_CLOSE, threshold, THRESH_OTSU
import numpy as np
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

''' 
Input/Expected
UploadFile(filename='currentFile_1753789502840', size=980191, headers=Headers({'content-disposition': 'form-data; name="file"; filename="currentFile_1753789502840"', 'content-type': 'image/jpeg'}))
'''

    

async def extract_info_Func(file, name, bank)->RecieptResponseOutput:
    receiptScanner = await interpreteImage(file, name, bank)
    return receiptScanner


''' 
 define a dictionary storing all regex and match data to be found and iterate thought them while updating copy of the dictionary

 1. name: nullable
    if name is set, then find the name on the receipt, if found, update matching-data
2. bank: nullable
    if bank is set, then find the bank name on the receipt, if found update the matching-data

3. amount: required.
    use regex to find from the receipt the following:
        a. a currency followed by number
        b. then can have comma and dot
4. date: required.
    use regex to find from the receipt all possible format of date
    a. dd-mm-yyyy
    b. dd/mm/yyyy
    etc

'''



async def interpreteImage(image, name, bank):

    matching_data = dict()
    matching_data['status'] = True


    matching_regex = dict()
    matching_regex['name'] = name
    matching_regex['bank'] = bank
    matching_regex['amount'] = r'₦?\d{1,3}(?:,\d{3})*\.\d{2}'
    matching_regex['date'] = '|'.join(f'({pattern})' for pattern in date_patterns)
    

    readable = await image.read()
    readableBuffer = np.frombuffer(readable, np.uint8)
    readableImage = imdecode(readableBuffer, IMREAD_COLOR)

     # Step 1: Convert to grayscale
    readableToGray = cvtColor(readableImage, COLOR_BGR2GRAY)

    # Step 3: Noise reduction using Gaussian blur
    denoised = GaussianBlur(readableToGray, (3, 3), 0)

    # Step 4: Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)

    # Step 5: Morphological operations to clean up text
    # Create kernel for morphological operations
    kernel = getStructuringElement(MORPH_RECT, (1, 1))


    # Opening operation (erosion followed by dilation) to remove noise
    cleaned = morphologyEx(enhanced, MORPH_OPEN, kernel)

    # Step 6: Sharpen the image
    kernel_sharp = np.array([[-1,-1,-1],
                            [-1, 9,-1],
                            [-1,-1,-1]])
    sharpened = filter2D(cleaned, -1, kernel_sharp)


    # Step 7: Binarization using adaptive thresholding
    _, binary = threshold(sharpened, 0, 255, THRESH_BINARY + THRESH_OTSU)

    # Step 8: Final cleanup with morphological operations
    final_kernel = getStructuringElement(MORPH_RECT, (1, 1))
    final = morphologyEx(binary, MORPH_CLOSE, final_kernel)

    conversion_to_string = pytesseract.image_to_string(final)

    for key, value in matching_regex.items():
        # print(f'key: {key}, value: {value}')

        if key == 'name' or key == 'bank':
            search = re.search(value, conversion_to_string)
            if search:
                matching_data[key] = search.group()
            else:
                matching_data[key] = None
                matching_data['status'] = False

            continue
        
        # for required parameter
        if key == 'amount':
            match = find_largest_currency_amount(value, conversion_to_string)
            if match:
                matching_data[key] = match
                continue
            else:
                matching_data[key] = None
                matching_data['status'] = False
                continue
    
        if key == 'date':
            match = find_dates_with_pattern_info(value, conversion_to_string)
            if match:
                matching_data[key] = match
                continue
            else:
                matching_data[key] = None
                matching_data['status'] = False
                continue


    return matching_data



def find_largest_currency_amount(pattern, text):
    """
    Find the currency amount with the largest value (₦, N, NGN formats).
    
    Args:
        text (str): The text to search for currency amounts
        
    Returns:
        str or None: Largest currency amount or None if not found
    """
    matches = re.findall(pattern, text)
    if not matches:
        return None
    
    # Convert to numeric values for comparison
    amounts_with_values = []
    for match in matches:
        # Extract numeric part and convert to float
        numeric_part = re.sub(r'[₦NGN\s]', '', match).replace(',', '')
        try:
            value = float(numeric_part)
            amounts_with_values.append((match, value))
        except ValueError:
            continue
    
    if not amounts_with_values:
        return None
    
    # Return the amount with the largest value
    return max(amounts_with_values, key=lambda x: x[1])[0]



def find_dates_with_pattern_info(pattern, text):
    """
    Find dates and return them with information about which pattern matched.
    
    Args:
        text (str): The text to search for dates
        
    Returns:
        list: List of tuples (date, pattern_description)
    """
    pattern_descriptions = [
        "DD/MM/YYYY or MM/DD/YYYY format",
        "DD/MM/YYYY or MM/DD/YYYY format", 
        "YYYY/MM/DD format",
        "DD/MM/YY format",
        "Full month name format",
        "DD Full month YYYY format",
        "Abbreviated month format",
        "DD Abbreviated month format",
        "DDMMYYYY no separators",
        "DD-Mon-YYYY format",
        "ISO datetime format",
        "ISO date format"
    ]
    
    results = []
    for i, pattern in enumerate(date_patterns):
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            results.append(match)
    
    return results[0]