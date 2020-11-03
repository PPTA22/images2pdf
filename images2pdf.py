import os
from PIL import Image

files = os.listdir()
files.pop()
print(files)

print()
images = []
for f in files:
    images.append(Image.open(f).convert('RGB'))

images[0].save('all.pdf',save_all=True,append_images=images[1:])
