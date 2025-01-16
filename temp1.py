
import pytesseract
from PIL import ImageGrab
imgObj = ImageGrab.grabclipboard()

pathToTesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = pathToTesseract
text = pytesseract.pytesseract.image_to_string(imgObj)
print(text)