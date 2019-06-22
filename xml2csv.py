#xml2csv
import csv
import os
from xml.etree import ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, "testovaci_nusl\\https___invenio.nusl.cz_oai2d_verb=GetRecord&metadataPrefix=marcxml&identifier=oai_invenio.nusl.cz_395994.xml")

tree = et.parse(xml_file)

root = tree.getroot()
"""
for element in root:
	print("element", element.tag, element.attrib, element.text, ";")
	for child in element:
		print("child", child.tag, child.attrib, child.text, ";")
		for subelement in child:
			print("subel", subelement.tag, ":", subelement.text)
			for record in subelement:
				print("record", record.tag, ":", record.text)
				for field in subelement:
					print("filed", field.tag, ":", field.text)
					for subfield in field:
						subelement.findtext("999")
						print("subfield", subfield.tag, ":",  subfield.attrib)
						for obsah in subfield:
							print("obsah", obsah.tag,":", obsah.attrib, ":" ,obsah.text)
	
	#    v tagu je "subfield", attribute je kod podpole a text je konečně obsah pole, co potřebuju zapsat do csv
"""
for field in root.iter('{http://www.loc.gov/MARC21/slim}datafield'):
	field_999 = field.findall('tag="999" ind1="C" ind2="1"')
	print(field_999)
	for subfield in root.iter('{http://www.loc.gov/MARC21/slim}subfield'):
		print(subfield.attrib, ":", subfield.text)
		

"""output = open('nusl.csv', 'w')
list_head = []
csv_writer = csv.writer(output)"""



#open xml
#take to a to
#write in csv
#close xml

#pro dokumenty extra skript, který řekne vezmi jen ty a ty typy dok, kde je průnik.
#podle identifátoru poznám do jaké sbírky to patří
