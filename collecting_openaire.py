import os
from xml.etree import ElementTree as et
import csv


from xml2csv_openaire import identifier, doc_type, langs, year, projects

xml_path = "D:/diplomka/praktická_část/download_xml/oaire_data/"

def make_headers():
    # create file, make headers
    with open('OpenAIRE_complete.csv', 'a',  newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";")
        writer.writerow(["id", "doc_type", "langs", "year",
                         "projects", "no_of_projects"])


def extracting_data(file):
    print(file)
    try:
        with open(file, encoding="utf8") as f:
            tree = et.parse(f)
            document_root = tree.getroot()
            results = document_root.findall("./results/result")
            # print(results)
            print(len(results))
            for result in results:
                # print(result)
                row = [identifier(result), doc_type(result), langs(
                    result), year(result), projects(result), len(projects(
                    result))]
                # print(row)

                with open('OpenAIRE_complete.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile, delimiter=";")
                    writer.writerow(row)

    except Exception as err:
        print(err)
        with open("errors_aire.txt", "a") as error_file:
            error_file.write(f"{file}: {str(err)}")


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
