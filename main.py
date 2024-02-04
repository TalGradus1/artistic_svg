from utils.filter_functions import remove_background
from PIL import Image
import numpy as np


input_image = Image.open(r"C:\Users\tal\Downloads\b4cd5dd08baf72fe86fbf5dfd41fc14d.jpg")

input_array = np.array(input_image)
output_array = remove_background(input_array)

output_image = Image.fromarray(output_array)
output_image.save('output_image.png')