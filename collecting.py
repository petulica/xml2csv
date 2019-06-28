import os
from xml.etree import ElementTree as et
import csv

from xml_nusl.xml2csv import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")


for file in os.listdir(directory):
    with open(os.path.join(directory,file)) as f:
        tree = et.parse(f)
        root = tree.getroot()
        row = [identifier(root), doc_type(root), langs(root), year(root), projects(root), len(projects(root))]

    with open('NUSL.csv', 'a') as csvFile:
        writer = csv.writer(csvFile, delimiter=";")
        if int(row[3]) >= 2014 and int(row[3]) != 2019:
            writer.writerow(row)

csvFile.close()


