import text
nan=""
section_words = {'start': -1, '3.5': 505, '4.12': 535, '1.25': 538, '1.7': 510, '1.15': 484, '2.15': 15, '1.16': 533, '4.22': 414, '4.19': 478, '1.23': 407, '4.35': 556, '2.1': 296, '4.5': 278, '1.10': 511, '4.21': 392, '2.9': 539, '4.27': 551, '4.24': 466, '1.32': 437, '1.41': 482, '4.25': 421, '4.23': 225, '2.45': 329, '2.35': 251, '4.10': 491, '1.8': 543, '2.41': 351, '1.4': 393, '1.29': 396, '2.20': 428, '4.16': 324, '2.11': 476, '4.1': 496, '2.21': 353, '3.8': 348, '3.9': 458, '2.22': 524, '2.19': 449, '2.32': 489, '2.43': 487, '2.31': 549, '1.40': 547, '1.39': 462, '1.26': 404, '2.29': 157, '2.12': 380, '1.22': 527, '2.6': 244, '2.5': 357, '4.30': 499, '1.24': 308, '1.6': 509, '1.31': 513, '2.42': 486, '4.9': 500, '2.3': 502, '1.2': 494, '3.3': 438, '1.37': 447, '1.11': 420, '1.33': 365, '1.30': 545, '3.11': 529, '1.12': 532, '3.1': 460, '3.2': 474, '1.1': 454, '1.9': 315, '4.11': 222, '1.18': 530, '1.27': 542, '2.4': 303, '4.33': 316, '4.34': 552, '1.17': 548, '4.15': 544, '2.40': 333, '3.7': 343, '4.14': 408, '1.5': 394, '4.2': 534, '2.18': 555, '2.24': 206, '2.28': 383, '4.37': 259, '2.14': 311, '2.16': 424, '1.3': 205, '3.10': 410, '3.12': 475, '1.21': 465, '1.34': 451, '2.10': 431, '4.26': 540, '4.32': 495, '1.20': 501, '2.7': 531, '4.8': 471, '4.17': 504, '3.4': 488, '4.13': 442, '1.13': 519, '4.4': 455, '1.38': 464, '2.36': 422, '1.35': 515, '4.7': 537, '1.14': 558, '1.19': 550, '2.33': 384, '2.26': 319, '2.27': 363, '4.36': 557, '4.3': 507, '4.6': 525, '2.38': 526, '4.31': 518, '4.18': 546, '1.36': 477, '2.23': 521, '4.20': 372, '2.13': 485, '4.28': 541, '2.39': 398, '4.29': 559, '1.28': 522, '2.25': 554, '2.37': 456, '2.34': 553, '3.6': 440, '2.30': 473, '2.44': 560, '2.8': 483, '2.17': 498, '2.2': 536, 'end': -2}
the_text =  [('AB', 0, 'AB', '', '', '3_5', 1), ('ACCENDO', 1, 'ACCENDERE', '', '', '4_12', 1), ('ACERBVS', 2, 'ACERBUS', '', '', '1_25', 1), ('ACHILLES/N', 3, 'ACHILLES', '', '', '1_7', 1), ('ADMITTO', 4, 'ADMITTERE', '', '', '1_15', 1), ('ADMODVLOR', 5, 'ADMODULARI', '', '', '2_15', 1), ('ADONIS/N', 6, 'ADONIS', '', '', '1_16', 1), ('ASSIDVVS', 7, 'ADSIDUUS', '', '', '4_22', 1), ('AESCVLVS', 8, 'AESCULUS', '', '', '4_19', 1), ('AESTVO', 9, 'AESTUARE', '', '', '1_23', 1), ('AETHERIVS', 10, 'AETHERIUS', '', '', '4_35', 1), ('AGO', 11, 'AGERE', '', '', '2_1', 1), ('AGGREDIOR', 12, 'AGGREDI', '', '', '4_5', 1), ('ALO', 13, 'ALERE', '', '', '1_10', 2), ('ALO', 14, 'ALES', '', '', '4_21', 2), ('ALNVS', 15, 'ALNUS', '', '', '2_15', 1), ('ALPINVS/A', 16, 'ALPINUS', '', '', '2_9', 1), ('ALTER', 17, 'ALTER', '', '', '4_27', 1), ('ALTERNVS', 18, 'ALTERNUS', '', '', '4_24', 1), ('AMAZON/N', 19, 'AMAZON', '', '', '1_32', 1), ('AMOR', 20, 'AMOR', '', '', '1_41', 1), ('AMPLEXVS', 21, 'AMPLEXUS', '', '', '4_25', 1), ('ANCEPS/2', 22, 'ANCEPS', '', '', '1_23', 1), ('ANHELITVS', 23, 'ANHELITUS', '', '', '4_24', 1), ('ANIMVS', 24, 'ANIMUS', '', '', '4_23', 1), ('ANNVS', 25, 'ANNUS', '', '', '2_45', 1), ('ANTRVM', 26, 'ANTRUM', '', '', '2_35', 1), ('APEX', 27, 'APEX', '', '', '2_9', 1), ('APIS', 28, 'APIS', '', '', '4_10', 1), ('APOLLO/N', 29, 'APOLLO', '', '', '1_8', 1), ('AQVILONIVS/A', 30, 'AQUILONIUS', '', '', '2_41', 1), ('ARDVVS', 31, 'ARDUUS', '', '', '1_4', 1), ('ARMO', 32, 'ARMARE', '', '', '4_10', 1), ('ARRIPIO', 33, 'ARRIPERE', '', '', '1_29', 1), ('ARX', 34, 'ARX', '', '', '2_20', 1), ('ASPIRO', 35, 'ASPIRARE', '', '', '4_16', 1), ('ATHESIS/N', 36, 'ATHESIS', '', '', '2_11', 1), ('ATTOLLO', 37, 'ATTOLLERE', '', '', '4_1', 1), ('AVDIO', 38, 'AUDIRE', '', '', '2_21', 1), ('AVGVSTVS/N', 39, 'AUGUSTUS', '', '', '3_8', 2), ('AVGVSTVS/N', 40, 'AUGUSTUS', '', '', '3_9', 2), ('AVLA/1', 41, 'AULA', '', '', '2_22', 2), ('AVLA/1', 42, 'AULA', '', '', '3_5', 2), ('AVREVS/2', 43, 'AUREUS', '', '', '2_19', 1), ('AVRVM', 44, 'AURUM', '', '', '2_32', 1), ('AVSTER', 45, 'AUSTER', '', '', '2_43', 1), ('AXIS', 46, 'AXIS', '', '', '4_35', 1), ('BAETIS/N', 47, 'BAETIS', '', '', '2_31', 1), ('BEATVS', 48, 'BEATUS', '', '', '1_40', 1), ('BELLVM', 49, 'BELLUM', '', '', '1_39', 1), ('BELVA', 50, 'BELUA', '', '', '1_26', 1), ('BLANDVS', 51, 'BLANDUS', '', '', '4_21', 1), ('CAESAREVS/A', 52, 'CAESAREUS', '', '', '2_29', 1), ('CALAMVS', 53, 'CALAMUS', '', '', '2_12', 1), ('CALEO', 54, 'CALERE', '', '', '4_25', 1), ('CALOR', 55, 'CALOR', '', '', '1_22', 1), ('CAMPVS/1', 56, 'CAMPUS', '', '', '2_6', 1), ('CANO', 57, 'CANERE', '', '', '2_5', 1), ('CARMEN/1', 58, 'CARMEN', '', '', '4_30', 1), ('CARPO', 59, 'CARPERE', '', '', '1_24', 1), ('CASTOR/N', 60, 'CASTOR', '', '', '1_6', 1), ('CATENA', 61, 'CATENA', '', '', '1_29', 1), ('CAVCASVS/N', 62, 'CAUCASUS', '', '', '1_31', 1), ('CAVRVS/N', 63, 'CAURUS', '', '', '2_42', 1), ('CAVEO', 64, 'CAUERE', '', '', '4_9', 1), ('CELEBRO', 65, 'CELEBRARE', '', '', '2_3', 1), ('CERTVS', 66, 'CERTUS', '', '', '1_2', 1), ('CESSO', 67, 'CESSARE', '', '', '3_3', 2), ('CESSO', 68, 'CESSARE', '', '', '4_5', 2), ('CHOREA', 69, 'CHOREA', '', '', '2_11', 1), ('CINGVLVM', 70, 'CINGULUM', '', '', '1_37', 1), ('CITO/1', 71, 'CITARE', '', '', '1_11', 1), ('COHORS', 72, 'COHORS', '', '', '1_33', 1), ('COLLVM', 73, 'COLLUM', '', '', '1_30', 1), ('COLOR', 74, 'COLOR', '', '', '3_11', 1), ('COMA', 75, 'COMA', '', '', '1_12', 2), ('COMA', 76, 'COMA', '', '', '3_1', 2), ('COMMINVS', 77, 'COMMINUS', '', '', '4_5', 1), ('CONCILIO', 78, 'CONCILIARE', '', '', '4_23', 1), ('CONFICIO', 79, 'CONFICERE', '', '', '1_39', 1), ('COR', 80, 'COR', '', '', '1_26', 1), ('CORNIPES/2', 81, 'CORNIPES', '', '', '1_11', 1), ('CORONA', 82, 'CORONA', '', '', '3_2', 1), ('CORONO', 83, 'CORONARE', '', '', '2_20', 1), ('CORVSCVS', 84, 'CORUSCUS', '', '', '1_1', 1), ('CREDO', 85, 'CREDERE', '', '', '1_9', 1), ('CRESCO', 86, 'CRESCERE', '', '', '4_11', 1), ('CRVOR', 87, 'CRUOR', '', '', '4_27', 1), ('CVM/3', 88, 'CUM', '', '', '1_10', 3), ('CVM/3', 89, 'CUM', '', '', '1_18', 3), ('CVM/3', 90, 'CUM', '', '', '1_27', 3), ('CVM/2', 91, 'CUM', '', '', '2_4', 3), ('CVM/2', 92, 'CUM', '', '', '4_33', 3), ('CVM/2', 93, 'CUM', '', '', '4_34', 3), ('CVNCTVS', 94, 'CUNCTUS', '', '', '2_1', 1), ('CYNTHIA/N', 95, 'CYNTHIA', '', '', '1_17', 1), ('DAMNO', 96, 'DAMNARE', '', '', '1_17', 1), ('DO', 97, 'DARE', '', '', '1_6', 2), ('DO', 98, 'DARE', '', '', '3_11', 2), ('DECEM', 99, 'DECIENS', '', '', '4_15', 1), ('DECOR', 100, 'DECOR', '', '', '1_39', 1), ('DECORO', 101, 'DECORARE', '', '', '2_31', 1), ('DEFICIO', 102, 'DEFICERE', '', '', '2_40', 1), ('DELOS/N', 103, 'DELOS', '', '', '1_8', 1), ('DESERO/2', 104, 'DESERERE', '', '', '1_33', 1), ('DEXTER', 105, 'DEXTER', '', '', '3_7', 1), ('DICO/2', 106, 'DICERE', '', '', '4_14', 1), ('DIFFICILIS', 107, 'DIFFICILIS', '', '', '4_11', 1), ('DIGNVS', 108, 'DIGNUS', '', '', '1_4', 2), ('DIGNVS', 109, 'DIGNUS', '', '', '1_5', 2), ('DILIGO/3', 110, 'DILIGERE', '', '', '4_2', 1), ('DOMINVS', 111, 'DOMINUS', '', '', '2_18', 1), ('DOMVS', 112, 'DOMUS', '', '', '2_24', 1), ('DRYAS', 113, 'DRYAS', '', '', '1_22', 1), ('DVCO', 114, 'DUCERE', '', '', '2_28', 3), ('DVCO', 115, 'DUCERE', '', '', '4_30', 3), ('DVCO', 116, 'DUCERE', '', '', '4_37', 3), ('DVLCIS', 117, 'DULCIS', '', '', '4_14', 1), ('DVX', 118, 'DUX', '', '', '4_33', 1), ('EGO', 119, 'EGO', '', '', '4_14', 1), ('ELECTRIFER', 120, 'ELECTRIFER', '', '', '2_14', 1), ('EPVLAE', 121, 'EPULAE', '', '', '2_16', 1), ('EQVES', 122, 'EQUES', '', '', '1_3', 1), ('HERILIS', 123, 'ERILIS', '', '', '2_3', 1), ('SVM/1', 124, 'ESSE', '', '', '1_4', 6), ('SVM/1', 125, 'ESSE', '', '', '1_5', 6), ('SVM/1', 126, 'ESSE', '', '', '3_8', 6), ('SVM/1', 127, 'ESSE', '', '', '3_9', 6), ('SVM/1', 128, 'ESSE', '', '', '3_10', 6), ('SVM/1', 129, 'ESSE', '', '', '3_12', 6), ('ET/2', 130, 'ET', '', '', '1_21', 8), ('ET/2', 131, 'ET', '', '', '1_34', 8), ('ET/2', 132, 'ET', '', '', '1_37', 8), ('ET/2', 133, 'ET', '', '', '2_10', 8), ('ET/2', 134, 'ET', '', '', '2_14', 8), ('ET/2', 135, 'ET', '', '', '4_21', 8), ('ET/2', 136, 'ET', '', '', '4_23', 8), ('ET/2', 137, 'ET', '', '', '4_26', 8), ('EXSVLTO', 138, 'EXULTARE', '', '', '4_32', 1), ('FACIO', 139, 'FACERE', '', '', '1_40', 1), ('FALLO', 140, 'FALLERE', '', '', '1_20', 1), ('FATEOR', 141, 'FATERI', '', '', '1_8', 1), ('FAVEO', 142, 'FAUERE', '', '', '2_6', 2), ('FAVEO', 143, 'FAUERE', '', '', '2_7', 2), ('FAVVS', 144, 'FAUUS', '', '', '4_8', 1), ('FAX', 145, 'FAX', '', '', '4_17', 1), ('FELIX', 146, 'FELIX', '', '', '3_4', 1), ('FERO', 147, 'FERRE', '', '', '4_13', 1), ('FERVS/2', 148, 'FERUS', '', '', '1_13', 1), ('FESSVS', 149, 'FESSUS', '', '', '1_21', 1), ('FETVS/2', 150, 'FETUS', '', '', '2_24', 1), ('FIDES/2', 151, 'FIDES', '', '', '4_16', 1), ('FLAMMEVS', 152, 'FLAMMEUS', '', '', '4_4', 1), ('FLAVVS', 153, 'FLAUUS', '', '', '4_15', 1), ('FLEO', 154, 'FLERE', '', '', '4_13', 1), ('FLEXVOSVS', 155, 'FLEXUOSUS', '', '', '2_12', 1), ('FLVO', 156, 'FLUERE', '', '', '2_22', 1), ('FLVMINEVS', 157, 'FLUMINEUS', '', '', '2_29', 1), ('FLVVIVS', 158, 'FLUUIUS', '', '', '2_4', 1), ('FORMA', 159, 'FORMA', '', '', '1_5', 1), ('FORMOSVS', 160, 'FORMOSUS', '', '', '4_37', 1), ('FORTIS', 161, 'FORTIS', '', '', '1_38', 1), ('FRATER', 162, 'FRATER', '', '', '2_36', 1), ('FREMO', 163, 'FREMERE', '', '', '1_35', 1), ('FRONDEO', 164, 'FRONDERE', '', '', '4_19', 1), ('FRONS/1', 165, 'FRONS', '', '', '4_9', 1), ('FRVOR', 166, 'FRUI', '', '', '4_7', 1), ('FVLGEO', 167, 'FULGERE', '', '', '3_1', 1), ('FVLGIDVS', 168, 'FULGIDUS', '', '', '4_26', 1), ('FVRO', 169, 'FURERE', '', '', '1_26', 1), ('FVRTIVVS', 170, 'FURTIUUS', '', '', '1_24', 1), ('GALEA', 171, 'GALEA', '', '', '3_1', 1), ('GAVDEO', 172, 'GAUDERE', '', '', '1_14', 1), ('GAVDIVM', 173, 'GAUDIUM', '', '', '4_11', 1), ('GELIDVS', 174, 'GELIDUS', '', '', '1_19', 1), ('GELONVS/N', 175, 'GELONUS', '', '', '1_3', 1), ('GEMINVS', 176, 'GEMINUS', '', '', '2_28', 1), ('GENER', 177, 'GENER', '', '', '2_33', 2), ('GENER', 178, 'GENER', '', '', '3_8', 2), ('GRADVS', 179, 'GRADUS', '', '', '1_23', 1), ('HABEO', 180, 'HABERE', '', '', '2_26', 2), ('HABEO', 181, 'HABERE', '', '', '2_27', 2), ('HASTA', 182, 'HASTA', '', '', '1_15', 1), ('HEDERA', 183, 'HEDERA', '', '', '4_19', 1), ('HERCVLES/N', 184, 'HERCULES', '', '', '1_38', 1), ('HESPERVS/N', 185, 'HESPERUS', '', '', '4_2', 1), ('HIBERVS/A', 186, 'HIBERUS', '', '', '2_21', 1), ('HIC/1', 187, 'HIC', '', '', '4_14', 3), ('HIC/1', 188, 'HIC', '', '', '4_35', 3), ('HIC/1', 189, 'HIC', '', '', '4_36', 3), ('HINC', 190, 'HINC', '', '', '2_26', 2), ('HINC', 191, 'HINC', '', '', '2_27', 2), ('HIPPOLYTVS/N', 192, 'HIPPOLYTE', '', '', '1_35', 1), ('HONORIVS/N', 193, 'HONORIUS', '', '', '4_37', 1), ('HORRIDVS', 194, 'HORRIDUS', '', '', '1_25', 1), ('HYBLAEVS/A', 195, 'HYBLAEUS', '', '', '4_8', 1), ('IACEO', 196, 'IACERE', '', '', '1_13', 1), ('IAM', 197, 'IAM', '', '', '2_16', 4), ('IAM', 198, 'IAM', '', '', '3_10', 4), ('IAM', 199, 'IAM', '', '', '4_3', 4), ('IAM', 200, 'IAM', '', '', '4_4', 4), ('IDALIVS/A', 201, 'IDALIUS', '', '', '4_1', 1), ('IGNEVS', 202, 'IGNEUS', '', '', '1_5', 1), ('ILEX', 203, 'ILEX', '', '', '1_10', 1), ('IMPACATVS', 204, 'IMPACATUS', '', '', '4_6', 1), ('IMPERIOSVS', 205, 'IMPERIOSUS', '', '', '1_3', 1), ('IMPERIVM', 206, 'IMPERIUM', '', '', '2_24', 1), ('IMPIGER', 207, 'IMPIGER', '', '', '1_10', 1), ('IN', 208, 'IN', '', '', '3_5', 1), ('IMMEMOR', 209, 'INMEMOR', '', '', '1_34', 1), ('INSONO/1', 210, 'INSONARE', '', '', '4_35', 1), ('INSTABILIS', 211, 'INSTABILIS', '', '', '1_12', 1), ('INTER', 212, 'INTER', '', '', '1_35', 1), ('INTVMESCO', 213, 'INTUMESCERE', '', '', '2_32', 1), ('INVIDIA', 214, 'INUIDIA', '', '', '3_11', 1), ('IOCOR', 215, 'IOCARI', '', '', '2_38', 1), ('IOCVS', 216, 'IOCUS', '', '', '4_31', 1), ('IVBAR', 217, 'IUBAR', '', '', '4_1', 1), ('IVGVM', 218, 'IUGUM', '', '', '1_31', 1), ('IVNGO', 219, 'IUNGERE', '', '', '1_41', 3), ('IVNGO', 220, 'IUNGERE', '', '', '3_7', 3), ('IVNGO', 221, 'IUNGERE', '', '', '4_18', 3), ('IVRGIVM', 222, 'IURGIUM', '', '', '4_11', 1), ('IVVENIS/2', 223, 'IUUENIS', '', '', '4_5', 1), ('LABOR/1', 224, 'LABOR', '', '', '1_18', 1), ('LABRVM/1', 225, 'LABRUM', '', '', '4_23', 1), ('LACRIMA', 226, 'LACRIMAE', '', '', '4_4', 1), ('LAETVS/2', 227, 'LAETUS', '', '', '2_18', 1), ('LANGVIDVS', 228, 'LANGUIDUS', '', '', '1_36', 1), ('LATEBRA', 229, 'LATEBRA', '', '', '4_8', 1), ('LAVREA', 230, 'LAUREA', '', '', '2_23', 1), ('LAVS', 231, 'LAUS', '', '', '1_4', 2), ('LAVS', 232, 'LAUS', '', '', '1_5', 2), ('LEDA/N', 233, 'LEDA', '', '', '1_6', 1), ('LENTVS', 234, 'LENTUS', '', '', '4_20', 1), ('LEO', 235, 'LEO', '', '', '1_14', 1), ('LEVIS/1', 236, 'LEUIS', '', '', '2_13', 1), ('LEX', 237, 'LEX', '', '', '4_32', 1), ('LIBENS', 238, 'LIBENS', '', '', '1_29', 1), ('LIBER/2', 239, 'LIBER', '', '', '1_30', 2), ('LIBER/2', 240, 'LIBER', '', '', '4_32', 2), ('LIBER/N', 241, 'LIBER', '', '', '1_9', 1), ('LICEO', 242, 'LICERE', '', '', '4_6', 2), ('LICEO', 243, 'LICERE', '', '', '4_31', 2), ('LIGVR/A', 244, 'LIGUS', '', '', '2_6', 1), ('LINGVA', 245, 'LINGUA', '', '', '4_22', 1), ('LITVVS', 246, 'LITUUS', '', '', '3_3', 1), ('LIVOR', 247, 'LIUOR', '', '', '3_10', 1), ('LVDO', 248, 'LUDERE', '', '', '1_12', 3), ('LVDO', 249, 'LUDERE', '', '', '4_33', 3), ('LVDO', 250, 'LUDERE', '', '', '4_34', 3), ('LVXVRIO', 251, 'LUXURIARE', '', '', '2_35', 1), ('LYDIA/N', 252, 'LYDIA', '', '', '1_9', 1), ('MADIDVS', 253, 'MADIDUS', '', '', '4_28', 1), ('MAGIS/2', 254, 'MAGIS', '', '', '4_12', 1), ('MALO', 255, 'MALLE', '', '', '1_6', 1), ('MANEO', 256, 'MANERE', '', '', '4_17', 1), ('MANVS/1', 257, 'MANUS', '', '', '4_18', 1), ('MARE', 258, 'MARE', '', '', '4_36', 1), ('MARIA/N', 259, 'MARIA', '', '', '4_37', 1), ('MARITVS/2', 260, 'MARITUS', '', '', '2_26', 1), ('MARS/N', 261, 'MARS', '', '', '3_4', 1), ('MATER', 262, 'MATER', '', '', '2_27', 1), ('MEL', 263, 'MEL', '', '', '4_10', 1), ('MEMBRVM', 264, 'MEMBRUM', '', '', '1_21', 1), ('MENS', 265, 'MENS', '', '', '1_4', 1), ('MICO', 266, 'MICARE', '', '', '1_27', 1), ('MILES', 267, 'MILES', '', '', '4_33', 1), ('MINCIVS/N', 268, 'MINCIUS', '', '', '2_13', 1), ('MOLLIS', 269, 'MOLLIS', '', '', '3_2', 1), ('MONS', 270, 'MONS', '', '', '2_7', 1), ('MORS', 271, 'MORS', '', '', '1_15', 1), ('MOX', 272, 'MOX', '', '', '1_40', 1), ('MVLTVS', 273, 'MULTUS', '', '', '4_13', 1), ('MVRMVR', 274, 'MURMUR', '', '', '4_21', 1), ('MVTVVS', 275, 'MUTUUS', '', '', '4_22', 1), ('NAIAS', 276, 'NAIS', '', '', '1_24', 1), ('NASCOR', 277, 'NASCI', '', '', '4_2', 1), ('NE/4', 278, 'NE', '', '', '4_5', 1), ('NEQVE', 279, 'NEQUE', '', '', '4_8', 1), ('NECTO', 280, 'NECTERE', '', '', '3_2', 2), ('NECTO', 281, 'NECTERE', '', '', '4_18', 2), ('NEGO', 282, 'NEGARE', '', '', '1_38', 1), ('NEMVS', 283, 'NEMUS', '', '', '2_4', 1), ('NITEO', 284, 'NITERE', '', '', '2_39', 1), ('NIVALIS', 285, 'NIUALIS', '', '', '1_31', 1), ('NOBILITO', 286, 'NOBILITARE', '', '', '4_27', 1), ('NOCTVRNVS', 287, 'NOCTURNUS', '', '', '4_29', 1), ('NON', 288, 'NON', '', '', '1_28', 3), ('NON', 289, 'NON', '', '', '1_29', 3), ('NON', 290, 'NON', '', '', '4_7', 3), ('NOVVS', 291, 'NOUUS', '', '', '2_39', 2), ('NOVVS', 292, 'NOUUS', '', '', '4_16', 2), ('NVBO', 293, 'NUBERE', '', '', '4_3', 1), ('NVMERO/1', 294, 'NUMERARE', '', '', '2_25', 1), ('NVNC', 295, 'NUNC', '', '', '3_9', 1), ('NVPTIALIS', 296, 'NUPTIALIS', '', '', '2_1', 1), ('O', 297, 'O', '', '', '1_22', 2), ('O', 298, 'O', '', '', '4_14', 2), ('OCCIDENS', 299, 'OCCIDENS', '', '', '2_37', 1), ('OCEANVS/N', 300, 'OCEANUS', '', '', '2_34', 1), ('ODOR', 301, 'ODOR', '', '', '4_7', 1), ('OFFICIVM', 302, 'OFFICIUM', '', '', '3_6', 1), ('OMNIS', 303, 'OMNIS', '', '', '2_4', 2), ('OMNIS', 304, 'OMNIS', '', '', '2_5', 2), ('OPTO', 305, 'OPTARE', '', '', '1_28', 1), ('ORIOR', 306, 'ORIRI', '', '', '2_36', 1), ('ORTVS', 307, 'ORTUS', '', '', '2_30', 1), ('OSCVLVM', 308, 'OSCULUM', '', '', '1_24', 2), ('OSCVLVM', 309, 'OSCULUM', '', '', '4_13', 2), ('OVO', 310, 'OUANS', '', '', '2_44', 1), ('PADVS/N', 311, 'PADUS', '', '', '2_14', 1), ('PALMES', 312, 'PALMES', '', '', '4_20', 1), ('PARS', 313, 'PARS', '', '', '2_28', 1), ('PARTHVS/A', 314, 'PARTHUS', '', '', '1_2', 1), ('PARVVS/2', 315, 'PARUUS', '', '', '1_9', 1), ('PASSIM', 316, 'PASSIM', '', '', '4_33', 2), ('PASSIM', 317, 'PASSIM', '', '', '4_34', 2), ('PATER', 318, 'PATER', '', '', '1_34', 4), ('PATER', 319, 'PATER', '', '', '2_26', 4), ('PATER', 320, 'PATER', '', '', '3_6', 4), ('PATER', 321, 'PATER', '', '', '3_12', 4), ('PATIOR', 322, 'PATI', '', '', '1_28', 1), ('PECTVS', 323, 'PECTUS', '', '', '1_37', 2), ('PECTVS', 324, 'PECTUS', '', '', '4_16', 2), ('PELTATVS', 325, 'PELTATUS', '', '', '1_33', 1), ('PER', 326, 'PER', '', '', '1_10', 3), ('PER', 327, 'PER', '', '', '1_31', 3), ('PER', 328, 'PER', '', '', '4_36', 3), ('PERDOMINOR', 329, 'PERDOMINARI', '', '', '2_45', 1), ('PERMITTO', 330, 'PERMITTERE', '', '', '4_31', 1), ('PERVIGIL', 331, 'PERUIGIL', '', '', '4_30', 1), ('PETO', 332, 'PETERE', '', '', '1_32', 1), ('PHOEBVS/N', 333, 'PHOEBUS', '', '', '2_40', 1), ('PIGNVS', 334, 'PIGNUS', '', '', '3_7', 1), ('PLACIDVS', 335, 'PLACIDUS', '', '', '2_38', 1), ('PLATANVS', 336, 'PLATANUS', '', '', '1_18', 1), ('PLAVDO', 337, 'PLAUDERE', '', '', '2_37', 1), ('PLENVS', 338, 'PLENUS', '', '', '2_23', 1), ('PONO', 339, 'PONERE', '', '', '1_36', 1), ('POPVLVS/1', 340, 'POPULUS', '', '', '4_20', 2), ('POPVLVS/1', 341, 'POPULUS', '', '', '4_36', 2), ('POSCO', 342, 'POSCERE', '', '', '1_30', 1), ('POSSVM/1', 343, 'POSSE', '', '', '3_7', 1), ('POST/2', 344, 'POST', '', '', '1_18', 1), ('PRAEDO', 345, 'PRAEDO', '', '', '1_11', 1), ('PRAEFERO', 346, 'PRAEFERRE', '', '', '1_7', 1), ('PREMO', 347, 'PREMERE', '', '', '4_20', 1), ('PRIDEM', 348, 'PRIDEM', '', '', '3_8', 1), ('PRINCEPS/1', 349, 'PRINCEPS', '', '', '1_1', 1), ('PRIOR', 350, 'PRIOR', '', '', '1_41', 1), ('PROCELLA', 351, 'PROCELLA', '', '', '2_41', 1), ('PROCREATOR', 352, 'PROCREATOR', '', '', '2_33', 1), ('PROCVL', 353, 'PROCUL', '', '', '2_21', 2), ('PROCVL', 354, 'PROCUL', '', '', '3_3', 2), ('PRODO', 355, 'PRODERE', '', '', '4_4', 1), ('PROELIVM', 356, 'PROELIUM', '', '', '4_29', 1), ('PROFVNDVS', 357, 'PROFUNDUS', '', '', '2_5', 1), ('PROPE/2', 358, 'PROPE', '', '', '1_27', 1), ('PROPRIVS', 359, 'PROPRIUS', '', '', '1_7', 1), ('PROSILIO', 360, 'PROSILIRE', '', '', '4_28', 1), ('PRVINA', 361, 'PRUINA', '', '', '2_10', 1), ('PVDOR', 362, 'PUDOR', '', '', '4_3', 1), ('PVELLA', 363, 'PUELLA', '', '', '2_27', 1), ('PVER', 364, 'PUER', '', '', '4_34', 1), ('PVGNA', 365, 'PUGNA', '', '', '1_33', 1), ('PVLCHER', 366, 'PULCHER', '', '', '1_1', 2), ('PVLCHER', 367, 'PULCHER', '', '', '1_32', 2), ('PVRPVRA', 368, 'PURPURA', '', '', '4_25', 1), ('QVAM/1', 369, 'QUAM', '', '', '1_6', 4), ('QVAM/1', 370, 'QUAM', '', '', '4_15', 4), ('QVAM/1', 371, 'QUAM', '', '', '4_19', 4), ('QVAM/1', 372, 'QUAM', '', '', '4_20', 4), ('QVANTVS/1', 373, 'QUANTUS', '', '', '1_22', 1), ('QVE', 374, 'QUE', '', '', '1_12', 18), ('QVE', 375, 'QUE', '', '', '1_14', 18), ('QVE', 376, 'QUE', '', '', '1_30', 18), ('QVE', 377, 'QUE', '', '', '1_39', 18), ('QVE', 378, 'QUE', '', '', '1_41', 18), ('QVE', 379, 'QUE', '', '', '2_8', 18), ('QVE', 380, 'QUE', '', '', '2_12', 18), ('QVE', 381, 'QUE', '', '', '2_16', 18), ('QVE', 382, 'QUE', '', '', '2_18', 18), ('QVE', 383, 'QUE', '', '', '2_28', 18), ('QVE', 384, 'QUE', '', '', '2_33', 18), ('QVE', 385, 'QUE', '', '', '2_36', 18), ('QVE', 386, 'QUE', '', '', '2_37', 18), ('QVE', 387, 'QUE', '', '', '2_39', 18), ('QVE', 388, 'QUE', '', '', '3_3', 18), ('QVE', 389, 'QUE', '', '', '4_12', 18), ('QVE', 390, 'QUE', '', '', '4_17', 18), ('QVE', 391, 'QUE', '', '', '4_31', 18), ('QVERVLVS', 392, 'QUERULUS', '', '', '4_21', 1), ('QVI/1', 393, 'QUI', '', '', '1_4', 9), ('QVI/1', 394, 'QUI', '', '', '1_5', 9), ('QVI/1', 395, 'QUI', '', '', '1_27', 9), ('QVI/1', 396, 'QUI', '', '', '1_29', 9), ('QVI/1', 397, 'QUI', '', '', '1_40', 9), ('QVI/1', 398, 'QUI', '', '', '2_39', 9), ('QVI/1', 399, 'QUI', '', '', '3_10', 9), ('QVI/1', 400, 'QUI', '', '', '4_12', 9), ('QVI/1', 401, 'QUI', '', '', '4_13', 9), ('QVIRITES/N', 402, 'QUIRITES', '', '', '2_17', 1), ('QVIS/1', 403, 'QUIS', '', '', '1_25', 3), ('QVIS/1', 404, 'QUIS', '', '', '1_26', 3), ('QVIS/1', 405, 'QUIS', '', '', '3_11', 3), ('QVISQVAM', 406, 'QUISQUAM', '', '', '4_7', 1), ('QVOT/1', 407, 'QUOT', '', '', '1_23', 1), ('QVOTIENS/2', 408, 'QUOTIENS', '', '', '4_14', 1), ('RABIDVS', 409, 'RABIDUS', '', '', '2_42', 1), ('RABIES', 410, 'RABIES', '', '', '3_10', 1), ('RAPIO', 411, 'RAPERE', '', '', '4_24', 1), ('RECIPIO', 412, 'RECIPERE', '', '', '1_34', 1), ('RECVRRO', 413, 'RECURRERE', '', '', '2_30', 1), ('REDDO', 414, 'REDDERE', '', '', '4_22', 1), ('REDIMO', 415, 'REDIMERE', '', '', '2_2', 1), ('REDEO/1', 416, 'REDIRE', '', '', '3_6', 1), ('REDVCO', 417, 'REDUCERE', '', '', '1_17', 1), ('REFERO', 418, 'REFERRE', '', '', '4_29', 1), ('REFVGIO', 419, 'REFUGERE', '', '', '4_12', 1), ('REGO', 420, 'REGERE', '', '', '1_11', 1), ('REGIVS', 421, 'REGIUS', '', '', '4_25', 1), ('REGNVM', 422, 'REGNUM', '', '', '2_36', 1), ('RELEGO/1', 423, 'RELEGARE', '', '', '3_4', 1), ('REPLEO', 424, 'REPLERE', '', '', '2_16', 1), ('RESOLVO', 425, 'RESOLUERE', '', '', '1_21', 1), ('RESONO/1', 426, 'RESONARE', '', '', '2_17', 1), ('REVERTO', 427, 'REUERTI', '', '', '1_16', 1), ('ROMA/N', 428, 'ROMA', '', '', '2_20', 1), ('ROSA', 429, 'ROSA', '', '', '4_10', 1), ('ROSETVM', 430, 'ROSETUM', '', '', '2_8', 1), ('RVBEO', 431, 'RUBERE', '', '', '2_10', 1), ('RVBVS', 432, 'RUBI', '', '', '4_9', 1), ('RVRSVS', 433, 'RURSUM', '', '', '3_5', 2), ('RVRSVS', 434, 'RURSUM', '', '', '3_9', 2), ('SACER', 435, 'SACER', '', '', '1_14', 1), ('SAEVIO', 436, 'SAEUIRE', '', '', '4_6', 1), ('SAEVVS', 437, 'SAEUUS', '', '', '1_32', 2), ('SAEVVS', 438, 'SAEUUS', '', '', '3_3', 2), ('SAGITTA', 439, 'SAGITTA', '', '', '1_2', 1), ('SANGVIS', 440, 'SANGUIS', '', '', '3_6', 2), ('SANGVIS', 441, 'SANGUIS', '', '', '4_26', 2), ('SAPIO', 442, 'SAPERE', '', '', '4_13', 1), ('SARMATA/N', 443, 'SARMATA', '', '', '4_15', 1), ('SCYTHES/A', 444, 'SCYTHA', '', '', '1_25', 1), ('SECVRIS', 445, 'SECURIS', '', '', '1_36', 1), ('SEMEN/1', 446, 'SEMEN', '', '', '2_22', 1), ('SEMINVDVS', 447, 'SEMINUDUS', '', '', '1_37', 1), ('SENSVS', 448, 'SENSUS', '', '', '4_17', 1), ('SEPTEMGEMINVS', 449, 'SEPTEMGEMINUS', '', '', '2_19', 1), ('SERVITIVM', 450, 'SERUITIUM', '', '', '1_28', 1), ('SEXVS', 451, 'SEXUS', '', '', '1_34', 1), ('SI/2', 452, 'SI', '', '', '1_31', 2), ('SI/2', 453, 'SI', '', '', '4_9', 2), ('SIDVS', 454, 'SIDUS', '', '', '1_1', 1), ('SIMPLEX', 455, 'SIMPLEX', '', '', '4_4', 1), ('SIMVL/1', 456, 'SIMUL', '', '', '2_37', 1), ('SIRIVS/N', 457, 'SIRIUS', '', '', '1_20', 1), ('SOCER', 458, 'SOCER', '', '', '3_9', 2), ('SOCER', 459, 'SOCER', '', '', '3_12', 2), ('SOLEO', 460, 'SOLERE', '', '', '3_1', 1), ('SOLLICITVS', 461, 'SOLLICITUS', '', '', '4_3', 1), ('SOLVS', 462, 'SOLUS', '', '', '1_39', 2), ('SOLVS', 463, 'SOLUS', '', '', '2_44', 2), ('SOLVO', 464, 'SOLUERE', '', '', '1_38', 1), ('SOMNVS', 465, 'SOMNUS', '', '', '1_21', 2), ('SOMNVS', 466, 'SOMNUS', '', '', '4_24', 2), ('SONORVS', 467, 'SONORUS', '', '', '2_43', 1), ('SPECVS', 468, 'SPECUS', '', '', '1_19', 1), ('SPERNO', 469, 'SPERNERE', '', '', '1_16', 1), ('SPINA', 470, 'SPINA', '', '', '4_10', 1), ('SPOLIO', 471, 'SPOLIARE', '', '', '4_8', 1), ('SPONTE', 472, 'SPONTE', '', '', '1_13', 1), ('STEMMA', 473, 'STEMMA', '', '', '2_30', 1), ('STILICHO/N', 474, 'STILICHO', '', '', '3_2', 2), ('STILICHO/N', 475, 'STILICHO', '', '', '3_12', 2), ('STREPO', 476, 'STREPERE', '', '', '2_11', 1), ('STRINGO', 477, 'STRINGERE', '', '', '1_36', 2), ('STRINGO', 478, 'STRINGERE', '', '', '4_19', 2), ('SVB', 479, 'SUB', '', '', '1_18', 2), ('SVB', 480, 'SUB', '', '', '2_34', 2), ('SVBEO/1', 481, 'SUBIRE', '', '', '2_8', 1), ('SVI/1', 482, 'SUI', '', '', '1_41', 2), ('SVI/1', 483, 'SUI', '', '', '2_8', 2), ('SVPERBVS/2', 484, 'SUPERBUS', '', '', '1_15', 1), ('SVSVRRO', 485, 'SUSURRARE', '', '', '2_13', 1), ('TACEO', 486, 'TACERE', '', '', '2_42', 2), ('TACEO', 487, 'TACERE', '', '', '2_43', 2), ('TAEDA', 488, 'TAEDA', '', '', '3_4', 1), ('TAGVS/N', 489, 'TAGUS', '', '', '2_32', 1), ('TAM', 490, 'TAM', '', '', '4_18', 1), ('TEGO', 491, 'TEGERE', '', '', '4_10', 1), ('TELLVS', 492, 'TELLUS', '', '', '2_2', 1), ('TELVM', 493, 'TELUM', '', '', '1_13', 1), ('TENDO', 494, 'TENDERE', '', '', '1_2', 1), ('TETRICVS', 495, 'TETRICUS', '', '', '4_32', 1), ('THALAMVS', 496, 'THALAMUS', '', '', '4_1', 1), ('THETIS/N', 497, 'THETIS', '', '', '1_7', 1), ('THYBRIS/N', 498, 'THYBRIS', '', '', '2_17', 1), ('TIBIA', 499, 'TIBIA', '', '', '4_30', 1), ('TIMEO', 500, 'TIMERE', '', '', '4_9', 1), ('TORRENS/1', 501, 'TORRENS', '', '', '1_20', 1), ('TORVS', 502, 'TORUS', '', '', '2_3', 2), ('TORVS', 503, 'TORUS', '', '', '4_28', 2), ('TRADO', 504, 'TRADERE', '', '', '4_17', 1), ('TRAHO', 505, 'TRAHERE', '', '', '3_5', 1), ('TRANSEO/1', 506, 'TRANSIRE', '', '', '4_36', 1), ('TREPIDO', 507, 'TREPIDARE', '', '', '4_3', 1), ('TRIVMPHVS', 508, 'TRIUMPHUS', '', '', '2_25', 1), ('TV', 509, 'TU', '', '', '1_6', 6), ('TV', 510, 'TU', '', '', '1_7', 6), ('TV', 511, 'TU', '', '', '1_10', 6), ('TV', 512, 'TU', '', '', '1_27', 6), ('TV', 513, 'TU', '', '', '1_31', 6), ('TV', 514, 'TU', '', '', '1_40', 6), ('TVBA', 515, 'TUBA', '', '', '1_35', 1), ('TVM', 516, 'TUM', '', '', '1_22', 2), ('TVM', 517, 'TUM', '', '', '4_28', 2), ('TVRBA', 518, 'TURBA', '', '', '4_31', 1), ('TVVS', 519, 'TUUS', '', '', '1_13', 1), ('TYRIVS/A', 520, 'TYRIUS', '', '', '4_26', 1), ('VBI/1', 521, 'UBI', '', '', '2_23', 1), ('VLTRO', 522, 'ULTRO', '', '', '1_28', 1), ('VMBRA', 523, 'UMBRA', '', '', '1_19', 1), ('VNDE/1', 524, 'UNDE', '', '', '2_22', 1), ('VNGVIS', 525, 'UNGUIS', '', '', '4_6', 1), ('VRBS', 526, 'URBS', '', '', '2_38', 1), ('VRO', 527, 'URERE', '', '', '1_22', 1), ('VEL/1', 528, 'UEL', '', '', '1_19', 2), ('VEL/1', 529, 'UEL', '', '', '3_11', 2), ('VOLO/3', 530, 'UELLE', '', '', '1_18', 1), ('VENETVS', 531, 'UENETUS', '', '', '2_7', 1), ('VENTVS', 532, 'UENTUS', '', '', '1_12', 1), ('VENVS/N', 533, 'UENUS', '', '', '1_16', 3), ('VENVS/N', 534, 'UENUS', '', '', '4_2', 3), ('VENVS/N', 535, 'UENUS', '', '', '4_12', 3), ('VER', 536, 'UER', '', '', '2_2', 2), ('VER', 537, 'UER', '', '', '4_7', 2), ('VERVS', 538, 'UERUS', '', '', '1_25', 1), ('VESTIO', 539, 'UESTIRE', '', '', '2_9', 1), ('VESTIS', 540, 'UESTIS', '', '', '4_26', 1), ('VICTOR', 541, 'UICTOR', '', '', '4_28', 1), ('VIDEO', 542, 'UIDERE', '', '', '1_27', 1), ('VINCO', 543, 'UINCERE', '', '', '1_8', 2), ('VINCO', 544, 'UINCERE', '', '', '4_15', 2), ('VINCVLVM', 545, 'UINCULA', '', '', '1_30', 2), ('VINCVLVM', 546, 'UINCULA', '', '', '4_18', 2), ('VIR', 547, 'UIR', '', '', '1_40', 1), ('VIRBIVS/N', 548, 'UIRBIUS', '', '', '1_17', 1), ('VIRECTVM', 549, 'UIRECTUM', '', '', '2_31', 1), ('VIREO/2', 550, 'UIRERE', '', '', '1_19', 1), ('VIRGINEVS', 551, 'UIRGINEUS', '', '', '4_27', 1), ('VIRGO', 552, 'UIRGO', '', '', '4_34', 1), ('VITREVS', 553, 'UITREUS', '', '', '2_34', 1), ('VIX', 554, 'UIX', '', '', '2_25', 1), ('VOVEO', 555, 'UOUERE', '', '', '2_18', 1), ('VOX', 556, 'UOX', '', '', '4_35', 2), ('VOX', 557, 'UOX', '', '', '4_36', 2), ('VVLNVS', 558, 'UULNUS', '', '', '1_14', 2), ('VVLNVS', 559, 'UULNUS', '', '', '4_29', 2), ('ZEPHYRVS/N', 560, 'ZEPHYRUS', '', '', '2_44', 1)]
section_list ={'1.1': '3.2', '3.5': 'start', '4.12': '3.5', '1.25': '4.12', '1.7': '1.25', '1.15': '1.7', '2.15': '1.15', '1.16': '2.15', '4.22': '1.16', '4.19': '4.22', '1.23': '4.19', '4.35': '1.23', '2.1': '4.35', '4.5': '2.1', '1.10': '4.5', '4.21': '1.10', '2.9': '4.21', '4.27': '2.9', '4.24': '4.27', '1.32': '4.24', '1.41': '1.32', '4.25': '1.41', '4.23': '4.25', '2.45': '4.23', '2.35': '2.45', '4.10': '2.35', '1.8': '4.10', '2.41': '1.8', '1.4': '2.41', '1.29': '1.4', '2.20': '1.29', '4.16': '2.20', '2.11': '4.16', '4.1': '2.11', '2.21': '4.1', '3.8': '2.21', '3.9': '3.8', '2.22': '3.9', '2.19': '2.22', '2.32': '2.19', '2.43': '2.32', '2.31': '2.43', '1.40': '2.31', '1.39': '1.40', '1.26': '1.39', '2.29': '1.26', '2.12': '2.29', '1.22': '2.12', '2.6': '1.22', '2.5': '2.6', '4.30': '2.5', '1.24': '4.30', '1.6': '1.24', '1.31': '1.6', '2.42': '1.31', '4.9': '2.42', '2.3': '4.9', '1.2': '2.3', '3.3': '1.2', '1.37': '3.3', '1.11': '1.37', '1.33': '1.11', '1.30': '1.33', '3.11': '1.30', '1.12': '3.11', '3.1': '1.12', '3.2': '3.1', '1.9': '1.1', '4.11': '1.9', '1.18': '4.11', '1.27': '1.18', '2.4': '1.27', '4.33': '2.4', '4.34': '4.33', '1.17': '4.34', '4.15': '1.17', '2.40': '4.15', '3.7': '2.40', '4.14': '3.7', '1.5': '4.14', '4.2': '1.5', '2.18': '4.2', '2.24': '2.18', '2.28': '2.24', '4.37': '2.28', '2.14': '4.37', '2.16': '2.14', '1.3': '2.16', '3.10': '1.3', '3.12': '3.10', '1.21': '3.12', '1.34': '1.21', '2.10': '1.34', '4.26': '2.10', '4.32': '4.26', '1.20': '4.32', '2.7': '1.20', '4.8': '2.7', '4.17': '4.8', '3.4': '4.17', '4.13': '3.4', '1.13': '4.13', '4.4': '1.13', '1.38': '4.4', '2.36': '1.38', '1.35': '2.36', '4.7': '1.35', '1.14': '4.7', '1.19': '1.14', '2.33': '1.19', '2.26': '2.33', '2.27': '2.26', '4.36': '2.27', '4.3': '4.36', '4.6': '4.3', '2.38': '4.6', '4.31': '2.38', '4.18': '4.31', '1.36': '4.18', '2.23': '1.36', '4.20': '2.23', '2.13': '4.20', '4.28': '2.13', '2.39': '4.28', '4.29': '2.39', '1.28': '4.29', '2.25': '1.28', '2.37': '2.25', '2.34': '2.37', '3.6': '2.34', '2.30': '3.6', '2.44': '2.30', '2.8': '2.44', '2.17': '2.8', '2.2': '2.17', 'end': '2.2', 'start': 'start'}
title = "Claudian, Epithalamium de Nuptii Honorii Augusti (Preface)"
section_level =  2
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)