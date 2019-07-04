import os
from xml.etree import ElementTree as et
import csv


from xml2csv_openaire import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")
xml_path = os.listdir("H:/datova_analyza/RIV")

with open('OpenAIRE.csv', 'a',  newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=";")
    writer.writerow(["id", "doc_type", "langs", "year", "projects", "no_of_projects"])

i = 1
for file in os.listdir(xml_path):
    print(i)
    i += 1
    print(file)
    # try:
    with open(os.path.join(xml_path,file), encoding="utf8") as f:
        tree = et.parse(f)
        root = tree.getroot()
        row = [identifier(root), doc_type(root), langs(root), year(root),  projects(root), len(projects(root))]

    with open('OpenAIRE.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";")
        year_row = row[3]
        if year_row is not None:
            if len(year_row) > 4:
                year_row = year_row[:4]
            if int(year_row) >= 2014 and int(year_row) != 2019:
                writer.writerow(row)
    # except:
    #     with open("errors_aire.txt", "a") as err:
    #         err.write(f"{file} \n")
    #     continue


#pokud skript vyhodí chybu, tak úkoly vyřešené před pádem se uloží do mezipaměti a při novém spuštění skriptu se tyto řádky vytisknou do csv, takže např. se může do csv zapsat 5x záhlaví

csvFile.close()
# err.close()
