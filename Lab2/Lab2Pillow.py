from PIL import Image, ImageDraw

img = Image.new('RGB', (1920, 1024), (255, 0, 255))

draw = ImageDraw.Draw(img)
draw.rectangle((50, 50, 500, 500), (0, 255, 0))

img.save('xD.png')