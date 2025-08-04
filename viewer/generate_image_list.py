import os
import re

def numeric_sort(filename):
    nums = re.findall(r'\d+', filename)
    return int(nums[0]) if nums else 0

folder = "assets/images"
images = sorted(
    [f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".png"))],
    key=numeric_sort
)

with open("image_list.js", "w") as f:
    f.write("const imageList = [\n")
    for img in images:
        name = os.path.splitext(img)[0]  # Remove .png or .jpg
        f.write(f'  "{name}",\n')
    f.write("];\n")
