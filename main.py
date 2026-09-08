from PIL import Image

im = Image.open("ascii-pineapple.jpg")

width, height = im.size
print(f"Successfully loaded image!\nImage size: {width} * {height}")
