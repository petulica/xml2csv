import os
from xml.etree import ElementTree as et
import csv


from xml2csv import identifier, doc_type, langs, year, projects

BASE = os.path.dirname(__file__)
directory = os.path.join(BASE, "testovaci_nusl")

with open('NUSL.csv', 'a',  newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=";")
    writer.writerow(["id", "doc_type", "langs", "year", "projects", "no_of_projects"])

for file in os.listdir(directory):
    with open(os.path.join(directory,file), encoding="utf8") as f:
        tree = et.parse(f)
        root = tree.getroot()
        row = [identifier(root), doc_type(root), langs(root), year(root), projects(root), len(projects(root))]

    with open('NUSL.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";")
        if int(row[3]) >= 2014 and int(row[3]) != 2019:
            writer.writerow(row)

#pokud skript vyhodí chybu, tak úkoly vyřešené před pádem se uloží do mezipaměti a při novém spuštění skriptu se tyto řádky vytisknou do csv, takže např. se může do csv zapsat 5x záhlaví

csvFile.close()
