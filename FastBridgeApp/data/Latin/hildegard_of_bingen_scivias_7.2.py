import text
nan=""
section_words = {'start': -1, '7.1': 301, '7.2': 432, '7.3': 496, '7.4': 546, '7.5': 597, 'end': -2}
the_text =  [('DEINDE', 0, 'Deinde', '', '', '7_1', 1), ('VIDEO', 1, 'uidi', '', '', '7_1', 5), ('ARDEO', 2, 'ardentem', '', '', '7_1', 3), ('LVX', 3, 'lucem', '', '', '7_1', 3), ('TANTVS', 4, 'tantae', '', '', '7_1', 2), ('MAGNITVDO', 5, 'magnitudinis', '', '', '7_1', 2), ('VT/4', 6, 'ut', '', '', '7_1', 2), ('ALIQVIS', 7, 'aliquis', '', '', '7_1', 1), ('MONS', 8, 'mons', '', '', '7_1', 1), ('MAGNVS', 9, 'magnus', '', '', '7_1', 3), ('ET/2', 10, 'et', '', '', '7_1', 33), ('ALTVS', 11, 'altus', '', '', '7_1', 1), ('SVM/1', 12, 'est', '', '', '7_1', 7), ('IN', 13, 'in', '', '', '7_1', 14), ('SVMMITAS', 14, 'summitate', '', '', '7_1', 1), ('SVVS', 15, 'sua', '', '', '7_1', 7), ('VELVT/1', 16, 'uelut', '', '', '7_1', 4), ('IN', 17, 'in', '', '', '7_1', 14), ('MVLTVS', 18, 'multas', '', '', '7_1', 5), ('LINGVA', 19, 'linguas', '', '', '7_1', 1), ('DIVIDO', 20, 'diuisam', '', '', '7_1', 2), ('ET/2', 21, 'Et', '', '', '7_1', 33), ('CORAM/1', 22, 'coram', '', '', '7_1', 1), ('LVX', 23, 'luce', '', '', '7_1', 3), ('ISTE', 24, 'ista', '', '', '7_1', 2), ('QVIDAM', 25, 'quaedam', '', '', '7_1', 14), ('MVLTITVDO', 26, 'multitudo', '', '', '7_1', 3), ('ALBATVS', 27, 'albatorum', '', '', '7_1', 1), ('HOMO', 28, 'hominum', '', '', '7_1', 11), ('STO', 29, 'stabat', '', '', '7_1', 1), ('ANTE/2', 30, 'ante', '', '', '7_1', 2), ('QVI/1', 31, 'quos', '', '', '7_1', 26), ('VELVT/1', 32, 'uelut', '', '', '7_1', 4), ('QVIDAM', 33, 'quoddam', '', '', '7_1', 14), ('VELVM', 34, 'uelum', '', '', '7_1', 1), ('TAMQVAM/1', 35, 'tamquam', '', '', '7_1', 1), ('CRYSTALLVM', 36, 'crystallus', '', '', '7_1', 1), ('PERLVCIDVS', 37, 'perlucidum', '', '', '7_1', 1), ('AB', 38, 'a', '', '', '7_1', 10), ('PECTVS', 39, 'pectore', '', '', '7_1', 2), ('VSQVE', 40, 'usque', '', '', '7_1', 5), ('AD/2', 41, 'ad', '', '', '7_1', 10), ('PES', 42, 'pedes', '', '', '7_1', 7), ('IS', 43, 'eorum', '', '', '7_1', 12), ('EXTENDO', 44, 'extensum', '', '', '7_1', 3), ('SVM/1', 45, 'erat', '', '', '7_1', 7), ('SED', 46, 'Sed', '', '', '7_1', 8), ('ET/2', 47, 'et', '', '', '7_1', 33), ('ANTE/2', 48, 'ante', '', '', '7_1', 2), ('MVLTITVDO', 49, 'multitudinem', '', '', '7_1', 3), ('ISTE', 50, 'istam', '', '', '7_1', 2), ('QVASI/1', 51, 'quasi', '', '', '7_1', 2), ('IN', 52, 'in', '', '', '7_1', 14), ('QVIDAM', 53, 'quadam', '', '', '7_1', 14), ('VIA', 54, 'uia', '', '', '7_1', 1), ('VELVT/1', 55, 'uelut', '', '', '7_1', 4), ('QVIDAM', 56, 'quidam', '', '', '7_1', 14), ('VERMIS', 57, 'uermis', '', '', '7_1', 4), ('MIRVS', 58, 'mirae', '', '', '7_1', 1), ('MAGNITVDO', 59, 'magnitudinis', '', '', '7_1', 2), ('ET/2', 60, 'et', '', '', '7_1', 33), ('LONGITVDO', 61, 'longitudinis', '', '', '7_1', 1), ('SVPINVS', 62, 'supinus', '', '', '7_1', 1), ('IACEO', 63, 'iacebat', '', '', '7_1', 1), ('QVI/1', 64, 'qui', '', '', '7_1', 26), ('TANTVS', 65, 'tanti', '', '', '7_1', 2), ('HORROR', 66, 'horroris', '', '', '7_1', 1), ('ET/2', 67, 'et', '', '', '7_1', 33), ('INSANIA', 68, 'insaniae', '', '', '7_1', 1), ('VIDEO', 69, 'uidebatur', '', '', '7_1', 5), ('VLTRA/2', 70, 'ultra', '', '', '7_1', 1), ('QVI/1', 71, 'quam', '', '', '7_1', 26), ('HOMO', 72, 'homo', '', '', '7_1', 11), ('EFFOR', 73, 'effari', '', '', '7_1', 1), ('POSSVM/1', 74, 'potest', '', '', '7_1', 4), ('AD/2', 75, 'Ad', '', '', '7_1', 10), ('QVI/1', 76, 'cuius', '', '', '7_1', 26), ('SINISTER', 77, 'sinistram', '', '', '7_1', 2), ('QVASI/1', 78, 'quasi', '', '', '7_1', 2), ('FORVM/1', 79, 'forum', '', '', '7_1', 1), ('SVM/1', 80, 'erat', '', '', '7_1', 7), ('VBI/1', 81, 'ubi', '', '', '7_1', 2), ('DIVITIAE', 82, 'diuitiae', '', '', '7_1', 1), ('HOMO', 83, 'hominum', '', '', '7_1', 11), ('ATQVE/1', 84, 'atque', '', '', '7_1', 4), ('DELICIA/1', 85, 'deliciae', '', '', '7_1', 1), ('SAECVLARIS', 86, 'saeculares', '', '', '7_1', 3), ('ET/2', 87, 'et', '', '', '7_1', 33), ('MERCATVS', 88, 'mercatus', '', '', '7_1', 2), ('DIVERTO', 89, 'diuersarum', '', '', '7_1', 2), ('RES', 90, 'rerum', '', '', '7_1', 1), ('APPAREO', 91, 'apparuerunt', '', '', '7_1', 3), ('VBI/1', 92, 'ubi', '', '', '7_1', 2), ('ETIAM', 93, 'etiam', '', '', '7_1', 3), ('QVIDAM', 94, 'quidam', '', '', '7_1', 14), ('HOMO', 95, 'homines', '', '', '7_1', 11), ('MVLTVS', 96, 'multa', '', '', '7_1', 5), ('CELERITAS', 97, 'celeritate', '', '', '7_1', 1), ('CVRRO', 98, 'currentes', '', '', '7_1', 1), ('NVLLVS', 99, 'nullum', '', '', '7_1', 1), ('MERCATVS', 100, 'mercatum', '', '', '7_1', 2), ('FACIO', 101, 'faciebant', '', '', '7_1', 2), ('QVIDAM', 102, 'quidam', '', '', '7_1', 14), ('AVTEM', 103, 'autem', '', '', '7_1', 11), ('TEPIDVS', 104, 'tepide', '', '', '7_1', 1), ('EO/1', 105, 'euntes', '', '', '7_1', 2), ('ET/2', 106, 'et', '', '', '7_1', 33), ('VENDITIO', 107, 'uenditioni', '', '', '7_1', 1), ('ET/2', 108, 'et', '', '', '7_1', 33), ('EMPTIO', 109, 'emptioni', '', '', '7_1', 1), ('IBI', 110, 'ibi', '', '', '7_1', 1), ('INSISTO', 111, 'insistebant', '', '', '7_1', 1), ('VERMIS', 112, 'Uermis', '', '', '7_1', 4), ('AVTEM', 113, 'autem', '', '', '7_1', 11), ('ILLE', 114, 'ille', '', '', '7_1', 14), ('NIGER', 115, 'niger', '', '', '7_1', 4), ('ET/2', 116, 'et', '', '', '7_1', 33), ('HIRSVTVS', 117, 'hirsutus', '', '', '7_1', 1), ('ATQVE/1', 118, 'atque', '', '', '7_1', 4), ('VLCVS', 119, 'ulceribus', '', '', '7_1', 1), ('ET/2', 120, 'et', '', '', '7_1', 33), ('PVSTVLA', 121, 'pustulis', '', '', '7_1', 1), ('PLENVS', 122, 'plenus', '', '', '7_1', 2), ('SVM/1', 123, 'erat', '', '', '7_1', 7), ('QVINQVE', 124, 'quinque', '', '', '7_1', 1), ('VARIETAS', 125, 'uarietates', '', '', '7_1', 1), ('AB', 126, 'a', '', '', '7_1', 10), ('CAPVT', 127, 'capite', '', '', '7_1', 3), ('PER', 128, 'per', '', '', '7_1', 2), ('VENTER', 129, 'uentrum', '', '', '7_1', 2), ('SVVS', 130, 'suum', '', '', '7_1', 7), ('VSQVE', 131, 'usque', '', '', '7_1', 5), ('AD/2', 132, 'ad', '', '', '7_1', 10), ('PES', 133, 'pedes', '', '', '7_1', 7), ('IN', 134, 'in', '', '', '7_1', 14), ('MODVS', 135, 'modum', '', '', '7_1', 2), ('ZONA', 136, 'zonarum', '', '', '7_1', 1), ('DESCENDO', 137, 'descendentes', '', '', '7_1', 3), ('IN', 138, 'in', '', '', '7_1', 14), ('SVI/1', 139, 'se', '', '', '7_1', 9), ('HABEO', 140, 'habens', '', '', '7_1', 2), ('QVI/1', 141, 'quarum', '', '', '7_1', 26), ('VNVS', 142, 'una', '', '', '7_1', 5), ('VIRIDIS', 143, 'uiridis', '', '', '7_1', 2), ('ALIVS', 144, 'alia', '', '', '7_1', 7), ('ALBVS', 145, 'alba', '', '', '7_1', 2), ('ALIVS', 146, 'alia', '', '', '7_1', 7), ('RVBEVS', 147, 'rubea', '', '', '7_1', 2), ('QVIDAM', 148, 'quaedam', '', '', '7_1', 14), ('CROCEVS', 149, 'crocea', '', '', '7_1', 2), ('QVIDAM', 150, 'quaedam', '', '', '7_1', 14), ('NIGER', 151, 'nigra', '', '', '7_1', 4), ('APPAREO', 152, 'apparebat', '', '', '7_1', 3), ('PLENVS', 153, 'plenae', '', '', '7_1', 2), ('VENENVM', 154, 'ueneno', '', '', '7_1', 3), ('MORTIFER', 155, 'mortifero', '', '', '7_1', 2), ('SED', 156, 'Sed', '', '', '7_1', 8), ('CAPVT', 157, 'caput', '', '', '7_1', 3), ('IS', 158, 'eius', '', '', '7_1', 12), ('ITA', 159, 'ita', '', '', '7_1', 5), ('CONTERO', 160, 'contritum', '', '', '7_1', 1), ('SVM/1', 161, 'fuit', '', '', '7_1', 7), ('QVI/1', 162, 'quod', '', '', '7_1', 26), ('ET/2', 163, 'et', '', '', '7_1', 33), ('SINISTER', 164, 'sinistra', '', '', '7_1', 2), ('MAXILLA', 165, 'maxilla', '', '', '7_1', 1), ('IPSE', 166, 'ipsius', '', '', '7_1', 7), ('IAM', 167, 'iam', '', '', '7_1', 1), ('DISSOLVO', 168, 'dissolui', '', '', '7_1', 1), ('VIDEO', 169, 'uidebatur', '', '', '7_1', 5), ('OCVLVS', 170, 'Oculi', '', '', '7_1', 1), ('VERO/3', 171, 'uero', '', '', '7_1', 5), ('IS', 172, 'eius', '', '', '7_1', 12), ('EXTRINSECVS', 173, 'extrinsecus', '', '', '7_1', 1), ('SANGVINEVS', 174, 'sanguinei', '', '', '7_1', 1), ('ET/2', 175, 'et', '', '', '7_1', 33), ('INTRINSECVS', 176, 'intrinsecus', '', '', '7_1', 1), ('IGNEVS', 177, 'ignei', '', '', '7_1', 1), ('AVRIS', 178, 'aures', '', '', '7_1', 1), ('AVTEM', 179, 'autem', '', '', '7_1', 11), ('ROTVNDVS', 180, 'rotundae', '', '', '7_1', 1), ('ET/2', 181, 'et', '', '', '7_1', 33), ('HISPIDVS', 182, 'hispidae', '', '', '7_1', 1), ('NARIS', 183, 'nares', '', '', '7_1', 2), ('VERO/3', 184, 'uero', '', '', '7_1', 5), ('ET/2', 185, 'et', '', '', '7_1', 33), ('OS/1', 186, 'os', '', '', '7_1', 4), ('SECVNDVS/1', 187, 'secundum', '', '', '7_1', 3), ('NARIS', 188, 'nares', '', '', '7_1', 2), ('ET/2', 189, 'et', '', '', '7_1', 33), ('OS/1', 190, 'os', '', '', '7_1', 4), ('VIPERA', 191, 'uiperae', '', '', '7_1', 2), ('SED', 192, 'sed', '', '', '7_1', 8), ('MANVS/1', 193, 'manus', '', '', '7_1', 3), ('SECVNDVS/1', 194, 'secundum', '', '', '7_1', 3), ('MANVS/1', 195, 'manus', '', '', '7_1', 3), ('HOMO', 196, 'hominis', '', '', '7_1', 11), ('PES', 197, 'pedes', '', '', '7_1', 7), ('AVTEM', 198, 'autem', '', '', '7_1', 11), ('VT/4', 199, 'ut', '', '', '7_1', 2), ('PES', 200, 'pedes', '', '', '7_1', 7), ('VIPERA', 201, 'uiperae', '', '', '7_1', 2), ('ET/2', 202, 'et', '', '', '7_1', 33), ('CAVDA', 203, 'cauda', '', '', '7_1', 1), ('BREVIS', 204, 'breuis', '', '', '7_1', 1), ('ET/2', 205, 'et', '', '', '7_1', 33), ('HORRIBILIS', 206, 'horribilis', '', '', '7_1', 1), ('APPAREO', 207, 'apparebat', '', '', '7_1', 3), ('ET/2', 208, 'Et', '', '', '7_1', 33), ('COLLVS', 209, 'collo', '', '', '7_1', 1), ('IS', 210, 'eius', '', '', '7_1', 12), ('CATENA', 211, 'catena', '', '', '7_1', 2), ('IMPONO', 212, 'imposita', '', '', '7_1', 1), ('SVM/1', 213, 'fuerat', '', '', '7_1', 7), ('QVI/1', 214, 'quae', '', '', '7_1', 26), ('ET/2', 215, 'et', '', '', '7_1', 33), ('MANVS/1', 216, 'manus', '', '', '7_1', 3), ('ET/2', 217, 'et', '', '', '7_1', 33), ('PES', 218, 'pedes', '', '', '7_1', 7), ('IPSE', 219, 'ipsius', '', '', '7_1', 7), ('ALLIGO/2', 220, 'alligauerat', '', '', '7_1', 1), ('ITA', 221, 'ita', '', '', '7_1', 5), ('QVI/1', 222, 'quod', '', '', '7_1', 26), ('ET/2', 223, 'et', '', '', '7_1', 33), ('IDEM', 224, 'eadem', '', '', '7_1', 4), ('CATENA', 225, 'catena', '', '', '7_1', 2), ('IN', 226, 'in', '', '', '7_1', 14), ('LAPIS', 227, 'lapidem', '', '', '7_1', 1), ('ABYSSVS', 228, 'abyssi', '', '', '7_1', 3), ('FORTIS', 229, 'fortissime', '', '', '7_1', 1), ('FIRMO', 230, 'firmata', '', '', '7_1', 1), ('ILLE', 231, 'illum', '', '', '7_1', 14), ('TAM', 232, 'tam', '', '', '7_1', 1), ('VALIDVS', 233, 'ualide', '', '', '7_1', 1), ('CONSTRINGO', 234, 'constrinxerat', '', '', '7_1', 1), ('QVI/1', 235, 'quod', '', '', '7_1', 26), ('SVI/1', 236, 'se', '', '', '7_1', 9), ('NEQVE', 237, 'nec', '', '', '7_1', 4), ('HIC/1', 238, 'hac', '', '', '7_1', 3), ('NEQVE', 239, 'nec', '', '', '7_1', 4), ('ILLE', 240, 'illae', '', '', '7_1', 14), ('SECVNDVS/1', 241, 'secundum', '', '', '7_1', 3), ('NEQVITIA', 242, 'nequitiam', '', '', '7_1', 1), ('VOLVNTAS', 243, 'uoluntatis', '', '', '7_1', 1), ('SVVS', 244, 'suae', '', '', '7_1', 7), ('MOVEO', 245, 'mouere', '', '', '7_1', 1), ('POSSVM/1', 246, 'poterat', '', '', '7_1', 4), ('EX', 247, 'Ex', '', '', '7_1', 3), ('OS/1', 248, 'ore', '', '', '7_1', 4), ('AVTEM', 249, 'autem', '', '', '7_1', 11), ('IS', 250, 'eius', '', '', '7_1', 12), ('MVLTVS', 251, 'multae', '', '', '7_1', 5), ('FLAMMA', 252, 'flammae', '', '', '7_1', 8), ('EXEO/1', 253, 'exeuntes', '', '', '7_1', 1), ('IN', 254, 'in', '', '', '7_1', 14), ('QVATVOR', 255, 'quattuor', '', '', '7_1', 1), ('PARS', 256, 'partes', '', '', '7_1', 2), ('SVI/1', 257, 'se', '', '', '7_1', 9), ('DIVIDO', 258, 'diuiserunt', '', '', '7_1', 2), ('QVI/1', 259, 'quarum', '', '', '7_1', 26), ('PARS', 260, 'pars', '', '', '7_1', 2), ('VNVS', 261, 'una', '', '', '7_1', 5), ('VSQVE', 262, 'usque', '', '', '7_1', 5), ('AD/2', 263, 'ad', '', '', '7_1', 10), ('NVBES', 264, 'nubes', '', '', '7_1', 4), ('ASCENDO', 265, 'ascendebat', '', '', '7_1', 1), ('ET/2', 266, 'et', '', '', '7_1', 33), ('ALIVS', 267, 'alia', '', '', '7_1', 7), ('INTER', 268, 'inter', '', '', '7_1', 5), ('SAECVLARIS', 269, 'saeculares', '', '', '7_1', 3), ('HOMO', 270, 'homines', '', '', '7_1', 11), ('ALIVS', 271, 'alia', '', '', '7_1', 7), ('AVTEM', 272, 'autem', '', '', '7_1', 11), ('INTER', 273, 'inter', '', '', '7_1', 5), ('SPIRITALIS', 274, 'spiritales', '', '', '7_1', 2), ('SVI/1', 275, 'se', '', '', '7_1', 9), ('EXTENDO', 276, 'extendebat', '', '', '7_1', 3), ('QVIDAM', 277, 'quaedam', '', '', '7_1', 14), ('VERO/3', 278, 'uero', '', '', '7_1', 5), ('VSQVE', 279, 'usque', '', '', '7_1', 5), ('IN', 280, 'in', '', '', '7_1', 14), ('ABYSSVS', 281, 'abyssum', '', '', '7_1', 3), ('DESCENDO', 282, 'descendebat', '', '', '7_1', 3), ('SED', 283, 'Sed', '', '', '7_1', 8), ('FLAMMA', 284, 'flamma', '', '', '7_1', 8), ('ILLE', 285, 'illa', '', '', '7_1', 14), ('QVI/1', 286, 'quae', '', '', '7_1', 26), ('NVBES', 287, 'nubes', '', '', '7_1', 4), ('PETO', 288, 'petebat', '', '', '7_1', 3), ('CONTRA/2', 289, 'contra', '', '', '7_1', 1), ('HOMO', 290, 'homines', '', '', '7_1', 11), ('ILLE', 291, 'illos', '', '', '7_1', 14), ('PROELIOR', 292, 'proeliabatur', '', '', '7_1', 1), ('QVI/1', 293, 'qui', '', '', '7_1', 26), ('AD/2', 294, 'ad', '', '', '7_1', 10), ('CAELVS', 295, 'caelos', '', '', '7_1', 4), ('EO/1', 296, 'ire', '', '', '7_1', 2), ('VOLO/3', 297, 'uolebant', '', '', '7_1', 2), ('QVI/1', 298, 'Quorum', '', '', '7_1', 26), ('TRES', 299, 'tres', '', '', '7_1', 1), ('ACIES', 300, 'acies', '', '', '7_1', 2), ('VIDEO', 301, 'uidebam', '', '', '7_1', 5), ('NAM', 302, 'Nam', '', '', '7_2', 2), ('ACIES', 303, 'acies', '', '', '7_2', 2), ('VNVS', 304, 'una', '', '', '7_2', 5), ('PROPE/2', 305, 'prope', '', '', '7_2', 1), ('NVBES', 306, 'nubes', '', '', '7_2', 4), ('ET/2', 307, 'et', '', '', '7_2', 33), ('VNVS', 308, 'una', '', '', '7_2', 5), ('IN', 309, 'in', '', '', '7_2', 14), ('MEDIETAS', 310, 'medietate', '', '', '7_2', 1), ('ILLE', 311, 'illa', '', '', '7_2', 14), ('QVI/1', 312, 'quae', '', '', '7_2', 26), ('INTER', 313, 'inter', '', '', '7_2', 5), ('NVBES', 314, 'nubes', '', '', '7_2', 4), ('ET/2', 315, 'et', '', '', '7_2', 33), ('TERRA', 316, 'terram', '', '', '7_2', 3), ('SVM/1', 317, 'est', '', '', '7_2', 7), ('ET/2', 318, 'et', '', '', '7_2', 33), ('VNVS', 319, 'una', '', '', '7_2', 5), ('IVXTA/1', 320, 'iuxta', '', '', '7_2', 1), ('TERRA', 321, 'terram', '', '', '7_2', 3), ('PERGO', 322, 'pergebat', '', '', '7_2', 3), ('OMNIS', 323, 'omnes', '', '', '7_2', 2), ('REPETO', 324, 'repetitis', '', '', '7_2', 1), ('VOX', 325, 'uocibus', '', '', '7_2', 2), ('PERGO', 326, 'pergamus', '', '', '7_2', 3), ('AD/2', 327, 'ad', '', '', '7_2', 10), ('CAELVS', 328, 'caelos', '', '', '7_2', 4), ('VOCIFEROR', 329, 'uociferantes', '', '', '7_2', 2), ('SED', 330, 'Sed', '', '', '7_2', 8), ('AB', 331, 'a', '', '', '7_2', 10), ('FLAMMA', 332, 'flamma', '', '', '7_2', 8), ('ILLE', 333, 'illa', '', '', '7_2', 14), ('HIC/1', 334, 'hac', '', '', '7_2', 3), ('ET/2', 335, 'et', '', '', '7_2', 33), ('ILLE', 336, 'illae', '', '', '7_2', 14), ('PROICIO', 337, 'proiecti', '', '', '7_2', 1), ('QVIDAM', 338, 'quidam', '', '', '7_2', 14), ('NON', 339, 'non', '', '', '7_2', 3), ('CADO', 340, 'cadebant', '', '', '7_2', 2), ('ALIVS', 341, 'alii', '', '', '7_2', 7), ('AVTEM', 342, 'autem', '', '', '7_2', 11), ('PES', 343, 'pedibus', '', '', '7_2', 7), ('SVVS', 344, 'suis', '', '', '7_2', 7), ('SVI/1', 345, 'se', '', '', '7_2', 9), ('VIX', 346, 'uix', '', '', '7_2', 1), ('SVSTENTO', 347, 'sustentabant', '', '', '7_2', 1), ('ALIVS', 348, 'alii', '', '', '7_2', 7), ('VERO/3', 349, 'uero', '', '', '7_2', 5), ('AD/2', 350, 'ad', '', '', '7_2', 10), ('TERRA', 351, 'terram', '', '', '7_2', 3), ('CADO', 352, 'cadentes', '', '', '7_2', 2), ('SED', 353, 'sed', '', '', '7_2', 8), ('ITERVM', 354, 'iterum', '', '', '7_2', 2), ('SVRGO', 355, 'surgentes', '', '', '7_2', 1), ('AD/2', 356, 'ad', '', '', '7_2', 10), ('CAELVS', 357, 'caelos', '', '', '7_2', 4), ('TENDO', 358, 'tendebant', '', '', '7_2', 1), ('FLAMMA', 359, 'Flamma', '', '', '7_2', 8), ('AVTEM', 360, 'autem', '', '', '7_2', 11), ('ILLE', 361, 'illa', '', '', '7_2', 14), ('QVI/1', 362, 'quae', '', '', '7_2', 26), ('SVI/1', 363, 'se', '', '', '7_2', 9), ('INTER', 364, 'inter', '', '', '7_2', 5), ('SAECVLARIS', 365, 'saeculares', '', '', '7_2', 3), ('HOMO', 366, 'homines', '', '', '7_2', 11), ('DIFFVNDO/2', 367, 'diffudit', '', '', '7_2', 1), ('QVIDAM', 368, 'quosdam', '', '', '7_2', 14), ('EX', 369, 'ex', '', '', '7_2', 3), ('IS', 370, 'eis', '', '', '7_2', 12), ('COMBVRO', 371, 'comburens', '', '', '7_2', 1), ('IN', 372, 'in', '', '', '7_2', 14), ('TETER', 373, 'taeterrimam', '', '', '7_2', 2), ('NIGREDO', 374, 'nigredinem', '', '', '7_2', 1), ('VERTO', 375, 'uertit', '', '', '7_2', 1), ('QVIDAM', 376, 'quosdam', '', '', '7_2', 14), ('AVTEM', 377, 'autem', '', '', '7_2', 11), ('SVVS', 378, 'suo', '', '', '7_2', 7), ('ACVMEN', 379, 'acumine', '', '', '7_2', 1), ('ITA', 380, 'ita', '', '', '7_2', 5), ('TRANSFIGO', 381, 'transfixit', '', '', '7_2', 2), ('QVI/1', 382, 'quod', '', '', '7_2', 26), ('IS', 383, 'eos', '', '', '7_2', 12), ('CVM/3', 384, 'cum', '', '', '7_2', 1), ('QVOQVE', 385, 'quoque', '', '', '7_2', 1), ('VOLO/3', 386, 'uolebat', '', '', '7_2', 2), ('INFLECTO', 387, 'inflexit', '', '', '7_2', 1), ('DE', 388, 'De', '', '', '7_2', 3), ('QVO/1', 389, 'qua', '', '', '7_2', 1), ('TAMEN', 390, 'tamen', '', '', '7_2', 2), ('QVIDAM', 391, 'quidam', '', '', '7_2', 14), ('SVI/1', 392, 'se', '', '', '7_2', 9), ('ERIPIO', 393, 'eripientes', '', '', '7_2', 1), ('ET/2', 394, 'et', '', '', '7_2', 33), ('AD/2', 395, 'ad', '', '', '7_2', 10), ('ILLE', 396, 'illos', '', '', '7_2', 14), ('QVI/1', 397, 'qui', '', '', '7_2', 26), ('CAELVS', 398, 'caelos', '', '', '7_2', 4), ('PETO', 399, 'petebant', '', '', '7_2', 3), ('PERGO', 400, 'pergentes', '', '', '7_2', 3), ('O', 401, 'o', '', '', '7_2', 1), ('TV', 402, 'uos', '', '', '7_2', 1), ('FIDELIS/2', 403, 'fideles', '', '', '7_2', 1), ('PRAESTO/1', 404, 'praestate', '', '', '7_2', 1), ('NOS', 405, 'nobis', '', '', '7_2', 1), ('AVDITORIVM', 406, 'adiutorium', '', '', '7_2', 1), ('ITERO', 407, 'iterato', '', '', '7_2', 1), ('CLAMOR', 408, 'clamore', '', '', '7_2', 1), ('VOCIFEROR', 409, 'uociferabantur', '', '', '7_2', 2), ('QVIDAM', 410, 'quidam', '', '', '7_2', 14), ('AVTEM', 411, 'autem', '', '', '7_2', 11), ('ITA', 412, 'ita', '', '', '7_2', 5), ('TRANSFIGO', 413, 'transfixi', '', '', '7_2', 2), ('PERMANEO', 414, 'permanserunt', '', '', '7_2', 1), ('ILLE', 415, 'Illa', '', '', '7_2', 14), ('VERO/3', 416, 'uero', '', '', '7_2', 5), ('FLAMMA', 417, 'flamma', '', '', '7_2', 8), ('QVI/1', 418, 'quae', '', '', '7_2', 26), ('SVI/1', 419, 'se', '', '', '7_2', 9), ('INTER', 420, 'inter', '', '', '7_2', 5), ('SPIRITALIS', 421, 'spiritales', '', '', '7_2', 2), ('EXTENDO', 422, 'extendebat', '', '', '7_2', 3), ('IS', 423, 'eos', '', '', '7_2', 12), ('SVVS', 424, 'sua', '', '', '7_2', 7), ('CALIGO/1', 425, 'caligine', '', '', '7_2', 1), ('OBTEGO', 426, 'obtexit', '', '', '7_2', 1), ('QVI/1', 427, 'Quos', '', '', '7_2', 26), ('ETIAM', 428, 'etiam', '', '', '7_2', 3), ('IN', 429, 'in', '', '', '7_2', 14), ('SEX', 430, 'sex', '', '', '7_2', 1), ('MODVS', 431, 'modis', '', '', '7_2', 2), ('CONSIDERO', 432, 'considerabam', '', '', '7_2', 1), ('NAM', 433, 'Nam', '', '', '7_3', 2), ('ALIVS', 434, 'alios', '', '', '7_3', 7), ('IDEM', 435, 'eadem', '', '', '7_3', 4), ('FLAMMA', 436, 'flamma', '', '', '7_3', 8), ('CRVDELITER', 437, 'crudeliter', '', '', '7_3', 1), ('INCENDIVM', 438, 'incendio', '', '', '7_3', 1), ('LAEDO', 439, 'laesit', '', '', '7_3', 3), ('QVI/1', 440, 'quos', '', '', '7_3', 26), ('AVTEM', 441, 'autem', '', '', '7_3', 11), ('LAEDO', 442, 'laedere', '', '', '7_3', 3), ('NON', 443, 'non', '', '', '7_3', 3), ('POSSVM/1', 444, 'potuit', '', '', '7_3', 4), ('HIC/1', 445, 'hos', '', '', '7_3', 3), ('AVT', 446, 'aut', '', '', '7_3', 5), ('VIRIDIS', 447, 'uiridi', '', '', '7_3', 2), ('AVT', 448, 'aut', '', '', '7_3', 5), ('ALBVS', 449, 'albo', '', '', '7_3', 2), ('AVT', 450, 'aut', '', '', '7_3', 5), ('RVBEVS', 451, 'rubeo', '', '', '7_3', 2), ('AVT', 452, 'aut', '', '', '7_3', 5), ('CROCEVS', 453, 'croceo', '', '', '7_3', 2), ('AVT', 454, 'aut', '', '', '7_3', 5), ('NIGER', 455, 'nigro', '', '', '7_3', 4), ('MORTIFER', 456, 'mortifero', '', '', '7_3', 2), ('VENENVM', 457, 'ueneno', '', '', '7_3', 3), ('ILLE', 458, 'illo', '', '', '7_3', 14), ('QVI/1', 459, 'quod', '', '', '7_3', 26), ('AB', 460, 'a', '', '', '7_3', 10), ('CAPVT', 461, 'capite', '', '', '7_3', 3), ('IDEM', 462, 'eiusdem', '', '', '7_3', 4), ('VERMIS', 463, 'uermis', '', '', '7_3', 4), ('VSQVE', 464, 'usque', '', '', '7_3', 5), ('AD/2', 465, 'ad', '', '', '7_3', 10), ('PES', 466, 'pedes', '', '', '7_3', 7), ('IS', 467, 'eius', '', '', '7_3', 12), ('DESCENDO', 468, 'descendebat', '', '', '7_3', 3), ('ARDEO', 469, 'ardenter', '', '', '7_3', 3), ('AFFLO', 470, 'afflauit', '', '', '7_3', 1), ('SED', 471, 'Sed', '', '', '7_3', 8), ('FLAMMA', 472, 'flamma', '', '', '7_3', 8), ('QVI/1', 473, 'quae', '', '', '7_3', 26), ('ABYSSVS', 474, 'abyssum', '', '', '7_3', 3), ('PETO', 475, 'petebat', '', '', '7_3', 3), ('DIVERTO', 476, 'diuersas', '', '', '7_3', 2), ('POENA', 477, 'poenas', '', '', '7_3', 1), ('ILLE', 478, 'illorum', '', '', '7_3', 14), ('IN', 479, 'in', '', '', '7_3', 14), ('SVI/1', 480, 'se', '', '', '7_3', 9), ('HABEO', 481, 'habebat', '', '', '7_3', 2), ('QVI/1', 482, 'qui', '', '', '7_3', 26), ('PER', 483, 'per', '', '', '7_3', 2), ('FONS', 484, 'fontem', '', '', '7_3', 1), ('BAPTISMA', 485, 'baptismatis', '', '', '7_3', 1), ('NON', 486, 'non', '', '', '7_3', 3), ('LAVTVS', 487, 'loti', '', '', '7_3', 1), ('LVX', 488, 'lucem', '', '', '7_3', 3), ('VERITAS', 489, 'ueritatis', '', '', '7_3', 1), ('ET/2', 490, 'et', '', '', '7_3', 33), ('FIDES/2', 491, 'fidei', '', '', '7_3', 1), ('IGNORO', 492, 'ignorantes', '', '', '7_3', 1), ('SATANAS/N', 493, 'Satanam', '', '', '7_3', 1), ('PRO/1', 494, 'pro', '', '', '7_3', 1), ('DEVS', 495, 'Deo', '', '', '7_3', 1), ('COLO/2', 496, 'coluerant', '', '', '7_3', 1), ('ET/2', 497, 'Et', '', '', '7_4', 33), ('VIDEO', 498, 'uidi', '', '', '7_4', 5), ('ETIAM', 499, 'etiam', '', '', '7_4', 3), ('EX', 500, 'ex', '', '', '7_4', 3), ('OS/1', 501, 'ore', '', '', '7_4', 4), ('IPSE', 502, 'ipsius', '', '', '7_4', 7), ('ACVTVS', 503, 'acutissimas', '', '', '7_4', 1), ('SAGITTA', 504, 'sagittas', '', '', '7_4', 1), ('PERSTREPO', 505, 'perstrepentes', '', '', '7_4', 1), ('ET/2', 506, 'et', '', '', '7_4', 33), ('AB', 507, 'a', '', '', '7_4', 10), ('PECTVS', 508, 'pectore', '', '', '7_4', 2), ('IS', 509, 'eius', '', '', '7_4', 12), ('NIGER', 510, 'nigrum', '', '', '7_4', 4), ('FVMVS', 511, 'fumum', '', '', '7_4', 1), ('VOLO/2', 512, 'uolantem', '', '', '7_4', 1), ('ATQVE/1', 513, 'ac', '', '', '7_4', 4), ('AB', 514, 'a', '', '', '7_4', 10), ('LVMBVS', 515, 'lumbis', '', '', '7_4', 1), ('IPSE', 516, 'ipsius', '', '', '7_4', 7), ('ARDEO', 517, 'ardentem', '', '', '7_4', 3), ('HVMOR', 518, 'umorem', '', '', '7_4', 1), ('EBVLLIO', 519, 'ebullientem', '', '', '7_4', 1), ('ET/2', 520, 'et', '', '', '7_4', 33), ('AB', 521, 'ab', '', '', '7_4', 10), ('VMBILICVS', 522, 'umbilico', '', '', '7_4', 1), ('IS', 523, 'eius', '', '', '7_4', 12), ('FERVIDVS', 524, 'feruidum', '', '', '7_4', 1), ('TVRBO/1', 525, 'turbinem', '', '', '7_4', 1), ('FLO', 526, 'flantem', '', '', '7_4', 1), ('ATQVE/1', 527, 'atque', '', '', '7_4', 4), ('AB', 528, 'ab', '', '', '7_4', 10), ('EXTREMITAS', 529, 'extremitate', '', '', '7_4', 1), ('VENTER', 530, 'uentris', '', '', '7_4', 2), ('IPSE', 531, 'ipsius', '', '', '7_4', 7), ('VELVT/1', 532, 'uelut', '', '', '7_4', 4), ('IMMVNDITIA', 533, 'immunditiam', '', '', '7_4', 1), ('RANA', 534, 'ranarum', '', '', '7_4', 1), ('SCATVRIO', 535, 'scaturientem', '', '', '7_4', 1), ('QVI/1', 536, 'quae', '', '', '7_4', 26), ('OMNIS', 537, 'omnia', '', '', '7_4', 2), ('MAGNVS', 538, 'magnam', '', '', '7_4', 3), ('INQVIETVDO', 539, 'inquietudinem', '', '', '7_4', 1), ('IN', 540, 'in', '', '', '7_4', 14), ('HOMO', 541, 'hominibus', '', '', '7_4', 11), ('FACIO', 542, 'faciebant', '', '', '7_4', 2), ('SED', 543, 'Sed', '', '', '7_4', 8), ('ET/2', 544, 'et', '', '', '7_4', 33), ('DE', 545, 'de', '', '', '7_4', 3), ('IPSE', 546, 'ipso', '', '', '7_4', 7), ('TETER', 547, 'taeterrima', '', '', '7_5', 2), ('NEBVLA', 548, 'nebula', '', '', '7_5', 1), ('CVM/2', 549, 'cum', '', '', '7_5', 1), ('PESSIMVS', 550, 'pessimo', '', '', '7_5', 1), ('FETOR', 551, 'foetore', '', '', '7_5', 1), ('EGREDIOR', 552, 'egrediens', '', '', '7_5', 1), ('MVLTVS', 553, 'multos', '', '', '7_5', 5), ('HOMO', 554, 'homines', '', '', '7_5', 11), ('SVVS', 555, 'sua', '', '', '7_5', 7), ('PERVERSITAS', 556, 'peruersitate', '', '', '7_5', 1), ('INFICIO', 557, 'infecit', '', '', '7_5', 1), ('ET/2', 558, 'Et', '', '', '7_5', 33), ('ECCE', 559, 'ecce', '', '', '7_5', 1), ('MAGNVS', 560, 'magna', '', '', '7_5', 3), ('MVLTITVDO', 561, 'multitudo', '', '', '7_5', 3), ('HOMO', 562, 'hominum', '', '', '7_5', 11), ('IN', 563, 'in', '', '', '7_5', 14), ('MVLTVS', 564, 'multa', '', '', '7_5', 5), ('CLARITAS', 565, 'claritate', '', '', '7_5', 1), ('FVLGEO', 566, 'fulgentium', '', '', '7_5', 1), ('VENIO', 567, 'ueniebat', '', '', '7_5', 1), ('QVI/1', 568, 'quae', '', '', '7_5', 26), ('IDEM', 569, 'eundem', '', '', '7_5', 4), ('VERMIS', 570, 'uermem', '', '', '7_5', 4), ('FORTITER', 571, 'fortiter', '', '', '7_5', 1), ('VBIQVE', 572, 'ubique', '', '', '7_5', 1), ('CONCVLCO', 573, 'conculcans', '', '', '7_5', 1), ('ACRITER', 574, 'acriter', '', '', '7_5', 1), ('IS', 575, 'eum', '', '', '7_5', 12), ('CRVCIO', 576, 'cruciabat', '', '', '7_5', 1), ('ITA', 577, 'ita', '', '', '7_5', 5), ('TAMEN', 578, 'tamen', '', '', '7_5', 2), ('QVI/1', 579, 'quod', '', '', '7_5', 26), ('IPSE', 580, 'ipsa', '', '', '7_5', 7), ('NEQVE', 581, 'nec', '', '', '7_5', 4), ('AB', 582, 'a', '', '', '7_5', 10), ('FLAMMA', 583, 'flammis', '', '', '7_5', 8), ('NEQVE', 584, 'nec', '', '', '7_5', 4), ('AB', 585, 'a', '', '', '7_5', 10), ('VENENVM', 586, 'ueneno', '', '', '7_5', 3), ('ILLE', 587, 'illius', '', '', '7_5', 14), ('LAEDO', 588, 'laedi', '', '', '7_5', 3), ('POSSVM/1', 589, 'poterat', '', '', '7_5', 4), ('AVDIO', 590, 'Audiui', '', '', '7_5', 1), ('QVE', 591, 'que', '', '', '7_5', 1), ('ITERVM', 592, 'iterum', '', '', '7_5', 2), ('VOX', 593, 'uocem', '', '', '7_5', 2), ('EGO', 594, 'mihi', '', '', '7_5', 1), ('DE', 595, 'de', '', '', '7_5', 3), ('CAELVM/1', 596, 'caelo', '', '', '7_5', 1), ('DICO/2', 597, 'dicentem', '', '', '7_5', 1)]
section_list ={'1': 'start', '7.1': 'start', '7.2': '7.1', '7.3': '7.2', '7.4': '7.3', '7.5': '7.4', 'end': '7.5', 'start': 'start'}
title = "Hildegard of Bingen, Scivias 7.2"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)