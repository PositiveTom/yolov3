from cProfile import label
import xml.etree.ElementTree as ET
import os

#   input:
xmlfilepath = "../../../data/VOCdevkit/VOC2007/Annotations"

#   output:
voc_classpath = "./voc_class.txt"

labelsets = set()

total_xml = os.listdir(xmlfilepath)

for xmlpath in total_xml:
    with open(xmlfilepath+'/'+xmlpath) as in_file:
        tree = ET.parse(in_file)
        root = tree.getroot()
        labels = root.iter('object')
        for obj in labels:
            label = obj.find('name').text
            labelsets.add(label)

with open(voc_classpath, 'w') as f:
    for i, label in enumerate(labelsets):
        if i != 19:
            f.write(label + '\n')
        else:
            f.write(label)