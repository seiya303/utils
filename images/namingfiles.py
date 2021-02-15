from glob import glob
import os
import re

files = glob("/home/seiya/yoloboard/cus_data/test_images/*.jpg")

files = sorted(files, key=lambda file: int(re.findall("[0-9]+", file)[-1]))

with open('/home/seiya/yoloboard/cus_data/cus_testing.txt', 'w') as f:
    for file in files:
        f.write("%s\n" % file)
