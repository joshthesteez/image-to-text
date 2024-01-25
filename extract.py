import os
import glob
from PIL import Image
import pytesseract
import pyperclip

def get_latest_screenshot_path():
    screenshot_directory = r"path-to-screenshots-directory"
    screenshots = glob.glob(os.path.join(screenshot_directory, "*.png"))
    # find the most recent screenshot
    return max(screenshots, key=os.path.getctime, default=None)

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def copy_text_to_clipboard(text):
    pyperclip.copy(text)
    print("Text copied to clipboard.")

if __name__ == "__main__":
    # Get the path of the most recent screenshot
    latest_screenshot_path = get_latest_screenshot_path()

    if latest_screenshot_path:
        # Extract text from the image
        extracted_text = extract_text_from_image(latest_screenshot_path)

        if extracted_text:
            # Copy the extracted text to the clipboard
            copy_text_to_clipboard(extracted_text)
        else:
            print("Text extraction failed.")
    else:
        print("No screenshot found.")
