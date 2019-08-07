xml, csv, python

Extrahuje z dat sesbíraných z NUŠL a OpenAIRE uložených v xml následující údaje: identifikátor záznamu, rok vydání/zveřejnění, jazyk(y) dokumentu, typ(y) dokumentu, čísla projektů.

soubory xml2csv_zdroj definují, jak a odkud se mají údaje v rámci xml sbírat
soubory collecting_zdroj volají funkce z předešlého souboru a zapisují získané údaje do csv. Pro NUŠL je přidán aspekt roku, jelikož bylo potřeba filtrovat záznamy pro rozmezí 2014-2018 včetně. V případě výskytu chyby se vytvoří soubor, který zapíše název souboru a typ chyby.
