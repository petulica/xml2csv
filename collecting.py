import os
from xml.etree import ElementTree as et
import csv

from xml_nusl.xml2csv_openaire import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")
# xml_path = "H:/datova_analyza/xml2csv/dp"
xml_path = "/home/semtex/Projekty/TEST_PROJECTS/xml_nusl/xml_nusl/test_openaire/one"


def make_headers():
    # create file, make headers
    with open('OpenAIRE3.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";")
        writer.writerow(["id", "doc_type", "langs", "year",
                         "projects", "no_of_projects"])


# input_path = "/Users/xah/web/xahlee_info/python/"

def extracting_data(file):
    # for file in os.listdir(xml_path):

    # with open("files.txt", 'a', newline='') as txtfile:
    #     txtfile.write(f"{file}\n")

    print(file)
    try:
        with open(file, encoding="utf8") as f:
            tree = et.parse(f)
            document_root = tree.getroot()
            results = document_root.findall("./results/result")
            # print(results)
            # print(len(results))
            i = 0
            for result in results:
                i += 1
                id_ = identifier(result)
                print(i, "################################################################")
                if id_ in identifiers_list:
                    with open("duplicit_id.txt", 'a') as f:
                        f.write(f"{file}:  {id_}\n")


                else:
                    identifiers_list.append(id_)

                if id_ in ids:
                    ids[id_].append(file)
                else:
                    ids[id_] = [file]

                row = [identifier(result), doc_type(result), langs(
                    result), year(result), projects(result), len(projects(
                    result))]
                print(row)

                with open('OpenAIRE3.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile, delimiter=";")
                    writer.writerow(row)

    except Exception as err:
        print(err)
        with open("errors_aire.txt", "a") as error_file:
            # error_file.write(f"{file}: {str(err)} /n")
            error_file.write(f"{file}: {str(err)}\n")
        # csvFile.close()


# PROGRAM START
make_headers()
i = 0
identifiers_list = []
files = []
ids = {}
for dir_path, subdir_list, file_list in os.walk(xml_path):
    for fname in file_list:
        # print(i)
        # i += 1
        files.append(fname)
        print(files)
        full_path = os.path.join(dir_path, fname)
        extracting_data(full_path)

print(ids)
duplicit_ids = {k: v for (k, v) in ids.items() if (v is not None) and (len(v) > 1)}
none_ids = {k: v for (k, v) in ids.items() if v is None}
with open("duplicit_ids.py", "w") as f:
    f.write(str(duplicit_ids))

with open("none_ids.py", "w") as f:
    f.write(str(none_ids))

# pokud skript vyhodí chybu, tak úkoly vyřešené před pádem se uloží do mezipaměti a při novém spuštění skriptu se tyto řádky vytisknou do csv, takže např. se může do csv zapsat 5x záhlaví
