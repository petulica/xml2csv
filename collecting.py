import os
from xml.etree import ElementTree as et
import csv


from xml2csv_openaire import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")
# xml_path = "H:/datova_analyza/xml2csv/dp"
xml_path = "/home/dobiasj/Projects/xml2csv/input"


def make_headers():
    # create file, make headers
    with open('OpenAIRE3.csv', 'a',  newline='') as csvFile:
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
            print(results)
            print(len(results))
            for result in results:
                print(result)

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
            error_file.write(f"{file}: {str(err)}")
        # csvFile.close()


# PROGRAM START
make_headers()
i = 1
for dir_path, subdir_list, file_list in os.walk(xml_path):
    for fname in file_list:
        print(i)
        i += 1
        full_path = os.path.join(dir_path, fname)
        extracting_data(full_path)


# pokud skript vyhodí chybu, tak úkoly vyřešené před pádem se uloží do mezipaměti a při novém spuštění skriptu se tyto řádky vytisknou do csv, takže např. se může do csv zapsat 5x záhlaví
