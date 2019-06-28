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
    field = root.findall(".//{http://www.openarchives.org/OAI/2.0/}identifier")
    return field[0].text


def langs(root):
    fields = root.findall(".//language")
    for field in fields:
        return field.attrib["classid"]


def year(root):
    fields = root.findall(".//dateofacceptance")
    return fields[0].text[:4]


def doc_type(root):
    fields = root.findall(".//instancetype[@classname]")
    doc = []
    for field in fields:
        doc.append(field.attrib["classname"])
    return doc


def projects(root):
    fields = root.findall(".//rel/code")
    codes = []
    for field in fields:
        codes.append(field.text)
    return codes



if __name__ == "__main__":
    # langs()
    # year()
    # doc_type()
    # identifier()
    # projects()
