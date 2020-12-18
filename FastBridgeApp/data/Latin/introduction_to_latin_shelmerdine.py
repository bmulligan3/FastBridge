import text
nan=""
section_words = {'start': -1, '26': 405, '1': 22, '10': 45, '11': 67, '12': 91, '13': 115, '14': 137, '15': 159, '16': 182, '17': 205, '18': 226, '19': 247, '2': 270, '20': 291, '21': 311, '22': 332, '23': 353, '24': 367, '25': 388, '27': 427, '28': 448, '29': 469, '3': 490, '30': 506, '31': 513, '32': 520, '4': 540, '5': 563, '6': 586, '7': 608, '8': 630, '9': 654, 'end': -2}
the_text =  [('QVAM/1', 0, 'quam', '', '', '26', 2), ('AGRICOLA', 1, 'agricola', '', '', '1', 1), ('AMO', 2, 'amo', '', '', '1', 1), ('AQVA', 3, 'aqua', '', '', '1', 1), ('DEBEO', 4, 'debeo', '', '', '1', 1), ('DOCEO', 5, 'doceo', '', '', '1', 1), ('FAMA', 6, 'fama', '', '', '1', 1), ('FEMINA', 7, 'femina', '', '', '1', 1), ('FORTVNA', 8, 'fortuna', '', '', '1', 1), ('HABEO', 9, 'habeo', '', '', '1', 1), ('IACEO', 10, 'iaceo', '', '', '1', 1), ('IVVO', 11, 'iuvo', '', '', '1', 1), ('LABORO', 12, 'laboro', '', '', '1', 1), ('LAVDO', 13, 'laudo', '', '', '1', 1), ('NAVTA', 14, 'nauta', '', '', '1', 1), ('NE/2', 15, 'ne', '', '', '1', 1), ('OPTO', 16, 'opto', '', '', '1', 1), ('ROSA', 17, 'rosa', '', '', '1', 1), ('SVPERO', 18, 'supero', '', '', '1', 1), ('TACEO', 19, 'taceo', '', '', '1', 1), ('TIMEO', 20, 'timeo', '', '', '1', 1), ('VIDEO', 21, 'video', '', '', '1', 1), ('VOCO', 22, 'voco', '', '', '1', 1), ('ALIVS', 23, 'alius', '', '', '10', 1), ('ALIVSALIVS', 24, 'alius', '', '', '10', 1), ('COGNOSCO', 25, 'cognosco', '', '', '10', 1), ('CREO', 26, 'creo', '', '', '10', 1), ('ETIAM', 27, 'etiam', '', '', '10', 1), ('FACTVM', 28, 'factum', '', '', '10', 1), ('FVGIO', 29, 'fugio', '', '', '10', 1), ('HIC/2', 30, 'hic', '', '', '10', 1), ('ILLE', 31, 'ille', '', '', '10', 1), ('INCIPIO', 32, 'incipio', '', '', '10', 1), ('IS', 33, 'is', '', '', '10', 1), ('ITA', 34, 'ita', '', '', '10', 1), ('IVDICO', 35, 'iudico', '', '', '10', 1), ('IVS/1', 36, 'ius', '', '', '10', 1), ('LEGO/2', 37, 'lego', '', '', '10', 1), ('NONSOLVM', 38, 'non', '', '', '10', 1), ('NVLLVS', 39, 'nullus', '', '', '10', 1), ('PERSVADEO', 40, 'persuadeo', '', '', '10', 1), ('SOLVS', 41, 'solus', '', '', '10', 1), ('TAMEN', 42, 'tamen', '', '', '10', 1), ('TOTVS', 43, 'totus', '', '', '10', 1), ('VLLVS', 44, 'ullus', '', '', '10', 1), ('VNVS', 45, 'unus', '', '', '10', 1), ('ANTE/2', 46, 'ante', '', '', '11', 2), ('CADO', 47, 'cado', '', '', '11', 1), ('CAVSA', 48, 'causa', '', '', '11', 1), ('CAVSA/2', 49, 'causa', '', '', '11', 1), ('CONIVX', 50, 'coniunx', '', '', '11', 1), ('CREDO', 51, 'credo', '', '', '11', 1), ('DEXTER', 52, 'dexter', '', '', '11', 1), ('FLVMEN', 53, 'flumen', '', '', '11', 1), ('GRATIA', 54, 'gratia', '', '', '11', 1), ('GRATIASAGERE', 55, 'gratias', '', '', '11', 1), ('LACRIMA', 56, 'lacrima', '', '', '11', 1), ('LAVS', 57, 'laus', '', '', '11', 1), ('MILES', 58, 'miles', '', '', '11', 1), ('NAM', 59, 'nam', '', '', '11', 1), ('NEC/2', 60, 'nec', '', '', '11', 1), ('NEQVE', 61, 'neque', '', '', '11', 1), ('NEQVENEC', 62, 'neque', '', '', '11', 1), ('PER', 63, 'per', '', '', '11', 1), ('PETO', 64, 'peto', '', '', '11', 1), ('RELINQVO', 65, 'relinquo', '', '', '11', 1), ('SECVNDVS/1', 66, 'secundus', '', '', '11', 1), ('TIMOR', 67, 'timor', '', '', '11', 1), ('ACER/2', 68, 'acer', '', '', '12', 1), ('AETAS', 69, 'aetas', '', '', '12', 1), ('ANNVS', 70, 'annus', '', '', '12', 1), ('BELLVMGERO', 71, 'bellum', '', '', '12', 1), ('BREVIS', 72, 'brevis', '', '', '12', 1), ('CELER', 73, 'celer', '', '', '12', 1), ('DIFFICILIS', 74, 'difficilis', '', '', '12', 1), ('DISCEDO/1', 75, 'discedo', '', '', '12', 1), ('DOLOR', 76, 'dolor', '', '', '12', 1), ('DVLCIS', 77, 'dulcis', '', '', '12', 1), ('FACILIS', 78, 'facilis', '', '', '12', 1), ('FELIX', 79, 'felix', '', '', '12', 1), ('FORTIS', 80, 'fortis', '', '', '12', 1), ('GALLIA/N', 81, 'Gallia', '', '', '12', 1), ('GENS', 82, 'gens', '', '', '12', 1), ('GERO', 83, 'gero', '', '', '12', 1), ('HORA', 84, 'hora', '', '', '12', 1), ('INGENS', 85, 'ingens', '', '', '12', 1), ('OMNIS', 86, 'omnis', '', '', '12', 1), ('PES', 87, 'pes', '', '', '12', 1), ('POTENS', 88, 'potens', '', '', '12', 1), ('SIC', 89, 'sic', '', '', '12', 1), ('TEMPVS/1', 90, 'tempus', '', '', '12', 1), ('TER', 91, 'ter', '', '', '12', 1), ('AVDIO', 92, 'audio', '', '', '13', 1), ('COPIA', 93, 'copia', '', '', '13', 1), ('DIGNVS', 94, 'dignus', '', '', '13', 1), ('DORMIO', 95, 'dormio', '', '', '13', 1), ('FINIO', 96, 'finio', '', '', '13', 1), ('FINIS', 97, 'finis', '', '', '13', 1), ('IMPEDIO', 98, 'impedio', '', '', '13', 1), ('INDIGNVS', 99, 'indignus', '', '', '13', 1), ('INTELLIGO', 100, 'intellego', '', '', '13', 1), ('ITER', 101, 'iter', '', '', '13', 1), ('MORA', 102, 'mora', '', '', '13', 1), ('MORTALIS/2', 103, 'mortalis', '', '', '13', 1), ('PAVCI', 104, 'paucus', '', '', '13', 1), ('PROHIBEO', 105, 'prohibeo', '', '', '13', 1), ('RELIQVVS', 106, 'reliquus', '', '', '13', 1), ('SAPIENS/2', 107, 'sapiens', '', '', '13', 1), ('SCIO', 108, 'scio', '', '', '13', 1), ('SENEX/1', 109, 'senex', '', '', '13', 1), ('SENTIO', 110, 'sentio', '', '', '13', 1), ('SERVIO', 111, 'servio', '', '', '13', 1), ('SVPERI', 112, 'superi', '', '', '13', 1), ('SVPERVS', 113, 'superus', '', '', '13', 1), ('SVVS', 114, 'suus', '', '', '13', 1), ('VENIO', 115, 'venio', '', '', '13', 1), ('ABSVM/1', 116, 'absum', '', '', '14', 1), ('ADVENIO', 117, 'advenio', '', '', '14', 1), ('ARBOR', 118, 'arbor', '', '', '14', 1), ('CIRCA/2', 119, 'circa', '', '', '14', 1), ('CIRCVM/2', 120, 'circum', '', '', '14', 1), ('CVRO', 121, 'curo', '', '', '14', 1), ('DIMITTO', 122, 'dimitto', '', '', '14', 1), ('GENVS/1', 123, 'genus', '', '', '14', 1), ('HONOR', 124, 'honor', '', '', '14', 1), ('HOSTIS', 125, 'hostis', '', '', '14', 1), ('IAM', 126, 'iam', '', '', '14', 1), ('INVENIO', 127, 'invenio', '', '', '14', 1), ('LEGATVS', 128, 'legatus', '', '', '14', 1), ('LONGVS', 129, 'longus', '', '', '14', 1), ('MARE', 130, 'mare', '', '', '14', 1), ('MEDIVS', 131, 'medius', '', '', '14', 1), ('MONEO', 132, 'moneo', '', '', '14', 1), ('NOX', 133, 'nox', '', '', '14', 1), ('RAPIO', 134, 'rapio', '', '', '14', 1), ('SCELVS', 135, 'scelus', '', '', '14', 1), ('STO', 136, 'sto', '', '', '14', 1), ('TANTVS', 137, 'tantus', '', '', '14', 1), ('ATQVE/1', 138, 'atque', '', '', '15', 1), ('AVREVS/2', 139, 'aureus', '', '', '15', 1), ('AVRVM', 140, 'aurum', '', '', '15', 1), ('CEDO/1', 141, 'cedo', '', '', '15', 1), ('CIVIS', 142, 'civis', '', '', '15', 1), ('DVRVS', 143, 'durus', '', '', '15', 1), ('FESSVS', 144, 'fessus', '', '', '15', 1), ('FORTE', 145, 'forte', '', '', '15', 1), ('HVMVS', 146, 'humus', '', '', '15', 1), ('IGNIS', 147, 'ignis', '', '', '15', 1), ('LABOR/1', 148, 'labor', '', '', '15', 1), ('LITVS/2', 149, 'litus', '', '', '15', 1), ('LVMEN', 150, 'lumen', '', '', '15', 1), ('PECTVS', 151, 'pectus', '', '', '15', 1), ('PONO', 152, 'pono', '', '', '15', 1), ('PROVINCIA', 153, 'provincia', '', '', '15', 1), ('SVPER/2', 154, 'super', '', '', '15', 1), ('SVRGO', 155, 'surgo', '', '', '15', 1), ('TEMPTO', 156, 'tempto', '', '', '15', 1), ('TRISTIS', 157, 'tristis', '', '', '15', 1), ('VNDA', 158, 'unda', '', '', '15', 1), ('VOLVO', 159, 'volvo', '', '', '15', 1), ('ARDEO', 160, 'ardeo', '', '', '16', 1), ('CASVS', 161, 'casus', '', '', '16', 1), ('CORNV', 162, 'cornu', '', '', '16', 1), ('DIES', 163, 'dies', '', '', '16', 1), ('DOMVS', 164, 'domus', '', '', '16', 1), ('FACIES', 165, 'facies', '', '', '16', 1), ('FIDES/2', 166, 'fides', '', '', '16', 1), ('FLVCTVS', 167, 'fluctus', '', '', '16', 1), ('GENV', 168, 'genu', '', '', '16', 1), ('IGITVR', 169, 'igitur', '', '', '16', 1), ('IMPETVS', 170, 'impetus', '', '', '16', 1), ('INDE', 171, 'inde', '', '', '16', 1), ('MANVS/1', 172, 'manus', '', '', '16', 1), ('METVS', 173, 'metus', '', '', '16', 1), ('MILLEPASSVS', 174, 'mile', '', '', '16', 1), ('PASSVS/1', 175, 'passus', '', '', '16', 1), ('RES', 176, 'res', '', '', '16', 1), ('RESPVBLICA', 177, 'res', '', '', '16', 1), ('RVS', 178, 'rus', '', '', '16', 1), ('SENATVS', 179, 'senatus', '', '', '16', 1), ('SPES', 180, 'spes', '', '', '16', 1), ('TAM', 181, 'tam', '', '', '16', 1), ('VVLTVS', 182, 'vultus', '', '', '16', 1), ('AB', 183, 'a', '', '', '17', 2), ('ACIES', 184, 'acies', '', '', '17', 1), ('ALTER', 185, 'alter', '', '', '17', 1), ('AMITTO', 186, 'amitto', '', '', '17', 1), ('CASTRA/2', 187, 'castra', '', '', '17', 1), ('CASTRAPONERE', 188, 'castra', '', '', '17', 1), ('CERNO', 189, 'cerno', '', '', '17', 1), ('CONCVRRO', 190, 'concurro', '', '', '17', 1), ('CONSTITVO', 191, 'constituo', '', '', '17', 1), ('CONTRA/2', 192, 'contra', '', '', '17', 1), ('CVRRO', 193, 'curro', '', '', '17', 1), ('EPISTOLA', 194, 'epistula', '', '', '17', 1), ('EXERCITVS/1', 195, 'exercitus', '', '', '17', 1), ('FERRVM', 196, 'ferrum', '', '', '17', 1), ('FERVS/2', 197, 'ferus', '', '', '17', 1), ('INCENDO', 198, 'incendo', '', '', '17', 1), ('INSTITVO', 199, 'instituo', '', '', '17', 1), ('IVDICIVM', 200, 'iudicium', '', '', '17', 2), ('MVLTITVDO', 201, 'multitudo', '', '', '17', 1), ('PROELIVM', 202, 'proelium', '', '', '17', 1), ('SPECTO', 203, 'specto', '', '', '17', 1), ('TRAHO', 204, 'traho', '', '', '17', 1), ('VIDEOR', 205, 'videor', '', '', '17', 1), ('ACCIPIO', 206, 'accipio', '', '', '18', 1), ('ADVENTVS', 207, 'adventus', '', '', '18', 1), ('AMICVS/2', 208, 'amicus', '', '', '18', 1), ('APTVS', 209, 'aptus', '', '', '18', 1), ('CARVS', 210, 'carus', '', '', '18', 1), ('CLAMOR', 211, 'clamor', '', '', '18', 1), ('CONFICIO', 212, 'conficio', '', '', '18', 1), ('CVM/3', 213, 'cum', '', '', '18', 1), ('DVM/2', 214, 'dum', '', '', '18', 1), ('FAS', 215, 'fas', '', '', '18', 2), ('FIDELIS/2', 216, 'fidelis', '', '', '18', 1), ('GAVDIVM', 217, 'gaudium', '', '', '18', 1), ('INIMICVS/2', 218, 'inimicus', '', '', '18', 1), ('PAR/2', 219, 'pār', '', '', '18', 1), ('POSTQVAM', 220, 'postquam', '', '', '18', 1), ('QVIA', 221, 'quia', '', '', '18', 1), ('QVOD/1', 222, 'quod', '', '', '18', 1), ('SI/2', 223, 'si', '', '', '18', 1), ('SIMILIS', 224, 'similis', '', '', '18', 1), ('VBI/1', 225, 'ubi', '', '', '18', 1), ('VVLNVS', 226, 'vulnus', '', '', '18', 1), ('AESTVS', 227, 'aestus', '', '', '19', 1), ('AVRIS', 228, 'auris', '', '', '19', 1), ('AVXILIVM', 229, 'auxilium', '', '', '19', 1), ('CAESAR/N', 230, 'Caesar', '', '', '19', 1), ('CAREO', 231, 'careo', '', '', '19', 1), ('EFFICIO', 232, 'efficio', '', '', '19', 1), ('EQVVS', 233, 'equus', '', '', '19', 1), ('FRANGO', 234, 'frango', '', '', '19', 1), ('GRAECIA/N', 235, 'Graecia', '', '', '19', 1), ('GRAECVS/A', 236, 'Graecus', '', '', '19', 1), ('LEVIS/1', 237, 'levis', '', '', '19', 1), ('MEMORIA', 238, 'memoria', '', '', '19', 1), ('NAVIS', 239, 'navis', '', '', '19', 1), ('NVBES', 240, 'nubes', '', '', '19', 1), ('PROPINQVVS', 241, 'propinquus', '', '', '19', 1), ('QVI/1', 242, 'qui', '', '', '19', 1), ('ROMA/N', 243, 'Roma', '', '', '19', 1), ('SOROR', 244, 'soror', '', '', '19', 1), ('TROIA/N', 245, 'Troia', '', '', '19', 1), ('TROIANVS/A', 246, 'Troianus', '', '', '19', 1), ('VERTO', 247, 'verto', '', '', '19', 1), ('AGER', 248, 'ager', '', '', '2', 1), ('AMICVS/1', 249, 'amicus', '', '', '2', 1), ('ANIMVS', 250, 'animus', '', '', '2', 1), ('AVDEO', 251, 'audeo', '', '', '2', 1), ('BELLVM', 252, 'bellum', '', '', '2', 1), ('CLAMO', 253, 'clamo', '', '', '2', 1), ('CONSILIVM', 254, 'consilium', '', '', '2', 1), ('DOMINVS', 255, 'dominus', '', '', '2', 1), ('DONVM', 256, 'donum', '', '', '2', 1), ('DVBITO', 257, 'dubito', '', '', '2', 1), ('ET/2', 258, 'et', '', '', '2', 1), ('ETET', 259, 'et', '', '', '2', 1), ('LITTERA', 260, 'littera', '', '', '2', 1), ('LOCVS', 261, 'locus', '', '', '2', 1), ('NATVRA', 262, 'natura', '', '', '2', 1), ('ORO', 263, 'oro', '', '', '2', 1), ('PVELLA', 264, 'puella', '', '', '2', 1), ('PVER', 265, 'puer', '', '', '2', 1), ('QVE', 266, 'que', '', '', '2', 1), ('REGNVM', 267, 'regnum', '', '', '2', 1), ('SED', 268, 'sed', '', '', '2', 1), ('TERREO', 269, 'terreo', '', '', '2', 1), ('VIR', 270, 'vir', '', '', '2', 1), ('APERIO', 271, 'aperio', '', '', '20', 1), ('APERTVS', 272, 'apertus', '', '', '20', 1), ('ARX', 273, 'arx', '', '', '20', 1), ('AVCTORITAS', 274, 'auctoritas', '', '', '20', 1), ('AVTEM', 275, 'autem', '', '', '20', 1), ('CAEDES', 276, 'caedes', '', '', '20', 1), ('CAEDO', 277, 'caedo', '', '', '20', 1), ('CANO', 278, 'cano', '', '', '20', 1), ('CONDO', 279, 'condo', '', '', '20', 1), ('CONSERVO', 280, 'conservo', '', '', '20', 1), ('CVPIO', 281, 'cupio', '', '', '20', 1), ('FATVM', 282, 'fatum', '', '', '20', 1), ('INTEREA', 283, 'interea', '', '', '20', 1), ('OB', 284, 'ob', '', '', '20', 1), ('ORA', 285, 'ora', '', '', '20', 1), ('PROCVL', 286, 'procul', '', '', '20', 1), ('SAEVVS', 287, 'saevus', '', '', '20', 1), ('SIGNVM', 288, 'signum', '', '', '20', 1), ('SOMNVS', 289, 'somnus', '', '', '20', 1), ('VIS', 290, 'vis', '', '', '20', 1), ('VITO', 291, 'vito', '', '', '20', 1), ('CELERITER', 292, 'celeriter', '', '', '21', 1), ('CETERVS', 293, 'ceterus', '', '', '21', 1), ('COGO', 294, 'cogo', '', '', '21', 1), ('DOLVS', 295, 'dolus', '', '', '21', 1), ('FORTITER', 296, 'fortiter', '', '', '21', 1), ('IVBEO', 297, 'iubeo', '', '', '21', 1), ('MALO', 298, 'malo', '', '', '21', 1), ('MOENIA', 299, 'moenia', '', '', '21', 1), ('MOS', 300, 'mos', '', '', '21', 1), ('NECESSEEST', 301, 'necesse', '', '', '21', 1), ('NOLO', 302, 'nolo', '', '', '21', 1), ('NVNTIVS/1', 303, 'nuntius', '', '', '21', 1), ('POSTVLO', 304, 'postulo', '', '', '21', 1), ('PRINCEPS/1', 305, 'princeps', '', '', '21', 1), ('QVAM/1', 306, 'quam', '', '', '21', 2), ('SERVVS/1', 307, 'servus', '', '', '21', 1), ('SINO', 308, 'sino', '', '', '21', 1), ('VETO', 309, 'veto', '', '', '21', 1), ('VIVO', 310, 'vivo', '', '', '21', 1), ('VOLO/3', 311, 'volo', '', '', '21', 1), ('AIO', 312, 'aio', '', '', '22', 1), ('ARTVS/1', 313, 'artus', '', '', '22', 1), ('BENE', 314, 'bene', '', '', '22', 1), ('COGITO', 315, 'cogito', '', '', '22', 1), ('GAVDEO', 316, 'gaudeo', '', '', '22', 1), ('HODIE', 317, 'hodie', '', '', '22', 1), ('IBI', 318, 'ibi', '', '', '22', 1), ('IMPRVDENS', 319, 'imprudens', '', '', '22', 1), ('INQVIO', 320, 'inquam', '', '', '22', 1), ('LIBERI', 321, 'liberi', '', '', '22', 1), ('MODVS', 322, 'modus', '', '', '22', 1), ('NEGO', 323, 'nego', '', '', '22', 1), ('NESCIO', 324, 'nescio', '', '', '22', 1), ('ORBIS', 325, 'orbis', '', '', '22', 1), ('ORBISTERRARVM', 326, 'orbis', '', '', '22', 1), ('OSTENDO', 327, 'ostendo', '', '', '22', 1), ('PRVDENS', 328, 'prudens', '', '', '22', 1), ('PVTO', 329, 'puto', '', '', '22', 1), ('RESPONDEO', 330, 'respondeo', '', '', '22', 1), ('SPERO', 331, 'spero', '', '', '22', 1), ('TRADO', 332, 'trado', '', '', '22', 1), ('ARBITROR', 333, 'arbitror', '', '', '23', 1), ('CIBVS', 334, 'cibus', '', '', '23', 1), ('CONOR', 335, 'conor', '', '', '23', 1), ('CRIMEN', 336, 'crimen', '', '', '23', 1), ('CVNCTVS', 337, 'cunctus', '', '', '23', 1), ('FIDO', 338, 'fido', '', '', '23', 1), ('FRVOR', 339, 'fruor', '', '', '23', 1), ('FVNGOR', 340, 'fungor', '', '', '23', 1), ('IDEM', 341, 'idem', '', '', '23', 1), ('INGREDIOR', 342, 'ingredior', '', '', '23', 1), ('IPSE', 343, 'ipse', '', '', '23', 1), ('LOQVOR', 344, 'loquor', '', '', '23', 1), ('MOROR/1', 345, 'moror', '', '', '23', 1), ('PATIOR', 346, 'patior', '', '', '23', 1), ('POTIOR', 347, 'potior', '', '', '23', 1), ('POTVS/2', 348, 'potus', '', '', '23', 1), ('PROFICISCOR', 349, 'proficiscor', '', '', '23', 1), ('QVIDAM', 350, 'quidam', '', '', '23', 1), ('SEQVOR', 351, 'sequor', '', '', '23', 1), ('VESCOR', 352, 'vescor', '', '', '23', 1), ('VTOR', 353, 'utor', '', '', '23', 1), ('EXITIVM', 354, 'exitium', '', '', '24', 1), ('IMPERO', 355, 'impero', '', '', '24', 1), ('INCOLO/2', 356, 'incolo', '', '', '24', 1), ('INGENIVM', 357, 'ingenium', '', '', '24', 1), ('INTERFICIO', 358, 'interficio', '', '', '24', 1), ('MAXIMVS', 359, 'maximus', '', '', '24', 1), ('MORIOR', 360, 'morior', '', '', '24', 1), ('OCCIDO/2', 361, 'occido', '', '', '24', 1), ('OS/1', 362, 'os', '', '', '24', 1), ('PATEO', 363, 'pateo', '', '', '24', 1), ('PROXIMVS/2', 364, 'proximus', '', '', '24', 1), ('ROGO', 365, 'rogo', '', '', '24', 1), ('SOCIVS/1', 366, 'socius', '', '', '24', 1), ('VVLNERO', 367, 'vulnero', '', '', '24', 1), ('ABEO/1', 368, 'abeo', '', '', '25', 1), ('ADEO/1', 369, 'adeo', '', '', '25', 1), ('AEQVVS', 370, 'aequus', '', '', '25', 1), ('AFFERO', 371, 'affero', '', '', '25', 1), ('AVFERO', 372, 'aufero', '', '', '25', 1), ('COMMVNIS', 373, 'communis', '', '', '25', 1), ('CONFERO', 374, 'confero', '', '', '25', 1), ('EO/3', 375, 'eo', '', '', '25', 1), ('EXEO/1', 376, 'exeo', '', '', '25', 1), ('FERO', 377, 'fero', '', '', '25', 1), ('INEO/1', 378, 'ineo', '', '', '25', 1), ('INFELIX', 379, 'infelix', '', '', '25', 1), ('INFERO', 380, 'infero', '', '', '25', 1), ('OFFERO', 381, 'offero', '', '', '25', 1), ('PEREO/1', 382, 'pereo', '', '', '25', 1), ('REDEO/1', 383, 'redeo', '', '', '25', 1), ('REFERO', 384, 'refero', '', '', '25', 1), ('SECONFERRE', 385, 'se', '', '', '25', 1), ('SVBEO/1', 386, 'subeo', '', '', '25', 1), ('TOLLO', 387, 'tollo', '', '', '25', 1), ('TRANSEO/1', 388, 'transeo', '', '', '25', 1), ('AMOR', 389, 'amor', '', '', '26', 1), ('CANIS', 390, 'canis', '', '', '26', 1), ('CVLPA', 391, 'culpa', '', '', '26', 1), ('DELEO', 392, 'deleo', '', '', '26', 1), ('FACILE', 393, 'facile', '', '', '26', 1), ('GRAVIS', 394, 'gravis', '', '', '26', 1), ('IVSTVS', 395, 'iustus', '', '', '26', 1), ('LONGE', 396, 'longe', '', '', '26', 1), ('MODO/1', 397, 'modo', '', '', '26', 1), ('NVMQVAM', 398, 'numquam', '', '', '26', 1), ('PRIMO', 399, 'primo', '', '', '26', 1), ('PRIMVM', 400, 'primum', '', '', '26', 1), ('RESISTO', 401, 'resisto', '', '', '26', 1), ('SANCTVS', 402, 'sanctus', '', '', '26', 1), ('TVRPIS', 403, 'turpis', '', '', '26', 1), ('VTERQVE', 404, 'uterque', '', '', '26', 1), ('VTILIS', 405, 'utilis', '', '', '26', 1), ('ACCIDO/1', 406, 'accido', '', '', '27', 1), ('AN', 407, 'an', '', '', '27', 1), ('ASSVM/1', 408, 'adsum', '', '', '27', 1), ('AT/2', 409, 'at', '', '', '27', 1), ('AVRA', 410, 'aura', '', '', '27', 1), ('BEATVS', 411, 'beatus', '', '', '27', 1), ('DENIQVE', 412, 'denique', '', '', '27', 1), ('DESPERO', 413, 'despero', '', '', '27', 1), ('FLOREO', 414, 'floreo', '', '', '27', 1), ('FRVCTVS', 415, 'fructus', '', '', '27', 1), ('GLORIA', 416, 'gloria', '', '', '27', 1), ('HORTOR', 417, 'hortor', '', '', '27', 1), ('MOTVS', 418, 'motus', '', '', '27', 1), ('NE/4', 419, 'ne', '', '', '27', 1), ('NEGLIGO', 420, 'neglego', '', '', '27', 1), ('NEQVIDEM', 421, 'quidem', '', '', '27', 1), ('QVIDEM', 422, 'quidem', '', '', '27', 1), ('RECTVS', 423, 'rectus', '', '', '27', 1), ('TELLVS', 424, 'tellus', '', '', '27', 1), ('TEMPERO', 425, 'tempero', '', '', '27', 1), ('VERO/3', 426, 'vero', '', '', '27', 1), ('VTINAM', 427, 'utinam', '', '', '27', 1), ('APPROPINQVO', 428, 'appropinquo', '', '', '28', 1), ('BIBO/2', 429, 'bibo', '', '', '28', 1), ('CIVILIS', 430, 'civilis', '', '', '28', 1), ('DEINDE', 431, 'deinde', '', '', '28', 1), ('DIRVS', 432, 'dirus', '', '', '28', 1), ('GLADIVS', 433, 'gladius', '', '', '28', 1), ('IVDEX', 434, 'iudex', '', '', '28', 1), ('IVDICIVM', 435, 'iudicium', '', '', '28', 2), ('LIBERE', 436, 'libere', '', '', '28', 1), ('NEFAS', 437, 'nefas', '', '', '28', 2), ('OPPIDVM', 438, 'oppidum', '', '', '28', 1), ('POENA', 439, 'poena', '', '', '28', 1), ('POENASDARE', 440, 'poenas', '', '', '28', 1), ('SOL', 441, 'sol', '', '', '28', 1), ('TALIS', 442, 'talis', '', '', '28', 1), ('TELVM', 443, 'telum', '', '', '28', 1), ('TOT', 444, 'tot', '', '', '28', 1), ('TOTIENS', 445, 'totiens', '', '', '28', 1), ('TREMO', 446, 'tremo', '', '', '28', 1), ('VINVM', 447, 'vinum', '', '', '28', 1), ('VT/4', 448, 'ut', '', '', '28', 1), ('APPELLO/1', 449, 'appello', '', '', '29', 1), ('APVD', 450, 'apud', '', '', '29', 1), ('COLO/2', 451, 'colo', '', '', '29', 1), ('CVR/1', 452, 'cur', '', '', '29', 1), ('ERIPIO', 453, 'eripio', '', '', '29', 1), ('FIO', 454, 'fio', '', '', '29', 1), ('HABITO', 455, 'habito', '', '', '29', 1), ('IVNGO', 456, 'iungo', '', '', '29', 1), ('LATVS/2', 457, 'latus', '', '', '29', 1), ('LIBERO', 458, 'libero', '', '', '29', 1), ('MIROR', 459, 'miror', '', '', '29', 1), ('NVM', 460, 'num', '', '', '29', 1), ('PRECOR', 461, 'precor', '', '', '29', 1), ('QVAERO', 462, 'quaero', '', '', '29', 1), ('QVIS/1', 463, 'quis', '', '', '29', 1), ('QVOMODO/1', 464, 'quomodo', '', '', '29', 1), ('QVOT/1', 465, 'quot', '', '', '29', 1), ('QVOTIENS/2', 466, 'quotiens', '', '', '29', 1), ('REQVIRO', 467, 'requiro', '', '', '29', 1), ('STATIM', 468, 'statim', '', '', '29', 1), ('VNDIQVE', 469, 'undique', '', '', '29', 1), ('AEDIFICO', 470, 'aedifico', '', '', '3', 1), ('ARMA', 471, 'arma', '', '', '3', 1), ('CAELVM/1', 472, 'caelum', '', '', '3', 1), ('DEVS', 473, 'deus', '', '', '3', 1), ('DO', 474, 'do', '', '', '3', 1), ('FABVLA/1', 475, 'fabula', '', '', '3', 1), ('IMPERIVM', 476, 'imperium', '', '', '3', 1), ('LIBER/1', 477, 'liber', '', '', '3', 1), ('MONSTRO', 478, 'monstro', '', '', '3', 1), ('NARRO', 479, 'narro', '', '', '3', 1), ('NEMO', 480, 'nemo', '', '', '3', 1), ('NIHIL', 481, 'nihil', '', '', '3', 1), ('NOCEO', 482, 'noceo', '', '', '3', 1), ('PAREO', 483, 'pareo', '', '', '3', 1), ('PLACEO', 484, 'placeo', '', '', '3', 1), ('PORTO', 485, 'porto', '', '', '3', 1), ('PVGNO', 486, 'pugno', '', '', '3', 1), ('SOLEO', 487, 'soleo', '', '', '3', 1), ('TEMPLVM', 488, 'templum', '', '', '3', 1), ('TVRBA', 489, 'turba', '', '', '3', 1), ('VENTVS', 490, 'ventus', '', '', '3', 1), ('ALIQVIS', 491, 'aliquis', '', '', '30', 1), ('AMICITIA', 492, 'amicitia', '', '', '30', 1), ('CERTE', 493, 'certo', '', '', '30', 1), ('CONSPICIO', 494, 'conspicio', '', '', '30', 1), ('IMPERATOR', 495, 'imperator', '', '', '30', 1), ('METVO', 496, 'metuo', '', '', '30', 1), ('MOX', 497, 'mox', '', '', '30', 1), ('NISI', 498, 'nisi', '', '', '30', 1), ('OPS', 499, 'ops', '', '', '30', 1), ('PHILOSOPHIA', 500, 'philosophia', '', '', '30', 1), ('QVOQVE', 501, 'quoque', '', '', '30', 1), ('SIMVL/1', 502, 'simul', '', '', '30', 1), ('SIN', 503, 'sin', '', '', '30', 1), ('SVSCIPIO', 504, 'suscipio', '', '', '30', 1), ('VEREOR', 505, 'vereor', '', '', '30', 1), ('VICTORIA', 506, 'victoria', '', '', '30', 1), ('COMMITTO', 507, 'committo', '', '', '31', 1), ('CONVENIO', 508, 'convenio', '', '', '31', 1), ('MALE', 509, 'male', '', '', '31', 1), ('PONS', 510, 'pons', '', '', '31', 1), ('PROBO', 511, 'probo', '', '', '31', 1), ('TAMQVAM/1', 512, 'tamquam', '', '', '31', 1), ('VOLVPTAS', 513, 'voluptas', '', '', '31', 1), ('ANTE/2', 514, 'ante', '', '', '32', 2), ('FAS', 515, 'fas', '', '', '32', 2), ('FORSITAN', 516, 'forsan', '', '', '32', 1), ('LICEO', 517, 'liceo', '', '', '32', 1), ('MIRABILIS', 518, 'mirabilis', '', '', '32', 1), ('NEFAS', 519, 'nefas', '', '', '32', 2), ('OPORTET', 520, 'oportet', '', '', '32', 1), ('AB', 521, 'a', '', '', '4', 2), ('AD/2', 522, 'ad', '', '', '4', 1), ('AMBVLO', 523, 'ambulo', '', '', '4', 1), ('CASA', 524, 'casa', '', '', '4', 1), ('ERRO/2', 525, 'erro', '', '', '4', 1), ('EX', 526, 'e', '', '', '4', 1), ('FESTINO', 527, 'festino', '', '', '4', 1), ('IN', 528, 'in', '', '', '4', 1), ('MOVEO', 529, 'moveo', '', '', '4', 1), ('NAVIGO', 530, 'navigo', '', '', '4', 1), ('NON', 531, 'non', '', '', '4', 1), ('NVNC', 532, 'nunc', '', '', '4', 1), ('OCVLVS', 533, 'oculus', '', '', '4', 1), ('PONTVS', 534, 'pontus', '', '', '4', 1), ('PRO/1', 535, 'pro', '', '', '4', 1), ('SAEPE', 536, 'saepe', '', '', '4', 1), ('TANDEM', 537, 'tandem', '', '', '4', 1), ('TRANS/2', 538, 'trans', '', '', '4', 1), ('TVM', 539, 'tum', '', '', '4', 1), ('VIA', 540, 'via', '', '', '4', 1), ('AEGER/2', 541, 'aeger', '', '', '5', 1), ('ALTVS', 542, 'altus', '', '', '5', 1), ('BONVS', 543, 'bonus', '', '', '5', 1), ('CVM/2', 544, 'cum', '', '', '5', 1), ('CVRA', 545, 'cura', '', '', '5', 1), ('DIVINVS/2', 546, 'divinus', '', '', '5', 1), ('IACTO', 547, 'iacto', '', '', '5', 1), ('LIBER/2', 548, 'liber', '', '', '5', 1), ('MAGNVS', 549, 'magnus', '', '', '5', 1), ('MALVS/3', 550, 'malus', '', '', '5', 1), ('MEVS', 551, 'meus', '', '', '5', 1), ('MVLTVS', 552, 'multus', '', '', '5', 1), ('NOSTER', 553, 'noster', '', '', '5', 1), ('PARVVS/2', 554, 'parvus', '', '', '5', 1), ('PVLCHER', 555, 'pulcher', '', '', '5', 1), ('SAPIENTIA', 556, 'sapientia', '', '', '5', 1), ('SAXVM', 557, 'saxum', '', '', '5', 1), ('SILVA', 558, 'silva', '', '', '5', 1), ('SVB', 559, 'sub', '', '', '5', 1), ('SVM/1', 560, 'sum', '', '', '5', 1), ('TERRA', 561, 'terra', '', '', '5', 1), ('TVVS', 562, 'tuus', '', '', '5', 1), ('VESTER', 563, 'vester', '', '', '5', 1), ('CENA', 564, 'cena', '', '', '6', 1), ('DE', 565, 'de', '', '', '6', 1), ('DIV', 566, 'diu', '', '', '6', 1), ('ENIM/2', 567, 'enim', '', '', '6', 1), ('EXEMPLVM', 568, 'exemplum', '', '', '6', 1), ('FILIA', 569, 'filia', '', '', '6', 1), ('FILIVS', 570, 'filius', '', '', '6', 1), ('INTRO/1', 571, 'intro', '', '', '6', 1), ('ITALIA/N', 572, 'Italia', '', '', '6', 1), ('LAETVS/2', 573, 'laetus', '', '', '6', 1), ('MANEO', 574, 'maneo', '', '', '6', 1), ('NOVVS', 575, 'novus', '', '', '6', 1), ('NVNTIO', 576, 'nuntio', '', '', '6', 1), ('PARO/2', 577, 'paro', '', '', '6', 1), ('PECVNIA', 578, 'pecunia', '', '', '6', 1), ('POPVLVS/1', 579, 'populus', '', '', '6', 1), ('PROPTER/2', 580, 'propter', '', '', '6', 1), ('REGINA', 581, 'regina', '', '', '6', 1), ('ROMANVS/A', 582, nan, '', '', '6', 2), ('ROMANVS/A', 583, 'Romanus', '', '', '6', 2), ('SEMPER', 584, 'semper', '', '', '6', 1), ('SINE', 585, 'sine', '', '', '6', 1), ('VITA', 586, 'vita', '', '', '6', 1), ('ARS', 587, 'ars', '', '', '7', 1), ('CAPVT', 588, 'caput', '', '', '7', 1), ('CIVITAS', 589, 'civitas', '', '', '7', 1), ('CONSVL', 590, 'consul', '', '', '7', 1), ('CORPVS', 591, 'corpus', '', '', '7', 1), ('DVX', 592, 'dux', '', '', '7', 1), ('FRATER', 593, 'frater', '', '', '7', 1), ('HOMO', 594, 'homo', '', '', '7', 1), ('IRA', 595, 'ira', '', '', '7', 1), ('MATER', 596, 'mater', '', '', '7', 1), ('MENS', 597, 'mens', '', '', '7', 1), ('MISER', 598, 'miser', '', '', '7', 1), ('MORS', 599, 'mors', '', '', '7', 1), ('NVMEN', 600, 'numen', '', '', '7', 1), ('PATER', 601, 'pater', '', '', '7', 1), ('REX', 602, 'rex', '', '', '7', 1), ('TENEO', 603, 'teneo', '', '', '7', 1), ('VERITAS', 604, 'veritas', '', '', '7', 1), ('VIRTVS', 605, 'virtus', '', '', '7', 1), ('VOX', 606, 'vox', '', '', '7', 1), ('VRBS', 607, 'urbs', '', '', '7', 1), ('VXOR', 608, 'uxor', '', '', '7', 1), ('CLARVS', 609, 'clarus', '', '', '8', 1), ('DOLEO', 610, 'doleo', '', '', '8', 1), ('IRATVS', 611, 'iratus', '', '', '8', 1), ('LEX', 612, 'lex', '', '', '8', 1), ('LIBERTAS', 613, 'libertas', '', '', '8', 1), ('LVNA', 614, 'luna', '', '', '8', 1), ('LVX', 615, 'lux', '', '', '8', 1), ('MONS', 616, 'mons', '', '', '8', 1), ('NOMEN', 617, 'nomen', '', '', '8', 1), ('OPVS/1', 618, 'opus', '', '', '8', 1), ('PARS', 619, 'pars', '', '', '8', 1), ('PATRIA', 620, 'patria', '', '', '8', 1), ('PAX', 621, 'pax', '', '', '8', 1), ('PERICVLVM', 622, 'periculum', '', '', '8', 1), ('PLENVS', 623, 'plenus', '', '', '8', 1), ('POSSVM/1', 624, 'possum', '', '', '8', 1), ('POST/2', 625, 'post', '', '', '8', 1), ('RATIO', 626, 'ratio', '', '', '8', 1), ('SACER', 627, 'sacer', '', '', '8', 1), ('STVDEO', 628, 'studeo', '', '', '8', 1), ('SVBITO', 629, 'subito', '', '', '8', 1), ('VERBVM', 630, 'verbum', '', '', '8', 1), ('AGO', 631, 'ago', '', '', '9', 1), ('AVT', 632, 'aut', '', '', '9', 1), ('CAPIO/2', 633, 'capio', '', '', '9', 1), ('CARMEN/1', 634, 'carmen', '', '', '9', 1), ('DICO/2', 635, 'dico', '', '', '9', 1), ('DISCO', 636, 'disco', '', '', '9', 1), ('DVCO', 637, 'duco', '', '', '9', 1), ('EGO', 638, 'ego', '', '', '9', 1), ('ET/1', 639, 'et', '', '', '9', 1), ('FACIO', 640, 'facio', '', '', '9', 1), ('INTER', 641, 'inter', '', '', '9', 1), ('MITTO', 642, 'mitto', '', '', '9', 1), ('NOS', 643, 'nos', '', '', '9', 1), ('OLIM', 644, 'olim', '', '', '9', 1), ('POETA', 645, 'poeta', '', '', '9', 1), ('QVIDAGIS', 646, 'quid', '', '', '9', 1), ('REGO', 647, 'rego', '', '', '9', 1), ('SCRIBO', 648, 'scribo', '', '', '9', 1), ('SEDEO', 649, 'sedeo', '', '', '9', 1), ('TV', 650, 'tu', '', '', '9', 1), ('VALE', 651, 'vale', '', '', '9', 1), ('VALEO', 652, 'valeo', '', '', '9', 1), ('VINCO', 653, 'vinco', '', '', '9', 1), ('VOS', 654, 'vos', '', '', '9', 1)]
section_list ={'1': '26', '26': 'start', '10': '1', '11': '10', '12': '11', '13': '12', '14': '13', '15': '14', '16': '15', '17': '16', '18': '17', '19': '18', '2': '19', '20': '2', '21': '20', '22': '21', '23': '22', '24': '23', '25': '24', '27': '25', '28': '27', '29': '28', '3': '29', '30': '3', '31': '30', '32': '31', '4': '32', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', 'end': '9', 'start': 'start'}
title = "Introduction to Latin (Shelmerdine)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)