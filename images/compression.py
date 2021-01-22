import os, glob
from PIL import Image
def compress_images(source=False, dest=False, quality=30):
    if os.path.isdir(source) == False or os.path.isdir(dest) == False:
        print("Please input directory")
        return ""
    if source:
        os.chdir(source)
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    for image in images:
        print(image)
        img = Image.open(image)
        if dest:
            os.chdir(dest)
            img.save("Compressed_"+image, optimize=True, quality=quality)
            if source:
                os.chdir(source)

if __name__ == "__main__":
    source = "/mnt/c/Users/2020A00139/Pictures/beer_data_raw/train_images"
    dest = "/mnt/c/Users/2020A00139/Pictures/beer_data/train_images"
    quality = 30
    compress_images(source, dest, quality)