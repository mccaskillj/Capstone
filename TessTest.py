from pytesseract import image_to_string
import Image

print image_to_string(Image.open('Images/hello.png'))

