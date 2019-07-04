import os
from xml.etree import ElementTree as et
import csv


from xml2csv_openaire import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")
xml_path = "H:/datova_analyza/RIV"/os.scandir()
print(xml_path)