import os
from xml.etree import ElementTree as et
from collections import Counter

# base_path = os.path.dirname(os.path.realpath(__file__))
#
# xml_file = os.path.join(base_path, "testovaci_nusl",
#                         "https___invenio.nusl.cz_oai2d_verb=GetRecord&metadataPrefix=marcxml&identifier=oai_invenio.nusl.cz_395994.xml")
#
# tree = et.parse(xml_file)
#
# root = tree.getroot()


def identifier(root):
    fields = root.findall(".//{http://www.loc.gov/MARC21/slim}controlfield[@tag='001']")
    for field in fields:
        return field.text


def doc_type(root):
    fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='980']")
    for field in fields:
        for subfield in field:
            return subfield.text


def langs(root):
    fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='041']")
    for field in fields:
        result = []
        for subfield in field:
            result.append(subfield.text)
        # if subfield.attrib["code"] == "a" or "b":
        return result


def year(root):
    fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='046']")
    for field in fields:
        for subfield in field:
            if subfield.attrib["code"] == "k":
                return subfield.text


def projects(root):
    fields = root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='999']")
    result = []
    for field in fields:
        for subfield in field:
            #C1 = C1['ind2']
            #if subfield.tag[C1] == "1" and subfield.attrib["code"] == "a":
            if subfield.attrib["code"] == "a":
                result.append(subfield.text)
    return result
