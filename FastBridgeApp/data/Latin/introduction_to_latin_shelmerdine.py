import text
nan=""
section_words = {'start': -1, '1': 21, '2': 44, '3': 65, '4': 85, '5': 108, '6': 131, '7': 153, '8': 175, '9': 199, '10': 222, '11': 244, '12': 268, '13': 292, '14': 314, '15': 336, '16': 359, '17': 382, '18': 403, '19': 424, '20': 445, '21': 465, '22': 486, '23': 507, '24': 521, '25': 542, '26': 560, '27': 582, '28': 603, '29': 624, '30': 640, '31': 647, '32': 654, 'end': -2}
the_text =  [('AGRICOLA', 0, 'agricola', '', '', '1', 1), ('AMO', 1, 'amo', '', '', '1', 1), ('AQVA', 2, 'aqua', '', '', '1', 1), ('DEBEO', 3, 'debeo', '', '', '1', 1), ('DOCEO', 4, 'doceo', '', '', '1', 1), ('FAMA', 5, 'fama', '', '', '1', 1), ('FEMINA', 6, 'femina', '', '', '1', 1), ('FORTVNA', 7, 'fortuna', '', '', '1', 1), ('HABEO', 8, 'habeo', '', '', '1', 1), ('IACEO', 9, 'iaceo', '', '', '1', 1), ('IVVO', 10, 'iuvo', '', '', '1', 1), ('LABORO', 11, 'laboro', '', '', '1', 1), ('LAVDO', 12, 'laudo', '', '', '1', 1), ('NAVTA', 13, 'nauta', '', '', '1', 1), ('NE/2', 14, 'ne', '', '', '1', 1), ('OPTO', 15, 'opto', '', '', '1', 1), ('ROSA', 16, 'rosa', '', '', '1', 1), ('SVPERO', 17, 'supero', '', '', '1', 1), ('TACEO', 18, 'taceo', '', '', '1', 1), ('TIMEO', 19, 'timeo', '', '', '1', 1), ('VIDEO', 20, 'video', '', '', '1', 1), ('VOCO', 21, 'voco', '', '', '1', 1), ('AGER', 22, 'ager', '', '', '2', 1), ('AMICVS/1', 23, 'amicus', '', '', '2', 1), ('ANIMVS', 24, 'animus', '', '', '2', 1), ('AVDEO', 25, 'audeo', '', '', '2', 1), ('BELLVM', 26, 'bellum', '', '', '2', 1), ('CLAMO', 27, 'clamo', '', '', '2', 1), ('CONSILIVM', 28, 'consilium', '', '', '2', 1), ('DOMINVS', 29, 'dominus', '', '', '2', 1), ('DONVM', 30, 'donum', '', '', '2', 1), ('DVBITO', 31, 'dubito', '', '', '2', 1), ('ET/2', 32, 'et', '', '', '2', 1), ('ETET', 33, 'et', '', '', '2', 1), ('LITTERA', 34, 'littera', '', '', '2', 1), ('LOCVS', 35, 'locus', '', '', '2', 1), ('NATVRA', 36, 'natura', '', '', '2', 1), ('ORO', 37, 'oro', '', '', '2', 1), ('PVELLA', 38, 'puella', '', '', '2', 1), ('PVER', 39, 'puer', '', '', '2', 1), ('QVE', 40, 'que', '', '', '2', 1), ('REGNVM', 41, 'regnum', '', '', '2', 1), ('SED', 42, 'sed', '', '', '2', 1), ('TERREO', 43, 'terreo', '', '', '2', 1), ('VIR', 44, 'vir', '', '', '2', 1), ('AEDIFICO', 45, 'aedifico', '', '', '3', 1), ('ARMA', 46, 'arma', '', '', '3', 1), ('CAELVM/1', 47, 'caelum', '', '', '3', 1), ('DEVS', 48, 'deus', '', '', '3', 1), ('DO', 49, 'do', '', '', '3', 1), ('FABVLA/1', 50, 'fabula', '', '', '3', 1), ('IMPERIVM', 51, 'imperium', '', '', '3', 1), ('LIBER/1', 52, 'liber', '', '', '3', 1), ('MONSTRO', 53, 'monstro', '', '', '3', 1), ('NARRO', 54, 'narro', '', '', '3', 1), ('NEMO', 55, 'nemo', '', '', '3', 1), ('NIHIL', 56, 'nihil', '', '', '3', 1), ('NOCEO', 57, 'noceo', '', '', '3', 1), ('PAREO', 58, 'pareo', '', '', '3', 1), ('PLACEO', 59, 'placeo', '', '', '3', 1), ('PORTO', 60, 'porto', '', '', '3', 1), ('PVGNO', 61, 'pugno', '', '', '3', 1), ('SOLEO', 62, 'soleo', '', '', '3', 1), ('TEMPLVM', 63, 'templum', '', '', '3', 1), ('TVRBA', 64, 'turba', '', '', '3', 1), ('VENTVS', 65, 'ventus', '', '', '3', 1), ('AB', 66, 'a', '', '', '4', 2), ('AD/2', 67, 'ad', '', '', '4', 1), ('AMBVLO', 68, 'ambulo', '', '', '4', 1), ('CASA', 69, 'casa', '', '', '4', 1), ('ERRO/2', 70, 'erro', '', '', '4', 1), ('EX', 71, 'e', '', '', '4', 1), ('FESTINO', 72, 'festino', '', '', '4', 1), ('IN', 73, 'in', '', '', '4', 1), ('MOVEO', 74, 'moveo', '', '', '4', 1), ('NAVIGO', 75, 'navigo', '', '', '4', 1), ('NON', 76, 'non', '', '', '4', 1), ('NVNC', 77, 'nunc', '', '', '4', 1), ('OCVLVS', 78, 'oculus', '', '', '4', 1), ('PONTVS', 79, 'pontus', '', '', '4', 1), ('PRO/1', 80, 'pro', '', '', '4', 1), ('SAEPE', 81, 'saepe', '', '', '4', 1), ('TANDEM', 82, 'tandem', '', '', '4', 1), ('TRANS/2', 83, 'trans', '', '', '4', 1), ('TVM', 84, 'tum', '', '', '4', 1), ('VIA', 85, 'via', '', '', '4', 1), ('AEGER/2', 86, 'aeger', '', '', '5', 1), ('ALTVS', 87, 'altus', '', '', '5', 1), ('BONVS', 88, 'bonus', '', '', '5', 1), ('CVM/2', 89, 'cum', '', '', '5', 1), ('CVRA', 90, 'cura', '', '', '5', 1), ('DIVINVS/2', 91, 'divinus', '', '', '5', 1), ('IACTO', 92, 'iacto', '', '', '5', 1), ('LIBER/2', 93, 'liber', '', '', '5', 1), ('MAGNVS', 94, 'magnus', '', '', '5', 1), ('MALVS/3', 95, 'malus', '', '', '5', 1), ('MEVS', 96, 'meus', '', '', '5', 1), ('MVLTVS', 97, 'multus', '', '', '5', 1), ('NOSTER', 98, 'noster', '', '', '5', 1), ('PARVVS/2', 99, 'parvus', '', '', '5', 1), ('PVLCHER', 100, 'pulcher', '', '', '5', 1), ('SAPIENTIA', 101, 'sapientia', '', '', '5', 1), ('SAXVM', 102, 'saxum', '', '', '5', 1), ('SILVA', 103, 'silva', '', '', '5', 1), ('SVB', 104, 'sub', '', '', '5', 1), ('SVM/1', 105, 'sum', '', '', '5', 1), ('TERRA', 106, 'terra', '', '', '5', 1), ('TVVS', 107, 'tuus', '', '', '5', 1), ('VESTER', 108, 'vester', '', '', '5', 1), ('CENA', 109, 'cena', '', '', '6', 1), ('DE', 110, 'de', '', '', '6', 1), ('DIV', 111, 'diu', '', '', '6', 1), ('ENIM/2', 112, 'enim', '', '', '6', 1), ('EXEMPLVM', 113, 'exemplum', '', '', '6', 1), ('FILIA', 114, 'filia', '', '', '6', 1), ('FILIVS', 115, 'filius', '', '', '6', 1), ('INTRO/1', 116, 'intro', '', '', '6', 1), ('ITALIA/N', 117, 'Italia', '', '', '6', 1), ('LAETVS/2', 118, 'laetus', '', '', '6', 1), ('MANEO', 119, 'maneo', '', '', '6', 1), ('NOVVS', 120, 'novus', '', '', '6', 1), ('NVNTIO', 121, 'nuntio', '', '', '6', 1), ('PARO/2', 122, 'paro', '', '', '6', 1), ('PECVNIA', 123, 'pecunia', '', '', '6', 1), ('POPVLVS/1', 124, 'populus', '', '', '6', 1), ('PROPTER/2', 125, 'propter', '', '', '6', 1), ('REGINA', 126, 'regina', '', '', '6', 1), ('ROMANVS/A', 127, nan, '', '', '6', 2), ('ROMANVS/A', 128, 'Romanus', '', '', '6', 2), ('SEMPER', 129, 'semper', '', '', '6', 1), ('SINE', 130, 'sine', '', '', '6', 1), ('VITA', 131, 'vita', '', '', '6', 1), ('ARS', 132, 'ars', '', '', '7', 1), ('CAPVT', 133, 'caput', '', '', '7', 1), ('CIVITAS', 134, 'civitas', '', '', '7', 1), ('CONSVL', 135, 'consul', '', '', '7', 1), ('CORPVS', 136, 'corpus', '', '', '7', 1), ('DVX', 137, 'dux', '', '', '7', 1), ('FRATER', 138, 'frater', '', '', '7', 1), ('HOMO', 139, 'homo', '', '', '7', 1), ('IRA', 140, 'ira', '', '', '7', 1), ('MATER', 141, 'mater', '', '', '7', 1), ('MENS', 142, 'mens', '', '', '7', 1), ('MISER', 143, 'miser', '', '', '7', 1), ('MORS', 144, 'mors', '', '', '7', 1), ('NVMEN', 145, 'numen', '', '', '7', 1), ('PATER', 146, 'pater', '', '', '7', 1), ('REX', 147, 'rex', '', '', '7', 1), ('TENEO', 148, 'teneo', '', '', '7', 1), ('VERITAS', 149, 'veritas', '', '', '7', 1), ('VIRTVS', 150, 'virtus', '', '', '7', 1), ('VOX', 151, 'vox', '', '', '7', 1), ('VRBS', 152, 'urbs', '', '', '7', 1), ('VXOR', 153, 'uxor', '', '', '7', 1), ('CLARVS', 154, 'clarus', '', '', '8', 1), ('DOLEO', 155, 'doleo', '', '', '8', 1), ('IRATVS', 156, 'iratus', '', '', '8', 1), ('LEX', 157, 'lex', '', '', '8', 1), ('LIBERTAS', 158, 'libertas', '', '', '8', 1), ('LVNA', 159, 'luna', '', '', '8', 1), ('LVX', 160, 'lux', '', '', '8', 1), ('MONS', 161, 'mons', '', '', '8', 1), ('NOMEN', 162, 'nomen', '', '', '8', 1), ('OPVS/1', 163, 'opus', '', '', '8', 1), ('PARS', 164, 'pars', '', '', '8', 1), ('PATRIA', 165, 'patria', '', '', '8', 1), ('PAX', 166, 'pax', '', '', '8', 1), ('PERICVLVM', 167, 'periculum', '', '', '8', 1), ('PLENVS', 168, 'plenus', '', '', '8', 1), ('POSSVM/1', 169, 'possum', '', '', '8', 1), ('POST/2', 170, 'post', '', '', '8', 1), ('RATIO', 171, 'ratio', '', '', '8', 1), ('SACER', 172, 'sacer', '', '', '8', 1), ('STVDEO', 173, 'studeo', '', '', '8', 1), ('SVBITO', 174, 'subito', '', '', '8', 1), ('VERBVM', 175, 'verbum', '', '', '8', 1), ('AGO', 176, 'ago', '', '', '9', 1), ('AVT', 177, 'aut', '', '', '9', 1), ('CAPIO/2', 178, 'capio', '', '', '9', 1), ('CARMEN/1', 179, 'carmen', '', '', '9', 1), ('DICO/2', 180, 'dico', '', '', '9', 1), ('DISCO', 181, 'disco', '', '', '9', 1), ('DVCO', 182, 'duco', '', '', '9', 1), ('EGO', 183, 'ego', '', '', '9', 1), ('ET/1', 184, 'et', '', '', '9', 1), ('FACIO', 185, 'facio', '', '', '9', 1), ('INTER', 186, 'inter', '', '', '9', 1), ('MITTO', 187, 'mitto', '', '', '9', 1), ('NOS', 188, 'nos', '', '', '9', 1), ('OLIM', 189, 'olim', '', '', '9', 1), ('POETA', 190, 'poeta', '', '', '9', 1), ('QVIDAGIS', 191, 'quid', '', '', '9', 1), ('REGO', 192, 'rego', '', '', '9', 1), ('SCRIBO', 193, 'scribo', '', '', '9', 1), ('SEDEO', 194, 'sedeo', '', '', '9', 1), ('TV', 195, 'tu', '', '', '9', 1), ('VALE', 196, 'vale', '', '', '9', 1), ('VALEO', 197, 'valeo', '', '', '9', 1), ('VINCO', 198, 'vinco', '', '', '9', 1), ('VOS', 199, 'vos', '', '', '9', 1), ('ALIVS', 200, 'alius', '', '', '10', 1), ('ALIVSALIVS', 201, 'alius', '', '', '10', 1), ('COGNOSCO', 202, 'cognosco', '', '', '10', 1), ('CREO', 203, 'creo', '', '', '10', 1), ('ETIAM', 204, 'etiam', '', '', '10', 1), ('FACTVM', 205, 'factum', '', '', '10', 1), ('FVGIO', 206, 'fugio', '', '', '10', 1), ('HIC/2', 207, 'hic', '', '', '10', 1), ('ILLE', 208, 'ille', '', '', '10', 1), ('INCIPIO', 209, 'incipio', '', '', '10', 1), ('IS', 210, 'is', '', '', '10', 1), ('ITA', 211, 'ita', '', '', '10', 1), ('IVDICO', 212, 'iudico', '', '', '10', 1), ('IVS/1', 213, 'ius', '', '', '10', 1), ('LEGO/2', 214, 'lego', '', '', '10', 1), ('NONSOLVM', 215, 'non', '', '', '10', 1), ('NVLLVS', 216, 'nullus', '', '', '10', 1), ('PERSVADEO', 217, 'persuadeo', '', '', '10', 1), ('SOLVS', 218, 'solus', '', '', '10', 1), ('TAMEN', 219, 'tamen', '', '', '10', 1), ('TOTVS', 220, 'totus', '', '', '10', 1), ('VLLVS', 221, 'ullus', '', '', '10', 1), ('VNVS', 222, 'unus', '', '', '10', 1), ('ANTE/2', 223, 'ante', '', '', '11', 2), ('CADO', 224, 'cado', '', '', '11', 1), ('CAVSA', 225, 'causa', '', '', '11', 1), ('CAVSA/2', 226, 'causa', '', '', '11', 1), ('CONIVX', 227, 'coniunx', '', '', '11', 1), ('CREDO', 228, 'credo', '', '', '11', 1), ('DEXTER', 229, 'dexter', '', '', '11', 1), ('FLVMEN', 230, 'flumen', '', '', '11', 1), ('GRATIA', 231, 'gratia', '', '', '11', 1), ('GRATIASAGERE', 232, 'gratias', '', '', '11', 1), ('LACRIMA', 233, 'lacrima', '', '', '11', 1), ('LAVS', 234, 'laus', '', '', '11', 1), ('MILES', 235, 'miles', '', '', '11', 1), ('NAM', 236, 'nam', '', '', '11', 1), ('NEC/2', 237, 'nec', '', '', '11', 1), ('NEQVE', 238, 'neque', '', '', '11', 1), ('NEQVENEC', 239, 'neque', '', '', '11', 1), ('PER', 240, 'per', '', '', '11', 1), ('PETO', 241, 'peto', '', '', '11', 1), ('RELINQVO', 242, 'relinquo', '', '', '11', 1), ('SECVNDVS/1', 243, 'secundus', '', '', '11', 1), ('TIMOR', 244, 'timor', '', '', '11', 1), ('ACER/2', 245, 'acer', '', '', '12', 1), ('AETAS', 246, 'aetas', '', '', '12', 1), ('ANNVS', 247, 'annus', '', '', '12', 1), ('BELLVMGERO', 248, 'bellum', '', '', '12', 1), ('BREVIS', 249, 'brevis', '', '', '12', 1), ('CELER', 250, 'celer', '', '', '12', 1), ('DIFFICILIS', 251, 'difficilis', '', '', '12', 1), ('DISCEDO/1', 252, 'discedo', '', '', '12', 1), ('DOLOR', 253, 'dolor', '', '', '12', 1), ('DVLCIS', 254, 'dulcis', '', '', '12', 1), ('FACILIS', 255, 'facilis', '', '', '12', 1), ('FELIX', 256, 'felix', '', '', '12', 1), ('FORTIS', 257, 'fortis', '', '', '12', 1), ('GALLIA/N', 258, 'Gallia', '', '', '12', 1), ('GENS', 259, 'gens', '', '', '12', 1), ('GERO', 260, 'gero', '', '', '12', 1), ('HORA', 261, 'hora', '', '', '12', 1), ('INGENS', 262, 'ingens', '', '', '12', 1), ('OMNIS', 263, 'omnis', '', '', '12', 1), ('PES', 264, 'pes', '', '', '12', 1), ('POTENS', 265, 'potens', '', '', '12', 1), ('SIC', 266, 'sic', '', '', '12', 1), ('TEMPVS/1', 267, 'tempus', '', '', '12', 1), ('TER', 268, 'ter', '', '', '12', 1), ('AVDIO', 269, 'audio', '', '', '13', 1), ('COPIA', 270, 'copia', '', '', '13', 1), ('DIGNVS', 271, 'dignus', '', '', '13', 1), ('DORMIO', 272, 'dormio', '', '', '13', 1), ('FINIO', 273, 'finio', '', '', '13', 1), ('FINIS', 274, 'finis', '', '', '13', 1), ('IMPEDIO', 275, 'impedio', '', '', '13', 1), ('INDIGNVS', 276, 'indignus', '', '', '13', 1), ('INTELLIGO', 277, 'intellego', '', '', '13', 1), ('ITER', 278, 'iter', '', '', '13', 1), ('MORA', 279, 'mora', '', '', '13', 1), ('MORTALIS/2', 280, 'mortalis', '', '', '13', 1), ('PAVCI', 281, 'paucus', '', '', '13', 1), ('PROHIBEO', 282, 'prohibeo', '', '', '13', 1), ('RELIQVVS', 283, 'reliquus', '', '', '13', 1), ('SAPIENS/2', 284, 'sapiens', '', '', '13', 1), ('SCIO', 285, 'scio', '', '', '13', 1), ('SENEX/1', 286, 'senex', '', '', '13', 1), ('SENTIO', 287, 'sentio', '', '', '13', 1), ('SERVIO', 288, 'servio', '', '', '13', 1), ('SVPERI', 289, 'superi', '', '', '13', 1), ('SVPERVS', 290, 'superus', '', '', '13', 1), ('SVVS', 291, 'suus', '', '', '13', 1), ('VENIO', 292, 'venio', '', '', '13', 1), ('ABSVM/1', 293, 'absum', '', '', '14', 1), ('ADVENIO', 294, 'advenio', '', '', '14', 1), ('ARBOR', 295, 'arbor', '', '', '14', 1), ('CIRCA/2', 296, 'circa', '', '', '14', 1), ('CIRCVM/2', 297, 'circum', '', '', '14', 1), ('CVRO', 298, 'curo', '', '', '14', 1), ('DIMITTO', 299, 'dimitto', '', '', '14', 1), ('GENVS/1', 300, 'genus', '', '', '14', 1), ('HONOR', 301, 'honor', '', '', '14', 1), ('HOSTIS', 302, 'hostis', '', '', '14', 1), ('IAM', 303, 'iam', '', '', '14', 1), ('INVENIO', 304, 'invenio', '', '', '14', 1), ('LEGATVS', 305, 'legatus', '', '', '14', 1), ('LONGVS', 306, 'longus', '', '', '14', 1), ('MARE', 307, 'mare', '', '', '14', 1), ('MEDIVS', 308, 'medius', '', '', '14', 1), ('MONEO', 309, 'moneo', '', '', '14', 1), ('NOX', 310, 'nox', '', '', '14', 1), ('RAPIO', 311, 'rapio', '', '', '14', 1), ('SCELVS', 312, 'scelus', '', '', '14', 1), ('STO', 313, 'sto', '', '', '14', 1), ('TANTVS', 314, 'tantus', '', '', '14', 1), ('ATQVE/1', 315, 'atque', '', '', '15', 1), ('AVREVS/2', 316, 'aureus', '', '', '15', 1), ('AVRVM', 317, 'aurum', '', '', '15', 1), ('CEDO/1', 318, 'cedo', '', '', '15', 1), ('CIVIS', 319, 'civis', '', '', '15', 1), ('DVRVS', 320, 'durus', '', '', '15', 1), ('FESSVS', 321, 'fessus', '', '', '15', 1), ('FORTE', 322, 'forte', '', '', '15', 1), ('HVMVS', 323, 'humus', '', '', '15', 1), ('IGNIS', 324, 'ignis', '', '', '15', 1), ('LABOR/1', 325, 'labor', '', '', '15', 1), ('LITVS/2', 326, 'litus', '', '', '15', 1), ('LVMEN', 327, 'lumen', '', '', '15', 1), ('PECTVS', 328, 'pectus', '', '', '15', 1), ('PONO', 329, 'pono', '', '', '15', 1), ('PROVINCIA', 330, 'provincia', '', '', '15', 1), ('SVPER/2', 331, 'super', '', '', '15', 1), ('SVRGO', 332, 'surgo', '', '', '15', 1), ('TEMPTO', 333, 'tempto', '', '', '15', 1), ('TRISTIS', 334, 'tristis', '', '', '15', 1), ('VNDA', 335, 'unda', '', '', '15', 1), ('VOLVO', 336, 'volvo', '', '', '15', 1), ('ARDEO', 337, 'ardeo', '', '', '16', 1), ('CASVS', 338, 'casus', '', '', '16', 1), ('CORNV', 339, 'cornu', '', '', '16', 1), ('DIES', 340, 'dies', '', '', '16', 1), ('DOMVS', 341, 'domus', '', '', '16', 1), ('FACIES', 342, 'facies', '', '', '16', 1), ('FIDES/2', 343, 'fides', '', '', '16', 1), ('FLVCTVS', 344, 'fluctus', '', '', '16', 1), ('GENV', 345, 'genu', '', '', '16', 1), ('IGITVR', 346, 'igitur', '', '', '16', 1), ('IMPETVS', 347, 'impetus', '', '', '16', 1), ('INDE', 348, 'inde', '', '', '16', 1), ('MANVS/1', 349, 'manus', '', '', '16', 1), ('METVS', 350, 'metus', '', '', '16', 1), ('MILLEPASSVS', 351, 'mile', '', '', '16', 1), ('PASSVS/1', 352, 'passus', '', '', '16', 1), ('RES', 353, 'res', '', '', '16', 1), ('RESPVBLICA', 354, 'res', '', '', '16', 1), ('RVS', 355, 'rus', '', '', '16', 1), ('SENATVS', 356, 'senatus', '', '', '16', 1), ('SPES', 357, 'spes', '', '', '16', 1), ('TAM', 358, 'tam', '', '', '16', 1), ('VVLTVS', 359, 'vultus', '', '', '16', 1), ('AB', 360, 'a', '', '', '17', 2), ('ACIES', 361, 'acies', '', '', '17', 1), ('ALTER', 362, 'alter', '', '', '17', 1), ('AMITTO', 363, 'amitto', '', '', '17', 1), ('CASTRA/2', 364, 'castra', '', '', '17', 1), ('CASTRAPONERE', 365, 'castra', '', '', '17', 1), ('CERNO', 366, 'cerno', '', '', '17', 1), ('CONCVRRO', 367, 'concurro', '', '', '17', 1), ('CONSTITVO', 368, 'constituo', '', '', '17', 1), ('CONTRA/2', 369, 'contra', '', '', '17', 1), ('CVRRO', 370, 'curro', '', '', '17', 1), ('EPISTOLA', 371, 'epistula', '', '', '17', 1), ('EXERCITVS/1', 372, 'exercitus', '', '', '17', 1), ('FERRVM', 373, 'ferrum', '', '', '17', 1), ('FERVS/2', 374, 'ferus', '', '', '17', 1), ('INCENDO', 375, 'incendo', '', '', '17', 1), ('INSTITVO', 376, 'instituo', '', '', '17', 1), ('IVDICIVM', 377, 'iudicium', '', '', '17', 2), ('MVLTITVDO', 378, 'multitudo', '', '', '17', 1), ('PROELIVM', 379, 'proelium', '', '', '17', 1), ('SPECTO', 380, 'specto', '', '', '17', 1), ('TRAHO', 381, 'traho', '', '', '17', 1), ('VIDEOR', 382, 'videor', '', '', '17', 1), ('ACCIPIO', 383, 'accipio', '', '', '18', 1), ('ADVENTVS', 384, 'adventus', '', '', '18', 1), ('AMICVS/2', 385, 'amicus', '', '', '18', 1), ('APTVS', 386, 'aptus', '', '', '18', 1), ('CARVS', 387, 'carus', '', '', '18', 1), ('CLAMOR', 388, 'clamor', '', '', '18', 1), ('CONFICIO', 389, 'conficio', '', '', '18', 1), ('CVM/3', 390, 'cum', '', '', '18', 1), ('DVM/2', 391, 'dum', '', '', '18', 1), ('FAS', 392, 'fas', '', '', '18', 2), ('FIDELIS/2', 393, 'fidelis', '', '', '18', 1), ('GAVDIVM', 394, 'gaudium', '', '', '18', 1), ('INIMICVS/2', 395, 'inimicus', '', '', '18', 1), ('PAR/2', 396, 'pār', '', '', '18', 1), ('POSTQVAM', 397, 'postquam', '', '', '18', 1), ('QVIA', 398, 'quia', '', '', '18', 1), ('QVOD/1', 399, 'quod', '', '', '18', 1), ('SI/2', 400, 'si', '', '', '18', 1), ('SIMILIS', 401, 'similis', '', '', '18', 1), ('VBI/1', 402, 'ubi', '', '', '18', 1), ('VVLNVS', 403, 'vulnus', '', '', '18', 1), ('AESTVS', 404, 'aestus', '', '', '19', 1), ('AVRIS', 405, 'auris', '', '', '19', 1), ('AVXILIVM', 406, 'auxilium', '', '', '19', 1), ('CAESAR/N', 407, 'Caesar', '', '', '19', 1), ('CAREO', 408, 'careo', '', '', '19', 1), ('EFFICIO', 409, 'efficio', '', '', '19', 1), ('EQVVS', 410, 'equus', '', '', '19', 1), ('FRANGO', 411, 'frango', '', '', '19', 1), ('GRAECIA/N', 412, 'Graecia', '', '', '19', 1), ('GRAECVS/A', 413, 'Graecus', '', '', '19', 1), ('LEVIS/1', 414, 'levis', '', '', '19', 1), ('MEMORIA', 415, 'memoria', '', '', '19', 1), ('NAVIS', 416, 'navis', '', '', '19', 1), ('NVBES', 417, 'nubes', '', '', '19', 1), ('PROPINQVVS', 418, 'propinquus', '', '', '19', 1), ('QVI/1', 419, 'qui', '', '', '19', 1), ('ROMA/N', 420, 'Roma', '', '', '19', 1), ('SOROR', 421, 'soror', '', '', '19', 1), ('TROIA/N', 422, 'Troia', '', '', '19', 1), ('TROIANVS/A', 423, 'Troianus', '', '', '19', 1), ('VERTO', 424, 'verto', '', '', '19', 1), ('APERIO', 425, 'aperio', '', '', '20', 1), ('APERTVS', 426, 'apertus', '', '', '20', 1), ('ARX', 427, 'arx', '', '', '20', 1), ('AVCTORITAS', 428, 'auctoritas', '', '', '20', 1), ('AVTEM', 429, 'autem', '', '', '20', 1), ('CAEDES', 430, 'caedes', '', '', '20', 1), ('CAEDO', 431, 'caedo', '', '', '20', 1), ('CANO', 432, 'cano', '', '', '20', 1), ('CONDO', 433, 'condo', '', '', '20', 1), ('CONSERVO', 434, 'conservo', '', '', '20', 1), ('CVPIO', 435, 'cupio', '', '', '20', 1), ('FATVM', 436, 'fatum', '', '', '20', 1), ('INTEREA', 437, 'interea', '', '', '20', 1), ('OB', 438, 'ob', '', '', '20', 1), ('ORA', 439, 'ora', '', '', '20', 1), ('PROCVL', 440, 'procul', '', '', '20', 1), ('SAEVVS', 441, 'saevus', '', '', '20', 1), ('SIGNVM', 442, 'signum', '', '', '20', 1), ('SOMNVS', 443, 'somnus', '', '', '20', 1), ('VIS', 444, 'vis', '', '', '20', 1), ('VITO', 445, 'vito', '', '', '20', 1), ('CELERITER', 446, 'celeriter', '', '', '21', 1), ('CETERVS', 447, 'ceterus', '', '', '21', 1), ('COGO', 448, 'cogo', '', '', '21', 1), ('DOLVS', 449, 'dolus', '', '', '21', 1), ('FORTITER', 450, 'fortiter', '', '', '21', 1), ('IVBEO', 451, 'iubeo', '', '', '21', 1), ('MALO', 452, 'malo', '', '', '21', 1), ('MOENIA', 453, 'moenia', '', '', '21', 1), ('MOS', 454, 'mos', '', '', '21', 1), ('NECESSEEST', 455, 'necesse', '', '', '21', 1), ('NOLO', 456, 'nolo', '', '', '21', 1), ('NVNTIVS/1', 457, 'nuntius', '', '', '21', 1), ('POSTVLO', 458, 'postulo', '', '', '21', 1), ('PRINCEPS/1', 459, 'princeps', '', '', '21', 1), ('QVAM/1', 460, 'quam', '', '', '21', 2), ('SERVVS/1', 461, 'servus', '', '', '21', 1), ('SINO', 462, 'sino', '', '', '21', 1), ('VETO', 463, 'veto', '', '', '21', 1), ('VIVO', 464, 'vivo', '', '', '21', 1), ('VOLO/3', 465, 'volo', '', '', '21', 1), ('AIO', 466, 'aio', '', '', '22', 1), ('ARTVS/1', 467, 'artus', '', '', '22', 1), ('BENE', 468, 'bene', '', '', '22', 1), ('COGITO', 469, 'cogito', '', '', '22', 1), ('GAVDEO', 470, 'gaudeo', '', '', '22', 1), ('HODIE', 471, 'hodie', '', '', '22', 1), ('IBI', 472, 'ibi', '', '', '22', 1), ('IMPRVDENS', 473, 'imprudens', '', '', '22', 1), ('INQVIO', 474, 'inquam', '', '', '22', 1), ('LIBERI', 475, 'liberi', '', '', '22', 1), ('MODVS', 476, 'modus', '', '', '22', 1), ('NEGO', 477, 'nego', '', '', '22', 1), ('NESCIO', 478, 'nescio', '', '', '22', 1), ('ORBIS', 479, 'orbis', '', '', '22', 1), ('ORBISTERRARVM', 480, 'orbis', '', '', '22', 1), ('OSTENDO', 481, 'ostendo', '', '', '22', 1), ('PRVDENS', 482, 'prudens', '', '', '22', 1), ('PVTO', 483, 'puto', '', '', '22', 1), ('RESPONDEO', 484, 'respondeo', '', '', '22', 1), ('SPERO', 485, 'spero', '', '', '22', 1), ('TRADO', 486, 'trado', '', '', '22', 1), ('ARBITROR', 487, 'arbitror', '', '', '23', 1), ('CIBVS', 488, 'cibus', '', '', '23', 1), ('CONOR', 489, 'conor', '', '', '23', 1), ('CRIMEN', 490, 'crimen', '', '', '23', 1), ('CVNCTVS', 491, 'cunctus', '', '', '23', 1), ('FIDO', 492, 'fido', '', '', '23', 1), ('FRVOR', 493, 'fruor', '', '', '23', 1), ('FVNGOR', 494, 'fungor', '', '', '23', 1), ('IDEM', 495, 'idem', '', '', '23', 1), ('INGREDIOR', 496, 'ingredior', '', '', '23', 1), ('IPSE', 497, 'ipse', '', '', '23', 1), ('LOQVOR', 498, 'loquor', '', '', '23', 1), ('MOROR/1', 499, 'moror', '', '', '23', 1), ('PATIOR', 500, 'patior', '', '', '23', 1), ('POTIOR', 501, 'potior', '', '', '23', 1), ('POTVS/2', 502, 'potus', '', '', '23', 1), ('PROFICISCOR', 503, 'proficiscor', '', '', '23', 1), ('QVIDAM', 504, 'quidam', '', '', '23', 1), ('SEQVOR', 505, 'sequor', '', '', '23', 1), ('VESCOR', 506, 'vescor', '', '', '23', 1), ('VTOR', 507, 'utor', '', '', '23', 1), ('EXITIVM', 508, 'exitium', '', '', '24', 1), ('IMPERO', 509, 'impero', '', '', '24', 1), ('INCOLO/2', 510, 'incolo', '', '', '24', 1), ('INGENIVM', 511, 'ingenium', '', '', '24', 1), ('INTERFICIO', 512, 'interficio', '', '', '24', 1), ('MAXIMVS', 513, 'maximus', '', '', '24', 1), ('MORIOR', 514, 'morior', '', '', '24', 1), ('OCCIDO/2', 515, 'occido', '', '', '24', 1), ('OS/1', 516, 'os', '', '', '24', 1), ('PATEO', 517, 'pateo', '', '', '24', 1), ('PROXIMVS/2', 518, 'proximus', '', '', '24', 1), ('ROGO', 519, 'rogo', '', '', '24', 1), ('SOCIVS/1', 520, 'socius', '', '', '24', 1), ('VVLNERO', 521, 'vulnero', '', '', '24', 1), ('ABEO/1', 522, 'abeo', '', '', '25', 1), ('ADEO/1', 523, 'adeo', '', '', '25', 1), ('AEQVVS', 524, 'aequus', '', '', '25', 1), ('AFFERO', 525, 'affero', '', '', '25', 1), ('AVFERO', 526, 'aufero', '', '', '25', 1), ('COMMVNIS', 527, 'communis', '', '', '25', 1), ('CONFERO', 528, 'confero', '', '', '25', 1), ('EO/3', 529, 'eo', '', '', '25', 1), ('EXEO/1', 530, 'exeo', '', '', '25', 1), ('FERO', 531, 'fero', '', '', '25', 1), ('INEO/1', 532, 'ineo', '', '', '25', 1), ('INFELIX', 533, 'infelix', '', '', '25', 1), ('INFERO', 534, 'infero', '', '', '25', 1), ('OFFERO', 535, 'offero', '', '', '25', 1), ('PEREO/1', 536, 'pereo', '', '', '25', 1), ('REDEO/1', 537, 'redeo', '', '', '25', 1), ('REFERO', 538, 'refero', '', '', '25', 1), ('SECONFERRE', 539, 'se', '', '', '25', 1), ('SVBEO/1', 540, 'subeo', '', '', '25', 1), ('TOLLO', 541, 'tollo', '', '', '25', 1), ('TRANSEO/1', 542, 'transeo', '', '', '25', 1), ('QVAM/1', 543, 'quam', '', '', '26', 2), ('AMOR', 544, 'amor', '', '', '26', 1), ('CANIS', 545, 'canis', '', '', '26', 1), ('CVLPA', 546, 'culpa', '', '', '26', 1), ('DELEO', 547, 'deleo', '', '', '26', 1), ('FACILE', 548, 'facile', '', '', '26', 1), ('GRAVIS', 549, 'gravis', '', '', '26', 1), ('IVSTVS', 550, 'iustus', '', '', '26', 1), ('LONGE', 551, 'longe', '', '', '26', 1), ('MODO/1', 552, 'modo', '', '', '26', 1), ('NVMQVAM', 553, 'numquam', '', '', '26', 1), ('PRIMO', 554, 'primo', '', '', '26', 1), ('PRIMVM', 555, 'primum', '', '', '26', 1), ('RESISTO', 556, 'resisto', '', '', '26', 1), ('SANCTVS', 557, 'sanctus', '', '', '26', 1), ('TVRPIS', 558, 'turpis', '', '', '26', 1), ('VTERQVE', 559, 'uterque', '', '', '26', 1), ('VTILIS', 560, 'utilis', '', '', '26', 1), ('ACCIDO/1', 561, 'accido', '', '', '27', 1), ('AN', 562, 'an', '', '', '27', 1), ('ASSVM/1', 563, 'adsum', '', '', '27', 1), ('AT/2', 564, 'at', '', '', '27', 1), ('AVRA', 565, 'aura', '', '', '27', 1), ('BEATVS', 566, 'beatus', '', '', '27', 1), ('DENIQVE', 567, 'denique', '', '', '27', 1), ('DESPERO', 568, 'despero', '', '', '27', 1), ('FLOREO', 569, 'floreo', '', '', '27', 1), ('FRVCTVS', 570, 'fructus', '', '', '27', 1), ('GLORIA', 571, 'gloria', '', '', '27', 1), ('HORTOR', 572, 'hortor', '', '', '27', 1), ('MOTVS', 573, 'motus', '', '', '27', 1), ('NE/4', 574, 'ne', '', '', '27', 1), ('NEGLIGO', 575, 'neglego', '', '', '27', 1), ('NEQVIDEM', 576, 'quidem', '', '', '27', 1), ('QVIDEM', 577, 'quidem', '', '', '27', 1), ('RECTVS', 578, 'rectus', '', '', '27', 1), ('TELLVS', 579, 'tellus', '', '', '27', 1), ('TEMPERO', 580, 'tempero', '', '', '27', 1), ('VERO/3', 581, 'vero', '', '', '27', 1), ('VTINAM', 582, 'utinam', '', '', '27', 1), ('APPROPINQVO', 583, 'appropinquo', '', '', '28', 1), ('BIBO/2', 584, 'bibo', '', '', '28', 1), ('CIVILIS', 585, 'civilis', '', '', '28', 1), ('DEINDE', 586, 'deinde', '', '', '28', 1), ('DIRVS', 587, 'dirus', '', '', '28', 1), ('GLADIVS', 588, 'gladius', '', '', '28', 1), ('IVDEX', 589, 'iudex', '', '', '28', 1), ('IVDICIVM', 590, 'iudicium', '', '', '28', 2), ('LIBERE', 591, 'libere', '', '', '28', 1), ('NEFAS', 592, 'nefas', '', '', '28', 2), ('OPPIDVM', 593, 'oppidum', '', '', '28', 1), ('POENA', 594, 'poena', '', '', '28', 1), ('POENASDARE', 595, 'poenas', '', '', '28', 1), ('SOL', 596, 'sol', '', '', '28', 1), ('TALIS', 597, 'talis', '', '', '28', 1), ('TELVM', 598, 'telum', '', '', '28', 1), ('TOT', 599, 'tot', '', '', '28', 1), ('TOTIENS', 600, 'totiens', '', '', '28', 1), ('TREMO', 601, 'tremo', '', '', '28', 1), ('VINVM', 602, 'vinum', '', '', '28', 1), ('VT/4', 603, 'ut', '', '', '28', 1), ('APPELLO/1', 604, 'appello', '', '', '29', 1), ('APVD', 605, 'apud', '', '', '29', 1), ('COLO/2', 606, 'colo', '', '', '29', 1), ('CVR/1', 607, 'cur', '', '', '29', 1), ('ERIPIO', 608, 'eripio', '', '', '29', 1), ('FIO', 609, 'fio', '', '', '29', 1), ('HABITO', 610, 'habito', '', '', '29', 1), ('IVNGO', 611, 'iungo', '', '', '29', 1), ('LATVS/2', 612, 'latus', '', '', '29', 1), ('LIBERO', 613, 'libero', '', '', '29', 1), ('MIROR', 614, 'miror', '', '', '29', 1), ('NVM', 615, 'num', '', '', '29', 1), ('PRECOR', 616, 'precor', '', '', '29', 1), ('QVAERO', 617, 'quaero', '', '', '29', 1), ('QVIS/1', 618, 'quis', '', '', '29', 1), ('QVOMODO/1', 619, 'quomodo', '', '', '29', 1), ('QVOT/1', 620, 'quot', '', '', '29', 1), ('QVOTIENS/2', 621, 'quotiens', '', '', '29', 1), ('REQVIRO', 622, 'requiro', '', '', '29', 1), ('STATIM', 623, 'statim', '', '', '29', 1), ('VNDIQVE', 624, 'undique', '', '', '29', 1), ('ALIQVIS', 625, 'aliquis', '', '', '30', 1), ('AMICITIA', 626, 'amicitia', '', '', '30', 1), ('CERTE', 627, 'certo', '', '', '30', 1), ('CONSPICIO', 628, 'conspicio', '', '', '30', 1), ('IMPERATOR', 629, 'imperator', '', '', '30', 1), ('METVO', 630, 'metuo', '', '', '30', 1), ('MOX', 631, 'mox', '', '', '30', 1), ('NISI', 632, 'nisi', '', '', '30', 1), ('OPS', 633, 'ops', '', '', '30', 1), ('PHILOSOPHIA', 634, 'philosophia', '', '', '30', 1), ('QVOQVE', 635, 'quoque', '', '', '30', 1), ('SIMVL/1', 636, 'simul', '', '', '30', 1), ('SIN', 637, 'sin', '', '', '30', 1), ('SVSCIPIO', 638, 'suscipio', '', '', '30', 1), ('VEREOR', 639, 'vereor', '', '', '30', 1), ('VICTORIA', 640, 'victoria', '', '', '30', 1), ('COMMITTO', 641, 'committo', '', '', '31', 1), ('CONVENIO', 642, 'convenio', '', '', '31', 1), ('MALE', 643, 'male', '', '', '31', 1), ('PONS', 644, 'pons', '', '', '31', 1), ('PROBO', 645, 'probo', '', '', '31', 1), ('TAMQVAM/1', 646, 'tamquam', '', '', '31', 1), ('VOLVPTAS', 647, 'voluptas', '', '', '31', 1), ('ANTE/2', 648, 'ante', '', '', '32', 2), ('FAS', 649, 'fas', '', '', '32', 2), ('FORSITAN', 650, 'forsan', '', '', '32', 1), ('LICEO', 651, 'liceo', '', '', '32', 1), ('MIRABILIS', 652, 'mirabilis', '', '', '32', 1), ('NEFAS', 653, 'nefas', '', '', '32', 2), ('OPORTET', 654, 'oportet', '', '', '32', 1)]
section_list ={'1': 'start', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': '10', '12': '11', '13': '12', '14': '13', '15': '14', '16': '15', '17': '16', '18': '17', '19': '18', '20': '19', '21': '20', '22': '21', '23': '22', '24': '23', '25': '24', '26': '25', '27': '26', '28': '27', '29': '28', '30': '29', '31': '30', '32': '31', 'end': '32', 'start': 'start'}
title = "Introduction to Latin (Shelmerdine)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)