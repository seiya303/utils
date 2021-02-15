from glob import glob
import os, re

jpgs = glob("/home/seiya/cardboardbox_det_loc/keras-retinanet/datasets/cardboard2/images/*.jpg")
jpgs = sorted(jpgs, key=lambda jpg: int(re.findall("[0-9]+", jpg)[-1]))

xmls = glob("/home/seiya/cardboardbox_det_loc/keras-retinanet/datasets/cardboard2/voclabels/*.xml")
xmls = sorted(xmls, key=lambda xml: int(re.findall("[0-9]+", xml)[-1]))

num = 0
for xml in xmls:
    data = ""
    with open(xml, 'r+') as fin:
        data = fin.read()
        path = re.search("(?<=\<path>)(.*?)(?=\</path>)", data).group()
        data = data.replace(path, jpgs[num])
    with open(xml, 'w+') as fout:
        fout.write(data)
    num += 1