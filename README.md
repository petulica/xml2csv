# Převod xml do csv / From xml to csv

xml, csv, python 3

## Short description in English

Scripts exctract record identifiers, year of issue, languages of document, type(s) of document, project identifiers from data collected from NUSL and OpenAIRE for master's thesis purpose. The output of this repository is stored in dataset (*resource*.csv) available from Zenodo.

**thesis**  
Petra Černohlávková. (2019). Relationships of research outputs and projects: NUSL, Czech R&D Information System and OpenAIRE. Prague. Master thesis. Charles University. Supervisior Dvořák, Jan.

**dataset**  
Petra Černohlávková. (2019). Relationships of research outputs and projects in NUSL, Czech R&D Information System and OpenAIRE: Supporting Data for Master Thesis [Data set]. Zenodo. http://doi.org/10.5281/zenodo.3338675

The details of this repository, which are given in the rest of this file, are described in the Czech language.

## Popis v češtině

Extrahuje z dat sesbíraných z NUŠL a OpenAIRE uložených v xml následující údaje: identifikátor záznamu, rok vydání/zveřejnění, jazyk(y) dokumentu, typ(y) dokumentu, identifikátory projektů.

soubory xml2csv_*zdroj* definují, jak a odkud se mají údaje v rámci xml sbírat a collecting_*zdroj* je určen ke spouštění.  
soubory collecting_*zdroj* si volají funkce z xml2csv_*zdroj* a na základě ve spouštěcím souboru definovaných podmínek zapisují získané údaje do csv. V případě výskytu chyby se vytvoří soubor, který zapíše název souboru a typ chyby.

Záznamy získané z **NUŠL** byly uloženy po jednom do xml s vnitřním formátem MARC. V collecting byla stanovena podmínka: záznam musí mít rok vydání v rozmezí let 2014 - 2018 včetně (5 let stanoveno pro účely diplomové práce). 

Záznamy z **OpenAIRE** byly ukládány po sto záznamech do xml s vnitřním formátem oaf. Collecting je pro tento případ uzpůsobeno a v rámci jednoho xml vyhledá všechny v něm uložené záznamy, z nichž extrahuje výše zmíněné údaje.

Výstupy jsou uloženy v datasetu pod názvem *zdroj*.csv Ty jsou základem pro další analýzu pomocí repozitáře ![datova_analyza](https://github.com/petulica/datova_analyza)

Repozitář může být užit k vytěžování dat z xml s vnitřní strukturou MARC a oaf a k jejich následnému uložení do csv.
