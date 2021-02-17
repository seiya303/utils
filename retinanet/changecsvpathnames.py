from glob import glob
import os, re

abspath = os.path.abspath("../images")

filepath = "/home/seiya/cardboardbox_det_loc/keras-retinanet/csv/val_annotations.csv"
lines = []
with open(filepath, "r+") as fin:
    for line in fin:
        strLatter = re.split('/', line, 2)[2]
        strFormer = re.split('/', line, 2)[0:2]
        string = '/'.join(strFormer)
        string = string.replace(string, abspath)
        line = string + "/" + strLatter
        lines.append(line)
with open(filepath, "w+") as fout:
    for line in lines:
        fout.write(line)