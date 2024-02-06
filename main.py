from utils.filter_functions import remove_background,to_line_art
from PIL import Image
import numpy as np


input_image = Image.open(r"C:\Users\tal\Downloads\WhatsApp Image 2024-01-26 at 13.11.28.jpeg")

input_array = np.array(input_image)
output_array = remove_background(input_array)

output_image = Image.fromarray(output_array)
line_art_image = to_line_art(output_image)

line_art_image.save('output_image.png')