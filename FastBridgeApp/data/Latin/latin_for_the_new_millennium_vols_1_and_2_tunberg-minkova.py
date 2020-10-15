import text
nan=""
section_words = {'start': -1, '1.1': 17, '1.2': 38, '1.3': 55, '1.4': 76, '1.5': 95, '1.6': 114, '1.7': 133, '1.8': 151, '1.9': 170, '1.10': 190, '1.11': 209, '1.12': 233, '1.13': 257, '1.14': 277, '1.15': 299, '1.16': 320, '1.17': 341, '1.18': 364, '1.19': 385, '1.20': 405, '1.21': 428, '2.1': 451, '2.2': 474, '2.3': 495, '2.4': 521, '2.5': 542, '2.6': 564, '2.7': 587, '2.8': 611, '2.9': 633, '2.10': 653, '2.11': 674, '2.12': 695, '2.13': 718, '2.14': 740, '2.15': 760, 'end': -2}
the_text =  [('AGRICOLA', 0, 'agricola', '', '', '1_1', 1), ('AMBVLO', 1, 'ambulo', '', '', '1_1', 2), ('AMO', 2, 'amo', '', '', '1_1', 2), ('AQVA', 3, 'aqua', '', '', '1_1', 1), ('ATHLETA', 4, 'athleta', '', '', '1_1', 1), ('BENE', 5, 'bene', '', '', '1_1', 1), ('CVRO', 6, 'curo', '', '', '1_1', 2), ('ET/2', 7, 'et', '', '', '1_1', 1), ('FILIA', 8, 'filia', '', '', '1_1', 1), ('ITAQVE', 9, 'itaque', '', '', '1_1', 1), ('LVPA', 10, 'lupa', '', '', '1_1', 1), ('NAVTA', 11, 'nauta', '', '', '1_1', 1), ('POETA', 12, 'poeta', '', '', '1_1', 1), ('POSTEA', 13, 'postea', '', '', '1_1', 1), ('PVELLA', 14, 'puella', '', '', '1_1', 1), ('ROMA/N', 15, 'Roma', '', '', '1_1', 1), ('SVM/1', 16, 'sum', '', '', '1_1', 3), ('TERRA', 17, 'terra', '', '', '1_1', 1), ('AMBVLO', 18, 'ambulo', '', '', '1_2', 2), ('AMO', 19, 'amo', '', '', '1_2', 2), ('CVRO', 20, 'curo', '', '', '1_2', 2), ('DEBEO', 21, 'debeo', '', '', '1_2', 1), ('DIV', 22, 'diu', '', '', '1_2', 1), ('EGO', 23, 'ego', '', '', '1_2', 3), ('EXSPECTO', 24, 'exspecto', '', '', '1_2', 1), ('FABVLA/1', 25, 'fabula', '', '', '1_2', 1), ('FORMA', 26, 'forma', '', '', '1_2', 1), ('HABEO', 27, 'habeo', '', '', '1_2', 1), ('HABITO', 28, 'habito', '', '', '1_2', 1), ('NARRO', 29, 'narro', '', '', '1_2', 1), ('NON', 30, 'non', '', '', '1_2', 1), ('NVNC', 31, 'nunc', '', '', '1_2', 1), ('PARO/2', 32, 'paro', '', '', '1_2', 2), ('PATRIA', 33, 'patria', '', '', '1_2', 1), ('SVM/1', 34, 'sum', '', '', '1_2', 3), ('TENEO', 35, 'teneo', '', '', '1_2', 1), ('TV', 36, 'tu', '', '', '1_2', 3), ('VIDEO', 37, 'video', '', '', '1_2', 1), ('VOCO', 38, 'voco', '', '', '1_2', 1), ('AGER', 39, 'ager', '', '', '1_3', 1), ('AMICVS/1', 40, 'amicus', '', '', '1_3', 1), ('ANIMVS', 41, 'animus', '', '', '1_3', 1), ('CASA', 42, 'casa', '', '', '1_3', 1), ('CVM/2', 43, 'cum', '', '', '1_3', 1), ('DEINDE', 44, 'deinde', '', '', '1_3', 1), ('DOMVS', 45, 'domus', '', '', '1_3', 2), ('EGO', 46, 'ego', '', '', '1_3', 3), ('FILIVS', 47, 'filius', '', '', '1_3', 1), ('IN', 48, 'in', '', '', '1_3', 2), ('PVER', 49, 'puer', '', '', '1_3', 1), ('RIVVS', 50, 'rivus', '', '', '1_3', 1), ('TIMEO', 51, 'timeo', '', '', '1_3', 1), ('TV', 52, 'tu', '', '', '1_3', 3), ('VALDE', 53, 'valde', '', '', '1_3', 1), ('VIA', 54, 'via', '', '', '1_3', 1), ('VIR', 55, 'vir', '', '', '1_3', 1), ('AD/2', 56, 'ad', '', '', '1_4', 1), ('ARMATVS/2', 57, 'armatus', '', '', '1_4', 1), ('AVTEM', 58, 'autem', '', '', '1_4', 1), ('BELLVM', 59, 'bellum', '', '', '1_4', 1), ('BONVS', 60, 'bonus', '', '', '1_4', 1), ('CASTRA/2', 61, 'castra', '', '', '1_4', 1), ('DO', 62, 'do', '', '', '1_4', 1), ('DOLVS', 63, 'dolus', '', '', '1_4', 1), ('EX', 64, 'e', '', '', '1_4', 1), ('IN', 65, 'in', '', '', '1_4', 2), ('INTRO/2', 66, 'intro', '', '', '1_4', 1), ('IVBEO', 67, 'iubeo', '', '', '1_4', 1), ('IVSTVS', 68, 'iustus', '', '', '1_4', 1), ('MAGNVS', 69, 'magnus', '', '', '1_4', 1), ('MALVS/3', 70, 'malus', '', '', '1_4', 1), ('PRAECLARVS', 71, 'praeclarus', '', '', '1_4', 1), ('PRAEMIVM', 72, 'praemium', '', '', '1_4', 1), ('ROMANVS/A', 73, 'Romanus', '', '', '1_4', 1), ('SED', 74, 'sed', '', '', '1_4', 1), ('VENENVM', 75, 'venenum', '', '', '1_4', 1), ('VINCVLVM', 76, 'vinculum', '', '', '1_4', 1), ('AB', 77, 'a', '', '', '1_5', 1), ('AVXILIVM', 78, 'auxilium', '', '', '1_5', 1), ('COGITO', 79, 'cogito', '', '', '1_5', 1), ('CONSILIVM', 80, 'consilium', '', '', '1_5', 2), ('DE', 81, 'de', '', '', '1_5', 1), ('DOLEO', 82, 'doleo', '', '', '1_5', 1), ('EPISTOLA', 83, 'epistula', '', '', '1_5', 1), ('FAMILIA', 84, 'familia', '', '', '1_5', 1), ('GAVDIVM', 85, 'gaudium', '', '', '1_5', 1), ('LACRIMA', 86, 'lacrima', '', '', '1_5', 1), ('LONGE', 87, 'longe', '', '', '1_5', 1), ('LONGVS', 88, 'longus', '', '', '1_5', 1), ('MISER', 89, 'miser', '', '', '1_5', 1), ('NAM', 90, 'nam', '', '', '1_5', 1), ('NONSOLVM', 91, 'non', '', '', '1_5', 1), ('PARO/2', 92, 'paro', '', '', '1_5', 2), ('PVLCHER', 93, 'pulcher', '', '', '1_5', 1), ('SEMPER', 94, 'semper', '', '', '1_5', 1), ('TAMEN', 95, 'tamen', '', '', '1_5', 2), ('DOCEO', 96, 'doceo', '', '', '1_6', 1), ('DVM/2', 97, 'dum', '', '', '1_6', 1), ('EXEMPLVM', 98, 'exemplum', '', '', '1_6', 1), ('FIRMO', 99, 'firmo', '', '', '1_6', 1), ('IACEO', 100, 'iaceo', '', '', '1_6', 1), ('IVDICO', 101, 'iudico', '', '', '1_6', 1), ('LIBER/1', 102, 'liber', '', '', '1_6', 1), ('LITTERA', 103, 'littera', '', '', '1_6', 1), ('MANEO', 104, 'maneo', '', '', '1_6', 1), ('MEMORIA', 105, 'memoria', '', '', '1_6', 1), ('MVLTVS', 106, 'multus', '', '', '1_6', 1), ('POSSVM/1', 107, 'possum', '', '', '1_6', 1), ('PROPTER/2', 108, 'propter', '', '', '1_6', 1), ('SAEPE', 109, 'saepe', '', '', '1_6', 1), ('SERVO', 110, 'servo', '', '', '1_6', 1), ('SOLEO', 111, 'soleo', '', '', '1_6', 1), ('SVM/1', 112, 'sum', '', '', '1_6', 3), ('TENEBRAE', 113, 'tenebrae', '', '', '1_6', 1), ('VITA', 114, 'vita', '', '', '1_6', 1), ('AESTIMO', 115, 'aestimo', '', '', '1_7', 1), ('AESTIMOVNIVSASSIS', 116, 'aestimo', '', '', '1_7', 1), ('AMOR', 117, 'amor', '', '', '1_7', 1), ('DELICIA/1', 118, 'delicia', '', '', '1_7', 1), ('DIGITVS', 119, 'digitus', '', '', '1_7', 1), ('DOMINA', 120, 'domina', '', '', '1_7', 1), ('GREMIVM', 121, 'gremium', '', '', '1_7', 1), ('INVIDEO', 122, 'invideo', '', '', '1_7', 1), ('MEVS', 123, 'meus', '', '', '1_7', 1), ('OCVLVS', 124, 'oculus', '', '', '1_7', 1), ('PASSER', 125, 'passer', '', '', '1_7', 1), ('PAX', 126, 'pax', '', '', '1_7', 1), ('PVTO', 127, 'puto', '', '', '1_7', 1), ('SENEX/1', 128, 'senex', '', '', '1_7', 1), ('SESESE', 129, 'se', '', '', '1_7', 1), ('SEVERVS', 130, 'severus', '', '', '1_7', 1), ('SOROR', 131, 'soror', '', '', '1_7', 1), ('SVI/1', 132, 'sui', '', '', '1_7', 1), ('VERBVM', 133, 'verbum', '', '', '1_7', 1), ('CONTRA/2', 134, 'contra', '', '', '1_8', 1), ('DECERNO', 135, 'decerno', '', '', '1_8', 1), ('DICO/2', 136, 'dico', '', '', '1_8', 1), ('DVX', 137, 'dux', '', '', '1_8', 1), ('FORTITVDO', 138, 'fortitudo', '', '', '1_8', 1), ('HOMO', 139, 'homo', '', '', '1_8', 1), ('INTELLIGO', 140, 'intellego', '', '', '1_8', 1), ('LIBERO', 141, 'libero', '', '', '1_8', 1), ('MILES', 142, 'miles', '', '', '1_8', 1), ('NAVIGO', 143, 'navigo', '', '', '1_8', 1), ('ORACVLVM', 144, 'oraculum', '', '', '1_8', 1), ('PETO', 145, 'peto', '', '', '1_8', 1), ('REX', 146, 'rex', '', '', '1_8', 1), ('TANDEM', 147, 'tandem', '', '', '1_8', 1), ('TEMPLVM', 148, 'templum', '', '', '1_8', 1), ('TIMOR', 149, 'timor', '', '', '1_8', 1), ('TVM', 150, 'tum', '', '', '1_8', 2), ('VINCO', 151, 'vinco', '', '', '1_8', 1), ('ANIMAL', 152, 'animal', '', '', '1_9', 1), ('ARMA', 153, 'arma', '', '', '1_9', 1), ('AVDIO', 154, 'audio', '', '', '1_9', 1), ('CAPVT', 155, 'caput', '', '', '1_9', 1), ('CIVIS', 156, 'civis', '', '', '1_9', 1), ('CONSVL', 157, 'consul', '', '', '1_9', 1), ('CORPVS', 158, 'corpus', '', '', '1_9', 1), ('CREDO', 159, 'credo', '', '', '1_9', 1), ('EXEMPLAR', 160, 'exemplar', '', '', '1_9', 1), ('GERO', 161, 'gero', '', '', '1_9', 2), ('MARE', 162, 'mare', '', '', '1_9', 1), ('MORS', 163, 'mors', '', '', '1_9', 1), ('MVLIER', 164, 'mulier', '', '', '1_9', 1), ('ORATIO', 165, 'oratio', '', '', '1_9', 1), ('SCIO', 166, 'scio', '', '', '1_9', 1), ('SENTIO', 167, 'sentio', '', '', '1_9', 1), ('TEMPVS/1', 168, 'tempus', '', '', '1_9', 1), ('VENIO', 169, 'venio', '', '', '1_9', 1), ('VRBS', 170, 'urbs', '', '', '1_9', 1), ('ACER/2', 171, 'acer', '', '', '1_10', 1), ('AEDIFICO', 172, 'aedifico', '', '', '1_10', 1), ('CAPIO/2', 173, 'capio', '', '', '1_10', 1), ('CELEBER', 174, 'celeber', '', '', '1_10', 1), ('CVPIO', 175, 'cupio', '', '', '1_10', 1), ('DELEO', 176, 'deleo', '', '', '1_10', 1), ('DEVS', 177, 'deus', '', '', '1_10', 1), ('DONVM', 178, 'donum', '', '', '1_10', 1), ('EQVVS', 179, 'equus', '', '', '1_10', 1), ('FELIX', 180, 'felix', '', '', '1_10', 1), ('FLAMMA', 181, 'flamma', '', '', '1_10', 1), ('FORTIS', 182, 'fortis', '', '', '1_10', 1), ('FVGIO', 183, 'fugio', '', '', '1_10', 1), ('HOSTIS', 184, 'hostis', '', '', '1_10', 1), ('MOVEO', 185, 'moveo', '', '', '1_10', 1), ('NEC/2', 186, 'nec', '', '', '1_10', 2), ('NOX', 187, 'nox', '', '', '1_10', 1), ('PAVCI', 188, 'paucus', '', '', '1_10', 1), ('PERICVLVM', 189, 'periculum', '', '', '1_10', 1), ('PVGNO', 190, 'pugno', '', '', '1_10', 1), ('AGO', 191, 'ago', '', '', '1_11', 1), ('ARDEO', 192, 'ardeo', '', '', '1_11', 1), ('CONSPICIO', 193, 'conspicio', '', '', '1_11', 1), ('CRVDELIS', 194, 'crudelis', '', '', '1_11', 1), ('DOLOR', 195, 'dolor', '', '', '1_11', 1), ('ITA', 196, 'ita', '', '', '1_11', 2), ('MINIME', 197, 'minime', '', '', '1_11', 1), ('MITTO', 198, 'mitto', '', '', '1_11', 1), ('NE/2', 199, 'ne', '', '', '1_11', 1), ('NOVVS', 200, 'novus', '', '', '1_11', 1), ('PARVM/2', 201, 'parum', '', '', '1_11', 2), ('QVE', 202, 'que', '', '', '1_11', 1), ('QVOQVE', 203, 'quoque', '', '', '1_11', 1), ('REGINA', 204, 'regina', '', '', '1_11', 1), ('RELINQVO', 205, 'relinquo', '', '', '1_11', 1), ('SILVA', 206, 'silva', '', '', '1_11', 1), ('SPELVNCA', 207, 'spelunca', '', '', '1_11', 1), ('TEMPESTAS', 208, 'tempestas', '', '', '1_11', 1), ('VNA', 209, 'una', '', '', '1_11', 1), ('BELLVMGERO', 210, 'bellum', '', '', '1_12', 1), ('CONSVMO', 211, 'consumo', '', '', '1_12', 1), ('DEXTERA', 212, 'dextera', '', '', '1_12', 1), ('FACIO', 213, 'facio', '', '', '1_12', 1), ('IBI', 214, 'ibi', '', '', '1_12', 1), ('IGNIS', 215, 'ignis', '', '', '1_12', 1), ('INQVIO', 216, 'inquam', '', '', '1_12', 3), ('IRA', 217, 'ira', '', '', '1_12', 1), ('IS', 218, 'is', '', '', '1_12', 1), ('NOMEN', 219, 'nomen', '', '', '1_12', 1), ('NOS', 220, 'nos', '', '', '1_12', 1), ('NOSTER', 221, 'noster', '', '', '1_12', 1), ('OCCIDO/2', 222, 'occido', '', '', '1_12', 1), ('OSTENDO', 223, 'ostendo', '', '', '1_12', 1), ('PONO', 224, 'pono', '', '', '1_12', 1), ('PROPE/2', 225, 'prope', '', '', '1_12', 2), ('PROVIRIBVS', 226, 'pro', '', '', '1_12', 1), ('SIMILIS', 227, 'similis', '', '', '1_12', 1), ('STATIM', 228, 'statim', '', '', '1_12', 1), ('TANTVS', 229, 'tantus', '', '', '1_12', 1), ('TVVS', 230, 'tuus', '', '', '1_12', 1), ('VESTER', 231, 'vester', '', '', '1_12', 1), ('VIS', 232, 'vis', '', '', '1_12', 1), ('VOS', 233, 'vos', '', '', '1_12', 1), ('ALIVS', 234, 'alius', '', '', '1_13', 1), ('APVD', 235, 'apud', '', '', '1_13', 1), ('ATQVE/1', 236, 'atque', '', '', '1_13', 2), ('DISCEDO/1', 237, 'discedo', '', '', '1_13', 1), ('DIVES', 238, 'dives', '', '', '1_13', 1), ('DOCTVS', 239, 'doctus', '', '', '1_13', 1), ('DVCO', 240, 'duco', '', '', '1_13', 2), ('EGO', 241, 'ego', '', '', '1_13', 3), ('ENIM/2', 242, 'enim', '', '', '1_13', 1), ('IVDEX', 243, 'iudex', '', '', '1_13', 1), ('LICET/1', 244, 'licet', '', '', '1_13', 1), ('NIHIL', 245, 'nihil', '', '', '1_13', 1), ('NOLO', 246, 'nolo', '', '', '1_13', 2), ('OMNIS', 247, 'omnis', '', '', '1_13', 1), ('PRO/1', 248, 'pro', '', '', '1_13', 1), ('QVID', 249, 'quid', '', '', '1_13', 1), ('RESPONDEO', 250, 'respondeo', '', '', '1_13', 1), ('ROGO', 251, 'rogo', '', '', '1_13', 1), ('SVVS', 252, 'suus', '', '', '1_13', 2), ('TANTVM/2', 253, 'tantum', '', '', '1_13', 1), ('TV', 254, 'tu', '', '', '1_13', 3), ('TVM', 255, 'tum', '', '', '1_13', 2), ('VALE', 256, 'vale', '', '', '1_13', 1), ('VALEO', 257, 'valeo', '', '', '1_13', 3), ('ALBVS', 258, 'albus', '', '', '1_14', 1), ('ARBOR', 259, 'arbor', '', '', '1_14', 1), ('CADO', 260, 'cado', '', '', '1_14', 1), ('COMEDO/2', 261, 'comedo', '', '', '1_14', 1), ('CONVENIO', 262, 'convenio', '', '', '1_14', 1), ('FLVO', 263, 'fluo', '', '', '1_14', 1), ('GLADIVS', 264, 'gladius', '', '', '1_14', 1), ('IAM', 265, 'iam', '', '', '1_14', 1), ('MOX', 266, 'mox', '', '', '1_14', 1), ('ODIVM', 267, 'odium', '', '', '1_14', 2), ('OS/1', 268, 'os', '', '', '1_14', 1), ('PARENS/1', 269, 'parens', '', '', '1_14', 1), ('PECTVS', 270, 'pectus', '', '', '1_14', 1), ('PER', 271, 'per', '', '', '1_14', 1), ('PRIMVS', 272, 'primus', '', '', '1_14', 1), ('QVI/1', 273, 'qui', '', '', '1_14', 2), ('RVBER', 274, 'ruber', '', '', '1_14', 1), ('SANGVIS', 275, 'sanguis', '', '', '1_14', 1), ('SEPARO/2', 276, 'separo', '', '', '1_14', 1), ('TANGO', 277, 'tango', '', '', '1_14', 1), ('ANTE/2', 278, 'ante', '', '', '1_15', 1), ('ARGVMENTVM', 279, 'argumentum', '', '', '1_15', 1), ('CVR/1', 280, 'cur', '', '', '1_15', 1), ('DIFFICILIS', 281, 'difficilis', '', '', '1_15', 1), ('ECCE', 282, 'ecce', '', '', '1_15', 1), ('ETIAM', 283, 'etiam', '', '', '1_15', 1), ('FORSITAN', 284, 'forsan', '', '', '1_15', 1), ('INQVIO', 285, 'inquam', '', '', '1_15', 3), ('NEGLIGO', 286, 'neglego', '', '', '1_15', 1), ('PARVVS/2', 287, 'parvus', '', '', '1_15', 1), ('QVI/1', 288, 'qui', '', '', '1_15', 2), ('QVIS/1', 289, 'quis', '', '', '1_15', 1), ('RVSTICVS/2', 290, 'rusticus', '', '', '1_15', 1), ('SAXVM', 291, 'saxum', '', '', '1_15', 1), ('SENECTVS/1', 292, 'senectus', '', '', '1_15', 1), ('SICVT/1', 293, 'sicut', '', '', '1_15', 1), ('STO', 294, 'sto', '', '', '1_15', 1), ('VBIQVE', 295, 'ubique', '', '', '1_15', 1), ('VERVS', 296, 'verus', '', '', '1_15', 1), ('VETVSTVS', 297, 'vetustus', '', '', '1_15', 1), ('VILLA', 298, 'villa', '', '', '1_15', 1), ('VMQVAM', 299, 'umquam', '', '', '1_15', 1), ('AVVNCVLVS', 300, 'avunculus', '', '', '1_16', 1), ('CAELVM/1', 301, 'caelum', '', '', '1_16', 1), ('CAVSA', 302, 'causa', '', '', '1_16', 1), ('CINIS', 303, 'cinis', '', '', '1_16', 1), ('CLADES', 304, 'clades', '', '', '1_16', 1), ('CLASSIS', 305, 'classis', '', '', '1_16', 1), ('FEMINA', 306, 'femina', '', '', '1_16', 1), ('FVMVS', 307, 'fumus', '', '', '1_16', 1), ('FVNESTVS', 308, 'funestus', '', '', '1_16', 1), ('IGITVR', 309, 'igitur', '', '', '1_16', 1), ('INCENDIVM', 310, 'incendium', '', '', '1_16', 1), ('LEGO/2', 311, 'lego', '', '', '1_16', 1), ('LITVS/2', 312, 'litus', '', '', '1_16', 1), ('MATER', 313, 'mater', '', '', '1_16', 1), ('MONS', 314, 'mons', '', '', '1_16', 1), ('NAVIS', 315, 'navis', '', '', '1_16', 1), ('NVBES', 316, 'nubes', '', '', '1_16', 1), ('NVMQVAM', 317, 'numquam', '', '', '1_16', 1), ('OPPRIMO', 318, 'opprimo', '', '', '1_16', 1), ('PARS', 319, 'pars', '', '', '1_16', 1), ('STVDEO', 320, 'studeo', '', '', '1_16', 1), ('ALO', 321, 'alo', '', '', '1_17', 1), ('AMITTO', 322, 'amitto', '', '', '1_17', 1), ('CORNV', 323, 'cornu', '', '', '1_17', 1), ('CORRIPIO', 324, 'corripio', '', '', '1_17', 1), ('CVRRO', 325, 'curro', '', '', '1_17', 1), ('DEVASTO', 326, 'devasto', '', '', '1_17', 1), ('DOMVS', 327, 'domus', '', '', '1_17', 2), ('EXSTINGVO', 328, 'exstinguo', '', '', '1_17', 1), ('FACILE', 329, 'facile', '', '', '1_17', 1), ('IACIO', 330, 'iacio', '', '', '1_17', 1), ('IMPERATOR', 331, 'imperator', '', '', '1_17', 1), ('IMPETVS', 332, 'impetus', '', '', '1_17', 1), ('INITIVM', 333, 'initium', '', '', '1_17', 1), ('IVSSVS', 334, 'iussus', '', '', '1_17', 1), ('LOCVS', 335, 'locus', '', '', '1_17', 1), ('MANVS/1', 336, 'manus', '', '', '1_17', 1), ('MVRVS', 337, 'murus', '', '', '1_17', 1), ('SINE', 338, 'sine', '', '', '1_17', 1), ('TEMPTO', 339, 'tempto', '', '', '1_17', 1), ('TVMVLTVS', 340, 'tumultus', '', '', '1_17', 1), ('VENTVS', 341, 'ventus', '', '', '1_17', 1), ('COLO/2', 342, 'colo', '', '', '1_18', 1), ('CVM/3', 343, 'cum', '', '', '1_18', 2), ('DEA', 344, 'dea', '', '', '1_18', 1), ('DIES', 345, 'dies', '', '', '1_18', 1), ('DORMIO', 346, 'dormio', '', '', '1_18', 1), ('DVCO', 347, 'duco', '', '', '1_18', 2), ('EXCITO/1', 348, 'excito', '', '', '1_18', 1), ('EXCLAMO', 349, 'exclamo', '', '', '1_18', 1), ('FACIES', 350, 'facies', '', '', '1_18', 1), ('FATVM', 351, 'fatum', '', '', '1_18', 1), ('ITA', 352, 'ita', '', '', '1_18', 2), ('MARITVS/1', 353, 'maritus', '', '', '1_18', 1), ('MERIDIES', 354, 'meridies', '', '', '1_18', 2), ('MVLTVM/2', 355, 'multum', '', '', '1_18', 1), ('OCCVLTO', 356, 'occulto', '', '', '1_18', 1), ('PATER', 357, 'pater', '', '', '1_18', 2), ('POST/2', 358, 'post', '', '', '1_18', 1), ('QVAERO', 359, 'quaero', '', '', '1_18', 1), ('RES', 360, 'res', '', '', '1_18', 1), ('SI/2', 361, 'si', '', '', '1_18', 1), ('SOMNVS', 362, 'somnus', '', '', '1_18', 1), ('TAM', 363, 'tam', '', '', '1_18', 1), ('VXOR', 364, 'uxor', '', '', '1_18', 2), ('BARBA', 365, 'barba', '', '', '1_19', 1), ('CARO/1', 366, 'caro', '', '', '1_19', 1), ('CELERITER', 367, 'celeriter', '', '', '1_19', 1), ('COQVO', 368, 'coquo', '', '', '1_19', 1), ('CRESCO', 369, 'cresco', '', '', '1_19', 1), ('FEROX', 370, 'ferox', '', '', '1_19', 1), ('FORIS/2', 371, 'foris', '', '', '1_19', 1), ('HERBA', 372, 'herba', '', '', '1_19', 1), ('HIC/1', 373, 'hic', '', '', '1_19', 1), ('INTER', 374, 'inter', '', '', '1_19', 1), ('PELLIS', 375, 'pellis', '', '', '1_19', 1), ('POSTQVAM', 376, 'postquam', '', '', '1_19', 1), ('PROELIVM', 377, 'proelium', '', '', '1_19', 1), ('SANO', 378, 'sano', '', '', '1_19', 1), ('SEDEO', 379, 'sedeo', '', '', '1_19', 1), ('TERO', 380, 'tero', '', '', '1_19', 1), ('TERRIBILIS', 381, 'terribilis', '', '', '1_19', 1), ('VESTIMENTVM', 382, 'vestimentum', '', '', '1_19', 1), ('VIVO', 383, 'vivo', '', '', '1_19', 1), ('VVLNERO', 384, 'vulnero', '', '', '1_19', 1), ('VVLNVS', 385, 'vulnus', '', '', '1_19', 1), ('ABVNDO', 386, 'abundo', '', '', '1_20', 1), ('ADOLESCENS/2', 387, 'adulescens', '', '', '1_20', 1), ('AEQVVS', 388, 'aequus', '', '', '1_20', 1), ('COR', 389, 'cor', '', '', '1_20', 1), ('DELECTO', 390, 'delecto', '', '', '1_20', 1), ('DIVINVS/2', 391, 'divinus', '', '', '1_20', 1), ('EGEO', 392, 'egeo', '', '', '1_20', 1), ('FVR', 393, 'fur', '', '', '1_20', 1), ('FVRTVM', 394, 'furtum', '', '', '1_20', 1), ('HVMANVS', 395, 'humanus', '', '', '1_20', 1), ('ILLE', 396, 'ille', '', '', '1_20', 1), ('INIQVITAS', 397, 'iniquitas', '', '', '1_20', 1), ('LEX', 398, 'lex', '', '', '1_20', 1), ('LVDO', 399, 'ludo', '', '', '1_20', 1), ('NOCTV', 400, 'noctu', '', '', '1_20', 1), ('PAENE', 401, 'paene', '', '', '1_20', 1), ('PAVPER', 402, 'pauper', '', '', '1_20', 1), ('PLENVS', 403, 'plenus', '', '', '1_20', 1), ('POMVM', 404, 'pomum', '', '', '1_20', 1), ('PVNIO', 405, 'punio', '', '', '1_20', 1), ('ACCIPIO', 406, 'accipio', '', '', '1_21', 1), ('ACCVSO', 407, 'accuso', '', '', '1_21', 1), ('ALIENVS/2', 408, 'alienus', '', '', '1_21', 1), ('AXIS', 409, 'axis', '', '', '1_21', 1), ('CIRCVM/2', 410, 'circum', '', '', '1_21', 1), ('CONSTANTIA', 411, 'constantia', '', '', '1_21', 1), ('DESCENDO', 412, 'descendo', '', '', '1_21', 1), ('DIVITIAE', 413, 'divitia', '', '', '1_21', 1), ('ERIPIO', 414, 'eripio', '', '', '1_21', 1), ('ERRO/2', 415, 'erro', '', '', '1_21', 1), ('EXTERNVS', 416, 'externus', '', '', '1_21', 1), ('FORTVNA', 417, 'fortuna', '', '', '1_21', 1), ('FVTVRVS', 418, 'futurus', '', '', '1_21', 1), ('HONOR', 419, 'honor', '', '', '1_21', 1), ('MVTO/2', 420, 'muto', '', '', '1_21', 1), ('POSSIDEO', 421, 'possideo', '', '', '1_21', 1), ('PROCERTO', 422, 'pro', '', '', '1_21', 1), ('RECIPIO', 423, 'recipio', '', '', '1_21', 2), ('REPREHENDO', 424, 'reprehendo', '', '', '1_21', 1), ('ROTA', 425, 'rota', '', '', '1_21', 1), ('TOLLO', 426, 'tollo', '', '', '1_21', 1), ('VERSO', 427, 'verso', '', '', '1_21', 1), ('VLLVS', 428, 'ullus', '', '', '1_21', 1), ('ASPICIO', 429, 'aspicio', '', '', '2_1', 1), ('CONSILIVM', 430, 'consilium', '', '', '2_1', 2), ('ETET', 431, 'et', '', '', '2_1', 1), ('GENS', 432, 'gens', '', '', '2_1', 1), ('GIGNO', 433, 'gigno', '', '', '2_1', 1), ('HODIE', 434, 'hodie', '', '', '2_1', 1), ('INCOLA', 435, 'incola', '', '', '2_1', 1), ('INSVLA', 436, 'insula', '', '', '2_1', 2), ('INVENIO', 437, 'invenio', '', '', '2_1', 1), ('MERIDIES', 438, 'meridies', '', '', '2_1', 2), ('MOS', 439, 'mos', '', '', '2_1', 1), ('MVNDVS/1', 440, 'mundus', '', '', '2_1', 1), ('NE/4', 441, 'ne', '', '', '2_1', 3), ('OCCVPO/2', 442, 'occupo', '', '', '2_1', 1), ('ORTVS', 443, 'ortus', '', '', '2_1', 1), ('PISCIS', 444, 'piscis', '', '', '2_1', 1), ('PROCVL', 445, 'procul', '', '', '2_1', 1), ('PROMITTO', 446, 'promitto', '', '', '2_1', 1), ('PROPE/2', 447, 'prope', '', '', '2_1', 2), ('SEPTENTRIONALIS', 448, 'septentrionalis', '', '', '2_1', 1), ('SITVS/2', 449, 'situs', '', '', '2_1', 1), ('SOL', 450, 'sol', '', '', '2_1', 1), ('VTINAM', 451, 'utinam', '', '', '2_1', 2), ('ALTVS', 452, 'altus', '', '', '2_2', 1), ('ANNVS', 453, 'annus', '', '', '2_2', 1), ('ARGENTVM', 454, 'argentum', '', '', '2_2', 1), ('AVRVM', 455, 'aurum', '', '', '2_2', 1), ('BREVIS', 456, 'brevis', '', '', '2_2', 1), ('CLARVS', 457, 'clarus', '', '', '2_2', 1), ('CVSTOS', 458, 'custos', '', '', '2_2', 1), ('EQVES', 459, 'eques', '', '', '2_2', 1), ('FINIS', 460, 'finis', '', '', '2_2', 1), ('GERO', 461, 'gero', '', '', '2_2', 2), ('GRAVIS', 462, 'gravis', '', '', '2_2', 1), ('INTERDVM', 463, 'interdum', '', '', '2_2', 1), ('LIS', 464, 'lis', '', '', '2_2', 1), ('MANE/2', 465, 'mane', '', '', '2_2', 1), ('ODIOHABEO', 466, 'odio', '', '', '2_2', 1), ('ODIVM', 467, 'odium', '', '', '2_2', 2), ('SINO', 468, 'sino', '', '', '2_2', 1), ('VALEO', 469, 'valeo', '', '', '2_2', 3), ('VEL/1', 470, 'vel', '', '', '2_2', 1), ('VESTIS', 471, 'vestis', '', '', '2_2', 1), ('VOX', 472, 'vox', '', '', '2_2', 1), ('VT/4', 473, 'ut', '', '', '2_2', 4), ('VVLTVS', 474, 'vultus', '', '', '2_2', 1), ('AT/2', 475, 'at', '', '', '2_3', 1), ('CONIVX', 476, 'coniunx', '', '', '2_3', 1), ('DISCIPVLA', 477, 'discipula', '', '', '2_3', 1), ('DISCO', 478, 'disco', '', '', '2_3', 1), ('DOMINVS', 479, 'dominus', '', '', '2_3', 1), ('FAMA', 480, 'fama', '', '', '2_3', 1), ('FRATER', 481, 'frater', '', '', '2_3', 1), ('IMPROBVS', 482, 'improbus', '', '', '2_3', 1), ('IVNGO', 483, 'iungo', '', '', '2_3', 1), ('MAGISTER', 484, 'magister', '', '', '2_3', 1), ('MATRIMONIVM', 485, 'matrimonium', '', '', '2_3', 1), ('NE/4', 486, 'ne', '', '', '2_3', 3), ('NVSQVAM', 487, 'nusquam', '', '', '2_3', 1), ('PARIO/2', 488, 'pario', '', '', '2_3', 1), ('PERDO', 489, 'perdo', '', '', '2_3', 1), ('SALVS', 490, 'salus', '', '', '2_3', 1), ('SALVTEMDICERE', 491, 'salutem', '', '', '2_3', 1), ('SCRIBO', 492, 'scribo', '', '', '2_3', 1), ('VT/4', 493, 'ut', '', '', '2_3', 4), ('VXOR', 494, 'uxor', '', '', '2_3', 2), ('VXOREMDEDVCERE', 495, 'uxorem', '', '', '2_3', 1), ('AGMEN', 496, 'agmen', '', '', '2_4', 1), ('APERIO', 497, 'aperio', '', '', '2_4', 1), ('COEPIO', 498, 'coepi', '', '', '2_4', 1), ('DEFENDO', 499, 'defendo', '', '', '2_4', 1), ('EDO/1', 500, 'edo', '', '', '2_4', 1), ('EXTRA/2', 501, 'extra', '', '', '2_4', 1), ('FVRO', 502, 'furo', '', '', '2_4', 1), ('INGENS', 503, 'ingens', '', '', '2_4', 1), ('INVADO/2', 504, 'invado', '', '', '2_4', 1), ('LIGNEVS', 505, 'ligneus', '', '', '2_4', 1), ('NEC/2', 506, 'nec', '', '', '2_4', 2), ('NEQVENEC', 507, 'neque', '', '', '2_4', 1), ('PARCO', 508, 'parco', '', '', '2_4', 1), ('PONS', 509, 'pons', '', '', '2_4', 1), ('PORTA', 510, 'porta', '', '', '2_4', 1), ('PRIMO', 511, 'primo', '', '', '2_4', 1), ('QVAM/1', 512, 'quam', '', '', '2_4', 2), ('QVANTVS/1', 513, 'quantus', '', '', '2_4', 1), ('RECIPIO', 514, 'recipio', '', '', '2_4', 2), ('RESISTO', 515, 'resisto', '', '', '2_4', 1), ('SIMVL/1', 516, 'simul', '', '', '2_4', 1), ('TVTVS', 517, 'tutus', '', '', '2_4', 1), ('VACVVS', 518, 'vacuus', '', '', '2_4', 1), ('VALEO', 519, 'valeo', '', '', '2_4', 3), ('VICTOR', 520, 'victor', '', '', '2_4', 1), ('VTINAM', 521, 'utinam', '', '', '2_4', 2), ('BIBO/2', 522, 'bibo', '', '', '2_5', 1), ('CARMEN/1', 523, 'carmen', '', '', '2_5', 1), ('CIBVS', 524, 'cibus', '', '', '2_5', 1), ('DVLCIS', 525, 'dulcis', '', '', '2_5', 1), ('FLVMEN', 526, 'flumen', '', '', '2_5', 1), ('IMMEMOR', 527, 'immemor', '', '', '2_5', 1), ('IOCVS', 528, 'iocus', '', '', '2_5', 1), ('IVVENTVS', 529, 'iuventus', '', '', '2_5', 1), ('LEVIS/1', 530, 'levis', '', '', '2_5', 1), ('MENS', 531, 'mens', '', '', '2_5', 1), ('NE/4', 532, 'ne', '', '', '2_5', 3), ('ORO', 533, 'oro', '', '', '2_5', 1), ('PLACEO', 534, 'placeo', '', '', '2_5', 1), ('PROXIMVS/2', 535, 'proximus', '', '', '2_5', 1), ('TAMQVAM/2', 536, 'tam', '', '', '2_5', 1), ('VEHEMENS', 537, 'vehemens', '', '', '2_5', 1), ('VETVS', 538, 'vetus', '', '', '2_5', 1), ('VINVM', 539, 'vinum', '', '', '2_5', 1), ('VIRTVS', 540, 'virtus', '', '', '2_5', 1), ('VITIVM', 541, 'vitium', '', '', '2_5', 1), ('VT/4', 542, 'ut', '', '', '2_5', 4), ('DECIPIO', 543, 'decipio', '', '', '2_6', 1), ('DILIGO/3', 544, 'diligo', '', '', '2_6', 1), ('DVO', 545, 'duo', '', '', '2_6', 1), ('EXERCITVS/1', 546, 'exercitus', '', '', '2_6', 1), ('FIDELIS/2', 547, 'fidelis', '', '', '2_6', 1), ('HERES', 548, 'heres', '', '', '2_6', 1), ('IMPERIVM', 549, 'imperium', '', '', '2_6', 1), ('INOPIA', 550, 'inopia', '', '', '2_6', 1), ('LAVDO', 551, 'laudo', '', '', '2_6', 1), ('NECESSEEST', 552, 'necesse', '', '', '2_6', 1), ('NEMO', 553, 'nemo', '', '', '2_6', 1), ('PATER', 554, 'pater', '', '', '2_6', 2), ('PAVLO', 555, 'paulo', '', '', '2_6', 1), ('QVAM/1', 556, 'quam', '', '', '2_6', 2), ('QVANTVM/3', 557, 'quantum', '', '', '2_6', 1), ('RESTITVO', 558, 'restituo', '', '', '2_6', 1), ('SATIS/2', 559, 'satis', '', '', '2_6', 1), ('SECVNDVS/1', 560, 'secundus', '', '', '2_6', 1), ('TERTIVS', 561, 'tertius', '', '', '2_6', 1), ('TRES', 562, 'tres', '', '', '2_6', 1), ('TRISTIS', 563, 'tristis', '', '', '2_6', 1), ('VEHEMENTER', 564, 'vehementer', '', '', '2_6', 1), ('AETAS', 565, 'aetas', '', '', '2_7', 1), ('FIDES/2', 566, 'fides', '', '', '2_7', 1), ('FVNDO/2', 567, 'fundo', '', '', '2_7', 1), ('GLORIA', 568, 'gloria', '', '', '2_7', 1), ('LIBERTAS', 569, 'libertas', '', '', '2_7', 1), ('LVMEN', 570, 'lumen', '', '', '2_7', 1), ('MALO', 571, 'malo', '', '', '2_7', 1), ('NOLO', 572, 'nolo', '', '', '2_7', 2), ('ORNATVS/1', 573, 'ornatus', '', '', '2_7', 1), ('OTIVM', 574, 'otium', '', '', '2_7', 1), ('POTENS', 575, 'potens', '', '', '2_7', 1), ('PVBLICVS/2', 576, 'publicus', '', '', '2_7', 1), ('QVALIS/1', 577, 'qualis', '', '', '2_7', 1), ('RESPVBLICA', 578, 'res', '', '', '2_7', 1), ('STVDIOSVS', 579, 'studiosus', '', '', '2_7', 1), ('TAMQVAM/1', 580, 'tamquam', '', '', '2_7', 1), ('TOT', 581, 'tot', '', '', '2_7', 1), ('TRAHO', 582, 'traho', '', '', '2_7', 1), ('VBI/1', 583, 'ubi', '', '', '2_7', 1), ('VIX', 584, 'vix', '', '', '2_7', 1), ('VNVS', 585, 'unus', '', '', '2_7', 1), ('VOLO/3', 586, 'volo', '', '', '2_7', 1), ('VTILIS', 587, 'utilis', '', '', '2_7', 1), ('ADHVC', 588, 'adhuc', '', '', '2_8', 1), ('ANTIQVVS', 589, 'antiquus', '', '', '2_8', 1), ('ARS', 590, 'ars', '', '', '2_8', 1), ('DOMINOR', 591, 'dominor', '', '', '2_8', 1), ('HORTOR', 592, 'hortor', '', '', '2_8', 1), ('LATINE', 593, 'Latine', '', '', '2_8', 1), ('LATINVS/A', 594, 'Latinus', '', '', '2_8', 1), ('LINGVA', 595, 'lingua', '', '', '2_8', 1), ('LOQVOR', 596, 'loquor', '', '', '2_8', 1), ('MAGIS/2', 597, 'magis', '', '', '2_8', 1), ('MAIOR', 598, 'maior', '', '', '2_8', 1), ('MAXIMVS', 599, 'maximus', '', '', '2_8', 1), ('MELIOR', 600, 'melior', '', '', '2_8', 1), ('MINIMVS', 601, 'minimus', '', '', '2_8', 1), ('MINVS', 602, 'minus', '', '', '2_8', 2), ('OPTIMVS', 603, 'optimus', '', '', '2_8', 1), ('PARTIOR', 604, 'partior', '', '', '2_8', 1), ('PATIOR', 605, 'patior', '', '', '2_8', 1), ('PEIOR', 606, 'peior', '', '', '2_8', 1), ('PESSIMVS', 607, 'pessimus', '', '', '2_8', 1), ('PLVRIMVS', 608, 'plurimus', '', '', '2_8', 1), ('PLVS', 609, 'plus', '', '', '2_8', 1), ('SEQVOR', 610, 'sequor', '', '', '2_8', 1), ('VEREOR', 611, 'vereor', '', '', '2_8', 1), ('ADDO', 612, 'addo', '', '', '2_9', 1), ('AVRIS', 613, 'auris', '', '', '2_9', 1), ('CONOR', 614, 'conor', '', '', '2_9', 1), ('DEMITTO', 615, 'demitto', '', '', '2_9', 1), ('DISSIMILIS', 616, 'dissimilis', '', '', '2_9', 1), ('FACILIS', 617, 'facilis', '', '', '2_9', 1), ('FERO', 618, 'fero', '', '', '2_9', 1), ('FIO', 619, 'fio', '', '', '2_9', 1), ('FRIGVS', 620, 'frigus', '', '', '2_9', 1), ('GENVS/1', 621, 'genus', '', '', '2_9', 1), ('GLACIES', 622, 'glacies', '', '', '2_9', 1), ('GRACILIS', 623, 'gracilis', '', '', '2_9', 1), ('HVMILIS', 624, 'humilis', '', '', '2_9', 1), ('ITER', 625, 'iter', '', '', '2_9', 1), ('LABOR/2', 626, 'labor', '', '', '2_9', 1), ('MODEROR', 627, 'moderor', '', '', '2_9', 1), ('NIX', 628, 'nix', '', '', '2_9', 1), ('ONVS', 629, 'onus', '', '', '2_9', 1), ('PERVENIO', 630, 'pervenio', '', '', '2_9', 1), ('PROGREDIOR', 631, 'progredior', '', '', '2_9', 1), ('QVOTIENS/2', 632, 'quotiens', '', '', '2_9', 1), ('SIMVLAC/2', 633, 'simulac', '', '', '2_9', 1), ('AEDES', 634, 'aedes', '', '', '2_10', 1), ('EO/1', 635, 'eo', '', '', '2_10', 1), ('IVCVNDVS', 636, 'iucundus', '', '', '2_10', 1), ('LABOR/1', 637, 'labor', '', '', '2_10', 1), ('LAEDO', 638, 'laedo', '', '', '2_10', 1), ('LIBER/2', 639, 'liber', '', '', '2_10', 1), ('LVCRVM', 640, 'lucrum', '', '', '2_10', 1), ('MARITIMVS', 641, 'maritimus', '', '', '2_10', 1), ('MODVS', 642, 'modus', '', '', '2_10', 1), ('PAVLISPER', 643, 'paulisper', '', '', '2_10', 1), ('PECVNIA', 644, 'pecunia', '', '', '2_10', 1), ('PLACIDVS', 645, 'placidus', '', '', '2_10', 1), ('POTIVS', 646, 'potius', '', '', '2_10', 1), ('PROSPER', 647, 'prosper', '', '', '2_10', 1), ('REDDO', 648, 'reddo', '', '', '2_10', 1), ('SARCINA', 649, 'sarcina', '', '', '2_10', 1), ('SCELESTVS', 650, 'scelestus', '', '', '2_10', 1), ('SEMEL', 651, 'semel', '', '', '2_10', 1), ('SERENVS', 652, 'serenus', '', '', '2_10', 1), ('SVVS', 653, 'suus', '', '', '2_10', 2), ('ALTER', 654, 'alter', '', '', '2_11', 1), ('GEMMA', 655, 'gemma', '', '', '2_11', 1), ('LEGATVS', 656, 'legatus', '', '', '2_11', 1), ('MAGNIHABEO', 657, 'magni', '', '', '2_11', 1), ('MINVS', 658, 'minus', '', '', '2_11', 2), ('NESCIO', 659, 'nescio', '', '', '2_11', 1), ('NEVTER', 660, 'neuter', '', '', '2_11', 1), ('NVLLVS', 661, 'nullus', '', '', '2_11', 1), ('OPERAEPRETIVMEST', 662, 'operae', '', '', '2_11', 1), ('PARVM/2', 663, 'parum', '', '', '2_11', 2), ('POPVLVS/1', 664, 'populus', '', '', '2_11', 1), ('QVOMODO/1', 665, 'quomodo', '', '', '2_11', 1), ('SALVTO', 666, 'saluto', '', '', '2_11', 1), ('SERVVS/1', 667, 'servus', '', '', '2_11', 1), ('SOLVS', 668, 'solus', '', '', '2_11', 1), ('SPECTO', 669, 'specto', '', '', '2_11', 1), ('TACEO', 670, 'taceo', '', '', '2_11', 1), ('TOTVS', 671, 'totus', '', '', '2_11', 1), ('TVRPIS', 672, 'turpis', '', '', '2_11', 1), ('VTER/4', 673, 'uter', '', '', '2_11', 1), ('VTOR', 674, 'utor', '', '', '2_11', 1), ('CARVS', 675, 'carus', '', '', '2_12', 1), ('CVM/3', 676, 'cum', '', '', '2_12', 2), ('INQVIO', 677, 'inquam', '', '', '2_12', 3), ('INSVLA', 678, 'insula', '', '', '2_12', 2), ('MORIOR', 679, 'morior', '', '', '2_12', 1), ('NIMIS', 680, 'nimis', '', '', '2_12', 1), ('NISI', 681, 'nisi', '', '', '2_12', 1), ('OFFICIVM', 682, 'officium', '', '', '2_12', 1), ('ORBIS', 683, 'orbis', '', '', '2_12', 1), ('ORBISTERRARVM', 684, 'orbis', '', '', '2_12', 1), ('PROBO', 685, 'probo', '', '', '2_12', 1), ('QVAMQVAM/2', 686, 'quamquam', '', '', '2_12', 1), ('QVAMVIS/1', 687, 'quamvis', '', '', '2_12', 1), ('QVIA', 688, 'quia', '', '', '2_12', 1), ('QVIDEM', 689, 'quidem', '', '', '2_12', 1), ('QVOD/1', 690, 'quod', '', '', '2_12', 1), ('SENTENTIA', 691, 'sententia', '', '', '2_12', 1), ('SORS', 692, 'sors', '', '', '2_12', 1), ('SPERO', 693, 'spero', '', '', '2_12', 1), ('SPES', 694, 'spes', '', '', '2_12', 1), ('TAMEN', 695, 'tamen', '', '', '2_12', 2), ('ABSENS', 696, 'absens', '', '', '2_13', 1), ('ABSVM/1', 697, 'absum', '', '', '2_13', 1), ('ATQVE/1', 698, 'atque', '', '', '2_13', 2), ('BENEVOLENTIA', 699, 'benevolentia', '', '', '2_13', 1), ('DECLARO', 700, 'declaro', '', '', '2_13', 1), ('IDEM', 701, 'idem', '', '', '2_13', 1), ('IPSE', 702, 'ipse', '', '', '2_13', 1), ('IRASCOR', 703, 'irascor', '', '', '2_13', 1), ('ISTE', 704, 'iste', '', '', '2_13', 1), ('MIROR', 705, 'miror', '', '', '2_13', 1), ('MVLTITVDO', 706, 'multitudo', '', '', '2_13', 1), ('NEGO', 707, 'nego', '', '', '2_13', 1), ('NVMERO/1', 708, 'numero', '', '', '2_13', 1), ('OFFENDO', 709, 'offendo', '', '', '2_13', 1), ('REDEO/1', 710, 'redeo', '', '', '2_13', 1), ('REFERO', 711, 'refero', '', '', '2_13', 1), ('SOCIVS/1', 712, 'socius', '', '', '2_13', 1), ('TALIS', 713, 'talis', '', '', '2_13', 1), ('TVRRIS', 714, 'turris', '', '', '2_13', 1), ('VENIA', 715, 'venia', '', '', '2_13', 1), ('VERSOR', 716, 'versor', '', '', '2_13', 1), ('VIRGA', 717, 'virga', '', '', '2_13', 1), ('VOLVNTAS', 718, 'voluntas', '', '', '2_13', 1), ('AFFIRMO', 719, 'affirmo', '', '', '2_14', 1), ('CIRCVMEO/1', 720, 'circumeo', '', '', '2_14', 1), ('CONTINEO', 721, 'contineo', '', '', '2_14', 1), ('COTIDIANVS', 722, 'cottidianus', '', '', '2_14', 1), ('ELEMENTVM', 723, 'elementum', '', '', '2_14', 1), ('ERGO/2', 724, 'ergo', '', '', '2_14', 1), ('GRAVITAS', 725, 'gravitas', '', '', '2_14', 1), ('IMMENSVS', 726, 'immensus', '', '', '2_14', 1), ('INFINITVS', 727, 'infinitus', '', '', '2_14', 1), ('MAXIME', 728, 'maxime', '', '', '2_14', 1), ('MEDIVS', 729, 'medius', '', '', '2_14', 1), ('MOTVS', 730, 'motus', '', '', '2_14', 1), ('MVLTO/2', 731, 'multo', '', '', '2_14', 1), ('NATVRA', 732, 'natura', '', '', '2_14', 1), ('NECESSARIO', 733, 'necessario', '', '', '2_14', 1), ('PERPERAM', 734, 'perperam', '', '', '2_14', 1), ('PONDVS', 735, 'pondus', '', '', '2_14', 1), ('PRAESERTIM', 736, 'praesertim', '', '', '2_14', 1), ('QVIES', 737, 'quies', '', '', '2_14', 1), ('VNDIQVE', 738, 'undique', '', '', '2_14', 1), ('VOLVO', 739, 'volvo', '', '', '2_14', 1), ('VT/4', 740, 'ut', '', '', '2_14', 4), ('ANIMADVERTO', 741, 'animadverto', '', '', '2_15', 1), ('APPROPINQVO', 742, 'appropinquo', '', '', '2_15', 1), ('CERNO', 743, 'cerno', '', '', '2_15', 1), ('CIRCA/2', 744, 'circa', '', '', '2_15', 1), ('CLAMO', 745, 'clamo', '', '', '2_15', 1), ('FINGO', 746, 'fingo', '', '', '2_15', 1), ('IMPINGO', 747, 'impingo', '', '', '2_15', 1), ('INFLIGO', 748, 'infligo', '', '', '2_15', 1), ('ITERVM', 749, 'iterum', '', '', '2_15', 1), ('OPPIDVM', 750, 'oppidum', '', '', '2_15', 1), ('PERCVTIO', 751, 'percutio', '', '', '2_15', 1), ('PRAEDITVS', 752, 'praeditus', '', '', '2_15', 1), ('REPELLO', 753, 'repello', '', '', '2_15', 1), ('RIDEO', 754, 'rideo', '', '', '2_15', 1), ('RVMPO', 755, 'rumpo', '', '', '2_15', 1), ('SEDES', 756, 'sedes', '', '', '2_15', 1), ('SIC', 757, 'sic', '', '', '2_15', 1), ('SIDVS', 758, 'sidus', '', '', '2_15', 1), ('TELVM', 759, 'telum', '', '', '2_15', 1), ('VEHO', 760, 'veho', '', '', '2_15', 1)]
section_list ={'1.1': 'start', '1.2': '1.1', '1.3': '1.2', '1.4': '1.3', '1.5': '1.4', '1.6': '1.5', '1.7': '1.6', '1.8': '1.7', '1.9': '1.8', '1.10': '1.9', '1.11': '1.10', '1.12': '1.11', '1.13': '1.12', '1.14': '1.13', '1.15': '1.14', '1.16': '1.15', '1.17': '1.16', '1.18': '1.17', '1.19': '1.18', '1.20': '1.19', '1.21': '1.20', '2.1': '1.21', '2.2': '2.1', '2.3': '2.2', '2.4': '2.3', '2.5': '2.4', '2.6': '2.5', '2.7': '2.6', '2.8': '2.7', '2.9': '2.8', '2.10': '2.9', '2.11': '2.10', '2.12': '2.11', '2.13': '2.12', '2.14': '2.13', '2.15': '2.14', 'end': '2.15', 'start': 'start'}
title = "Latin for the New Millennium Vols 1 and 2 (Tunberg-Minkova)"
section_level =  2
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)