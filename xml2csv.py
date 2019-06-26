import os
from xml.etree import ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, "testovaci_nusl", "https___invenio.nusl.cz_oai2d_verb=GetRecord&metadataPrefix=marcxml&identifier=oai_invenio.nusl.cz_395994.xml")

tree = et.parse(xml_file)

root = tree.getroot()

fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='999']")
for field in fields:
	for subfield in field:
		if subfield.attrib["code"] == "a":
			print(subfield.text)

