import os
from xml.etree import ElementTree as et

# base_path = os.path.dirname(os.path.realpath(__file__))
#
# xml_file = os.path.join(base_path, "testovaci_openaire", "openaire_exmaple.xml")
#
# tree = et.parse(xml_file)
#
# root = tree.getroot()


def identifier(root):
		for field in root.iter('{http://www.driver-repository.eu/namespace/dri}objIdentifier'):
			return field.text
'''
def identifier(root):

fields = root.findall(".//{http://www.driver-repository.eu/namespace/dri}objIdentifier")
    for field in fields:
        return field.attrib["id"]
    # if len(field) > 0:
    #     return field[0].text
'''

def langs(root):
    fields = root.findall(".//language")
    for field in fields:
        return field.attrib["classid"]
'''	
	for langs in root.iter('language'):
		return langs.attrib['classid']
'''

def year(root):
    fields = root.findall(".//dateofacceptance")
    if fields is not None:
        if fields[0].text:
            return fields[0].text[:4]


def doc_type(root):
    fields = root.findall(".//instancetype[@classname]")
    doc = set()
    for field in fields:
        doc.add(field.attrib["classname"])
    return doc


def projects(root):
    fields = root.findall(".//rel/code")
    codes = []
    for field in fields:
        codes.append(field.text)
    return codes



# if __name__ == "__main__":
    # langs(root)
    # year(root)
    # doc_type(root)
    # identifier(root)
    # projects(root)
