#!/usr/bin/env python3
# -*- coding: utf-8 -*-
nrtonavn = { 
101 : u"Halden",
102 : u"Sarpsborg",
103 : u"Fredrikstad",
104 : u"Moss",
105 : u"Sarpsborg",
106 : u"Fredrikstad",
111 : u"Hvaler",
112 : u"Torsnes",
113 : u"Borge",
114 : u"Varteig",
115 : u"Skjeberg",
116 : u"Berg",
117 : u"Idd",
118 : u"Aremark",
119 : u"Øymark",
119 : u"Marker",
120 : u"Rødenes",
121 : u"Rømskog",
122 : u"Trøgstad",
123 : u"Spydeberg",
124 : u"Askim",
125 : u"Eidsberg",
126 : u"Mysen",
127 : u"Skiptvet",
128 : u"Rakkestad",
129 : u"Degernes",
130 : u"Tune",
131 : u"Rolvsøy",
132 : u"Glemmen",
133 : u"Kråkerøy",
134 : u"Onsøy",
135 : u"Råde",
136 : u"Rygge",
137 : u"Våler",
138 : u"Hobøl",
194 : u"Jeløy",
201 : u"Soon og Hølen",
201 : u"Son",
202 : u"Hvitsten",
203 : u"Drøbak",
204 : u"Hølen",
211 : u"Vestby",
212 : u"Kråkstad",
213 : u"Ski",
214 : u"Ås",
215 : u"Frogn",
216 : u"Nesodden",
217 : u"Oppegård",
218 : u"Aker",
219 : u"Bærum",
220 : u"Asker",
221 : u"Høland",
221 : u"Søndre Høland",
221 : u"Aurskog-Høland",
222 : u"Nordre Høland",
223 : u"Setskog",
224 : u"Aurskog",
225 : u"Blaker",
226 : u"Sørum",
227 : u"Fet",
228 : u"Rælingen",
229 : u"Enebakk",
230 : u"Lørenskog",
231 : u"Skedsmo",
232 : u"Lillestrøm",
233 : u"Nittedal",
234 : u"Gjerdrum",
235 : u"Ullensaker",
236 : u"Nes",
237 : u"Eidsvoll",
238 : u"Nannestad",
239 : u"Hurdal",
240 : u"Feiring",
301 : u"Oslo",
401 : u"Hamar",
402 : u"Kongsvinger",
402 : u"Kongsvinger",
403 : u"Hamar",
411 : u"Nes",
412 : u"Ringsaker",
413 : u"Furnes",
414 : u"Vang",
415 : u"Løten",
416 : u"Romedal",
417 : u"Stange",
418 : u"Nord-Odal",
419 : u"Sør-Odal",
420 : u"Eidskog",
421 : u"Vinger",
421 : u"Kongsvinger",
422 : u"Brandval",
423 : u"Grue",
424 : u"Hof",
425 : u"Aasnæs og Vaaler",
425 : u"Åsnes",
426 : u"Våler",
427 : u"Elverum",
428 : u"Trysil",
429 : u"Åmot",
430 : u"Stor-Elvdal",
431 : u"Sollia",
432 : u"Rendalen",
432 : u"Ytre Rendal",
432 : u"Rendalen",
433 : u"Øvre Rendal",
434 : u"Engerdal",
435 : u"Os",
435 : u"Tolga-Os",
436 : u"Tolga",
436 : u"Tolga",
437 : u"Tynset",
438 : u"Alvdal",
439 : u"Folldal",
440 : u"Kvikne",
441 : u"Os",
501 : u"Lillehammer",
502 : u"Gjøvik",
511 : u"Dovre",
512 : u"Lesja",
513 : u"Skjåk",
514 : u"Lom",
515 : u"Vågå",
516 : u"Heidal",
516 : u"Nord-Fron",
517 : u"Sel",
518 : u"Fron",
518 : u"Nord-Fron",
518 : u"Fron",
519 : u"Sør-Fron",
519 : u"Sør-Fron",
520 : u"Ringebu",
521 : u"Øyer",
522 : u"Gausdal",
522 : u"Østre Gausdal",
522 : u"Gausdal",
523 : u"Vestre Gausdal",
524 : u"Fåberg",
525 : u"Biri",
526 : u"Snertingdal",
527 : u"Vardal",
528 : u"Østre Toten",
529 : u"Vestre Toten",
530 : u"Eina",
531 : u"Kolbu",
532 : u"Jevnaker",
533 : u"Lunner",
534 : u"Gran",
535 : u"Brandbu",
536 : u"Land",
536 : u"Søndre Land",
537 : u"Fluberg",
538 : u"Nordre Land",
539 : u"Torpa",
540 : u"Sør-Aurdal",
541 : u"Etnedal",
542 : u"Nord-Aurdal",
543 : u"Slidre",
543 : u"Vestre Slidre",
544 : u"Øystre Slidre",
545 : u"Vang",
580 : u"Sollien",
601 : u"Hønefoss",
601 : u"Ringerike",
602 : u"Drammen",
603 : u"Holmsbu",
604 : u"Kongsberg",
605 : u"Ringerike",
611 : u"Tyristrand",
612 : u"Hole",
612 : u"Hole",
613 : u"Norderhov",
614 : u"Ådal",
615 : u"Flå",
616 : u"Nes",
617 : u"Gol",
618 : u"Hemsedal",
619 : u"Ål",
620 : u"Hol",
621 : u"Sigdal",
622 : u"Krødsherad",
623 : u"Modum",
624 : u"Eker",
624 : u"Øvre Eiker",
625 : u"Nedre Eiker",
626 : u"Lier",
627 : u"Røyken",
628 : u"Hurum",
629 : u"Sandsvær",
629 : u"Ytre Sandsvær",
630 : u"Øvre Sandsvær",
631 : u"Flesberg",
632 : u"Rollag",
633 : u"Nore",
633 : u"Nore og Uvdal",
634 : u"Uvdal",
680 : u"Strømmen",
681 : u"Strømsgodset",
701 : u"Svelvik",
701 : u"Horten",
702 : u"Holmestrand",
703 : u"Horten",
704 : u"Åsgårdstrand",
704 : u"Tønsberg",
705 : u"Tønsberg",
706 : u"Sandefjord",
707 : u"Larvik",
708 : u"Stavern",
709 : u"Larvik",
711 : u"Strømm",
711 : u"Svelvik",
712 : u"Skoger",
713 : u"Sande",
714 : u"Hof",
715 : u"Botne",
716 : u"Våle",
716 : u"Re",
717 : u"Borre",
718 : u"Ramnes",
719 : u"Andebu",
720 : u"Stokke",
721 : u"Sem",
722 : u"Nøtterøy",
723 : u"Tjøme",
724 : u"Sandar",
725 : u"Tjølling",
726 : u"Brunlanes",
727 : u"Hedrum",
728 : u"Lardal",
798 : u"Stavern",
801 : u"Kragerø",
802 : u"Langesund",
803 : u"Stathelle",
804 : u"Brevik",
805 : u"Porsgrunn",
806 : u"Skien",
807 : u"Notodden",
811 : u"Siljan",
812 : u"Gjerpen",
813 : u"Eidanger",
814 : u"Bamble",
815 : u"Skåtøy",
815 : u"Kragerø",
816 : u"Sannidal",
817 : u"Drangedal",
818 : u"Solum",
819 : u"Holla",
819 : u"Nome",
820 : u"Lunde",
821 : u"Bø",
822 : u"Sauherad",
823 : u"Heddal",
824 : u"Gransherad",
825 : u"Hovin",
826 : u"Tinn",
827 : u"Hjartdal",
828 : u"Seljord",
829 : u"Kviteseid",
830 : u"Nissedal",
831 : u"Fyresdal",
832 : u"Mo",
833 : u"Lårdal",
833 : u"Tokke",
834 : u"Vinje",
835 : u"Rauland",
901 : u"Risør",
902 : u"Tvedestrand",
903 : u"Arendal",
904 : u"Grimstad",
905 : u"Lillesand",
906 : u"Arendal",
911 : u"Gjerstad",
912 : u"Vegårshei",
913 : u"Søndeled",
914 : u"Holt",
914 : u"Tvedestrand",
915 : u"Dypvåg",
916 : u"Flosta",
917 : u"Stokken",
918 : u"Austre Moland",
918 : u"Moland",
919 : u"Froland",
920 : u"Øyestad",
921 : u"Tromøy",
922 : u"Hisøy",
923 : u"Fjære",
924 : u"Landvik",
925 : u"Eide",
926 : u"Vestre Moland",
926 : u"Lillesand",
927 : u"Høvåg",
928 : u"Birkenes",
929 : u"Åmli",
930 : u"Gjøvdal",
931 : u"Tovdal",
932 : u"Mykland",
933 : u"Herefoss",
934 : u"Evje og Veigusdal",
934 : u"Vegusdal",
935 : u"Hornnes og Iveland",
935 : u"Iveland",
936 : u"Hornnes",
937 : u"Evje",
937 : u"Evje og Hornnes",
938 : u"Bygland",
939 : u"Hylestad",
940 : u"Valle",
941 : u"Bykle",
980 : u"Aaseral",
990 : u"Barbu",
1001 : u"Kristiansand",
1002 : u"Mandal",
1003 : u"Farsund",
1004 : u"Flekkefjord",
1011 : u"Randesund",
1012 : u"Oddernes",
1013 : u"Tveit",
1014 : u"Vennesla",
1015 : u"Hægeland",
1016 : u"Øvrebø",
1016 : u"Øvrebø og Hægeland",
1016 : u"Øvrebø",
1017 : u"Greipstad",
1017 : u"Songdalen",
1018 : u"Søgne",
1019 : u"Halse og Harkmark",
1020 : u"Holum",
1021 : u"Øislebø og Laudal",
1021 : u"Øyslebø",
1021 : u"Marnardal",
1022 : u"Laudal",
1023 : u"Finsland",
1024 : u"Bjelland og Grindum",
1024 : u"Bjelland",
1025 : u"Grindheim",
1026 : u"Åseral",
1027 : u"Undal",
1027 : u"Nordre Undal",
1027 : u"Konsmo",
1027 : u"Audnedal",
1028 : u"Vigmostad",
1029 : u"Sør-Audnedal",
1029 : u"Lindesnes",
1030 : u"Spangereid",
1031 : u"Austad",
1032 : u"Lyngdal",
1033 : u"Kvås",
1034 : u"Hægebostad",
1035 : u"Eiken",
1036 : u"Fjotland",
1036 : u"Fjotland",
1037 : u"Kvinesdal",
1037 : u"Kvinesdal",
1038 : u"Feda",
1039 : u"Herad",
1040 : u"Spind",
1041 : u"Lista",
1042 : u"Nes og Hitterø",
1042 : u"Hidra",
1043 : u"Nes",
1044 : u"Gyland",
1045 : u"Bakke",
1046 : u"Siredalen",
1046 : u"Tonstad",
1046 : u"Sirdal",
1047 : u"Øvre Sirdal",
1101 : u"Egersund",
1101 : u"Eigersund",
1102 : u"Sandnes",
1103 : u"Stavanger",
1104 : u"Skudeneshavn",
1105 : u"Kopervik",
1106 : u"Haugesund",
1107 : u"Sogndal",
1111 : u"Sokndal",
1112 : u"Lund",
1113 : u"Heskestad",
1114 : u"Bjerkreim",
1115 : u"Helleland",
1116 : u"Eigersund",
1117 : u"Ogna",
1118 : u"Varhaug",
1119 : u"Haa",
1119 : u"Nærbø",
1119 : u"Hå",
1120 : u"Klepp",
1121 : u"Time",
1122 : u"Gjestal",
1122 : u"Gjesdal",
1123 : u"Høyland",
1124 : u"Håland",
1124 : u"Sola",
1125 : u"Madla",
1126 : u"Hetland",
1127 : u"Randaberg",
1128 : u"Høgsfjord",
1128 : u"Høle",
1129 : u"Forsand",
1130 : u"Strand",
1131 : u"Årdal",
1132 : u"Fister",
1133 : u"Hjelmeland og Fister",
1133 : u"Hjelmeland",
1134 : u"Suldal",
1135 : u"Sauda",
1136 : u"Sand",
1137 : u"Erfjord",
1138 : u"Jelsa",
1139 : u"Nærstrand",
1139 : u"Nedstrand",
1140 : u"Sjernarøy",
1141 : u"Finnøy",
1142 : u"Rennesøy",
1143 : u"Mosterøy",
1144 : u"Kvitsøy",
1145 : u"Bokn",
1146 : u"Tysvær",
1147 : u"Avaldsnæs med Kopervik",
1147 : u"Avaldsnes",
1148 : u"Stangaland",
1149 : u"Åkra",
1149 : u"Karmøy",
1150 : u"Skudenes",
1151 : u"Utsira",
1152 : u"Torvastad",
1153 : u"Skåre",
1154 : u"Skjold",
1154 : u"Vindafjord",
1155 : u"Vats",
1156 : u"Imsland",
1157 : u"Vikedal",
1158 : u"Sandeid",
1159 : u"Ølen",
1160 : u"Vindafjord",
1201 : u"Bergen",
1211 : u"Etne",
1212 : u"Skånevik",
1213 : u"Fjelberg",
1214 : u"Ølen",
1215 : u"Vikebygd",
1216 : u"Sveio",
1217 : u"Valestrand",
1218 : u"Finnaas",
1218 : u"Moster",
1219 : u"Bømlo",
1220 : u"Bremnes",
1221 : u"Stord",
1222 : u"Fitjar",
1223 : u"Tysnes",
1224 : u"Kvinnherad",
1225 : u"Varaldsøy",
1226 : u"Strandebarm og Varaldsø",
1226 : u"Strandebarm",
1227 : u"Jondal",
1228 : u"Odda",
1229 : u"Røldal",
1230 : u"Ullensvang",
1231 : u"Kinsarvik",
1231 : u"Ullensvang",
1232 : u"Eidfjord",
1232 : u"Eidfjord",
1233 : u"Ulvik",
1234 : u"Granvin",
1235 : u"Voss",
1236 : u"Vossestrand",
1237 : u"Evanger",
1238 : u"Kvam",
1239 : u"Hålandsdal",
1240 : u"Strandvik",
1241 : u"Fusa",
1242 : u"Samnanger",
1243 : u"Os",
1244 : u"Austevoll",
1245 : u"Sund",
1246 : u"Fjell",
1247 : u"Askøy",
1248 : u"Laksevåg",
1249 : u"Fana",
1250 : u"Haus",
1250 : u"Arna",
1251 : u"Bruvik",
1251 : u"Vaksdal",
1252 : u"Modalen",
1253 : u"Hosanger",
1253 : u"Osterøy",
1254 : u"Hamre",
1255 : u"Åsane",
1256 : u"Meland",
1257 : u"Alversund",
1258 : u"Herdla",
1259 : u"Hjelme",
1259 : u"Øygarden",
1260 : u"Hordabø",
1260 : u"Radøy",
1261 : u"Manger",
1262 : u"Sæbø",
1263 : u"Lindås",
1264 : u"Austrheim",
1265 : u"Masfjorden",
1265 : u"Fedje",
1266 : u"Masfjorden",
1280 : u"Aarstad",
1281 : u"Dom- og Korskirkens Landdistrikt",
1282 : u"Eid",
1301 : u"Bergen",
1401 : u"Florø",
1401 : u"Flora",
1411 : u"Gulen",
1412 : u"Solund",
1413 : u"Hyllestad",
1414 : u"Brække",
1414 : u"Brekke",
1415 : u"Ladvik",
1415 : u"Lavik og Brekke",
1415 : u"Lavik",
1416 : u"Kyrkjebø",
1416 : u"Høyanger",
1417 : u"Vik",
1418 : u"Balestrand",
1419 : u"Leikanger",
1420 : u"Sogndal",
1421 : u"Aurland",
1422 : u"Lærdal",
1423 : u"Borgund",
1424 : u"Årdal",
1425 : u"Hafslo",
1426 : u"Luster",
1427 : u"Jostedal",
1428 : u"Askvoll",
1429 : u"Fjaler",
1430 : u"Gaular",
1431 : u"Jølster",
1432 : u"Førde",
1433 : u"Naustdal",
1434 : u"Vevring",
1435 : u"Eikefjord",
1436 : u"Bru",
1437 : u"Kinn",
1438 : u"Bremanger",
1439 : u"Sør-Vågsøy",
1439 : u"Vågsøy",
1440 : u"Nord-Vågsøy",
1441 : u"Selje",
1442 : u"Davik",
1443 : u"Eid",
1444 : u"Hornindal",
1444 : u"Hornindal",
1445 : u"Gloppen",
1446 : u"Breim",
1447 : u"Innvik",
1448 : u"Stryn",
1449 : u"Stryn",
1501 : u"Ålesund",
1502 : u"Molde",
1503 : u"Kristiansund",
1504 : u"Ålesund",
1505 : u"Kristiansund",
1511 : u"Vanylven",
1512 : u"Syvde",
1513 : u"Rovde",
1514 : u"Sande",
1515 : u"Herøy",
1516 : u"Ulstein",
1517 : u"Hareid",
1518 : u"Dalsfjord",
1519 : u"Volda",
1520 : u"Ørsta",
1521 : u"Vartdal",
1522 : u"Hjørundfjord",
1523 : u"Sunnylven",
1523 : u"Ørskog",
1524 : u"Norddal",
1525 : u"Stranda",
1526 : u"Stordal",
1526 : u"Stordal",
1527 : u"Ørskog",
1528 : u"Sykkylven",
1529 : u"Skodje",
1529 : u"Skodje",
1530 : u"Vatne",
1531 : u"Borgund",
1531 : u"Sula",
1532 : u"Giske",
1533 : u"Vigra",
1534 : u"Haram",
1535 : u"Vestnes",
1536 : u"Tresfjord",
1537 : u"Eid og Vold",
1537 : u"Voll",
1538 : u"Eid",
1539 : u"Grytten",
1539 : u"Rauma",
1540 : u"Hen",
1541 : u"Veøy",
1542 : u"Eresfjord og Vistdal",
1543 : u"Nesset",
1544 : u"Bolsøy",
1545 : u"Aukra",
1545 : u"Sør-Aukra",
1545 : u"Midsund",
1546 : u"Sandøy",
1547 : u"Aukra",
1548 : u"Fræna",
1549 : u"Bud",
1550 : u"Hustad",
1551 : u"Eide",
1552 : u"Kornstad",
1553 : u"Kvernes",
1554 : u"Bremsnes",
1554 : u"Averøy",
1555 : u"Grip",
1556 : u"Frei",
1557 : u"Gjemnes",
1558 : u"Øre",
1559 : u"Straumsnes",
1560 : u"Tingvoll",
1561 : u"Øksendal",
1562 : u"Ålvundeid",
1563 : u"Sunndal",
1564 : u"Stangvik",
1565 : u"Åsskard",
1566 : u"Surnadal",
1567 : u"Rindal",
1568 : u"Stemshaug",
1569 : u"Aure",
1570 : u"Valsøyfjord",
1571 : u"Halsa",
1572 : u"Tustna",
1573 : u"Edøy",
1573 : u"Smøla",
1574 : u"Brattvær",
1575 : u"Hopen",
1576 : u"Aure",
1601 : u"Trondheim",
1611 : u"Vinje",
1612 : u"Hemne",
1613 : u"Snillfjord",
1614 : u"Heim",
1615 : u"Sandstad",
1616 : u"Fillan",
1617 : u"Hitra",
1618 : u"Kvenvær",
1619 : u"Frøien",
1619 : u"Sør-Frøya",
1620 : u"Nord-Frøya",
1620 : u"Frøya",
1621 : u"Ørland",
1622 : u"Agdenes",
1623 : u"Lensvik",
1624 : u"Rissa",
1625 : u"Stadsbygd",
1626 : u"Stjørna",
1627 : u"Bjugn",
1628 : u"Nes",
1629 : u"Jøssund",
1630 : u"Åfjord",
1631 : u"Stoksund",
1632 : u"Bjørnør",
1632 : u"Roan",
1633 : u"Osen",
1634 : u"Oppdal",
1635 : u"Rennebu",
1636 : u"Meldal",
1637 : u"Orkland",
1638 : u"Orkdal",
1639 : u"Orkanger",
1640 : u"Røros",
1641 : u"Røros landsogn",
1642 : u"Brekken",
1643 : u"Glåmos",
1644 : u"Ålen",
1644 : u"Holtålen",
1645 : u"Haltdalen",
1646 : u"Singsås",
1647 : u"Budal",
1648 : u"Støren",
1648 : u"Midtre Gauldal",
1649 : u"Soknedal",
1650 : u"Horg",
1651 : u"Hølonda",
1652 : u"Flå",
1653 : u"Melhus",
1654 : u"Leinstrand",
1655 : u"Byneset",
1656 : u"Buvik",
1657 : u"Skaun",
1658 : u"Børsa",
1659 : u"Geitastrand",
1660 : u"Strinda",
1661 : u"Tiller",
1662 : u"Klæbu",
1663 : u"Malvik",
1664 : u"Selbu",
1665 : u"Tydal",
1701 : u"Levanger",
1702 : u"Steinkjer",
1703 : u"Namsos",
1711 : u"Øvre Stjørdalen",
1711 : u"Meråker",
1712 : u"Hegra",
1713 : u"Lånke",
1714 : u"Størdalen",
1714 : u"Nedre Stjørdalen",
1714 : u"Stjørdal",
1715 : u"Skatval",
1716 : u"Åsen",
1717 : u"Frosta",
1718 : u"Leksvik",
1719 : u"Skogn",
1719 : u"Levanger",
1720 : u"Frol",
1721 : u"Verdal",
1722 : u"Ytterøy",
1723 : u"Mosviken og Verran",
1723 : u"Mosvik",
1724 : u"Verran",
1725 : u"Namdalseid",
1726 : u"Malm",
1727 : u"Beitstad",
1728 : u"Sandvollan",
1729 : u"Inderøy",
1730 : u"Røra",
1731 : u"Sparbu",
1732 : u"Ogndal",
1733 : u"Egge",
1734 : u"Stod",
1735 : u"Kvam",
1736 : u"Snåsa",
1737 : u"Lierne",
1737 : u"Sørli",
1738 : u"Nordli",
1738 : u"Lierne",
1739 : u"Røyrvik",
1740 : u"Namsskogan",
1741 : u"Harran",
1742 : u"Grong",
1743 : u"Høylandet",
1744 : u"Overhalla",
1745 : u"Sævik",
1745 : u"Namsos Landdistrikt",
1745 : u"Vemundvik",
1746 : u"Klinga",
1747 : u"Otterøy",
1748 : u"Fosnes",
1749 : u"Flatanger",
1750 : u"Vikna",
1751 : u"Nærøy",
1752 : u"Kolvereid og Foldereid",
1752 : u"Kolvereid",
1753 : u"Foldereid",
1754 : u"Gravvik",
1755 : u"Leka",
1756 : u"Inderøy",
1780 : u"Sørbindalen",
1801 : u"Brønnøysund",
1802 : u"Mosjøen",
1803 : u"Mo",
1804 : u"Bodø",
1805 : u"Narvik",
1806 : u"Svolvær",
1811 : u"Nordbindalen",
1811 : u"Bindal",
1812 : u"Sømna",
1812 : u"Sømna",
1813 : u"Velfjord",
1813 : u"Brønnøy",
1814 : u"Brønnøy",
1815 : u"Vega",
1816 : u"Vevelstad",
1817 : u"Tjøtta",
1818 : u"Herøy",
1819 : u"Nordvik",
1820 : u"Alstahaug",
1821 : u"Sandnessjøen",
1822 : u"Leirfjord",
1823 : u"Drevja",
1824 : u"Vefsn",
1825 : u"Grane",
1826 : u"Hattfjelldal",
1827 : u"Dønnes",
1827 : u"Dønna",
1828 : u"Nesna",
1829 : u"Elsfjord",
1830 : u"Korgen",
1831 : u"Sør-Rana",
1832 : u"Hemnes",
1833 : u"Mo",
1833 : u"Nord-Rana",
1833 : u"Rana",
1834 : u"Lurøy",
1835 : u"Træna",
1836 : u"Rødøy",
1837 : u"Meløy",
1838 : u"Gildeskål",
1839 : u"Beiarn",
1840 : u"Saltdal",
1841 : u"Fauske",
1842 : u"Skjerstad",
1843 : u"Bodin",
1844 : u"Kjerringøy",
1845 : u"Folden",
1845 : u"Sørfold",
1846 : u"Nordfolden-Kjerringø",
1846 : u"Nordfold",
1847 : u"Leiranger",
1848 : u"Steigen",
1849 : u"Hamarøy",
1850 : u"Tysfjord",
1851 : u"Lødingen",
1852 : u"Tjeldsund",
1853 : u"Ofoten",
1853 : u"Evenes",
1854 : u"Ballangen",
1855 : u"Ankenes",
1856 : u"Røst",
1857 : u"Værøy",
1858 : u"Moskenes",
1859 : u"Flakstad",
1859 : u"Flakstad",
1860 : u"Buksnes",
1860 : u"Vestvågøy",
1861 : u"Hol",
1862 : u"Borge",
1863 : u"Valberg",
1864 : u"Gimsøy",
1865 : u"Vågan",
1866 : u"Hadsel",
1867 : u"Bø",
1868 : u"Øksnes",
1869 : u"Langenes",
1870 : u"Sortland",
1871 : u"Bjørnskinn",
1871 : u"Andøy",
1872 : u"Dverberg",
1873 : u"Andenes",
1874 : u"Moskenes",
1901 : u"Harstad",
1902 : u"Tromsø",
1903 : u"Harstad",
1911 : u"Kvæfjord",
1912 : u"Sandtorg",
1913 : u"Skånland",
1914 : u"Trondenes",
1915 : u"Bjarkøy",
1916 : u"Andørja",
1917 : u"Ibestad",
1918 : u"Astafjord",
1919 : u"Gratangen",
1920 : u"Lavangen",
1920 : u"Lavangen",
1921 : u"Salangen",
1922 : u"Bardu",
1923 : u"Øverbygd",
1923 : u"Salangen",
1924 : u"Målselv",
1925 : u"Sørreisa",
1926 : u"Dyrøy",
1927 : u"Tranøy",
1928 : u"Torsken",
1929 : u"Berg",
1930 : u"Hillesøy",
1931 : u"Lenvik",
1932 : u"Malangen",
1933 : u"Balsfjord",
1934 : u"Tromsøysund",
1935 : u"Helgøy",
1936 : u"Karlsøy",
1937 : u"Ullsfjord",
1938 : u"Lyngen",
1939 : u"Storfjord",
1940 : u"Kåfjord",
1941 : u"Skjervøy",
1942 : u"Nordreisa",
1943 : u"Kvænangen",
2001 : u"Hammerfest",
2002 : u"Vardø",
2003 : u"Vadsø",
2004 : u"Hammerfest",
2011 : u"Kautokeino",
2012 : u"Alten-Talvik",
2012 : u"Alta",
2013 : u"Talvik",
2014 : u"Loppa",
2015 : u"Hasvik",
2016 : u"Sørøysund",
2017 : u"Kvalsund",
2018 : u"Måsøy",
2019 : u"Nordkapp",
2020 : u"Porsanger",
2021 : u"Karasjok",
2022 : u"Lebesby",
2023 : u"Gamvik",
2024 : u"Berlevåg",
2025 : u"Tana",
2026 : u"Polmak",
2027 : u"Næsseby",
2027 : u"Nesseby",
2028 : u"Båtsfjord",
2029 : u"Nord-Varanger",
2030 : u"Sør-Varanger",
}
