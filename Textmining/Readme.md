# Übersicht Textmining
Dieser Abschnitt beinhaltet eine kurze Erläuterung zu den einzelnen Themenbereichen des Textminings, bei dem aus dem unbearbeiteten Text eines Artikels die Daten extrahiert werden. Hierzu zählen eine Textverständlichkeit-, eine Topicmodelling- und Sentimentanalyse, sowie Wortzählung, usw.. Eine genaueren Beschreibung der einzelnen Arbeitsschritte anhand des Python-Skriptes, findet sich im jeweiligen Unterordner.

## Textverständlichkeit
Als Methode zur Ermittlung der Lesbarkeit wurde der "Flesch-Reading-Ease"-Index (FRE-Index) von [Flesch (1948)](https://psycnet.apa.org/record/1949-01274-001) verwendet, welcher später auf die deutsche Sprache von [Amistad (1978)](https://books.google.de/books/about/Wie_verst%C3%A4ndlich_sind_unsere_Zeitungen.html?id=kiI7vwEACAAJ&redir_esc=y) übertragen wurde und zur Auswertung von Zeitungstexten benutzt wurde].
Obwohl es bereits neuere Entwicklungen im Bereich der LEsbarkeitsanalyse gibt, findet der FRE-Index aufgrund seiner einfach Anwendung immer noch Verwendung in aktuellen Arbeiten, wie [Wasike (2018)](https://journals.sagepub.com/doi/pdf/10.1177/1464884916673387?casa_token=iTeO8-UtiLgAAAAA:FjTec3PYjhX0Y_Xh6WkqRLVtIDIG-a7Z5rhl53eJn7LxdGPqwFCwCmtc5SIX4pfWh8wvhBEX5h_O), [Rollins and Lewis (2013)](https://www.researchgate.net/profile/Louise-Patterson-4/publication/287511231_Gender_inequality_in_korean_firms_Results_from_stakeholders_interviews/links/5699ab6a08aea1476943748a/Gender-inequality-in-korean-firms-Results-from-stakeholders-interviews.pdf#page=155) und [Santos et al. (2020)](https://aclanthology.org/2020.lrec-1.176.pdf) zum Einsatz kommt, jedoch sollte der Index zur Einordnung in den Kontext zu modereneren Verfahren gesetzt werden. Ein ausführlicher Überblick zu aktuellen Entwicklungen im Bereich der Lesbarkeitsanalyse findet sich z.B. in [Benjamin (2012)](https://link.springer.com/content/pdf/10.1007/s10648-011-9181-8.pdf).
Zur Berechnung des FRE-Index wurde das Python-Modul [textstat](https://pypi.org/project/textstat/) verwendet.

## Topicmodellierung

Themenanzahl soll ermittelt werden

 Bei TopicModelling wird mithilfe eines Logarithmus die Verteilung der Themen über die Anzahl der Artikel ermittel. Herkömmliche Verfahren sind hierbei Latent Semantic Analysis (LSA), Probabilistic Latent Semantic Analysis (PLSA) und Latent Dirichlet Allocation (LDA), welche unter anderem [Alghamdi und Alfalqi (2015)](https://thesai.org/Downloads/Volume6No1/Paper_21-A_Survey_of_Topic_Modeling_in_Text_Mining.pdf) beschrieben werden. Da zur Anwendung der beschriebenen Modelle jedoch eine vorherige Festlegung der Themenanzahl notwendig ist, wurde für die vorliegende Untersuchung eine Hierachical Dirichlet Processes (HDP) Modellierung nach [Teh et al. (2015)](https://www.jstor.org/stable/pdf/27639773.pdf) benutzt, welche neben der Vertielung der Themen auch die Anzahl der Themen automatisch bestimmt. 
 Innerhalb Pythons wurde das Modul [tomotopy](https://pypi.org/project/tomotopy/) benutzt. Neben dem HDP-Modell enthält das Modul auch die weiter oben beschriebenen Modelle und eigenet sich somit zur Gegenüberstellung einzelner Modelle[^1].

## Sentimentanalyse


## Wortzählung


## 
[^1]: Für eine detallierte Beschreibung der einzelnen Funktionen eignet sich neben der Dokumentation des Moduls auch das [github-Repositoy von tomotopy](https://bab2min.github.io/tomotopy/v0.12.2/en/).
