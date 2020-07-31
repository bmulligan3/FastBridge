import text
nan=""
section_words = {'start': -1, '11': 64, '12': 80, '19': 228, '28': 438, '1': 27, '10': 47, '13': 97, '14': 119, '15': 159, '16': 179, '17': 194, '18': 209, '2': 255, '20': 277, '21': 299, '22': 319, '23': 340, '24': 360, '25': 378, '26': 397, '27': 422, '29': 462, '3': 483, '30': 504, '31': 526, '32': 555, '33': 571, '34': 594, '35': 614, '36': 634, '37': 658, '38': 680, '39': 698, '4': 723, '40': 747, '5': 771, '6': 792, '7': 814, '8': 838, '9': 857, 'end': -2}
the_text =  [('EGO', 0, 'ego', '', '', '11', 2), ('ADOLESCENS/2', 1, 'adulescens', '', '', '12', 2), ('QVIS/1', 2, 'quis', '', '', '19', 2), ('VT/4', 3, 'ut', '', '', '28', 2), ('AMABOTE', 4, 'amabo', '', '', '1', 1), ('AMO', 5, 'amo', '', '', '1', 1), ('COGITO', 6, 'cogito', '', '', '1', 1), ('CONSERVO', 7, 'conservo', '', '', '1', 1), ('DEBEO', 8, 'debeo', '', '', '1', 1), ('DO', 9, 'do', '', '', '1', 1), ('EGO', 10, 'ego', '', '', '1', 2), ('ERRO/2', 11, 'erro', '', '', '1', 1), ('LAVDO', 12, 'laudo', '', '', '1', 1), ('MONEO', 13, 'moneo', '', '', '1', 1), ('NIHIL', 14, 'nihil', '', '', '1', 2), ('NON', 15, 'non', '', '', '1', 1), ('QVIS/1', 16, 'quis', '', '', '1', 2), ('SAEPE', 17, 'saepe', '', '', '1', 1), ('SALVE', 18, 'salve', '', '', '1', 1), ('SALVEO', 19, 'salveo', '', '', '1', 1), ('SERVO', 20, 'servo', '', '', '1', 1), ('SI/2', 21, 'si', '', '', '1', 1), ('SVM/1', 22, 'sum', '', '', '1', 2), ('TERREO', 23, 'terreo', '', '', '1', 1), ('VALE', 24, 'vale', '', '', '1', 1), ('VALEO', 25, 'valeo', '', '', '1', 1), ('VIDEO', 26, 'video', '', '', '1', 1), ('VOCO', 27, 'voco', '', '', '1', 1), ('AMICITIA', 28, 'amicitia', '', '', '10', 1), ('AVDIO', 29, 'audio', '', '', '10', 1), ('BEATVS', 30, 'beatus', '', '', '10', 1), ('CAPIO/2', 31, 'capio', '', '', '10', 1), ('CVM/2', 32, 'cum', '', '', '10', 1), ('CVPIDITAS', 33, 'cupiditas', '', '', '10', 1), ('DICO/2', 34, 'dico', '', '', '10', 1), ('FACIO', 35, 'facio', '', '', '10', 1), ('FVGIO', 36, 'fugio', '', '', '10', 1), ('HORA', 37, 'hora', '', '', '10', 1), ('INVENIO', 38, 'invenio', '', '', '10', 1), ('NATVRA', 39, 'natura', '', '', '10', 1), ('QVONIAM', 40, 'quoniam', '', '', '10', 1), ('SENECTVS/1', 41, 'senectus', '', '', '10', 1), ('TIMOR', 42, 'timor', '', '', '10', 1), ('VENIO', 43, 'venio', '', '', '10', 1), ('VERITAS', 44, 'veritas', '', '', '10', 1), ('VIA', 45, 'via', '', '', '10', 1), ('VIVO', 46, 'vivo', '', '', '10', 1), ('VOLVPTAS', 47, 'voluptas', '', '', '10', 1), ('AMICVS/2', 48, 'amicus', '', '', '11', 1), ('AVTEM', 49, 'autem', '', '', '11', 1), ('BENE', 50, 'bene', '', '', '11', 2), ('CAPVT', 51, 'caput', '', '', '11', 1), ('CARVS', 52, 'carus', '', '', '11', 1), ('CONSVL', 53, 'consul', '', '', '11', 1), ('ETIAM', 54, 'etiam', '', '', '11', 1), ('IDEM', 55, 'idem', '', '', '11', 1), ('INTELLIGO', 56, 'intellego', '', '', '11', 1), ('IS', 57, 'is', '', '', '11', 1), ('MITTO', 58, 'mitto', '', '', '11', 1), ('NEMO', 59, 'nemo', '', '', '11', 1), ('NEQVE', 60, 'neque', '', '', '11', 1), ('NEQVENEC', 61, 'neque', '', '', '11', 1), ('QVOD/1', 62, 'quod', '', '', '11', 1), ('SENTIO', 63, 'sentio', '', '', '11', 1), ('TV', 64, 'tu', '', '', '11', 2), ('ACERBVS', 65, 'acerbus', '', '', '12', 1), ('AMITTO', 66, 'amitto', '', '', '12', 1), ('ANNVS', 67, 'annus', '', '', '12', 1), ('ASIA/N', 68, 'Asia', '', '', '12', 1), ('CADO', 69, 'cado', '', '', '12', 1), ('CAESAR/N', 70, 'Caesar', '', '', '12', 1), ('CREO', 71, 'creo', '', '', '12', 1), ('DIV', 72, 'diu', '', '', '12', 1), ('MATER', 73, 'mater', '', '', '12', 1), ('MEDICA/1', 74, 'medica', '', '', '12', 1), ('MEDICVS/1', 75, 'medicus', '', '', '12', 1), ('NVPER', 76, 'nuper', '', '', '12', 1), ('PATER', 77, 'pater', '', '', '12', 1), ('PATIENTIA', 78, 'patientia', '', '', '12', 1), ('PRINCIPIVM', 79, 'principium', '', '', '12', 1), ('PRO/1', 80, 'pro', '', '', '12', 1), ('ALO', 81, 'alo', '', '', '13', 1), ('ANTE/2', 82, 'ante', '', '', '13', 1), ('DILIGO/3', 83, 'diligo', '', '', '13', 1), ('DIVITIAE', 84, 'divitia', '', '', '13', 1), ('DOCTVS', 85, 'doctus', '', '', '13', 1), ('FACTVM', 86, 'factum', '', '', '13', 1), ('FORTVNATVS', 87, 'fortunatus', '', '', '13', 1), ('IPSE', 88, 'ipse', '', '', '13', 1), ('IVNGO', 89, 'iungo', '', '', '13', 1), ('NAM', 90, 'nam', '', '', '13', 1), ('OLIM', 91, 'olim', '', '', '13', 1), ('PER', 92, 'per', '', '', '13', 1), ('QVISQVE/2', 93, 'quisque', '', '', '13', 1), ('SIGNVM', 94, 'signum', '', '', '13', 1), ('STO', 95, 'sto', '', '', '13', 1), ('SVI/1', 96, 'sui', '', '', '13', 1), ('SVVS', 97, 'suus', '', '', '13', 1), ('AB', 98, 'a', '', '', '14', 1), ('ANIMAL', 99, 'animal', '', '', '14', 1), ('APPELLO/1', 100, 'appello', '', '', '14', 1), ('AQVA', 101, 'aqua', '', '', '14', 1), ('ARS', 102, 'ars', '', '', '14', 1), ('AVRIS', 103, 'auris', '', '', '14', 1), ('CIVIS', 104, 'civis', '', '', '14', 1), ('CVRRO', 105, 'curro', '', '', '14', 1), ('IVS/1', 106, 'ius', '', '', '14', 1), ('MARE', 107, 'mare', '', '', '14', 1), ('MORS', 108, 'mors', '', '', '14', 1), ('MVTO/2', 109, 'muto', '', '', '14', 1), ('NVBES', 110, 'nubes', '', '', '14', 1), ('OS/1', 111, 'os', '', '', '14', 1), ('PARS', 112, 'pars', '', '', '14', 1), ('ROMA/N', 113, 'Roma', '', '', '14', 1), ('TENEO', 114, 'teneo', '', '', '14', 1), ('TRANS/2', 115, 'trans', '', '', '14', 1), ('TVRBA', 116, 'turba', '', '', '14', 1), ('VIS', 117, 'vis', '', '', '14', 1), ('VITO', 118, 'vito', '', '', '14', 1), ('VRBS', 119, 'urbs', '', '', '14', 1), ('CENTVM', 120, 'centum', '', '', '15', 1), ('COMMITTO', 121, 'committo', '', '', '15', 1), ('DECEM', 122, 'decem', '', '', '15', 1), ('DVO', 123, 'duo', '', '', '15', 1), ('DVODECIM', 124, 'duodecim', '', '', '15', 1), ('DVODEVIGINTI', 125, 'duodevigenti', '', '', '15', 1), ('EICIO', 126, 'eicio', '', '', '15', 1), ('EXSPECTO', 127, 'exspecto', '', '', '15', 1), ('IACIO', 128, 'iacio', '', '', '15', 1), ('INTER', 129, 'inter', '', '', '15', 1), ('ITALIA/N', 130, 'Italia', '', '', '15', 1), ('ITAQVE', 131, 'itaque', '', '', '15', 1), ('MEMORIA', 132, 'memoria', '', '', '15', 1), ('MILLE', 133, 'mille', '', '', '15', 1), ('MISER', 134, 'miser', '', '', '15', 1), ('NOVEM', 135, 'novem', '', '', '15', 1), ('OCTO', 136, 'octo', '', '', '15', 1), ('PRIMVS', 137, 'primus', '', '', '15', 2), ('QVATVOR', 138, 'quattuor', '', '', '15', 1), ('QVINDECIM', 139, 'quindecim', '', '', '15', 1), ('QVINQVE', 140, 'quinque', '', '', '15', 1), ('SECVNDVS/1', 141, 'secundus', '', '', '15', 2), ('SEDECIM', 142, 'sedecim', '', '', '15', 1), ('SEPTEM', 143, 'septem', '', '', '15', 1), ('SEPTENDECIM', 144, 'septendecim', '', '', '15', 1), ('SEX', 145, 'sex', '', '', '15', 1), ('TEMPESTAS', 146, 'tempestas', '', '', '15', 1), ('TERTIVS', 147, 'tertius', '', '', '15', 1), ('TIMEO', 148, 'timeo', '', '', '15', 1), ('TREDECIM', 149, 'tredecim', '', '', '15', 1), ('TRES', 150, 'tres', '', '', '15', 1), ('VIGINTI', 151, 'viginti', '', '', '15', 1), ('VIGINTIDVO', 152, 'viginti', '', '', '15', 1), ('VIGINTIQVATTVOR', 153, 'viginti', '', '', '15', 1), ('VIGINTIQVINQVE', 154, 'viginti', '', '', '15', 1), ('VIGINTITRES', 155, 'viginti', '', '', '15', 1), ('VIGINTIVNVS', 156, 'viginti', '', '', '15', 1), ('VNDECIM', 157, 'undecim', '', '', '15', 1), ('VNDEVIGINTI', 158, 'undeviginti', '', '', '15', 1), ('VNVS', 159, 'unus', '', '', '15', 2), ('ACER/2', 160, 'acer', '', '', '16', 1), ('AETAS', 161, 'aetas', '', '', '16', 1), ('AVDITOR', 162, 'auditor', '', '', '16', 1), ('BREVIS', 163, 'brevis', '', '', '16', 1), ('CELER', 164, 'celer', '', '', '16', 1), ('CLEMENTIA', 165, 'clementia', '', '', '16', 1), ('DIFFICILIS', 166, 'difficilis', '', '', '16', 1), ('DVLCIS', 167, 'dulcis', '', '', '16', 1), ('FACILIS', 168, 'facilis', '', '', '16', 1), ('FORTIS', 169, 'fortis', '', '', '16', 1), ('INGENS', 170, 'ingens', '', '', '16', 1), ('IVCVNDVS', 171, 'iucundus', '', '', '16', 1), ('LONGVS', 172, 'longus', '', '', '16', 1), ('MENS', 173, 'mens', '', '', '16', 1), ('OMNIS', 174, 'omnis', '', '', '16', 1), ('POTENS', 175, 'potens', '', '', '16', 1), ('QVAM/1', 176, 'quam', '', '', '16', 2), ('REGO', 177, 'rego', '', '', '16', 1), ('SATVRA', 178, 'satura', '', '', '16', 1), ('SENEX/1', 179, 'senex', '', '', '16', 1), ('AVT', 180, 'aut', '', '', '17', 1), ('CAECVS', 181, 'caecus', '', '', '17', 1), ('CITO/2', 182, 'cito', '', '', '17', 1), ('COEPIO', 183, 'coepi', '', '', '17', 1), ('CVPIO', 184, 'cupio', '', '', '17', 1), ('DELEO', 185, 'deleo', '', '', '17', 1), ('DESIDERO', 186, 'desidero', '', '', '17', 1), ('INCIPIO', 187, 'incipio', '', '', '17', 1), ('LEVIS/1', 188, 'levis', '', '', '17', 1), ('LIBELLVS', 189, 'libellus', '', '', '17', 1), ('NAVIGO', 190, 'navigo', '', '', '17', 1), ('NEGLIGO', 191, 'neglego', '', '', '17', 1), ('QVI/1', 192, 'qui', '', '', '17', 2), ('QVOQVE', 193, 'quoque', '', '', '17', 1), ('RECITO/1', 194, 'recito', '', '', '17', 1), ('CLARVS', 195, 'clarus', '', '', '18', 1), ('CVR/1', 196, 'cur', '', '', '18', 1), ('DEINDE', 197, 'deinde', '', '', '18', 1), ('FLVMEN', 198, 'flumen', '', '', '18', 1), ('FLVO', 199, 'fluo', '', '', '18', 1), ('GENVS/1', 200, 'genus', '', '', '18', 1), ('HOSTIS', 201, 'hostis', '', '', '18', 1), ('LEGO/2', 202, 'lego', '', '', '18', 1), ('LVDVS', 203, 'ludus', '', '', '18', 1), ('MISCEO', 204, 'misceo', '', '', '18', 1), ('MORTALIS/2', 205, 'mortalis', '', '', '18', 1), ('MOVEO', 206, 'moveo', '', '', '18', 1), ('PROBITAS', 207, 'probitas', '', '', '18', 1), ('SCIENTIA', 208, 'scientia', '', '', '18', 1), ('VIDEOR', 209, 'videor', '', '', '18', 1), ('ARGVMENTVM', 210, 'argumentum', '', '', '19', 1), ('AT/2', 211, 'at', '', '', '19', 1), ('AVCTOR', 212, 'auctor', '', '', '19', 1), ('BENEFICIVM', 213, 'beneficium', '', '', '19', 1), ('CERTVS', 214, 'certus', '', '', '19', 1), ('CONTRA/2', 215, 'contra', '', '', '19', 1), ('DELECTO', 216, 'delecto', '', '', '19', 1), ('FAMILIA', 217, 'familia', '', '', '19', 1), ('GRAECIA/N', 218, 'Graecia', '', '', '19', 1), ('GRAVIS', 219, 'gravis', '', '', '19', 1), ('IAM', 220, 'iam', '', '', '19', 1), ('IMMORTALIS', 221, 'immortalis', '', '', '19', 1), ('IVDEX', 222, 'iudex', '', '', '19', 1), ('IVDICIVM', 223, 'iudicium', '', '', '19', 1), ('LIBERO', 224, 'libero', '', '', '19', 1), ('NISI', 225, 'nisi', '', '', '19', 1), ('PARO/2', 226, 'paro', '', '', '19', 1), ('QVI/1', 227, 'qui', '', '', '19', 2), ('SCELVS', 228, 'scelus', '', '', '19', 1), ('ANTIQVVS', 229, 'antiquus', '', '', '2', 1), ('ET/1', 230, 'et', '', '', '2', 1), ('ET/2', 231, 'et', '', '', '2', 1), ('ETET', 232, 'et', '', '', '2', 1), ('FAMA', 233, 'fama', '', '', '2', 1), ('FORMA', 234, 'forma', '', '', '2', 1), ('FORTVNA', 235, 'fortuna', '', '', '2', 1), ('IRA', 236, 'ira', '', '', '2', 1), ('MAGNVS', 237, 'magnus', '', '', '2', 1), ('MEVS', 238, 'meus', '', '', '2', 1), ('MVLTVS', 239, 'multus', '', '', '2', 1), ('NAVTA', 240, 'nauta', '', '', '2', 1), ('O', 241, 'o', '', '', '2', 1), ('PATRIA', 242, 'patria', '', '', '2', 1), ('PECVNIA', 243, 'pecunia', '', '', '2', 1), ('PHILOSOPHIA', 244, 'philosophia', '', '', '2', 1), ('POENA', 245, 'poena', '', '', '2', 1), ('POENASDARE', 246, 'poenas', '', '', '2', 1), ('POETA', 247, 'poeta', '', '', '2', 1), ('PORTA', 248, 'porta', '', '', '2', 1), ('PVELLA', 249, 'puella', '', '', '2', 1), ('ROSA', 250, 'rosa', '', '', '2', 1), ('SED', 251, 'sed', '', '', '2', 1), ('SENTENTIA', 252, 'sententia', '', '', '2', 1), ('SINE', 253, 'sine', '', '', '2', 1), ('TVVS', 254, 'tuus', '', '', '2', 1), ('VITA', 255, 'vita', '', '', '2', 1), ('CAREO', 256, 'careo', '', '', '20', 1), ('COMMVNIS', 257, 'communis', '', '', '20', 1), ('CONIVRATI', 258, 'coniurati', '', '', '20', 1), ('CORNV', 259, 'cornu', '', '', '20', 1), ('DEFENDO', 260, 'defendo', '', '', '20', 1), ('DEXTER', 261, 'dexter', '', '', '20', 1), ('DISCEDO/1', 262, 'discedo', '', '', '20', 1), ('FRVCTVS', 263, 'fructus', '', '', '20', 1), ('GENV', 264, 'genu', '', '', '20', 1), ('MANVS/1', 265, 'manus', '', '', '20', 1), ('METVS', 266, 'metus', '', '', '20', 1), ('MONS', 267, 'mons', '', '', '20', 1), ('ODI', 268, 'odi', '', '', '20', 1), ('PROHIBEO', 269, 'prohibeo', '', '', '20', 1), ('PRONVNTIO', 270, 'pronuntio', '', '', '20', 1), ('SENATVS', 271, 'senatus', '', '', '20', 1), ('SENSVS', 272, 'sensus', '', '', '20', 1), ('SERVITVS', 273, 'servitus', '', '', '20', 1), ('SINISTER', 274, 'sinister', '', '', '20', 1), ('SPIRITVS', 275, 'spiritus', '', '', '20', 1), ('STATVS/1', 276, 'status', '', '', '20', 1), ('VERSVS/1', 277, 'versus', '', '', '20', 1), ('ASPER', 278, 'asper', '', '', '21', 1), ('ATQVE/1', 279, 'atque', '', '', '21', 1), ('CASA', 280, 'casa', '', '', '21', 1), ('CAVSA', 281, 'causa', '', '', '21', 1), ('CONTINEO', 282, 'contineo', '', '', '21', 1), ('FENESTRA', 283, 'fenestra', '', '', '21', 1), ('FINIS', 284, 'finis', '', '', '21', 1), ('GENS', 285, 'gens', '', '', '21', 1), ('ITERVM', 286, 'iterum', '', '', '21', 1), ('IVBEO', 287, 'iubeo', '', '', '21', 1), ('LABORO', 288, 'laboro', '', '', '21', 1), ('MVNDVS/1', 289, 'mundus', '', '', '21', 1), ('NAVIS', 290, 'navis', '', '', '21', 1), ('RAPIO', 291, 'rapio', '', '', '21', 1), ('RELINQVO', 292, 'relinquo', '', '', '21', 1), ('SALVS', 293, 'salus', '', '', '21', 1), ('SCIO', 294, 'scio', '', '', '21', 1), ('TANGO', 295, 'tango', '', '', '21', 1), ('TROIA/N', 296, 'Troia', '', '', '21', 1), ('VICINA', 297, 'vicina', '', '', '21', 1), ('VICINVS/2', 298, 'vicinus', '', '', '21', 1), ('VVLGVS', 299, 'vulgus', '', '', '21', 1), ('AEQVVS', 300, 'aequus', '', '', '22', 1), ('CERNO', 301, 'cerno', '', '', '22', 1), ('DIES', 302, 'dies', '', '', '22', 1), ('ERIPIO', 303, 'eripio', '', '', '22', 1), ('FELIX', 304, 'felix', '', '', '22', 1), ('FERRVM', 305, 'ferrum', '', '', '22', 1), ('FIDES/2', 306, 'fides', '', '', '22', 1), ('IGNIS', 307, 'ignis', '', '', '22', 1), ('INCERTVS', 308, 'incertus', '', '', '22', 1), ('INQVIO', 309, 'inquam', '', '', '22', 1), ('LATINVS/A', 310, 'Latinus', '', '', '22', 1), ('MEDIVS', 311, 'medius', '', '', '22', 1), ('MODVS', 312, 'modus', '', '', '22', 1), ('PROTINVS', 313, 'protinus', '', '', '22', 1), ('QVONDAM', 314, 'quondam', '', '', '22', 1), ('RES', 315, 'res', '', '', '22', 1), ('RESPVBLICA', 316, 'res', '', '', '22', 1), ('SPES', 317, 'spes', '', '', '22', 1), ('TOLLO', 318, 'tollo', '', '', '22', 1), ('VLTRA/2', 319, 'ultra', '', '', '22', 1), ('ALIQVIS', 320, 'aliquis', '', '', '23', 1), ('ARX', 321, 'arx', '', '', '23', 1), ('AVERTO', 322, 'averto', '', '', '23', 1), ('DVX', 323, 'dux', '', '', '23', 1), ('EDVCO/1', 324, 'educo', '', '', '23', 1), ('EQVVS', 325, 'equus', '', '', '23', 1), ('GAVDEO', 326, 'gaudeo', '', '', '23', 1), ('HASTA', 327, 'hasta', '', '', '23', 1), ('INSVLA', 328, 'insula', '', '', '23', 1), ('LITVS/2', 329, 'litus', '', '', '23', 1), ('MAGNANIMVS', 330, 'magnanimus', '', '', '23', 1), ('MILES', 331, 'miles', '', '', '23', 1), ('OPPRIMO', 332, 'opprimo', '', '', '23', 1), ('ORATOR', 333, 'orator', '', '', '23', 1), ('OSTENDO', 334, 'ostendo', '', '', '23', 1), ('PETO', 335, 'peto', '', '', '23', 1), ('PREMO', 336, 'premo', '', '', '23', 1), ('QVISQVIS/2', 337, 'quisquis', '', '', '23', 1), ('SACERDOS', 338, 'sacerdos', '', '', '23', 1), ('VERTO', 339, 'verto', '', '', '23', 1), ('VMQVAM', 340, 'umquam', '', '', '23', 1), ('ACCIPIO', 341, 'accipio', '', '', '24', 1), ('CARTHAGO/N', 342, 'Carthago', '', '', '24', 1), ('EXCIPIO', 343, 'excipio', '', '', '24', 1), ('EXPELLO', 344, 'expello', '', '', '24', 1), ('FABVLA/1', 345, 'fabula', '', '', '24', 1), ('IMPERATOR', 346, 'imperator', '', '', '24', 1), ('IMPERIVM', 347, 'imperium', '', '', '24', 1), ('NARRO', 348, 'narro', '', '', '24', 1), ('PELLO', 349, 'pello', '', '', '24', 1), ('PERFVGIVM', 350, 'perfugium', '', '', '24', 1), ('POSTEA', 351, 'postea', '', '', '24', 1), ('QVAERO', 352, 'quaero', '', '', '24', 1), ('RECIPIO', 353, 'recipio', '', '', '24', 1), ('RED', 354, 're', '', '', '24', 1), ('RIDEO', 355, 'rideo', '', '', '24', 1), ('SERVA', 356, 'serva', '', '', '24', 1), ('SERVVS/1', 357, 'servus', '', '', '24', 1), ('SOLACIVM', 358, 'solacium', '', '', '24', 1), ('VT/4', 359, 'ut', '', '', '24', 2), ('VVLNVS', 360, 'vulnus', '', '', '24', 1), ('AIO', 361, 'aio', '', '', '25', 1), ('CREDO', 362, 'credo', '', '', '25', 1), ('DEHINC', 363, 'dehinc', '', '', '25', 1), ('FEROX', 364, 'ferox', '', '', '25', 1), ('FIDELIS/2', 365, 'fidelis', '', '', '25', 1), ('GEMINVS', 366, 'geminus', '', '', '25', 1), ('HIC/2', 367, 'hic', '', '', '25', 1), ('IACEO', 368, 'iaceo', '', '', '25', 1), ('LINGVA', 369, 'lingua', '', '', '25', 1), ('NEGO', 370, 'nego', '', '', '25', 1), ('NESCIO', 371, 'nescio', '', '', '25', 1), ('NVNTIO', 372, 'nuntio', '', '', '25', 1), ('PATEFACIO', 373, 'patefacio', '', '', '25', 1), ('PVTO', 374, 'puto', '', '', '25', 1), ('SAPIENS/2', 375, 'sapiens', '', '', '25', 2), ('SPERO', 376, 'spero', '', '', '25', 1), ('SVSCIPIO', 377, 'suscipio', '', '', '25', 1), ('VLTIMVS', 378, 'ulterior', '', '', '25', 1), ('CENA', 379, 'cena', '', '', '26', 1), ('FORVM/1', 380, 'forum', '', '', '26', 1), ('INVITO', 381, 'invito', '', '', '26', 1), ('LEX', 382, 'lex', '', '', '26', 1), ('LIMEN', 383, 'limen', '', '', '26', 1), ('LVX', 384, 'lux', '', '', '26', 1), ('MENSA', 385, 'mensa', '', '', '26', 1), ('MENSASECVNDA', 386, 'mensa', '', '', '26', 1), ('NOX', 387, 'nox', '', '', '26', 1), ('PRAE/1', 388, 'prae', '', '', '26', 1), ('PVDICVS', 389, 'pudicus', '', '', '26', 1), ('QVAM/1', 390, 'quam', '', '', '26', 2), ('QVIDAM', 391, 'quidam', '', '', '26', 1), ('SOMNVS', 392, 'somnus', '', '', '26', 1), ('SVPERBVS/2', 393, 'superbus', '', '', '26', 1), ('TANTVM/2', 394, 'tantum', '', '', '26', 1), ('TRISTIS', 395, 'tristis', '', '', '26', 1), ('TVRPIS', 396, 'turpis', '', '', '26', 1), ('VRBANVS', 397, 'urbanus', '', '', '26', 1), ('DELECTATIO', 398, 'delectatio', '', '', '27', 1), ('DILIGENS', 399, 'diligens', '', '', '27', 1), ('DISSIMILIS', 400, 'dissimilis', '', '', '27', 1), ('GRACILIS', 401, 'gracilis', '', '', '27', 1), ('HVMILIS', 402, 'humilis', '', '', '27', 1), ('MAIOR', 403, 'maior', '', '', '27', 1), ('MAIORES', 404, 'maiores', '', '', '27', 1), ('MELIOR', 405, 'melior', '', '', '27', 1), ('NEPOS/1', 406, 'nepos', '', '', '27', 1), ('OPTIMVS', 407, 'optimus', '', '', '27', 1), ('PARVVS/2', 408, 'parvus', '', '', '27', 2), ('PEIOR', 409, 'peior', '', '', '27', 1), ('PESSIMVS', 410, 'pessimus', '', '', '27', 1), ('PLVRIMVS', 411, 'plurimus', '', '', '27', 1), ('PLVS', 412, 'plus', '', '', '27', 1), ('PONO', 413, 'pono', '', '', '27', 1), ('PRIMVS', 414, 'primus', '', '', '27', 2), ('PRIOR', 415, 'prior', '', '', '27', 1), ('PROBO', 416, 'probo', '', '', '27', 1), ('QVOT/1', 417, 'quot', '', '', '27', 1), ('SIMILIS', 418, 'similis', '', '', '27', 1), ('SOL', 419, 'sol', '', '', '27', 1), ('SVPERIOR', 420, 'superior', '', '', '27', 1), ('SVPERVS', 421, 'superus', '', '', '27', 1), ('VTILIS', 422, 'utilis', '', '', '27', 1), ('ARMA', 423, 'arma', '', '', '28', 1), ('CEDO/1', 424, 'cedo', '', '', '28', 1), ('CVRSVS', 425, 'cursus', '', '', '28', 1), ('DEDICO/1', 426, 'dedico', '', '', '28', 1), ('EGEO', 427, 'egeo', '', '', '28', 1), ('EXPLEO', 428, 'expleo', '', '', '28', 1), ('LVNA', 429, 'luna', '', '', '28', 1), ('MORTVVS/2', 430, 'mortuus', '', '', '28', 1), ('NE/4', 431, 'ne', '', '', '28', 1), ('OCCASIO', 432, 'occasio', '', '', '28', 1), ('PARENS/1', 433, 'parens', '', '', '28', 1), ('PRAESTO/1', 434, 'praesto', '', '', '28', 1), ('PRINCEPS/1', 435, 'princeps', '', '', '28', 1), ('STELLA', 436, 'stella', '', '', '28', 1), ('TACEO', 437, 'taceo', '', '', '28', 1), ('VESPER', 438, 'vesper', '', '', '28', 1), ('CONDO', 439, 'condo', '', '', '29', 1), ('CONTENDO', 440, 'contendo', '', '', '29', 1), ('DENIQVE', 441, 'denique', '', '', '29', 1), ('DIGNVS', 442, 'dignus', '', '', '29', 1), ('DVRVS', 443, 'durus', '', '', '29', 1), ('FATVM', 444, 'fatum', '', '', '29', 1), ('INGENIVM', 445, 'ingenium', '', '', '29', 1), ('ITA', 446, 'ita', '', '', '29', 1), ('MOENIA', 447, 'moenia', '', '', '29', 1), ('MOLLIO', 448, 'mollio', '', '', '29', 1), ('NATA', 449, 'nata', '', '', '29', 1), ('NEQVIDEM', 450, 'quidem', '', '', '29', 1), ('OSCVLVM', 451, 'osculum', '', '', '29', 1), ('PVGNO', 452, 'pugno', '', '', '29', 1), ('QVIDEM', 453, 'quidem', '', '', '29', 1), ('RESPONDEO', 454, 'respondeo', '', '', '29', 1), ('SIC', 455, 'sic', '', '', '29', 1), ('SIDVS', 456, 'sidus', '', '', '29', 1), ('SVRGO', 457, 'surgo', '', '', '29', 1), ('TAM', 458, 'tam', '', '', '29', 1), ('TAMQVAM/1', 459, 'tamquam', '', '', '29', 1), ('TAMQVAM/2', 460, 'tam', '', '', '29', 1), ('TANTVS', 461, 'tantus', '', '', '29', 1), ('VERO/3', 462, 'vero', '', '', '29', 1), ('AGER', 463, 'ager', '', '', '3', 1), ('AGRICOLA', 464, 'agricola', '', '', '3', 1), ('AMICA', 465, 'amica', '', '', '3', 1), ('AMICVS/1', 466, 'amicus', '', '', '3', 1), ('AVARVS/2', 467, 'avarus', '', '', '3', 1), ('DE', 468, 'de', '', '', '3', 1), ('FEMINA', 469, 'femina', '', '', '3', 1), ('FILIA', 470, 'filia', '', '', '3', 1), ('FILIVS', 471, 'filius', '', '', '3', 1), ('HABEO', 472, 'habeo', '', '', '3', 1), ('HODIE', 473, 'hodie', '', '', '3', 1), ('IN', 474, 'in', '', '', '3', 2), ('NVMERVS', 475, 'numerus', '', '', '3', 1), ('PAVCI', 476, 'paucus', '', '', '3', 1), ('POPVLVS/1', 477, 'populus', '', '', '3', 1), ('PVER', 478, 'puer', '', '', '3', 1), ('ROMANVS/A', 479, 'Romanus', '', '', '3', 1), ('SAPIENTIA', 480, 'sapientia', '', '', '3', 1), ('SATIO/2', 481, 'satio', '', '', '3', 1), ('SEMPER', 482, 'semper', '', '', '3', 1), ('VIR', 483, 'vir', '', '', '3', 1), ('BIBO/2', 484, 'bibo', '', '', '30', 1), ('CETERVS', 485, 'ceterus', '', '', '30', 1), ('COGNOSCO', 486, 'cognosco', '', '', '30', 1), ('COMPREHENDO', 487, 'comprehendo', '', '', '30', 1), ('CONSVMO', 488, 'consumo', '', '', '30', 1), ('DVBITO', 489, 'dubito', '', '', '30', 1), ('EXPONO', 490, 'expono', '', '', '30', 1), ('FVRTIM', 491, 'furtim', '', '', '30', 1), ('HONOR', 492, 'honor', '', '', '30', 1), ('MINVO', 493, 'minuo', '', '', '30', 1), ('MOX', 494, 'mox', '', '', '30', 1), ('NOSCO', 495, 'nosco', '', '', '30', 1), ('PRIMO', 496, 'primo', '', '', '30', 1), ('QVANTVS/1', 497, 'quantus', '', '', '30', 1), ('REPENTE', 498, 'repente', '', '', '30', 1), ('RIDICVLVS/2', 499, 'ridiculus', '', '', '30', 1), ('ROGO', 500, 'rogo', '', '', '30', 1), ('TANTVSDEM', 501, 'tantusdem', '', '', '30', 1), ('VIVVS/2', 502, 'vivus', '', '', '30', 1), ('VNDE/1', 503, 'unde', '', '', '30', 1), ('VTRVMAN', 504, 'utrum', '', '', '30', 1), ('AFFERO', 505, 'affero', '', '', '31', 1), ('APVD', 506, 'apud', '', '', '31', 1), ('AS', 507, 'as', '', '', '31', 1), ('AVXILIVM', 508, 'auxilium', '', '', '31', 1), ('CONFERO', 509, 'confero', '', '', '31', 1), ('CVM/3', 510, 'cum', '', '', '31', 1), ('DIGITVS', 511, 'digitus', '', '', '31', 1), ('DOLEO', 512, 'doleo', '', '', '31', 1), ('DORMIO', 513, 'dormio', '', '', '31', 1), ('ELEPHANTVS', 514, 'elephantus', '', '', '31', 1), ('EXSILIVM', 515, 'exilium', '', '', '31', 1), ('FERO', 516, 'fero', '', '', '31', 1), ('INVIDEO', 517, 'invideo', '', '', '31', 1), ('INVIDIA', 518, 'invidia', '', '', '31', 1), ('MEDIOCRIS', 519, 'mediocris', '', '', '31', 1), ('OCCIDO/1', 520, 'occido', '', '', '31', 1), ('OFFERO', 521, 'offero', '', '', '31', 1), ('REFERO', 522, 'refero', '', '', '31', 1), ('RVMOR', 523, 'rumor', '', '', '31', 1), ('SEMEL', 524, 'semel', '', '', '31', 1), ('VINVM', 525, 'vinum', '', '', '31', 1), ('VSQVE', 526, 'usque', '', '', '31', 1), ('ACRITER', 527, 'acriter', '', '', '32', 1), ('BENE', 528, 'bene', '', '', '32', 2), ('CELERITER', 529, 'celeriter', '', '', '32', 1), ('CVSTODIA', 530, 'custodia', '', '', '32', 1), ('DIVES', 531, 'dives', '', '', '32', 1), ('DIVTIVS', 532, 'diutius', '', '', '32', 1), ('DVMMODO', 533, 'dummodo', '', '', '32', 1), ('EXERCEO/2', 534, 'exerceo', '', '', '32', 1), ('FACILE', 535, 'facile', '', '', '32', 1), ('FELICITER', 536, 'feliciter', '', '', '32', 1), ('FORTITER', 537, 'fortiter', '', '', '32', 1), ('LIBERE', 538, 'libere', '', '', '32', 1), ('LONGE', 539, 'longe', '', '', '32', 1), ('MAGNOPERE', 540, 'magnopere', '', '', '32', 1), ('MALE', 541, 'male', '', '', '32', 1), ('MALO', 542, 'malo', '', '', '32', 1), ('MELIVS', 543, 'melius', '', '', '32', 1), ('MVLTVM/2', 544, 'multum', '', '', '32', 1), ('NOLO', 545, 'nolo', '', '', '32', 1), ('PAR/2', 546, 'pār', '', '', '32', 1), ('PARVM/2', 547, 'parum', '', '', '32', 1), ('PATEO', 548, 'pateo', '', '', '32', 1), ('PAVPER', 549, 'pauper', '', '', '32', 1), ('PAVPERTAS', 550, 'paupertas', '', '', '32', 1), ('PRAEBEO', 551, 'praebeo', '', '', '32', 1), ('PROMITTO', 552, 'promitto', '', '', '32', 1), ('PVLCHRE', 553, 'pulchre', '', '', '32', 1), ('SAPIENS/2', 554, 'sapiens', '', '', '32', 2), ('VOLO/3', 555, 'volo', '', '', '32', 1), ('CANDIDVS', 556, 'candidus', '', '', '33', 1), ('HEV', 557, 'heu', '', '', '33', 1), ('INITIVM', 558, 'initium', '', '', '33', 1), ('MERVS', 559, 'merus', '', '', '33', 1), ('OPS', 560, 'ops', '', '', '33', 1), ('PHILOSOPHA', 561, 'philosopha', '', '', '33', 1), ('PHILOSOPHVS/1', 562, 'philosophus', '', '', '33', 1), ('PLEBS', 563, 'plebs', '', '', '33', 1), ('QVIS/2', 564, 'quis', '', '', '33', 1), ('RECVSO', 565, 'recuso', '', '', '33', 1), ('SAL', 566, 'sal', '', '', '33', 1), ('SPECVLVM', 567, 'speculum', '', '', '33', 1), ('SVAVIS', 568, 'suavis', '', '', '33', 1), ('SVBITO', 569, 'subito', '', '', '33', 1), ('TRADO', 570, 'trado', '', '', '33', 1), ('VE', 571, 've', '', '', '33', 1), ('ADVERSVS/2', 572, 'adversus', '', '', '34', 1), ('ANIMA', 573, 'anima', '', '', '34', 1), ('ARBITROR', 574, 'arbitror', '', '', '34', 1), ('CONOR', 575, 'conor', '', '', '34', 1), ('CRESCO', 576, 'cresco', '', '', '34', 1), ('EGREDIOR', 577, 'egredior', '', '', '34', 1), ('FATEOR', 578, 'fateor', '', '', '34', 1), ('HORTOR', 579, 'hortor', '', '', '34', 1), ('LOQVOR', 580, 'loquor', '', '', '34', 1), ('MOLIOR', 581, 'molior', '', '', '34', 1), ('MORIOR', 582, 'morior', '', '', '34', 1), ('NASCOR', 583, 'nascor', '', '', '34', 1), ('PATIOR', 584, 'patior', '', '', '34', 1), ('PROFICISCOR', 585, 'proficiscor', '', '', '34', 1), ('REMISSIO', 586, 'remissio', '', '', '34', 1), ('RVSTICOR', 587, 'rusticor', '', '', '34', 1), ('SEDEO', 588, 'sedeo', '', '', '34', 1), ('SEQVOR', 589, 'sequor', '', '', '34', 1), ('SPECTO', 590, 'specto', '', '', '34', 1), ('TALIS', 591, 'talis', '', '', '34', 1), ('VAE', 592, 'vae', '', '', '34', 1), ('VOX', 593, 'vox', '', '', '34', 1), ('VTOR', 594, 'utor', '', '', '34', 1), ('AESTAS', 595, 'aestas', '', '', '35', 1), ('ANTEPONO', 596, 'antepono', '', '', '35', 1), ('FOVEO', 597, 'foveo', '', '', '35', 1), ('IANVA', 598, 'ianua', '', '', '35', 1), ('IGNOSCO', 599, 'ignosco', '', '', '35', 1), ('IMPERO', 600, 'impero', '', '', '35', 1), ('IRATVS', 601, 'iratus', '', '', '35', 1), ('MIROR', 602, 'miror', '', '', '35', 1), ('NOCEO', 603, 'noceo', '', '', '35', 1), ('NVBO', 604, 'nubo', '', '', '35', 1), ('PARCO', 605, 'parco', '', '', '35', 1), ('PAREO', 606, 'pareo', '', '', '35', 1), ('PECTVS', 607, 'pectus', '', '', '35', 1), ('PERSVADEO', 608, 'persuadeo', '', '', '35', 1), ('PLACEO', 609, 'placeo', '', '', '35', 1), ('PRAEMIVM', 610, 'praemium', '', '', '35', 1), ('SAPIO', 611, 'sapio', '', '', '35', 1), ('SERVIO', 612, 'servio', '', '', '35', 1), ('STVDEO', 613, 'studeo', '', '', '35', 1), ('SVBRIDEO', 614, 'subrideo', '', '', '35', 1), ('ACCEDO/1', 615, 'accedo', '', '', '36', 1), ('CARPO', 616, 'carpo', '', '', '36', 1), ('COGO', 617, 'cogo', '', '', '36', 1), ('CONTEMNO', 618, 'contemno', '', '', '36', 1), ('CONTVNDO', 619, 'contundo', '', '', '36', 1), ('COTIDIE', 620, 'cotidie', '', '', '36', 1), ('CVPIDO', 621, 'cupido', '', '', '36', 1), ('CVRO', 622, 'curo', '', '', '36', 1), ('DECERNO', 623, 'decerno', '', '', '36', 1), ('EXIGO', 624, 'exigo', '', '', '36', 1), ('FIO', 625, 'fio', '', '', '36', 1), ('FORTASSE', 626, 'fortasse', '', '', '36', 1), ('LECTOR', 627, 'lector', '', '', '36', 1), ('LECTRIX', 628, 'lectrix', '', '', '36', 1), ('OBLECTO', 629, 'oblecto', '', '', '36', 1), ('ORO', 630, 'oro', '', '', '36', 1), ('RECREO', 631, 'recreo', '', '', '36', 1), ('REQVIRO', 632, 'requiro', '', '', '36', 1), ('SERENO', 633, 'sereno', '', '', '36', 1), ('VINCVLVM', 634, 'vinculum', '', '', '36', 1), ('ABEO/1', 635, 'abeo', '', '', '37', 1), ('ABSENS', 636, 'absens', '', '', '37', 1), ('ADEO/1', 637, 'adeo', '', '', '37', 1), ('ATHENAE/N', 638, 'Athenae', '', '', '37', 1), ('DOMVS', 639, 'domus', '', '', '37', 1), ('EO/1', 640, 'eo', '', '', '37', 1), ('EXEO/1', 641, 'exeo', '', '', '37', 1), ('FORIS/2', 642, 'foris', '', '', '37', 1), ('GRATVS', 643, 'gratus', '', '', '37', 1), ('HVMVS', 644, 'humus', '', '', '37', 1), ('IDONEVS', 645, 'idoneus', '', '', '37', 1), ('IMMOTVS', 646, 'immotus', '', '', '37', 1), ('INEO/1', 647, 'ineo', '', '', '37', 1), ('INTERFICIO', 648, 'interficio', '', '', '37', 1), ('ITER', 649, 'iter', '', '', '37', 1), ('LICET/1', 650, 'licet', '', '', '37', 1), ('OBEO/1', 651, 'obeo', '', '', '37', 1), ('PEREGRINOR', 652, 'peregrinor', '', '', '37', 1), ('PEREO/1', 653, 'pereo', '', '', '37', 1), ('REDEO/1', 654, 'redeo', '', '', '37', 1), ('REQVIESCO', 655, 'requiesco', '', '', '37', 1), ('RVS', 656, 'rus', '', '', '37', 1), ('SOLEO', 657, 'soleo', '', '', '37', 1), ('SYRACVSAE/N', 658, 'Syracusae', '', '', '37', 1), ('ARBOR', 659, 'arbor', '', '', '38', 1), ('DIGNITAS', 660, 'dignitas', '', '', '38', 1), ('DOLOR', 661, 'dolor', '', '', '38', 1), ('ERGA', 662, 'erga', '', '', '38', 1), ('ETSI/2', 663, 'etsi', '', '', '38', 1), ('FIRMVS', 664, 'firmus', '', '', '38', 1), ('IMPEDIO', 665, 'impedio', '', '', '38', 1), ('INFIRMVS', 666, 'infirmus', '', '', '38', 1), ('LIBENTER', 667, 'libenter', '', '', '38', 1), ('METVO', 668, 'metuo', '', '', '38', 1), ('MIRABILIS', 669, 'mirabilis', '', '', '38', 1), ('ODIVM', 670, 'odium', '', '', '38', 1), ('OPVS/1', 671, 'opus', '', '', '38', 1), ('ORATIO', 672, 'oratio', '', '', '38', 1), ('PES', 673, 'pes', '', '', '38', 1), ('PRISTINVS', 674, 'pristinus', '', '', '38', 1), ('QVEROR', 675, 'queror', '', '', '38', 1), ('RECOGNOSCO', 676, 'recognosco', '', '', '38', 1), ('SATOR', 677, 'sator', '', '', '38', 1), ('SVBLIMIS', 678, 'sublimis', '', '', '38', 1), ('SVSPENDO', 679, 'suspendo', '', '', '38', 1), ('VENDO', 680, 'vendo', '', '', '38', 1), ('AEDIFICIVM', 681, 'aedificium', '', '', '39', 1), ('AMBVLO', 682, 'ambulo', '', '', '39', 1), ('CVPIDVS', 683, 'cupidus', '', '', '39', 1), ('EXPERIOR', 684, 'experior', '', '', '39', 1), ('INIVRIA', 685, 'iniuria', '', '', '39', 1), ('LIBERALIS', 686, 'liberalis', '', '', '39', 1), ('LIBO', 687, 'libo', '', '', '39', 1), ('MVLIER', 688, 'mulier', '', '', '39', 1), ('NECESSE', 689, 'necesse', '', '', '39', 1), ('OPORTET', 690, 'oportet', '', '', '39', 1), ('OPPVGNO', 691, 'oppugno', '', '', '39', 1), ('ORNO', 692, 'orno', '', '', '39', 1), ('PERNOCTO', 693, 'pernocto', '', '', '39', 1), ('QVASI/1', 694, 'quasi', '', '', '39', 1), ('TRANSEO/1', 695, 'transeo', '', '', '39', 1), ('TRANSITVS', 696, 'transitus', '', '', '39', 1), ('VENTVS', 697, 'ventus', '', '', '39', 1), ('VETVS', 698, 'vetus', '', '', '39', 1), ('ADIVVO', 699, 'adiuvo', '', '', '4', 1), ('BASIVM', 700, 'basium', '', '', '4', 1), ('BELLVM', 701, 'bellum', '', '', '4', 1), ('BELLVS', 702, 'bellus', '', '', '4', 1), ('BONVS', 703, 'bonus', '', '', '4', 1), ('CONSILIVM', 704, 'consilium', '', '', '4', 1), ('CVRA', 705, 'cura', '', '', '4', 1), ('DONVM', 706, 'donum', '', '', '4', 1), ('EXITIVM', 707, 'exitium', '', '', '4', 1), ('HVMANVS', 708, 'humanus', '', '', '4', 1), ('IVVO', 709, 'iuvo', '', '', '4', 1), ('MAGISTER', 710, 'magister', '', '', '4', 1), ('MAGISTRA', 711, 'magistra', '', '', '4', 1), ('MALVS/3', 712, 'malus', '', '', '4', 1), ('MORA', 713, 'mora', '', '', '4', 1), ('NIHIL', 714, 'nihil', '', '', '4', 2), ('OCVLVS', 715, 'oculus', '', '', '4', 1), ('OFFICIVM', 716, 'officium', '', '', '4', 1), ('OTIVM', 717, 'otium', '', '', '4', 1), ('PARVVS/2', 718, 'parvus', '', '', '4', 2), ('PERICVLVM', 719, 'periculum', '', '', '4', 1), ('REMEDIVM', 720, 'remedium', '', '', '4', 1), ('STVLTVS', 721, 'stultus', '', '', '4', 1), ('SVM/1', 722, 'sum', '', '', '4', 2), ('VERVS', 723, 'verus', '', '', '4', 1), ('AES', 724, 'aes', '', '', '40', 1), ('DOMINA', 725, 'domina', '', '', '40', 1), ('DOMINVS', 726, 'dominus', '', '', '40', 1), ('EXPLICO', 727, 'explico', '', '', '40', 1), ('FATIGO', 728, 'fatigo', '', '', '40', 1), ('FOR', 729, 'for', '', '', '40', 1), ('IVSTVS', 730, 'iustus', '', '', '40', 1), ('LACRIMA', 731, 'lacrima', '', '', '40', 1), ('META', 732, 'meta', '', '', '40', 1), ('MONVMENTVM', 733, 'monumentum', '', '', '40', 1), ('NASVS', 734, 'nasus', '', '', '40', 1), ('NONNE', 735, 'nonne', '', '', '40', 1), ('NVM', 736, 'num', '', '', '40', 1), ('OMNINO', 737, 'omnino', '', '', '40', 1), ('OPINOR', 738, 'opinor', '', '', '40', 1), ('POSTREMVM', 739, 'postremum', '', '', '40', 1), ('PRAETER/2', 740, 'praeter', '', '', '40', 1), ('QVIN/1', 741, 'quin', '', '', '40', 1), ('REPERIO', 742, 'reperio', '', '', '40', 1), ('SAXVM', 743, 'saxum', '', '', '40', 1), ('TOT', 744, 'tot', '', '', '40', 1), ('TOTQVOT', 745, 'tot', '', '', '40', 1), ('VEREOR', 746, 'vereor', '', '', '40', 1), ('VVLTVS', 747, 'vultus', '', '', '40', 1), ('ADOLESCENS/2', 748, 'adulescens', '', '', '5', 2), ('ANIMVS', 749, 'animus', '', '', '5', 1), ('CAELVM/1', 750, 'caelum', '', '', '5', 1), ('CENO', 751, 'ceno', '', '', '5', 1), ('CRAS/2', 752, 'cras', '', '', '5', 1), ('CVLPA', 753, 'culpa', '', '', '5', 1), ('CVLPO', 754, 'culpo', '', '', '5', 1), ('GLORIA', 755, 'gloria', '', '', '5', 1), ('HERI', 756, 'heri', '', '', '5', 1), ('IGITVR', 757, 'igitur', '', '', '5', 1), ('LIBER/2', 758, 'liber', '', '', '5', 1), ('MANEO', 759, 'maneo', '', '', '5', 1), ('NE/2', 760, 'ne', '', '', '5', 1), ('NOSTER', 761, 'noster', '', '', '5', 1), ('PROPTER/2', 762, 'propter', '', '', '5', 1), ('PVLCHER', 763, 'pulcher', '', '', '5', 1), ('QVANDO/1', 764, 'quando', '', '', '5', 1), ('REMANEO', 765, 'remaneo', '', '', '5', 1), ('SANVS', 766, 'sanus', '', '', '5', 1), ('SATIS/2', 767, 'satis', '', '', '5', 1), ('SVPERO', 768, 'supero', '', '', '5', 1), ('TV', 769, 'tu', '', '', '5', 2), ('TVM', 770, 'tum', '', '', '5', 1), ('VERBVM', 771, 'verbum', '', '', '5', 1), ('DEA', 772, 'dea', '', '', '6', 1), ('DEVS', 773, 'deus', '', '', '6', 1), ('DISCIPVLA', 774, 'discipula', '', '', '6', 1), ('DISCIPVLVS', 775, 'discipulus', '', '', '6', 1), ('GRAECVS/A', 776, 'Graecus', '', '', '6', 1), ('IBI', 777, 'ibi', '', '', '6', 1), ('INSIDIAE', 778, 'insidiae', '', '', '6', 1), ('LIBER/1', 779, 'liber', '', '', '6', 1), ('NVNC', 780, 'nunc', '', '', '6', 1), ('PERPETVVS', 781, 'perpetuus', '', '', '6', 1), ('PLENVS', 782, 'plenus', '', '', '6', 1), ('POSSVM/1', 783, 'possum', '', '', '6', 1), ('QVARE/1', 784, 'quare', '', '', '6', 1), ('QVE', 785, 'que', '', '', '6', 1), ('SALVVS', 786, 'salvus', '', '', '6', 1), ('SECVNDVS/1', 787, 'secundus', '', '', '6', 2), ('TOLERO', 788, 'tolero', '', '', '6', 1), ('TYRANNVS', 789, 'tyrannus', '', '', '6', 1), ('VBI/1', 790, 'ubi', '', '', '6', 1), ('VESTER', 791, 'vester', '', '', '6', 1), ('VITIVM', 792, 'vitium', '', '', '6', 1), ('AMOR', 793, 'amor', '', '', '7', 1), ('AVDEO', 794, 'audeo', '', '', '7', 1), ('CARMEN/1', 795, 'carmen', '', '', '7', 1), ('CIVITAS', 796, 'civitas', '', '', '7', 1), ('CORPVS', 797, 'corpus', '', '', '7', 1), ('HOMO', 798, 'homo', '', '', '7', 1), ('LABOR/1', 799, 'labor', '', '', '7', 1), ('LITTERA', 800, 'littera', '', '', '7', 1), ('MOS', 801, 'mos', '', '', '7', 1), ('NECO', 802, 'neco', '', '', '7', 1), ('NOMEN', 803, 'nomen', '', '', '7', 1), ('NOVVS', 804, 'novus', '', '', '7', 1), ('PAX', 805, 'pax', '', '', '7', 1), ('POST/2', 806, 'post', '', '', '7', 1), ('REGINA', 807, 'regina', '', '', '7', 1), ('REX', 808, 'rex', '', '', '7', 1), ('SVB', 809, 'sub', '', '', '7', 1), ('TEMPVS/1', 810, 'tempus', '', '', '7', 1), ('TERRA', 811, 'terra', '', '', '7', 1), ('VIRGO', 812, 'virgo', '', '', '7', 1), ('VIRTVS', 813, 'virtus', '', '', '7', 1), ('VXOR', 814, 'uxor', '', '', '7', 1), ('AD/2', 815, 'ad', '', '', '8', 1), ('AGO', 816, 'ago', '', '', '8', 1), ('CICERO/N', 817, 'Cicero', '', '', '8', 1), ('COPIA', 818, 'copia', '', '', '8', 1), ('DEMONSTRO', 819, 'demonstro', '', '', '8', 1), ('DISCO', 820, 'disco', '', '', '8', 1), ('DOCEO', 821, 'doceo', '', '', '8', 1), ('DVCO', 822, 'duco', '', '', '8', 1), ('DVM/2', 823, 'dum', '', '', '8', 1), ('EX', 824, 'e', '', '', '8', 1), ('FRATER', 825, 'frater', '', '', '8', 1), ('GERO', 826, 'gero', '', '', '8', 1), ('GRATIASAGERE', 827, 'gratias', '', '', '8', 1), ('LAVS', 828, 'laus', '', '', '8', 1), ('LIBERTAS', 829, 'libertas', '', '', '8', 1), ('NVMQVAM', 830, 'numquam', '', '', '8', 1), ('RATIO', 831, 'ratio', '', '', '8', 1), ('SCRIBO', 832, 'scribo', '', '', '8', 1), ('SCRIPTOR', 833, 'scriptor', '', '', '8', 1), ('SOROR', 834, 'soror', '', '', '8', 1), ('TAMEN', 835, 'tamen', '', '', '8', 1), ('TRAHO', 836, 'traho', '', '', '8', 1), ('VICTORIA', 837, 'victoria', '', '', '8', 1), ('VINCO', 838, 'vinco', '', '', '8', 1), ('ALIVS', 839, 'alius', '', '', '9', 1), ('ALTER', 840, 'alter', '', '', '9', 1), ('ENIM/2', 841, 'enim', '', '', '9', 1), ('HIC/1', 842, 'hic', '', '', '9', 1), ('ILLE', 843, 'ille', '', '', '9', 1), ('IN', 844, 'in', '', '', '9', 2), ('ISTE', 845, 'iste', '', '', '9', 1), ('LOCVS', 846, 'locus', '', '', '9', 1), ('MORBVS', 847, 'morbus', '', '', '9', 1), ('NEVTER', 848, 'neuter', '', '', '9', 1), ('NIMIS', 849, 'nimis', '', '', '9', 1), ('NONSOLVM', 850, 'non', '', '', '9', 1), ('NVLLVS', 851, 'nullus', '', '', '9', 1), ('SOLVS', 852, 'solus', '', '', '9', 1), ('STVDIVM', 853, 'studium', '', '', '9', 1), ('TOTVS', 854, 'totus', '', '', '9', 1), ('VLLVS', 855, 'ullus', '', '', '9', 1), ('VNVS', 856, 'unus', '', '', '9', 2), ('VTER/4', 857, 'uter', '', '', '9', 1)]
section_list ={'1': '28', '11': 'start', '12': '11', '19': '12', '28': '19', '10': '1', '13': '10', '14': '13', '15': '14', '16': '15', '17': '16', '18': '17', '2': '18', '20': '2', '21': '20', '22': '21', '23': '22', '24': '23', '25': '24', '26': '25', '27': '26', '29': '27', '3': '29', '30': '3', '31': '30', '32': '31', '33': '32', '34': '33', '35': '34', '36': '35', '37': '36', '38': '37', '39': '38', '4': '39', '40': '4', '5': '40', '6': '5', '7': '6', '8': '7', '9': '8', 'end': '9', 'start': 'start'}
title = "Wheelock’s Latin (LaFleur)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)