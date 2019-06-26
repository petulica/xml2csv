import os
from xml.etree import ElementTree as et
from collections import Counter

base_path = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, "testovaci_nusl", "https___invenio.nusl.cz_oai2d_verb=GetRecord&metadataPrefix=marcxml&identifier=oai_invenio.nusl.cz_395994.xml")

tree = et.parse(xml_file)

root = tree.getroot()

def identifier():
	fields = root.findall(".//{http://www.loc.gov/MARC21/slim}controlfield[@tag='001']")
	for field in fields:
		print(field.text)

def doc_type():
	fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='980']")
	for field in fields:
		for subfield in field:
			print(subfield.text)

def langs():
	fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='041']")
	for field in fields:
		for subfield in field:
			#if subfield.attrib["code"] == "a" or "b":
				print(subfield.text)
def year():
	fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='046']")
	for field in fields:
		for subfield in field:
			if subfield.attrib["code"] == "k":
				print(subfield.text)

def projects():
	fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='999']")
	for field in fields:
		for subfield in field:
			if subfield.attrib["code"] == "a":
				project_sum = sum(Counter("a").values())
				#print(subfield.text)
				print(project_sum)

identifier(), doc_type(),langs(), year(), projects()
