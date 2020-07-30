import text
nan=""
section_words = {'start': -1, '1.1': 14, '1.2': 39, '2.1': 52, '2.2': 76, '3.1': 98, '3.2': 350, '3.3': 462, '4.1': 496, '4.2': 505, 'end': -2}
the_text =  [('CAVSA', 0, 'Causas', '', '', '1_1', 3), ('RES', 1, 'rerum', '', '', '1_1', 2), ('NATVRALIS', 2, 'naturalium', '', '', '1_1', 2), ('NON', 3, 'non', '', '', '1_1', 10), ('MVLTVS', 4, 'plures', '', '', '1_1', 3), ('ADMITTO', 5, 'admitti', '', '', '1_1', 1), ('DEBEO', 6, 'debere', '', '', '1_1', 3), ('QVAM/1', 7, 'quam', '', '', '1_1', 3), ('QVI/1', 8, 'quæ', '', '', '1_1', 15), ('VERVS', 9, 'ueræ', '', '', '1_1', 2), ('SVM/1', 10, 'sint', '', '', '1_1', 28), ('IS', 11, 'earum', '', '', '1_1', 4), ('PHAENOMENON', 12, 'phænomenis', '', '', '1_1', 5), ('EXPLICO', 13, 'explicandis', '', '', '1_1', 1), ('SVFFICIO', 14, 'sufficiant', '', '', '1_1', 1), ('DICO/2', 15, 'Dicunt', '', '', '1_2', 2), ('VTIQVE', 16, 'utique', '', '', '1_2', 2), ('PHILOSOPHVS/2', 17, 'philosophi', '', '', '1_2', 1), ('NATVRA', 18, 'Natura', '', '', '1_2', 4), ('NIHIL', 19, 'nihil', '', '', '1_2', 1), ('AGO', 20, 'agit', '', '', '1_2', 1), ('FRVSTRA', 21, 'frustra', '', '', '1_2', 2), ('FRVSTRA', 22, 'frustra', '', '', '1_2', 2), ('SVM/1', 23, 'sit', '', '', '1_2', 28), ('PER', 24, 'per', '', '', '1_2', 11), ('MVLTVS', 25, 'plura', '', '', '1_2', 3), ('QVI/1', 26, 'quod', '', '', '1_2', 15), ('FIO', 27, 'fieri', '', '', '1_2', 3), ('POSSVM/1', 28, 'potest', '', '', '1_2', 8), ('PER', 29, 'per', '', '', '1_2', 11), ('PAVCI', 30, 'pauciora', '', '', '1_2', 1), ('NATVRA', 31, 'Natura', '', '', '1_2', 4), ('ENIM/2', 32, 'enim', '', '', '1_2', 1), ('SIMPLEX', 33, 'simplex', '', '', '1_2', 2), ('SVM/1', 34, 'est', '', '', '1_2', 28), ('RES', 35, 'rerum', '', '', '1_2', 2), ('CAVSA', 36, 'causis', '', '', '1_2', 3), ('SVPERFLVVS', 37, 'superfluis', '', '', '1_2', 1), ('NON', 38, 'non', '', '', '1_2', 10), ('LVXVRIO', 39, 'luxuriat', '', '', '1_2', 1), ('DEVS', 40, 'deo', '', '', '2_1', 1), ('QVE', 41, 'que', '', '', '2_1', 4), ('EFFECTVS/1', 42, 'effectum', '', '', '2_1', 1), ('NATVRALIS', 43, 'naturalium', '', '', '2_1', 2), ('IDEM', 44, 'eiusdem', '', '', '2_1', 2), ('GENVS/1', 45, 'generis', '', '', '2_1', 1), ('IDEM', 46, 'eædem', '', '', '2_1', 2), ('ASSIGNO', 47, 'assignandæ', '', '', '2_1', 1), ('SVM/1', 48, 'sunt', '', '', '2_1', 28), ('CAVSA', 49, 'causæ', '', '', '2_1', 3), ('QVATENVS/1', 50, 'quatenus', '', '', '2_1', 1), ('FIO', 51, 'fieri', '', '', '2_1', 3), ('POSSVM/1', 52, 'potest', '', '', '2_1', 8), ('VT/4', 53, 'Uti', '', '', '2_2', 1), ('RESPIRATIO', 54, 'respirationis', '', '', '2_2', 1), ('IN', 55, 'in', '', '', '2_2', 23), ('HOMO', 56, 'homine', '', '', '2_2', 1), ('IN', 57, 'in', '', '', '2_2', 23), ('BESTIA', 58, 'bestia', '', '', '2_2', 1), ('DESCENSVS', 59, 'descensus', '', '', '2_2', 1), ('LAPIS', 60, 'lapidum', '', '', '2_2', 1), ('IN', 61, 'in', '', '', '2_2', 23), ('EVROPA/N', 62, 'Europa', '', '', '2_2', 1), ('IN', 63, 'in', '', '', '2_2', 23), ('AMERICA/N', 64, 'America', '', '', '2_2', 1), ('LVX', 65, 'lucis', '', '', '2_2', 2), ('IN', 66, 'in', '', '', '2_2', 23), ('IGNIS', 67, 'igne', '', '', '2_2', 1), ('CVLINARIS', 68, 'culinari', '', '', '2_2', 1), ('IN', 69, 'in', '', '', '2_2', 23), ('SOL', 70, 'sole', '', '', '2_2', 2), ('REFLEXIO', 71, 'reflexionis', '', '', '2_2', 1), ('LVX', 72, 'lucis', '', '', '2_2', 2), ('IN', 73, 'in', '', '', '2_2', 23), ('TERRA', 74, 'terra', '', '', '2_2', 5), ('IN', 75, 'in', '', '', '2_2', 23), ('PLANETA', 76, 'planetis', '', '', '2_2', 2), ('QVALITAS', 77, 'Qualitates', '', '', '3_1', 3), ('CORPVS', 78, 'corporum', '', '', '3_1', 19), ('QVI/1', 79, 'quæ', '', '', '3_1', 15), ('INTENDO', 80, 'intendi', '', '', '3_1', 1), ('REMITTO', 81, 'remitti', '', '', '3_1', 1), ('NEQVEO', 82, 'nequeunt', '', '', '3_1', 1), ('QVI/1', 83, 'quæ', '', '', '3_1', 15), ('QVE', 84, 'que', '', '', '3_1', 4), ('CORPVS', 85, 'corporibus', '', '', '3_1', 19), ('OMNIS', 86, 'omnibus', '', '', '3_1', 11), ('COMPETO', 87, 'competunt', '', '', '3_1', 2), ('IN', 88, 'in', '', '', '3_1', 23), ('QVI/1', 89, 'quibus', '', '', '3_1', 15), ('EXPERIMENTVM', 90, 'experimenta', '', '', '3_1', 7), ('INSTITVO', 91, 'instituere', '', '', '3_1', 1), ('LICEO', 92, 'licet', '', '', '3_1', 1), ('PRO/1', 93, 'pro', '', '', '3_1', 4), ('QVALITAS', 94, 'qualitatibus', '', '', '3_1', 3), ('CORPVS', 95, 'corporum', '', '', '3_1', 19), ('VNIVERSVS', 96, 'uniuersorum', '', '', '3_1', 3), ('HABEO', 97, 'habendæ', '', '', '3_1', 3), ('SVM/1', 98, 'sunt', '', '', '3_1', 28), ('NAM', 99, 'Nam', '', '', '3_2', 2), ('QVALITAS', 100, 'qualitates', '', '', '3_2', 3), ('CORPVS', 101, 'corporum', '', '', '3_2', 19), ('NON', 102, 'non', '', '', '3_2', 10), ('NISI', 103, 'nisi', '', '', '3_2', 2), ('PER', 104, 'per', '', '', '3_2', 11), ('EXPERIMENTVM', 105, 'experimenta', '', '', '3_2', 7), ('INNOTESCO', 106, 'innotescunt', '', '', '3_2', 2), ('IDEO', 107, 'ideo', '', '', '3_2', 1), ('QVE', 108, 'que', '', '', '3_2', 4), ('GENERALIS', 109, 'generales', '', '', '3_2', 2), ('STATVO', 110, 'statuendæ', '', '', '3_2', 1), ('SVM/1', 111, 'sunt', '', '', '3_2', 28), ('QVOTQVOT/1', 112, 'quotquot', '', '', '3_2', 1), ('CVM/2', 113, 'cum', '', '', '3_2', 2), ('EXPERIMENTVM', 114, 'experimentis', '', '', '3_2', 7), ('GENERALIS', 115, 'generaliter', '', '', '3_2', 2), ('QVADRO', 116, 'quadrant', '', '', '3_2', 1), ('QVI/1', 117, 'quæ', '', '', '3_2', 15), ('MINVO', 118, 'minui', '', '', '3_2', 1), ('NON', 119, 'non', '', '', '3_2', 10), ('POSSVM/1', 120, 'possunt', '', '', '3_2', 8), ('NON', 121, 'non', '', '', '3_2', 10), ('POSSVM/1', 122, 'possunt', '', '', '3_2', 8), ('AVFERO', 123, 'auferri', '', '', '3_2', 1), ('CERTVS', 124, 'Certe', '', '', '3_2', 2), ('CONTRA/2', 125, 'contra', '', '', '3_2', 1), ('EXPERIMENTVM', 126, 'experimentorum', '', '', '3_2', 7), ('TENOR', 127, 'tenorem', '', '', '3_2', 1), ('SOMNIVM', 128, 'somnia', '', '', '3_2', 1), ('TEMERE', 129, 'temere', '', '', '3_2', 1), ('CONFIGO', 130, 'confingenda', '', '', '3_2', 1), ('NON', 131, 'non', '', '', '3_2', 10), ('SVM/1', 132, 'sunt', '', '', '3_2', 28), ('NEQVE', 133, 'nec', '', '', '3_2', 2), ('AB', 134, 'a', '', '', '3_2', 6), ('NATVRA', 135, 'naturæ', '', '', '3_2', 4), ('ANALOGIA', 136, 'analogia', '', '', '3_2', 1), ('RECEDO/1', 137, 'recedendum', '', '', '3_2', 2), ('SVM/1', 138, 'est', '', '', '3_2', 28), ('CVM/2', 139, 'cum', '', '', '3_2', 2), ('IS', 140, 'ea', '', '', '3_2', 4), ('SIMPLEX', 141, 'simplex', '', '', '3_2', 2), ('SVM/1', 142, 'esse', '', '', '3_2', 28), ('SOLEO', 143, 'soleat', '', '', '3_2', 1), ('SVI/1', 144, 'sibi', '', '', '3_2', 4), ('SEMPER', 145, 'semper', '', '', '3_2', 1), ('CONSONVS', 146, 'consona', '', '', '3_2', 1), ('EXTENSIO', 147, 'Extensio', '', '', '3_2', 3), ('CORPVS', 148, 'corporum', '', '', '3_2', 19), ('NON', 149, 'non', '', '', '3_2', 10), ('NISI', 150, 'nisi', '', '', '3_2', 2), ('PER', 151, 'per', '', '', '3_2', 11), ('SENSVS', 152, 'sensus', '', '', '3_2', 2), ('INNOTESCO', 153, 'innotescit', '', '', '3_2', 2), ('NEQVE', 154, 'nec', '', '', '3_2', 2), ('IN', 155, 'in', '', '', '3_2', 23), ('OMNIS', 156, 'omnibus', '', '', '3_2', 11), ('SENTIO', 157, 'sentitur', '', '', '3_2', 2), ('SED', 158, 'sed', '', '', '3_2', 4), ('QVIA', 159, 'quia', '', '', '3_2', 1), ('SENSIBILIS', 160, 'sensibilibus', '', '', '3_2', 1), ('OMNIS', 161, 'omnibus', '', '', '3_2', 11), ('COMPETO', 162, 'competit', '', '', '3_2', 2), ('DE', 163, 'de', '', '', '3_2', 4), ('VNIVERSVS', 164, 'uniuersis', '', '', '3_2', 3), ('AFFIRMO', 165, 'affirmatur', '', '', '3_2', 2), ('CORPVS', 166, 'Corpora', '', '', '3_2', 19), ('MVLTVS', 167, 'plura', '', '', '3_2', 3), ('DVRVS', 168, 'dura', '', '', '3_2', 4), ('SVM/1', 169, 'esse', '', '', '3_2', 28), ('EXPERIOR', 170, 'experimur', '', '', '3_2', 1), ('ORIOR', 171, 'Oritur', '', '', '3_2', 2), ('AVTEM', 172, 'autem', '', '', '3_2', 1), ('DVRITIES', 173, 'durities', '', '', '3_2', 4), ('TOTVS', 174, 'totius', '', '', '3_2', 3), ('AB', 175, 'a', '', '', '3_2', 6), ('DVRITIES', 176, 'duritie', '', '', '3_2', 4), ('PARS', 177, 'partium', '', '', '3_2', 8), ('INDE', 178, 'inde', '', '', '3_2', 3), ('NON', 179, 'non', '', '', '3_2', 10), ('IS', 180, 'horum', '', '', '3_2', 4), ('TANTVS', 181, 'tantum', '', '', '3_2', 1), ('CORPVS', 182, 'corporum', '', '', '3_2', 19), ('QVI/1', 183, 'quæ', '', '', '3_2', 15), ('SENTIO', 184, 'sentiuntur', '', '', '3_2', 2), ('SED', 185, 'sed', '', '', '3_2', 4), ('ALIVS', 186, 'aliorum', '', '', '3_2', 2), ('ETIAM', 187, 'etiam', '', '', '3_2', 2), ('OMNIS', 188, 'omnium', '', '', '3_2', 11), ('PARTICVLA', 189, 'particulas', '', '', '3_2', 2), ('INDIVISVS', 190, 'indiuisas', '', '', '3_2', 4), ('SVM/1', 191, 'esse', '', '', '3_2', 28), ('DVRVS', 192, 'duras', '', '', '3_2', 4), ('MERITO/2', 193, 'merito', '', '', '3_2', 1), ('CONCLVDO', 194, 'concludimus', '', '', '3_2', 4), ('CORPVS', 195, 'Corpora', '', '', '3_2', 19), ('OMNIS', 196, 'omnia', '', '', '3_2', 11), ('IMPENETRABILIS', 197, 'impenetrabilia', '', '', '3_2', 3), ('SVM/1', 198, 'esse', '', '', '3_2', 28), ('NON', 199, 'non', '', '', '3_2', 10), ('RATIO', 200, 'ratione', '', '', '3_2', 2), ('SED', 201, 'sed', '', '', '3_2', 4), ('SENSVS', 202, 'sensu', '', '', '3_2', 2), ('COLLIGO/3', 203, 'colligimus', '', '', '3_2', 3), ('QVI/1', 204, 'Quæ', '', '', '3_2', 15), ('TRACTO', 205, 'tractamus', '', '', '3_2', 1), ('IMPENETRABILIS', 206, 'impenetrabilia', '', '', '3_2', 3), ('INVENIO', 207, 'inueniuntur', '', '', '3_2', 1), ('INDE', 208, 'inde', '', '', '3_2', 3), ('CONCLVDO', 209, 'concludimus', '', '', '3_2', 4), ('IMPENETRABILITAS', 210, 'impenetrabilitatem', '', '', '3_2', 4), ('SVM/1', 211, 'esse', '', '', '3_2', 28), ('PROPRIETAS', 212, 'proprietatem', '', '', '3_2', 2), ('CORPVS', 213, 'corporum', '', '', '3_2', 19), ('VNIVERSVS', 214, 'uniuersorum', '', '', '3_2', 3), ('CORPVS', 215, 'Corpora', '', '', '3_2', 19), ('OMNIS', 216, 'omnia', '', '', '3_2', 11), ('MOBILIS', 217, 'mobilia', '', '', '3_2', 2), ('SVM/1', 218, 'esse', '', '', '3_2', 28), ('VIS', 219, 'uiribus', '', '', '3_2', 9), ('QVIDAM', 220, 'quibusdam', '', '', '3_2', 1), ('QVI/1', 221, 'quas', '', '', '3_2', 15), ('VIS', 222, 'uires', '', '', '3_2', 9), ('INERTIA', 223, 'inertiæ', '', '', '3_2', 5), ('VOCO', 224, 'uocamus', '', '', '3_2', 1), ('PERSEVERO', 225, 'perseuerare', '', '', '3_2', 1), ('IN', 226, 'in', '', '', '3_2', 23), ('MOTVS', 227, 'motu', '', '', '3_2', 1), ('VEL/1', 228, 'uel', '', '', '3_2', 2), ('QVIES', 229, 'quiete', '', '', '3_2', 1), ('EX', 230, 'ex', '', '', '3_2', 5), ('HIC/1', 231, 'hisce', '', '', '3_2', 6), ('CORPVS', 232, 'corporum', '', '', '3_2', 19), ('VIDEO', 233, 'uisorum', '', '', '3_2', 1), ('PROPRIETAS', 234, 'proprietatibus', '', '', '3_2', 2), ('COLLIGO/3', 235, 'colligimus', '', '', '3_2', 3), ('EXTENSIO', 236, 'Extensio', '', '', '3_2', 3), ('DVRITIES', 237, 'durities', '', '', '3_2', 4), ('IMPENETRABILITAS', 238, 'impenetrabilitas', '', '', '3_2', 4), ('MOBILITAS', 239, 'mobilitas', '', '', '3_2', 2), ('VIS', 240, 'uis', '', '', '3_2', 9), ('INERTIA', 241, 'inertiæ', '', '', '3_2', 5), ('TOTVS', 242, 'totius', '', '', '3_2', 3), ('ORIOR', 243, 'oritur', '', '', '3_2', 2), ('AB', 244, 'ab', '', '', '3_2', 6), ('EXTENSIO', 245, 'extensione', '', '', '3_2', 3), ('DVRITIES', 246, 'duritie', '', '', '3_2', 4), ('IMPENETRABILITAS', 247, 'impenetrabilitate', '', '', '3_2', 4), ('MOBILITAS', 248, 'mobilitate', '', '', '3_2', 2), ('VIS', 249, 'uiribus', '', '', '3_2', 9), ('INERTIA', 250, 'inertiæ', '', '', '3_2', 5), ('PARS', 251, 'partium', '', '', '3_2', 8), ('INDE', 252, 'inde', '', '', '3_2', 3), ('CONCLVDO', 253, 'concludimus', '', '', '3_2', 4), ('OMNIS', 254, 'omnes', '', '', '3_2', 11), ('OMNIS', 255, 'omnium', '', '', '3_2', 11), ('CORPVS', 256, 'corporum', '', '', '3_2', 19), ('PARS', 257, 'partes', '', '', '3_2', 8), ('MINIMVS', 258, 'minimas', '', '', '3_2', 1), ('EXTENDO', 259, 'extendi', '', '', '3_2', 1), ('DVRVS', 260, 'duras', '', '', '3_2', 4), ('SVM/1', 261, 'esse', '', '', '3_2', 28), ('IMPENETRABILIS', 262, 'impenetrabiles', '', '', '3_2', 3), ('MOBILIS', 263, 'mobiles', '', '', '3_2', 2), ('VIS', 264, 'uiribus', '', '', '3_2', 9), ('INERTIA', 265, 'inertiæ', '', '', '3_2', 5), ('PRAEDITVS', 266, 'præditas', '', '', '3_2', 1), ('ET/2', 267, 'Et', '', '', '3_2', 1), ('HIC/1', 268, 'hoc', '', '', '3_2', 6), ('SVM/1', 269, 'est', '', '', '3_2', 28), ('FVNDAMENTVM', 270, 'fundamentum', '', '', '3_2', 1), ('PHILOSOPHIA', 271, 'philosophiæ', '', '', '3_2', 2), ('TOTVS', 272, 'totius', '', '', '3_2', 3), ('PORRO', 273, 'Porro', '', '', '3_2', 1), ('CORPVS', 274, 'corporum', '', '', '3_2', 19), ('PARS', 275, 'partes', '', '', '3_2', 8), ('DIVIDO', 276, 'diuisas', '', '', '3_2', 5), ('SVI/1', 277, 'sibi', '', '', '3_2', 4), ('MVTVO/2', 278, 'mutuo', '', '', '3_2', 3), ('CONTIGVVS', 279, 'contiguas', '', '', '3_2', 1), ('AB', 280, 'ab', '', '', '3_2', 6), ('INVICEM', 281, 'inuicem', '', '', '3_2', 2), ('SEPARO/2', 282, 'separari', '', '', '3_2', 2), ('POSSVM/1', 283, 'posse', '', '', '3_2', 8), ('EX', 284, 'ex', '', '', '3_2', 5), ('PHAENOMENON', 285, 'phænomenis', '', '', '3_2', 5), ('NOSCO', 286, 'nouimus', '', '', '3_2', 1), ('PARS', 287, 'partes', '', '', '3_2', 8), ('INDIVISVS', 288, 'indiuisas', '', '', '3_2', 4), ('IN', 289, 'in', '', '', '3_2', 23), ('PARS', 290, 'partes', '', '', '3_2', 8), ('PARVVS/2', 291, 'minores', '', '', '3_2', 1), ('RATIO', 292, 'ratione', '', '', '3_2', 2), ('DISTINGVO', 293, 'distingui', '', '', '3_2', 2), ('POSSVM/1', 294, 'posse', '', '', '3_2', 8), ('EX', 295, 'ex', '', '', '3_2', 5), ('MATHEMATICVS/2', 296, 'mathematica', '', '', '3_2', 1), ('CERTVS', 297, 'certum', '', '', '3_2', 2), ('SVM/1', 298, 'est', '', '', '3_2', 28), ('VTRVM', 299, 'Utrum', '', '', '3_2', 1), ('VERO/3', 300, 'uero', '', '', '3_2', 1), ('PARS', 301, 'partes', '', '', '3_2', 8), ('ILLE', 302, 'illæ', '', '', '3_2', 1), ('DISTINGVO', 303, 'distinctæ', '', '', '3_2', 2), ('NONDVM', 304, 'nondum', '', '', '3_2', 1), ('DIVIDO', 305, 'diuisæ', '', '', '3_2', 5), ('PER', 306, 'per', '', '', '3_2', 11), ('VIS', 307, 'uires', '', '', '3_2', 9), ('NATVRA', 308, 'naturæ', '', '', '3_2', 4), ('DIVIDO', 309, 'diuidi', '', '', '3_2', 5), ('AB', 310, 'ab', '', '', '3_2', 6), ('INVICEM', 311, 'inuicem', '', '', '3_2', 2), ('SEPARO/2', 312, 'separari', '', '', '3_2', 2), ('POSSVM/1', 313, 'possint', '', '', '3_2', 8), ('INCERTVS', 314, 'incertum', '', '', '3_2', 1), ('SVM/1', 315, 'est', '', '', '3_2', 28), ('AT/2', 316, 'At', '', '', '3_2', 1), ('SI/2', 317, 'si', '', '', '3_2', 2), ('VEL/1', 318, 'uel', '', '', '3_2', 2), ('VNICVS', 319, 'unico', '', '', '3_2', 1), ('CONSTO', 320, 'constaret', '', '', '3_2', 2), ('EXPERIMENTVM', 321, 'experimento', '', '', '3_2', 7), ('QVI/1', 322, 'quod', '', '', '3_2', 15), ('PARTICVLA', 323, 'particula', '', '', '3_2', 2), ('ALIQVIS', 324, 'aliqua', '', '', '3_2', 1), ('INDIVISVS', 325, 'indiuisa', '', '', '3_2', 4), ('FRANGO', 326, 'frangendo', '', '', '3_2', 1), ('CORPVS', 327, 'corpus', '', '', '3_2', 19), ('DVRVS', 328, 'durum', '', '', '3_2', 4), ('SOLIDVS/2', 329, 'solidum', '', '', '3_2', 1), ('DIVISIO', 330, 'diuisionem', '', '', '3_2', 1), ('PATEO', 331, 'pateretur', '', '', '3_2', 1), ('CONCLVDO', 332, 'concluderemus', '', '', '3_2', 4), ('VIS', 333, 'ui', '', '', '3_2', 9), ('HIC/1', 334, 'huius', '', '', '3_2', 6), ('REGVLA', 335, 'regulæ', '', '', '3_2', 2), ('QVI/1', 336, 'quod', '', '', '3_2', 15), ('NONSOLVM', 337, 'non', '', '', '3_2', 2), ('NONSOLVM', 338, 'solum', '', '', '3_2', 2), ('PARS', 339, 'partes', '', '', '3_2', 8), ('DIVIDO', 340, 'diuisæ', '', '', '3_2', 5), ('SEPARABILIS', 341, 'separabiles', '', '', '3_2', 1), ('SVM/1', 342, 'essent', '', '', '3_2', 28), ('SED', 343, 'sed', '', '', '3_2', 4), ('ETIAM', 344, 'etiam', '', '', '3_2', 2), ('QVI/1', 345, 'quod', '', '', '3_2', 15), ('INDIVISVS', 346, 'indiuisæ', '', '', '3_2', 4), ('IN', 347, 'in', '', '', '3_2', 23), ('INFINITVM', 348, 'infinitum', '', '', '3_2', 1), ('DIVIDO', 349, 'diuidi', '', '', '3_2', 5), ('POSSVM/1', 350, 'possent', '', '', '3_2', 8), ('DENIQVE', 351, 'Denique', '', '', '3_3', 1), ('SI/2', 352, 'si', '', '', '3_3', 2), ('CORPVS', 353, 'corpora', '', '', '3_3', 19), ('OMNIS', 354, 'omnia', '', '', '3_3', 11), ('IN', 355, 'in', '', '', '3_3', 23), ('CIRCVITVS', 356, 'circuitu', '', '', '3_3', 1), ('TERRA', 357, 'terræ', '', '', '3_3', 5), ('GRAVIS', 358, 'grauia', '', '', '3_3', 4), ('SVM/1', 359, 'esse', '', '', '3_3', 28), ('IN', 360, 'in', '', '', '3_3', 23), ('TERRA', 361, 'terram', '', '', '3_3', 5), ('IS', 362, 'id', '', '', '3_3', 4), ('QVE', 363, 'que', '', '', '3_3', 4), ('PRO/1', 364, 'pro', '', '', '3_3', 4), ('QVANTITAS', 365, 'quantitate', '', '', '3_3', 2), ('MATERIA', 366, 'materiæ', '', '', '3_3', 2), ('IN', 367, 'in', '', '', '3_3', 23), ('SINGVLVS', 368, 'singulis', '', '', '3_3', 1), ('LVNA', 369, 'lunam', '', '', '3_3', 2), ('GRAVIS', 370, 'grauem', '', '', '3_3', 4), ('SVM/1', 371, 'esse', '', '', '3_3', 28), ('IN', 372, 'in', '', '', '3_3', 23), ('TERRA', 373, 'terram', '', '', '3_3', 5), ('PRO/1', 374, 'pro', '', '', '3_3', 4), ('QVANTITAS', 375, 'quantitate', '', '', '3_3', 2), ('MATERIA', 376, 'materiæ', '', '', '3_3', 2), ('SVVS', 377, 'sua', '', '', '3_3', 1), ('VICISSIM', 378, 'uicissim', '', '', '3_3', 1), ('MARE', 379, 'mare', '', '', '3_3', 1), ('NOSTER', 380, 'nostrum', '', '', '3_3', 1), ('GRAVIS', 381, 'graue', '', '', '3_3', 4), ('SVM/1', 382, 'esse', '', '', '3_3', 28), ('IN', 383, 'in', '', '', '3_3', 23), ('LVNA', 384, 'lunam', '', '', '3_3', 2), ('PLANETA', 385, 'planetas', '', '', '3_3', 2), ('OMNIS', 386, 'omnes', '', '', '3_3', 11), ('GRAVIS', 387, 'graues', '', '', '3_3', 4), ('SVM/1', 388, 'esse', '', '', '3_3', 28), ('IN', 389, 'in', '', '', '3_3', 23), ('SVI/1', 390, 'se', '', '', '3_3', 4), ('MVTVO/2', 391, 'mutuo', '', '', '3_3', 3), ('COMETES', 392, 'cometarum', '', '', '3_3', 1), ('SIMILIS', 393, 'similem', '', '', '3_3', 1), ('SVM/1', 394, 'esse', '', '', '3_3', 28), ('GRAVITAS', 395, 'grauitatem', '', '', '3_3', 4), ('IN', 396, 'in', '', '', '3_3', 23), ('SOL', 397, 'solem', '', '', '3_3', 2), ('PER', 398, 'per', '', '', '3_3', 11), ('EXPERIMENTVM', 399, 'experimenta', '', '', '3_3', 7), ('OBSERVATIO', 400, 'obseruationes', '', '', '3_3', 2), ('ASTRONOMICVS', 401, 'astronomicas', '', '', '3_3', 1), ('VNIVERSALIS', 402, 'uniuersaliter', '', '', '3_3', 2), ('CONSTO', 403, 'constet', '', '', '3_3', 2), ('DICO/2', 404, 'dicendum', '', '', '3_3', 2), ('SVM/1', 405, 'erit', '', '', '3_3', 28), ('PER', 406, 'per', '', '', '3_3', 11), ('HIC/1', 407, 'hanc', '', '', '3_3', 6), ('REGVLA', 408, 'regulam', '', '', '3_3', 2), ('QVI/1', 409, 'quod', '', '', '3_3', 15), ('CORPVS', 410, 'corpora', '', '', '3_3', 19), ('OMNIS', 411, 'omnia', '', '', '3_3', 11), ('IN', 412, 'in', '', '', '3_3', 23), ('SVI/1', 413, 'se', '', '', '3_3', 4), ('MVTVO/2', 414, 'mutuo', '', '', '3_3', 3), ('GRAVITO', 415, 'grauitant', '', '', '3_3', 1), ('NAM', 416, 'Nam', '', '', '3_3', 2), ('FORTIS', 417, 'fortius', '', '', '3_3', 1), ('SVM/1', 418, 'erit', '', '', '3_3', 28), ('ARGVMENTVM', 419, 'argumentum', '', '', '3_3', 2), ('EX', 420, 'ex', '', '', '3_3', 5), ('PHAENOMENON', 421, 'phænomenis', '', '', '3_3', 5), ('DE', 422, 'de', '', '', '3_3', 4), ('GRAVITAS', 423, 'grauitate', '', '', '3_3', 4), ('VNIVERSALIS', 424, 'uniuersali', '', '', '3_3', 2), ('QVAM/1', 425, 'quam', '', '', '3_3', 3), ('DE', 426, 'de', '', '', '3_3', 4), ('CORPVS', 427, 'corporum', '', '', '3_3', 19), ('IMPENETRABILITAS', 428, 'impenetrabilitate', '', '', '3_3', 4), ('DE', 429, 'de', '', '', '3_3', 4), ('QVI/1', 430, 'qua', '', '', '3_3', 15), ('VTIQVE', 431, 'utique', '', '', '3_3', 2), ('IN', 432, 'in', '', '', '3_3', 23), ('CORPVS', 433, 'corporibus', '', '', '3_3', 19), ('CAELESTIS', 434, 'coelestibus', '', '', '3_3', 1), ('NVLLVS', 435, 'nullum', '', '', '3_3', 2), ('EXPERIMENTVM', 436, 'experimentum', '', '', '3_3', 7), ('NVLLVS', 437, 'nullam', '', '', '3_3', 2), ('PRORSVS/2', 438, 'prorsus', '', '', '3_3', 1), ('OBSERVATIO', 439, 'obseruationem', '', '', '3_3', 2), ('HABEO', 440, 'habemus', '', '', '3_3', 3), ('ATTAMEN', 441, 'Attamen', '', '', '3_3', 1), ('GRAVITAS', 442, 'grauitatem', '', '', '3_3', 4), ('CORPVS', 443, 'corporibus', '', '', '3_3', 19), ('ESSENTIALIS', 444, 'essentialem', '', '', '3_3', 1), ('SVM/1', 445, 'esse', '', '', '3_3', 28), ('MINIME', 446, 'minime', '', '', '3_3', 1), ('AFFIRMO', 447, 'affirmo', '', '', '3_3', 2), ('PER', 448, 'Per', '', '', '3_3', 11), ('VIS', 449, 'uim', '', '', '3_3', 9), ('INSERO/3', 450, 'insitam', '', '', '3_3', 1), ('INTELLIGO', 451, 'intelligo', '', '', '3_3', 1), ('SOLVS', 452, 'solam', '', '', '3_3', 1), ('VIS', 453, 'uim', '', '', '3_3', 9), ('INERTIA', 454, 'inertiæ', '', '', '3_3', 5), ('HIC/1', 455, 'Hæc', '', '', '3_3', 6), ('IMMVTABILIS/1', 456, 'immutabilis', '', '', '3_3', 1), ('SVM/1', 457, 'est', '', '', '3_3', 28), ('GRAVITAS', 458, 'Grauitas', '', '', '3_3', 4), ('RECEDO/1', 459, 'recedendo', '', '', '3_3', 2), ('AB', 460, 'a', '', '', '3_3', 6), ('TERRA', 461, 'terra', '', '', '3_3', 5), ('DIMINVO', 462, 'diminuitur', '', '', '3_3', 1), ('IN', 463, 'In', '', '', '4_1', 23), ('PHILOSOPHIA', 464, 'philosophia', '', '', '4_1', 2), ('EXPERIMENTALIS', 465, 'experimentali', '', '', '4_1', 1), ('PROPOSITIO', 466, 'propositiones', '', '', '4_1', 1), ('EX', 467, 'ex', '', '', '4_1', 5), ('PHAENOMENON', 468, 'phænomenis', '', '', '4_1', 5), ('PER', 469, 'per', '', '', '4_1', 11), ('INDVCTIO', 470, 'inductionem', '', '', '4_1', 2), ('COLLIGO/3', 471, 'collectæ', '', '', '4_1', 3), ('NON', 472, 'non', '', '', '4_1', 10), ('OBSTO', 473, 'obstantibus', '', '', '4_1', 1), ('CONTRARIVS', 474, 'contrariis', '', '', '4_1', 1), ('HYPOTHESIS', 475, 'hypothesibus', '', '', '4_1', 2), ('PRO/1', 476, 'pro', '', '', '4_1', 4), ('VERVS', 477, 'ueris', '', '', '4_1', 2), ('AVT', 478, 'aut', '', '', '4_1', 4), ('ACCVRO', 479, 'accurate', '', '', '4_1', 1), ('AVT', 480, 'aut', '', '', '4_1', 4), ('QVAM/1', 481, 'quamproxime', '', '', '4_1', 3), ('PROPIOR', 482, 'PROXIME', '', '', '4_1', 1), ('HABEO', 483, 'haberi', '', '', '4_1', 3), ('DEBEO', 484, 'debent', '', '', '4_1', 3), ('DONEC', 485, 'donec', '', '', '4_1', 1), ('ALIVS', 486, 'alia', '', '', '4_1', 2), ('OCCVRRO', 487, 'occurrerint', '', '', '4_1', 1), ('PHAENOMENON', 488, 'phænomena', '', '', '4_1', 5), ('PER', 489, 'per', '', '', '4_1', 11), ('QVI/1', 490, 'quæ', '', '', '4_1', 15), ('AVT', 491, 'aut', '', '', '4_1', 4), ('ACCVRATVS', 492, 'accuratiores', '', '', '4_1', 1), ('REDDO', 493, 'reddantur', '', '', '4_1', 1), ('AVT', 494, 'aut', '', '', '4_1', 4), ('EXCEPTIO', 495, 'exceptionibus', '', '', '4_1', 1), ('OBNOXIVS', 496, 'obnoxiæ', '', '', '4_1', 1), ('HIC/1', 497, 'Hoc', '', '', '4_2', 6), ('FIO', 498, 'fieri', '', '', '4_2', 3), ('DEBEO', 499, 'debet', '', '', '4_2', 3), ('NE/4', 500, 'ne', '', '', '4_2', 1), ('ARGVMENTVM', 501, 'argumentum', '', '', '4_2', 2), ('INDVCTIO', 502, 'inductionis', '', '', '4_2', 2), ('TOLLO', 503, 'tollatur', '', '', '4_2', 1), ('PER', 504, 'per', '', '', '4_2', 11), ('HYPOTHESIS', 505, 'hypotheses', '', '', '4_2', 2)]
section_list ={'1.1': 'start', '1.2': '1.1', '2.1': '1.2', '2.2': '2.1', '3.1': '2.2', '3.2': '3.1', '3.3': '3.2', '4.1': '3.3', '4.2': '4.1', 'end': '4.2', 'start': 'start'}
title = "Newton, Regulae Philosophandi"
section_level =  2
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)