import text
nan=""
section_words = {'start': -1, '1': 48, '2': 54, '3': 74, '4': 98, '5': 308, '6': 385, '7': 410, '8': 429, '9': 460, '10': 470, '11': 510, 'end': -2}
the_text =  [('REQVIES', 0, 'Requiem', '', '', '1', 10), ('AETERNVS', 1, 'aeternam', '', '', '1', 11), ('DONO', 2, 'dona', '', '', '1', 10), ('IS', 3, 'eis', '', '', '1', 21), ('DOMINVS', 4, 'Domine', '', '', '1', 13), ('ET/2', 5, 'Et', '', '', '1', 20), ('LVX', 6, 'lux', '', '', '1', 8), ('PERPETVVS', 7, 'perpetua', '', '', '1', 5), ('LVCEO', 8, 'luceat', '', '', '1', 5), ('IS', 9, 'eis', '', '', '1', 21), ('TV', 10, 'Te', '', '', '1', 6), ('DECET', 11, 'decet', '', '', '1', 1), ('HYMNVS', 12, 'hymnus', '', '', '1', 1), ('DEVS', 13, 'Deus', '', '', '1', 6), ('IN', 14, 'in', '', '', '1', 14), ('SION/N', 15, 'Sion', '', '', '1', 1), ('ET/2', 16, 'Et', '', '', '1', 20), ('TV', 17, 'tibi', '', '', '1', 6), ('REDDO', 18, 'reddetur', '', '', '1', 1), ('VOTVM', 19, 'uotum', '', '', '1', 1), ('IN', 20, 'in', '', '', '1', 14), ('HIERVSALEM/N', 21, 'Ierusalem', '', '', '1', 1), ('EXAVDIO', 22, 'Exaudi', '', '', '1', 2), ('ORATIO', 23, 'orationem', '', '', '1', 1), ('MEVS', 24, 'meam', '', '', '1', 3), ('AD/2', 25, 'Ad', '', '', '1', 2), ('TV', 26, 'te', '', '', '1', 6), ('OMNIS', 27, 'omnis', '', '', '1', 5), ('CARO/1', 28, 'caro', '', '', '1', 1), ('VENIO', 29, 'ueniet', '', '', '1', 6), ('REQVIES', 30, 'Requiem', '', '', '1', 10), ('AETERNVS', 31, 'aeternam', '', '', '1', 11), ('DONO', 32, 'dona', '', '', '1', 10), ('DEFVNGOR', 33, 'defunctis', '', '', '1', 3), ('DOMINVS', 34, 'Domine', '', '', '1', 13), ('ET/2', 35, 'Et', '', '', '1', 20), ('LVX', 36, 'lux', '', '', '1', 8), ('PERPETVVS', 37, 'perpetua', '', '', '1', 5), ('LVCEO', 38, 'luceat', '', '', '1', 5), ('IS', 39, 'eis', '', '', '1', 21), ('REQVIES', 40, 'Requiem', '', '', '1', 10), ('AETERNVS', 41, 'aeternam', '', '', '1', 11), ('DONO', 42, 'dona', '', '', '1', 10), ('IS', 43, 'eis', '', '', '1', 21), ('DOMINVS', 44, 'Domine', '', '', '1', 13), ('ET/2', 45, 'Et', '', '', '1', 20), ('LVX', 46, 'lux', '', '', '1', 8), ('PERPETVVS', 47, 'perpetua', '', '', '1', 5), ('IS', 48, 'eis', '', '', '1', 21), ('KYRIOS/G', 49, 'Kyrie', '', '', '2', 2), ('ELEEO/G', 50, 'eleison', '', '', '2', 3), ('CHRISTVS/N', 51, 'Christe', '', '', '2', 2), ('ELEEO/G', 52, 'eleison', '', '', '2', 3), ('KYRIOS/G', 53, 'Kyrie', '', '', '2', 2), ('ELEEO/G', 54, 'eleison', '', '', '2', 3), ('REQVIES', 55, 'Requiem', '', '', '3', 10), ('AETERNVS', 56, 'æternam', '', '', '3', 11), ('DONO', 57, 'dona', '', '', '3', 10), ('IS', 58, 'eis', '', '', '3', 21), ('DOMINVS', 59, 'Domine', '', '', '3', 13), ('ET/2', 60, 'et', '', '', '3', 20), ('LVX', 61, 'lux', '', '', '3', 8), ('PERPETVVS', 62, 'perpetua', '', '', '3', 5), ('LVCEO', 63, 'luceat', '', '', '3', 5), ('IS', 64, 'eis', '', '', '3', 21), ('IN', 65, 'In', '', '', '3', 14), ('MEMORIA', 66, 'memoria', '', '', '3', 2), ('AETERNVS', 67, 'æterna', '', '', '3', 11), ('SVM/1', 68, 'erit', '', '', '3', 15), ('IVSTVS', 69, 'iustus', '', '', '3', 3), ('AB', 70, 'ab', '', '', '3', 3), ('AVDITIO', 71, 'auditione', '', '', '3', 1), ('MALVM/1', 72, 'mala', '', '', '3', 1), ('NON', 73, 'non', '', '', '3', 3), ('TIMEO', 74, 'timebit', '', '', '3', 2), ('ABSOLVO', 75, 'Absolue', '', '', '4', 2), ('DOMINVS', 76, 'Domine', '', '', '4', 13), ('ANIMA', 77, 'animas', '', '', '4', 3), ('OMNIS', 78, 'omnium', '', '', '4', 5), ('FIDELIS/2', 79, 'fidelium', '', '', '4', 2), ('DEFVNGOR', 80, 'defunctorum', '', '', '4', 3), ('AB', 81, 'ab', '', '', '4', 3), ('OMNIS', 82, 'omni', '', '', '4', 5), ('VINCVLVM', 83, 'uinculo', '', '', '4', 1), ('DELICTOR', 84, 'delictorum', '', '', '4', 1), ('ET/2', 85, 'Et', '', '', '4', 20), ('GRATIA', 86, 'gratia', '', '', '4', 1), ('TVVS', 87, 'tua', '', '', '4', 5), ('ILLE', 88, 'illis', '', '', '4', 6), ('SVCCVRRO', 89, 'succurrente', '', '', '4', 1), ('MEREO', 90, 'mereantur', '', '', '4', 1), ('EVADO/2', 91, 'euadere', '', '', '4', 1), ('IVDICIVM', 92, 'iudicium', '', '', '4', 1), ('VLTIO', 93, 'ultionis', '', '', '4', 2), ('ET/2', 94, 'Et', '', '', '4', 20), ('LVX', 95, 'lucis', '', '', '4', 8), ('AETERNVS', 96, 'æternae', '', '', '4', 11), ('BEATITVDO', 97, 'beatitudine', '', '', '4', 1), ('PERFRVOR', 98, 'perfrui', '', '', '4', 1), ('DIES', 99, 'Dies', '', '', '5', 6), ('IRA', 100, 'irae', '', '', '5', 2), ('DIES', 101, 'dies', '', '', '5', 6), ('ILLE', 102, 'illa', '', '', '5', 6), ('SOLVO', 103, 'Soluet', '', '', '5', 1), ('SAECVLVM', 104, 'saeclum', '', '', '5', 2), ('IN', 105, 'in', '', '', '5', 14), ('FAVILLA', 106, 'fauilla', '', '', '5', 2), ('TESTIS/1', 107, 'Teste', '', '', '5', 1), ('DAVID/N', 108, 'Dauid', '', '', '5', 1), ('CVM/2', 109, 'cum', '', '', '5', 3), ('SIBYLLA/N', 110, 'Sibylla', '', '', '5', 1), ('QVANTVS/1', 111, 'Quantus', '', '', '5', 1), ('TREMOR', 112, 'tremor', '', '', '5', 1), ('SVM/1', 113, 'est', '', '', '5', 15), ('SVM/1', 114, 'futurus', '', '', '5', 15), ('QVANDO/1', 115, 'Quando', '', '', '5', 3), ('IVDEX', 116, 'iudex', '', '', '5', 3), ('SVM/1', 117, 'est', '', '', '5', 15), ('VENIO', 118, 'uenturus', '', '', '5', 6), ('CVNCTVS', 119, 'Cuncta', '', '', '5', 1), ('STRINGO', 120, 'stricte', '', '', '5', 1), ('DISCVTIO', 121, 'discussurus', '', '', '5', 2), ('TVBA', 122, 'Tuba', '', '', '5', 1), ('MIRVS', 123, 'mirum', '', '', '5', 1), ('SPARGO/2', 124, 'spargens', '', '', '5', 1), ('SONVS', 125, 'sonum', '', '', '5', 1), ('PER', 126, 'Per', '', '', '5', 2), ('SEPVLCRVM', 127, 'sepulcra', '', '', '5', 1), ('REGIO', 128, 'regionum', '', '', '5', 1), ('COGO', 129, 'Coget', '', '', '5', 1), ('OMNIS', 130, 'omnes', '', '', '5', 5), ('ANTE/2', 131, 'ante', '', '', '5', 2), ('THRONVS', 132, 'thronum', '', '', '5', 1), ('MORS', 133, 'Mors', '', '', '5', 3), ('STVPEO', 134, 'stupebit', '', '', '5', 1), ('ET/2', 135, 'et', '', '', '5', 20), ('NATVRA', 136, 'natura', '', '', '5', 1), ('CVM/3', 137, 'Cum', '', '', '5', 4), ('RESVRGO', 138, 'resurget', '', '', '5', 2), ('CREO', 139, 'creatura', '', '', '5', 1), ('IVDICO', 140, 'Iudicanti', '', '', '5', 4), ('RESPONDEO', 141, 'responsura', '', '', '5', 1), ('LIBER/1', 142, 'Liber', '', '', '5', 1), ('SCRIBO', 143, 'scriptus', '', '', '5', 1), ('PROFERO', 144, 'proferetur', '', '', '5', 1), ('IN', 145, 'In', '', '', '5', 14), ('QVI/1', 146, 'quo', '', '', '5', 12), ('TOTVS', 147, 'totum', '', '', '5', 1), ('CONTINEO', 148, 'continetur', '', '', '5', 1), ('VNDE/1', 149, 'Unde', '', '', '5', 1), ('MVNDVS/1', 150, 'mundus', '', '', '5', 3), ('IVDICO', 151, 'iudicetur', '', '', '5', 4), ('IVDEX', 152, 'Iudex', '', '', '5', 3), ('ERGO/2', 153, 'ergo', '', '', '5', 2), ('CVM/3', 154, 'cum', '', '', '5', 4), ('SEDEO', 155, 'sedebit', '', '', '5', 2), ('QVISQVIS/2', 156, 'Quidquid', '', '', '5', 1), ('LATEO', 157, 'latet', '', '', '5', 1), ('APPAREO', 158, 'apparebit', '', '', '5', 1), ('NIHIL', 159, 'Nil', '', '', '5', 1), ('INVLTVS', 160, 'inultum', '', '', '5', 1), ('REMANEO', 161, 'remanebit', '', '', '5', 1), ('QVIS/1', 162, 'Quid', '', '', '5', 1), ('SVM/1', 163, 'sum', '', '', '5', 15), ('MISER', 164, 'miser', '', '', '5', 1), ('TVM', 165, 'tunc', '', '', '5', 1), ('DICO/2', 166, 'dicturus', '', '', '5', 1), ('QVI/1', 167, 'Quem', '', '', '5', 12), ('PATRONVS', 168, 'patronum', '', '', '5', 1), ('ROGO', 169, 'rogaturus', '', '', '5', 1), ('CVM/3', 170, 'Cum', '', '', '5', 4), ('VIX', 171, 'uix', '', '', '5', 1), ('IVSTVS', 172, 'iustus', '', '', '5', 3), ('SVM/1', 173, 'sit', '', '', '5', 15), ('SECVRVS', 174, 'securus', '', '', '5', 1), ('REX', 175, 'Rex', '', '', '5', 2), ('TREMO', 176, 'tremendae', '', '', '5', 3), ('MAIESTAS', 177, 'maiestatus', '', '', '5', 1), ('QVI/1', 178, 'qui', '', '', '5', 12), ('SALVO', 179, 'saluandos', '', '', '5', 3), ('SALVO', 180, 'saluas', '', '', '5', 3), ('GRATVS', 181, 'gratis', '', '', '5', 1), ('SALVO', 182, 'sale', '', '', '5', 3), ('EGO', 183, 'me', '', '', '5', 9), ('FONS', 184, 'fons', '', '', '5', 1), ('PIETAS', 185, 'pietatis', '', '', '5', 1), ('RECORDOR', 186, 'Recordare', '', '', '5', 1), ('IESVS/N', 187, 'Iesu', '', '', '5', 4), ('PIVS', 188, 'pie', '', '', '5', 5), ('QVI/1', 189, 'Quod', '', '', '5', 12), ('SVM/1', 190, 'sum', '', '', '5', 15), ('CAVSA', 191, 'causa', '', '', '5', 1), ('TVVS', 192, 'tuae', '', '', '5', 5), ('VIA', 193, 'uiae', '', '', '5', 1), ('NE/4', 194, 'Ne', '', '', '5', 4), ('EGO', 195, 'me', '', '', '5', 9), ('PERDO', 196, 'perdas', '', '', '5', 1), ('ILLE', 197, 'illa', '', '', '5', 6), ('DIES', 198, 'die', '', '', '5', 6), ('QVAERO', 199, 'Quaerens', '', '', '5', 1), ('EGO', 200, 'me', '', '', '5', 9), ('SEDEO', 201, 'sedisti', '', '', '5', 2), ('LASSVS', 202, 'lassus', '', '', '5', 1), ('REDIMO', 203, 'Redemisti', '', '', '5', 1), ('CRVX', 204, 'crucem', '', '', '5', 1), ('PATIOR', 205, 'passus', '', '', '5', 1), ('TANTVS', 206, 'Tantus', '', '', '5', 1), ('LABOR/1', 207, 'labor', '', '', '5', 1), ('NON', 208, 'non', '', '', '5', 3), ('SVM/1', 209, 'sit', '', '', '5', 15), ('CASSVS', 210, 'cassus', '', '', '5', 1), ('IVSTVS', 211, 'Iuste', '', '', '5', 3), ('IVDEX', 212, 'Iudex', '', '', '5', 3), ('VLTIO', 213, 'ultionis', '', '', '5', 2), ('DONVM', 214, 'Donum', '', '', '5', 1), ('FACIO', 215, 'fac', '', '', '5', 5), ('REMISSIO', 216, 'remissionis', '', '', '5', 1), ('ANTE/2', 217, 'Ante', '', '', '5', 2), ('DIES', 218, 'diem', '', '', '5', 6), ('RATIO', 219, 'rationis', '', '', '5', 1), ('INGEMISCO', 220, 'Ingemisco', '', '', '5', 1), ('TAMQVAM/1', 221, 'tanquam', '', '', '5', 1), ('REVS', 222, 'reus', '', '', '5', 2), ('CVLPA', 223, 'Culpa', '', '', '5', 1), ('RVBEO', 224, 'rubet', '', '', '5', 1), ('VVLTVS', 225, 'uultus', '', '', '5', 1), ('MEVS', 226, 'meus', '', '', '5', 3), ('SVPPLICO', 227, 'Supplicanti', '', '', '5', 1), ('PARCO', 228, 'parce', '', '', '5', 2), ('DEVS', 229, 'Deus', '', '', '5', 6), ('QVI/1', 230, 'Qui', '', '', '5', 12), ('MARIA/N', 231, 'Mariam', '', '', '5', 1), ('ABSOLVO', 232, 'absoluisti', '', '', '5', 2), ('ET/2', 233, 'Et', '', '', '5', 20), ('LATRO/1', 234, 'latronem', '', '', '5', 1), ('EXAVDIO', 235, 'exaudisti', '', '', '5', 2), ('EGO', 236, 'Mihi', '', '', '5', 9), ('QVOQVE', 237, 'quoque', '', '', '5', 1), ('SPES', 238, 'spem', '', '', '5', 1), ('DO', 239, 'dedisti', '', '', '5', 1), ('PREX', 240, 'Preces', '', '', '5', 2), ('MEVS', 241, 'meae', '', '', '5', 3), ('NON', 242, 'non', '', '', '5', 3), ('SVM/1', 243, 'sunt', '', '', '5', 15), ('DIGNVS', 244, 'dignae', '', '', '5', 1), ('SED', 245, 'Sed', '', '', '5', 2), ('TV', 246, 'tu', '', '', '5', 6), ('BONVS', 247, 'bonus', '', '', '5', 1), ('FACIO', 248, 'fac', '', '', '5', 5), ('BENIGNVS', 249, 'benigne', '', '', '5', 1), ('NE/4', 250, 'Ne', '', '', '5', 4), ('PERENNIS', 251, 'perenni', '', '', '5', 1), ('CREMO', 252, 'cremer', '', '', '5', 1), ('IGNIS', 253, 'igne', '', '', '5', 2), ('INTER', 254, 'Inter', '', '', '5', 1), ('OVIS', 255, 'oues', '', '', '5', 1), ('LOCVS', 256, 'locum', '', '', '5', 1), ('PRAESTO/1', 257, 'praesta', '', '', '5', 1), ('ET/2', 258, 'Et', '', '', '5', 20), ('AB', 259, 'ab', '', '', '5', 3), ('HAEDVS', 260, 'hoedis', '', '', '5', 1), ('EGO', 261, 'me', '', '', '5', 9), ('SEQVESTRO', 262, 'sequestra', '', '', '5', 1), ('STATVO', 263, 'Statuens', '', '', '5', 1), ('IN', 264, 'in', '', '', '5', 14), ('PARS', 265, 'parte', '', '', '5', 1), ('DEXTER', 266, 'dextra', '', '', '5', 1), ('CONFVTO', 267, 'Confutatis', '', '', '5', 1), ('MALEDICO', 268, 'maledictis', '', '', '5', 1), ('FLAMMA', 269, 'Flammis', '', '', '5', 1), ('ACER/2', 270, 'acribus', '', '', '5', 1), ('ADICIO', 271, 'addictis', '', '', '5', 1), ('VOCO', 272, 'Uoca', '', '', '5', 1), ('EGO', 273, 'me', '', '', '5', 9), ('CVM/3', 274, 'cum', '', '', '5', 4), ('BENEDICO', 275, 'benedictus', '', '', '5', 2), ('ORO', 276, 'Oro', '', '', '5', 1), ('SVPPLEX/2', 277, 'supplex', '', '', '5', 1), ('ET/2', 278, 'et', '', '', '5', 20), ('ACCLINIS', 279, 'acclinis', '', '', '5', 1), ('COR', 280, 'Cor', '', '', '5', 1), ('CONTERO', 281, 'contritum', '', '', '5', 1), ('QVASI/1', 282, 'quasi', '', '', '5', 1), ('CINIS', 283, 'cinis', '', '', '5', 1), ('GERO', 284, 'Gere', '', '', '5', 1), ('CVRA', 285, 'curam', '', '', '5', 1), ('EGO', 286, 'mei', '', '', '5', 9), ('FINIS', 287, 'finis', '', '', '5', 1), ('LACRIMOSVS', 288, 'Lacrimosa', '', '', '5', 1), ('DIES', 289, 'dies', '', '', '5', 6), ('ILLE', 290, 'illa', '', '', '5', 6), ('QVI/1', 291, 'Qua', '', '', '5', 12), ('RESVRGO', 292, 'resurget', '', '', '5', 2), ('EX', 293, 'ex', '', '', '5', 1), ('FAVILLA', 294, 'fauilla', '', '', '5', 2), ('IVDICO', 295, 'Iudicandus', '', '', '5', 4), ('HOMO', 296, 'homo', '', '', '5', 1), ('REVS', 297, 'reus', '', '', '5', 2), ('HIC/1', 298, 'Huic', '', '', '5', 1), ('ERGO/2', 299, 'ergo', '', '', '5', 2), ('PARCO', 300, 'parce', '', '', '5', 2), ('DEVS', 301, 'Deus', '', '', '5', 6), ('PIVS', 302, 'Pie', '', '', '5', 5), ('IESVS/N', 303, 'Iesu', '', '', '5', 4), ('DOMINVS', 304, 'Domine', '', '', '5', 13), ('DONO', 305, 'Dona', '', '', '5', 10), ('IS', 306, 'eis', '', '', '5', 21), ('REQVIES', 307, 'requiem', '', '', '5', 10), ('AMEN', 308, 'Amen', '', '', '5', 1), ('DOMVS', 309, 'Domine', '', '', '6', 1), ('IESVS/N', 310, 'Iesu', '', '', '6', 4), ('CHRISTVS/N', 311, 'Christe', '', '', '6', 2), ('REX', 312, 'Rex', '', '', '6', 2), ('GLORIA', 313, 'gloriae', '', '', '6', 2), ('LIBERO', 314, 'libera', '', '', '6', 3), ('ANIMA', 315, 'animas', '', '', '6', 3), ('OMNIS', 316, 'omnium', '', '', '6', 5), ('FIDELIS/2', 317, 'fidelium', '', '', '6', 2), ('DEFVNGOR', 318, 'defunctorum', '', '', '6', 3), ('DE', 319, 'de', '', '', '6', 5), ('POENA', 320, 'poenis', '', '', '6', 1), ('INFERNVS', 321, 'inferni', '', '', '6', 1), ('ET/2', 322, 'et', '', '', '6', 20), ('DE', 323, 'de', '', '', '6', 5), ('PROFVNDVS', 324, 'profundo', '', '', '6', 1), ('LACVS', 325, 'lacu', '', '', '6', 1), ('LIBERO', 326, 'Libera', '', '', '6', 3), ('IS', 327, 'eas', '', '', '6', 21), ('DE', 328, 'de', '', '', '6', 5), ('OS/1', 329, 'ore', '', '', '6', 1), ('LEO', 330, 'leonis', '', '', '6', 1), ('NE/4', 331, 'ne', '', '', '6', 4), ('ABSORBEO', 332, 'absorbeat', '', '', '6', 1), ('IS', 333, 'eas', '', '', '6', 21), ('TARTARVS/N', 334, 'tartarus', '', '', '6', 1), ('NE/4', 335, 'ne', '', '', '6', 4), ('CADO', 336, 'cadant', '', '', '6', 1), ('IN', 337, 'in', '', '', '6', 14), ('OBSCVRVS', 338, 'obscurum', '', '', '6', 1), ('SED', 339, 'Sed', '', '', '6', 2), ('SIGNIFER/1', 340, 'signifer', '', '', '6', 1), ('SANCTVS', 341, 'sanctus', '', '', '6', 6), ('MICHAEL/N', 342, 'Michael', '', '', '6', 1), ('REPRAESENTO', 343, 'repraesentet', '', '', '6', 1), ('IS', 344, 'eas', '', '', '6', 21), ('IN', 345, 'in', '', '', '6', 14), ('LVX', 346, 'lucem', '', '', '6', 8), ('SANCIO', 347, 'sanctam', '', '', '6', 1), ('QVI/1', 348, 'Quam', '', '', '6', 12), ('OLIM', 349, 'olim', '', '', '6', 2), ('ABRAHAM/N', 350, 'Abrahae', '', '', '6', 2), ('PROMITTO', 351, 'promisisti', '', '', '6', 2), ('ET/2', 352, 'et', '', '', '6', 20), ('SEMEN/1', 353, 'semini', '', '', '6', 2), ('IS', 354, 'eius', '', '', '6', 21), ('HOSTIA', 355, 'Hostias', '', '', '6', 2), ('ET/2', 356, 'et', '', '', '6', 20), ('PREX', 357, 'preces', '', '', '6', 2), ('TV', 358, 'tibi', '', '', '6', 6), ('HOSTIA', 359, 'Domine', '', '', '6', 2), ('LAVS', 360, 'laudis', '', '', '6', 1), ('OFFERO', 361, 'offerimus', '', '', '6', 1), ('TV', 362, 'tu', '', '', '6', 6), ('SVSCIPIO', 363, 'suscipe', '', '', '6', 1), ('PRO/1', 364, 'pro', '', '', '6', 1), ('ANIMA', 365, 'animabus', '', '', '6', 3), ('ILLE', 366, 'illis', '', '', '6', 6), ('QVI/1', 367, 'quarum', '', '', '6', 12), ('HODIE', 368, 'hodie', '', '', '6', 1), ('MEMORIA', 369, 'memoriam', '', '', '6', 2), ('FACIO', 370, 'facimus', '', '', '6', 5), ('FACIO', 371, 'Fac', '', '', '6', 5), ('IS', 372, 'eas', '', '', '6', 21), ('DOMINVS', 373, 'Domine', '', '', '6', 13), ('DE', 374, 'de', '', '', '6', 5), ('MORS', 375, 'morte', '', '', '6', 3), ('TRANSEO/1', 376, 'transire', '', '', '6', 1), ('AD/2', 377, 'ad', '', '', '6', 2), ('VITA', 378, 'uitam', '', '', '6', 1), ('QVI/1', 379, 'Quam', '', '', '6', 12), ('OLIM', 380, 'olim', '', '', '6', 2), ('ABRAHAM/N', 381, 'Abrahae', '', '', '6', 2), ('PROMITTO', 382, 'promisisti', '', '', '6', 2), ('ET/2', 383, 'et', '', '', '6', 20), ('SEMEN/1', 384, 'semine', '', '', '6', 2), ('IS', 385, 'eius', '', '', '6', 21), ('SANCTVS', 386, 'Sanctus', '', '', '7', 6), ('SANCTVS', 387, 'sanctus', '', '', '7', 6), ('SANCTVS', 388, 'sanctus', '', '', '7', 6), ('DOMINVS', 389, 'Dominus', '', '', '7', 13), ('DEVS', 390, 'Deus', '', '', '7', 6), ('SABAOTH', 391, 'Sabaoth', '', '', '7', 1), ('PLENVS', 392, 'Pleni', '', '', '7', 1), ('SVM/1', 393, 'sunt', '', '', '7', 15), ('CAELVM/1', 394, 'coeli', '', '', '7', 3), ('ET/2', 395, 'et', '', '', '7', 20), ('TERRA', 396, 'terra', '', '', '7', 3), ('GLORIA', 397, 'gloria', '', '', '7', 2), ('TVVS', 398, 'tua', '', '', '7', 5), ('HOSANNA', 399, 'Hosanna', '', '', '7', 2), ('IN', 400, 'in', '', '', '7', 14), ('EXCELSVS', 401, 'excelsis', '', '', '7', 2), ('BENEDICO', 402, 'Benedictus', '', '', '7', 2), ('QVI/1', 403, 'qui', '', '', '7', 12), ('VENIO', 404, 'uenit', '', '', '7', 6), ('IN', 405, 'in', '', '', '7', 14), ('NOMEN', 406, 'nomine', '', '', '7', 1), ('DOMINVS', 407, 'Domine', '', '', '7', 13), ('HOSANNA', 408, 'Hosanna', '', '', '7', 2), ('IN', 409, 'in', '', '', '7', 14), ('EXCELSVS', 410, 'excelsis', '', '', '7', 2), ('AGNVS', 411, 'Agnus', '', '', '8', 2), ('DEVS', 412, 'Dei', '', '', '8', 6), ('QVI/1', 413, 'qui', '', '', '8', 12), ('TOLLO', 414, 'tollis', '', '', '8', 2), ('PECCATVM', 415, 'peccatta', '', '', '8', 2), ('MVNDVS/1', 416, 'mundi', '', '', '8', 3), ('DONO', 417, 'dona', '', '', '8', 10), ('IS', 418, 'eis', '', '', '8', 21), ('REQVIES', 419, 'requiem', '', '', '8', 10), ('AGNVS', 420, 'Agnus', '', '', '8', 2), ('DEVS', 421, 'Dei', '', '', '8', 6), ('QVI/1', 422, 'qui', '', '', '8', 12), ('TOLLO', 423, 'tollis', '', '', '8', 2), ('PECCATVM', 424, 'peccata', '', '', '8', 2), ('MVNDVS/1', 425, 'mundi', '', '', '8', 3), ('DONO', 426, 'dona', '', '', '8', 10), ('IS', 427, 'eis', '', '', '8', 21), ('REQVIES', 428, 'requiem', '', '', '8', 10), ('SEMPITERNVS', 429, 'sempitername', '', '', '8', 2), ('LVX', 430, 'Lux', '', '', '9', 8), ('AETERNVS', 431, 'aeterna', '', '', '9', 11), ('LVCEO', 432, 'luceat', '', '', '9', 5), ('IS', 433, 'eis', '', '', '9', 21), ('DOMINVS', 434, 'Domine', '', '', '9', 13), ('CVM/2', 435, 'cum', '', '', '9', 3), ('SANCTVS', 436, 'sanctis', '', '', '9', 6), ('TVVS', 437, 'tuis', '', '', '9', 5), ('IN', 438, 'in', '', '', '9', 14), ('AETERNVS', 439, 'aeternum', '', '', '9', 11), ('QVIA', 440, 'quia', '', '', '9', 2), ('PIVS', 441, 'pius', '', '', '9', 5), ('SVM/1', 442, 'es', '', '', '9', 15), ('REQVIES', 443, 'Requiem', '', '', '9', 10), ('AETERNVS', 444, 'aeternam', '', '', '9', 11), ('DONO', 445, 'dona', '', '', '9', 10), ('IS', 446, 'eis', '', '', '9', 21), ('DOMINVS', 447, 'Domine', '', '', '9', 13), ('ET/2', 448, 'et', '', '', '9', 20), ('LVX', 449, 'lux', '', '', '9', 8), ('PERPETVVS', 450, 'perpetua', '', '', '9', 5), ('LVCEO', 451, 'luceat', '', '', '9', 5), ('IS', 452, 'eis', '', '', '9', 21), ('CVM/2', 453, 'Cum', '', '', '9', 3), ('SANCTVS', 454, 'sanctis', '', '', '9', 6), ('TVVS', 455, 'tuis', '', '', '9', 5), ('IN', 456, 'in', '', '', '9', 14), ('AETERNVS', 457, 'aeternum', '', '', '9', 11), ('QVIA', 458, 'quia', '', '', '9', 2), ('PIVS', 459, 'pius', '', '', '9', 5), ('SVM/1', 460, 'es', '', '', '9', 15), ('PIVS', 461, 'Pie', '', '', '10', 5), ('IESVS/N', 462, 'Iesu', '', '', '10', 4), ('DOMINVS', 463, 'Domine', '', '', '10', 13), ('DONO', 464, 'dona', '', '', '10', 10), ('IS', 465, 'eis', '', '', '10', 21), ('REQVIES', 466, 'requiem', '', '', '10', 10), ('DONO', 467, 'Dona', '', '', '10', 10), ('IS', 468, 'eis', '', '', '10', 21), ('REQVIES', 469, 'requiem', '', '', '10', 10), ('SEMPITERNVS', 470, 'sempiternam', '', '', '10', 2), ('LIBERO', 471, 'Libera', '', '', '11', 3), ('EGO', 472, 'me', '', '', '11', 9), ('DOMINVS', 473, 'Domine', '', '', '11', 13), ('DE', 474, 'de', '', '', '11', 5), ('MORS', 475, 'morte', '', '', '11', 3), ('AETERNVS', 476, 'aeterna', '', '', '11', 11), ('IN', 477, 'in', '', '', '11', 14), ('DIES', 478, 'die', '', '', '11', 6), ('ILLE', 479, 'illa', '', '', '11', 6), ('TREMO', 480, 'tremenda', '', '', '11', 3), ('QVANDO/1', 481, 'quando', '', '', '11', 3), ('CAELVM/1', 482, 'coeli', '', '', '11', 3), ('MOVEO', 483, 'mouendi', '', '', '11', 2), ('SVM/1', 484, 'sunt', '', '', '11', 15), ('ET/2', 485, 'et', '', '', '11', 20), ('TERRA', 486, 'terra', '', '', '11', 3), ('DVM/2', 487, 'dum', '', '', '11', 2), ('VENIO', 488, 'ueneris', '', '', '11', 6), ('IVDICO', 489, 'iudicare', '', '', '11', 4), ('SAECVLVM', 490, 'saeculum', '', '', '11', 2), ('PER', 491, 'per', '', '', '11', 2), ('IGNIS', 492, 'ignem', '', '', '11', 2), ('TREMO', 493, 'Tremens', '', '', '11', 3), ('FACIO', 494, 'factus', '', '', '11', 5), ('SVM/1', 495, 'sum', '', '', '11', 15), ('EGO', 496, 'ego', '', '', '11', 9), ('ET/2', 497, 'et', '', '', '11', 20), ('TIMEO', 498, 'timeo', '', '', '11', 2), ('DVM/2', 499, 'dum', '', '', '11', 2), ('DISCVTIO', 500, 'discussio', '', '', '11', 2), ('VENIO', 501, 'uenerit', '', '', '11', 6), ('ATQVE/1', 502, 'atque', '', '', '11', 1), ('VENIO', 503, 'uenture', '', '', '11', 6), ('IRA', 504, 'ira', '', '', '11', 2), ('QVANDO/1', 505, 'quando', '', '', '11', 3), ('CAELVM/1', 506, 'coeli', '', '', '11', 3), ('MOVEO', 507, 'mouendi', '', '', '11', 2), ('SVM/1', 508, 'sunt', '', '', '11', 15), ('ET/2', 509, 'et', '', '', '11', 20), ('TERRA', 510, 'terra', '', '', '11', 3)]
section_list ={'1': 'start', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': '10', 'end': '11', 'start': 'start'}
title = "Requiem Mass"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)