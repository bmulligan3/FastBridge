import text
nan=""
section_words = {'start': -1, '2.21.1': 33, '2.21.2': 52, '2.21.3': 98, '2.21.4': 131, '2.21.5': 172, '2.21.6': 216, '2.21.7': 254, '2.21.8': 267, '2.21.9': 313, '2.21.10': 345, '2.21.12': 371, 'end': -2}
the_text =  [('FVROR/1', 0, 'Furor', '', '', '2_21_1', 1), ('ANTONIVS/N', 1, 'Antonii', '', '', '2_21_1', 5), ('QVATENVS/1', 2, 'quatenus', '', '', '2_21_1', 1), ('PER', 3, 'per', '', '', '2_21_1', 1), ('AMBITVS', 4, 'ambitum', '', '', '2_21_1', 1), ('NON', 5, 'non', '', '', '2_21_1', 3), ('POSSVM/1', 6, 'poterat', '', '', '2_21_1', 1), ('INTEREO/1', 7, 'interire', '', '', '2_21_1', 1), ('LVXVS/1', 8, 'luxu', '', '', '2_21_1', 1), ('ET/2', 9, 'et', '', '', '2_21_1', 9), ('LIBIDO', 10, 'libidine', '', '', '2_21_1', 2), ('EXSTINGVO', 11, 'extinctus', '', '', '2_21_1', 1), ('SVM/1', 12, 'est', '', '', '2_21_1', 5), ('QVIPPE/1', 13, 'Quippe', '', '', '2_21_1', 3), ('CVM/3', 14, 'cum', '', '', '2_21_1', 1), ('POST/2', 15, 'post', '', '', '2_21_1', 2), ('PARTHVS/A', 16, 'Parthos', '', '', '2_21_1', 2), ('EXOSVS', 17, 'exosus', '', '', '2_21_1', 1), ('ARMA', 18, 'arma', '', '', '2_21_1', 1), ('IN', 19, 'in', '', '', '2_21_1', 12), ('OTIVM', 20, 'otio', '', '', '2_21_1', 1), ('AGO', 21, 'ageret', '', '', '2_21_1', 1), ('CAPIO/2', 22, 'captus', '', '', '2_21_1', 2), ('AMOR', 23, 'amore', '', '', '2_21_1', 1), ('CLEOPATRA/N', 24, 'Cleopatrae', '', '', '2_21_1', 1), ('QVASI/1', 25, 'quasi', '', '', '2_21_1', 3), ('BENE', 26, 'bene', '', '', '2_21_1', 1), ('GERO', 27, 'gestis', '', '', '2_21_1', 1), ('RES', 28, 'rebus', '', '', '2_21_1', 2), ('IN', 29, 'in', '', '', '2_21_1', 12), ('REGIVS', 30, 'regio', '', '', '2_21_1', 1), ('SVI/1', 31, 'se', '', '', '2_21_1', 5), ('SINVS', 32, 'sinu', '', '', '2_21_1', 2), ('REFICIO', 33, 'reficiebat', '', '', '2_21_1', 1), ('HINC', 34, 'Hinc', '', '', '2_21_2', 1), ('MVLIER', 35, 'mulier', '', '', '2_21_2', 1), ('AEGYPTIVS/A', 36, 'Aegyptia', '', '', '2_21_2', 1), ('AB', 37, 'ab', '', '', '2_21_2', 5), ('EBRIVS', 38, 'ebrio', '', '', '2_21_2', 1), ('IMPERATOR', 39, 'imperatore', '', '', '2_21_2', 1), ('PRETIVM', 40, 'pretium', '', '', '2_21_2', 1), ('LIBIDO', 41, 'libidinum', '', '', '2_21_2', 2), ('ROMANVS/A', 42, 'Romanum', '', '', '2_21_2', 2), ('IMPERIVM', 43, 'imperium', '', '', '2_21_2', 1), ('PETO', 44, 'petit', '', '', '2_21_2', 1), ('ET/2', 45, 'et', '', '', '2_21_2', 9), ('PROMITTO', 46, 'promisit', '', '', '2_21_2', 1), ('ANTONIVS/N', 47, 'Antonius', '', '', '2_21_2', 5), ('QVASI/1', 48, 'quasi', '', '', '2_21_2', 3), ('FACILIS', 49, 'facilior', '', '', '2_21_2', 1), ('SVM/1', 50, 'esset', '', '', '2_21_2', 5), ('PARTHVS/A', 51, 'Partho', '', '', '2_21_2', 2), ('ROMANVS/A', 52, 'Romanus', '', '', '2_21_2', 2), ('IGITVR', 53, 'Igitur', '', '', '2_21_3', 1), ('COEPIO', 54, 'coepit', '', '', '2_21_3', 1), ('NON', 55, 'non', '', '', '2_21_3', 3), ('SVI/1', 56, 'sibi', '', '', '2_21_3', 5), ('DOMINATIO', 57, 'dominationem', '', '', '2_21_3', 1), ('PARO/2', 58, 'parare', '', '', '2_21_3', 1), ('NEQVE', 59, 'nec', '', '', '2_21_3', 6), ('TACITE', 60, 'tacite', '', '', '2_21_3', 1), ('SED', 61, 'sed', '', '', '2_21_3', 4), ('PATRIA', 62, 'patriae', '', '', '2_21_3', 1), ('NOMEN', 63, 'nominis', '', '', '2_21_3', 1), ('TOGA', 64, 'togae', '', '', '2_21_3', 1), ('FASCIS', 65, 'fascium', '', '', '2_21_3', 1), ('OBLIVISCOR', 66, 'oblitus', '', '', '2_21_3', 1), ('TOTVS', 67, 'totus', '', '', '2_21_3', 2), ('IN', 68, 'in', '', '', '2_21_3', 12), ('MONSTRVM', 69, 'monstrum', '', '', '2_21_3', 1), ('ILLE', 70, 'illud', '', '', '2_21_3', 3), ('VT/4', 71, 'ut', '', '', '2_21_3', 4), ('MENS', 72, 'mente', '', '', '2_21_3', 1), ('ITA', 73, 'ita', '', '', '2_21_3', 1), ('AMICTVS', 74, 'amictu', '', '', '2_21_3', 1), ('QVOQVE', 75, 'quoque', '', '', '2_21_3', 1), ('CVLTVS/1', 76, 'cultu', '', '', '2_21_3', 2), ('QVE', 77, 'que', '', '', '2_21_3', 9), ('DESCIO', 78, 'desciuerat', '', '', '2_21_3', 1), ('AVREVS/2', 79, 'Aureum', '', '', '2_21_3', 2), ('IN', 80, 'in', '', '', '2_21_3', 12), ('MANVS/1', 81, 'manu', '', '', '2_21_3', 2), ('BACVLVM', 82, 'baculum', '', '', '2_21_3', 1), ('IN', 83, 'in', '', '', '2_21_3', 12), ('LATVS/1', 84, 'latere', '', '', '2_21_3', 1), ('ACINACES', 85, 'acinaces', '', '', '2_21_3', 1), ('PVRPVREVS', 86, 'purpurea', '', '', '2_21_3', 3), ('VESTIS', 87, 'uestis', '', '', '2_21_3', 1), ('INGENS', 88, 'ingentibus', '', '', '2_21_3', 1), ('OBSTRINGO', 89, 'obstricta', '', '', '2_21_3', 1), ('GEMMA', 90, 'gemmis', '', '', '2_21_3', 1), ('DIADEMA', 91, 'diadema', '', '', '2_21_3', 1), ('DESVM/1', 92, 'deerat', '', '', '2_21_3', 1), ('VT/4', 93, 'ut', '', '', '2_21_3', 4), ('REGINA', 94, 'regina', '', '', '2_21_3', 3), ('REX', 95, 'rex', '', '', '2_21_3', 2), ('ET/2', 96, 'et', '', '', '2_21_3', 9), ('IPSE', 97, 'ipse', '', '', '2_21_3', 2), ('FRVOR', 98, 'frueretur', '', '', '2_21_3', 1), ('AD/2', 99, 'Ad', '', '', '2_21_4', 8), ('PRIMVS', 100, 'primam', '', '', '2_21_4', 2), ('NOVVS', 101, 'nouorum', '', '', '2_21_4', 1), ('MOTVS', 102, 'motuum', '', '', '2_21_4', 1), ('FAMA', 103, 'famam', '', '', '2_21_4', 1), ('CAESAR/N', 104, 'Caesar', '', '', '2_21_4', 4), ('AB', 105, 'a', '', '', '2_21_4', 5), ('BRVNDISIVM/N', 106, 'Brundisio', '', '', '2_21_4', 1), ('TRAICIO', 107, 'traiecerat', '', '', '2_21_4', 1), ('VT/4', 108, 'ut', '', '', '2_21_4', 4), ('VENIO', 109, 'uenienti', '', '', '2_21_4', 1), ('BELLVM', 110, 'bello', '', '', '2_21_4', 2), ('OCCVRRO', 111, 'occurreret', '', '', '2_21_4', 1), ('PONO', 112, 'positis', '', '', '2_21_4', 1), ('QVE', 113, 'que', '', '', '2_21_4', 9), ('CASTRA/2', 114, 'castris', '', '', '2_21_4', 1), ('IN', 115, 'in', '', '', '2_21_4', 12), ('EPIRVS/N', 116, 'Epiro', '', '', '2_21_4', 1), ('OMNIS', 117, 'omne', '', '', '2_21_4', 3), ('LITVS/2', 118, 'litus', '', '', '2_21_4', 1), ('ACTIACVS/A', 119, 'Actiacum', '', '', '2_21_4', 1), ('LEVCAS/N', 120, 'Leucada', '', '', '2_21_4', 1), ('INSVLA', 121, 'insulam', '', '', '2_21_4', 1), ('MONS', 122, 'montem', '', '', '2_21_4', 1), ('QVE', 123, 'que', '', '', '2_21_4', 9), ('LEVCATE/N', 124, 'Leucaten', '', '', '2_21_4', 1), ('ET/2', 125, 'et', '', '', '2_21_4', 9), ('AMBRACIVS/A', 126, 'Ambracii', '', '', '2_21_4', 1), ('SINVS', 127, 'sinus', '', '', '2_21_4', 2), ('CORNV', 128, 'cornua', '', '', '2_21_4', 2), ('INFESTVS', 129, 'infesta', '', '', '2_21_4', 1), ('CLASSIS', 130, 'classe', '', '', '2_21_4', 2), ('SVCCINGO', 131, 'succinxerat', '', '', '2_21_4', 1), ('NOS', 132, 'Nobis', '', '', '2_21_5', 1), ('QVADRINGENTI', 133, 'quadrigentae', '', '', '2_21_5', 1), ('AMPLVS', 134, 'amplius', '', '', '2_21_5', 2), ('NAVIS', 135, 'naues', '', '', '2_21_5', 2), ('DVCENTI', 136, 'ducentae', '', '', '2_21_5', 1), ('PARVVS/2', 137, 'minus', '', '', '2_21_5', 1), ('HOSTIS', 138, 'hostium', '', '', '2_21_5', 1), ('SED', 139, 'sed', '', '', '2_21_5', 4), ('NVMERVS', 140, 'numerum', '', '', '2_21_5', 1), ('MAGNITVDO', 141, 'magnitudo', '', '', '2_21_5', 2), ('PENSO', 142, 'pensabat', '', '', '2_21_5', 1), ('QVIPPE/1', 143, 'Quippe', '', '', '2_21_5', 3), ('AB', 144, 'a', '', '', '2_21_5', 5), ('SENVS', 145, 'senis', '', '', '2_21_5', 1), ('NOVENVS', 146, 'nouenos', '', '', '2_21_5', 1), ('REMVS', 147, 'remorum', '', '', '2_21_5', 1), ('ORDO', 148, 'ordines', '', '', '2_21_5', 2), ('AD/2', 149, 'ad', '', '', '2_21_5', 8), ('HIC/1', 150, 'hoc', '', '', '2_21_5', 2), ('TVRRIS', 151, 'turribus', '', '', '2_21_5', 1), ('ATQVE/1', 152, 'atque', '', '', '2_21_5', 2), ('TABVLATVM', 153, 'tabulatis', '', '', '2_21_5', 1), ('ALLEVO/1', 154, 'adleuatae', '', '', '2_21_5', 1), ('CASTELLVM', 155, 'castellorum', '', '', '2_21_5', 1), ('VEL/1', 156, 'uel', '', '', '2_21_5', 1), ('VRBS', 157, 'urbium', '', '', '2_21_5', 1), ('SPECIES', 158, 'specie', '', '', '2_21_5', 1), ('NON', 159, 'non', '', '', '2_21_5', 3), ('SINE', 160, 'sine', '', '', '2_21_5', 1), ('GEMITVS', 161, 'gemitu', '', '', '2_21_5', 1), ('MARE', 162, 'maris', '', '', '2_21_5', 3), ('ET/2', 163, 'et', '', '', '2_21_5', 9), ('LABOR/1', 164, 'labore', '', '', '2_21_5', 1), ('VENTVS', 165, 'uentorum', '', '', '2_21_5', 2), ('FERO', 166, 'ferebantur', '', '', '2_21_5', 1), ('QVI/1', 167, 'quae', '', '', '2_21_5', 4), ('QVIDEM', 168, 'quidem', '', '', '2_21_5', 2), ('IPSE', 169, 'ipsa', '', '', '2_21_5', 2), ('MOLES', 170, 'moles', '', '', '2_21_5', 1), ('EXITIVM', 171, 'exitio', '', '', '2_21_5', 1), ('SVM/1', 172, 'fuit', '', '', '2_21_5', 5), ('CAESAR/N', 173, 'Caesaris', '', '', '2_21_6', 4), ('NAVIS', 174, 'naues', '', '', '2_21_6', 2), ('AB', 175, 'a', '', '', '2_21_6', 5), ('BINVS', 176, 'bini', '', '', '2_21_6', 1), ('REMEX', 177, 'remigum', '', '', '2_21_6', 1), ('IN', 178, 'in', '', '', '2_21_6', 12), ('SENI', 179, 'senos', '', '', '2_21_6', 1), ('NEQVE', 180, 'nec', '', '', '2_21_6', 6), ('AMPLVS', 181, 'amplius', '', '', '2_21_6', 2), ('ORDO', 182, 'ordines', '', '', '2_21_6', 2), ('CERNO', 183, 'creuerant', '', '', '2_21_6', 1), ('ITAQVE', 184, 'itaque', '', '', '2_21_6', 2), ('HABILIS', 185, 'habiles', '', '', '2_21_6', 1), ('IN', 186, 'in', '', '', '2_21_6', 12), ('OMNIS', 187, 'omnia', '', '', '2_21_6', 3), ('QVI/1', 188, 'quae', '', '', '2_21_6', 4), ('VSVS', 189, 'usus', '', '', '2_21_6', 1), ('POSCO', 190, 'posceret', '', '', '2_21_6', 1), ('AD/2', 191, 'ad', '', '', '2_21_6', 8), ('IMPETVS', 192, 'impetus', '', '', '2_21_6', 1), ('ET/2', 193, 'et', '', '', '2_21_6', 9), ('RECVRSVS', 194, 'recursus', '', '', '2_21_6', 1), ('FLEXVS', 195, 'flexus', '', '', '2_21_6', 1), ('QVE', 196, 'que', '', '', '2_21_6', 9), ('CAPIO/2', 197, 'capiendos', '', '', '2_21_6', 2), ('ILLE', 198, 'illas', '', '', '2_21_6', 3), ('GRAVIS', 199, 'graues', '', '', '2_21_6', 1), ('ET/2', 200, 'et', '', '', '2_21_6', 9), ('AD/2', 201, 'ad', '', '', '2_21_6', 8), ('OMNIS', 202, 'omnia', '', '', '2_21_6', 3), ('PRAEPEDIO', 203, 'praepeditas', '', '', '2_21_6', 1), ('SINGVLVS', 204, 'singulas', '', '', '2_21_6', 1), ('MVLTVS', 205, 'plures', '', '', '2_21_6', 1), ('ADORIOR', 206, 'adortae', '', '', '2_21_6', 1), ('MISSILIS', 207, 'missilibus', '', '', '2_21_6', 1), ('SIMVL/1', 208, 'simul', '', '', '2_21_6', 1), ('ROSTRVM', 209, 'rostris', '', '', '2_21_6', 1), ('AD/2', 210, 'ad', '', '', '2_21_6', 8), ('HIC/1', 211, 'hoc', '', '', '2_21_6', 2), ('IGNIS', 212, 'ignibus', '', '', '2_21_6', 1), ('IACIO', 213, 'iactis', '', '', '2_21_6', 1), ('AD/2', 214, 'ad', '', '', '2_21_6', 8), ('ARBITRIVM', 215, 'arbitrium', '', '', '2_21_6', 1), ('DISSIPO', 216, 'dissipauere', '', '', '2_21_6', 1), ('NEQVE', 217, 'Nec', '', '', '2_21_7', 6), ('VLLVS', 218, 'ulla', '', '', '2_21_7', 1), ('RES', 219, 're', '', '', '2_21_7', 2), ('MAGIS/2', 220, 'magis', '', '', '2_21_7', 1), ('HOSTILIS', 221, 'hostilium', '', '', '2_21_7', 1), ('COPIA', 222, 'copiarum', '', '', '2_21_7', 1), ('APPAREO', 223, 'apparuit', '', '', '2_21_7', 1), ('MAGNITVDO', 224, 'magnitudo', '', '', '2_21_7', 2), ('QVAM/1', 225, 'quam', '', '', '2_21_7', 1), ('POST/2', 226, 'post', '', '', '2_21_7', 2), ('VICTORIA', 227, 'uictoriam', '', '', '2_21_7', 1), ('QVIPPE/1', 228, 'Quippe', '', '', '2_21_7', 3), ('IMMENSVS', 229, 'inmensae', '', '', '2_21_7', 1), ('CLASSIS', 230, 'classis', '', '', '2_21_7', 2), ('NAVFRAGIVM', 231, 'naufragium', '', '', '2_21_7', 1), ('BELLVM', 232, 'bello', '', '', '2_21_7', 2), ('FACIO', 233, 'factum', '', '', '2_21_7', 1), ('TOTVS', 234, 'toto', '', '', '2_21_7', 2), ('MARE', 235, 'mari', '', '', '2_21_7', 3), ('FLVITO', 236, 'fluitabat', '', '', '2_21_7', 1), ('ARABVS/A', 237, 'Arabum', '', '', '2_21_7', 1), ('QVE', 238, 'que', '', '', '2_21_7', 9), ('ET/2', 239, 'et', '', '', '2_21_7', 9), ('SABAEVS/A', 240, 'Sabaeorum', '', '', '2_21_7', 1), ('ET/2', 241, 'et', '', '', '2_21_7', 9), ('MILLE', 242, 'mille', '', '', '2_21_7', 1), ('ASIA/N', 243, 'Asiae', '', '', '2_21_7', 1), ('GENS', 244, 'gentium', '', '', '2_21_7', 1), ('SPOLIVM', 245, 'spolia', '', '', '2_21_7', 1), ('PVRPVREVS', 246, 'purpura', '', '', '2_21_7', 3), ('AVRVM', 247, 'auro', '', '', '2_21_7', 1), ('QVE', 248, 'que', '', '', '2_21_7', 9), ('ILLINO', 249, 'inlita', '', '', '2_21_7', 1), ('ASSIDVE', 250, 'adsidue', '', '', '2_21_7', 1), ('MOVEO', 251, 'mota', '', '', '2_21_7', 1), ('VENTVS', 252, 'uentis', '', '', '2_21_7', 2), ('MARE', 253, 'maria', '', '', '2_21_7', 3), ('REVOMO', 254, 'reuomebant', '', '', '2_21_7', 1), ('PRIMVS', 255, 'Prima', '', '', '2_21_8', 2), ('DVX', 256, 'dux', '', '', '2_21_8', 2), ('FVGA', 257, 'fugae', '', '', '2_21_8', 2), ('REGINA', 258, 'regina', '', '', '2_21_8', 3), ('CVM/2', 259, 'cum', '', '', '2_21_8', 1), ('AVREVS/2', 260, 'aurea', '', '', '2_21_8', 2), ('PVPPIS', 261, 'puppe', '', '', '2_21_8', 1), ('VELVM', 262, 'uelo', '', '', '2_21_8', 1), ('QVE', 263, 'que', '', '', '2_21_8', 9), ('PVRPVREVS', 264, 'purpureo', '', '', '2_21_8', 3), ('IN', 265, 'in', '', '', '2_21_8', 12), ('ALTVM', 266, 'altum', '', '', '2_21_8', 1), ('DO', 267, 'dedit', '', '', '2_21_8', 1), ('MOX', 268, 'Mox', '', '', '2_21_9', 1), ('SEQVOR', 269, 'secutus', '', '', '2_21_9', 1), ('ANTONIVS/N', 270, 'Antonius', '', '', '2_21_9', 5), ('SED', 271, 'sed', '', '', '2_21_9', 4), ('INSTO', 272, 'instare', '', '', '2_21_9', 1), ('VESTIGIVM', 273, 'uestigiis', '', '', '2_21_9', 1), ('CAESAR/N', 274, 'Caesar', '', '', '2_21_9', 4), ('ITAQVE', 275, 'Itaque', '', '', '2_21_9', 2), ('NEQVE', 276, 'nec', '', '', '2_21_9', 6), ('PRAEPARO/2', 277, 'praeparata', '', '', '2_21_9', 1), ('IN', 278, 'in', '', '', '2_21_9', 12), ('OCEANVS/1', 279, 'Oceanum', '', '', '2_21_9', 1), ('FVGA', 280, 'fuga', '', '', '2_21_9', 2), ('NEQVE', 281, 'nec', '', '', '2_21_9', 6), ('MVNIO/2', 282, 'munita', '', '', '2_21_9', 1), ('PRAESIDIVM', 283, 'praesidiis', '', '', '2_21_9', 1), ('VTER/1', 284, 'utraque', '', '', '2_21_9', 1), ('AEGYPTVS/N', 285, 'Aegypti', '', '', '2_21_9', 1), ('CORNV', 286, 'cornua', '', '', '2_21_9', 2), ('PARAETONIVM/N', 287, 'Paraetonium', '', '', '2_21_9', 1), ('ATQVE/1', 288, 'atque', '', '', '2_21_9', 2), ('PELVSIVM/N', 289, 'Pelusium', '', '', '2_21_9', 1), ('PROSVM/1', 290, 'profuere', '', '', '2_21_9', 1), ('PROPE/2', 291, 'prope', '', '', '2_21_9', 1), ('MANVS/1', 292, 'manu', '', '', '2_21_9', 2), ('TENEO', 293, 'tenebantur', '', '', '2_21_9', 1), ('PRIOR', 294, 'Prior', '', '', '2_21_9', 1), ('FERRVM', 295, 'ferrum', '', '', '2_21_9', 1), ('OCCVPO/2', 296, 'occupauit', '', '', '2_21_9', 1), ('ANTONIVS/N', 297, 'Antonius', '', '', '2_21_9', 5), ('REGINA', 298, 'regina', '', '', '2_21_9', 3), ('AD/2', 299, 'ad', '', '', '2_21_9', 8), ('PES', 300, 'pedes', '', '', '2_21_9', 1), ('CAESAR/N', 301, 'Caesaris', '', '', '2_21_9', 4), ('PROVOLO/2', 302, 'prouoluta', '', '', '2_21_9', 1), ('TENTO', 303, 'temptauit', '', '', '2_21_9', 1), ('OCVLVS', 304, 'oculos', '', '', '2_21_9', 1), ('DVX', 305, 'ducis', '', '', '2_21_9', 2), ('FRVSTRA', 306, 'Frustra', '', '', '2_21_9', 1), ('QVIDEM', 307, 'quidem', '', '', '2_21_9', 2), ('NAM', 308, 'nam', '', '', '2_21_9', 1), ('PVLCHRITVDO', 309, 'pulchritudo', '', '', '2_21_9', 1), ('INFRA/2', 310, 'infra', '', '', '2_21_9', 1), ('PVDICITIA', 311, 'pudicitiam', '', '', '2_21_9', 1), ('PRINCEPS/1', 312, 'principis', '', '', '2_21_9', 2), ('SVM/1', 313, 'fuit', '', '', '2_21_9', 5), ('NEQVE', 314, 'Nec', '', '', '2_21_10', 6), ('ILLE', 315, 'illa', '', '', '2_21_10', 3), ('DE', 316, 'de', '', '', '2_21_10', 2), ('VITA', 317, 'uita', '', '', '2_21_10', 1), ('QVI/1', 318, 'quae', '', '', '2_21_10', 4), ('OFFERO', 319, 'offerebatur', '', '', '2_21_10', 1), ('SED', 320, 'sed', '', '', '2_21_10', 4), ('DE', 321, 'de', '', '', '2_21_10', 2), ('PARS', 322, 'parte', '', '', '2_21_10', 1), ('REGNVM', 323, 'regni', '', '', '2_21_10', 1), ('LABORO', 324, 'laborabat', '', '', '2_21_10', 1), ('QVI/1', 325, 'Quod', '', '', '2_21_10', 4), ('VBI/1', 326, 'ubi', '', '', '2_21_10', 1), ('DESPERO', 327, 'desperauit', '', '', '2_21_10', 1), ('AB', 328, 'a', '', '', '2_21_10', 5), ('PRINCEPS/1', 329, 'principe', '', '', '2_21_10', 2), ('SERVO', 330, 'seruari', '', '', '2_21_10', 1), ('QVE', 331, 'que', '', '', '2_21_10', 9), ('SVI/1', 332, 'se', '', '', '2_21_10', 5), ('TRIVMPHVS', 333, 'triumpho', '', '', '2_21_10', 1), ('VIDEO', 334, 'uidit', '', '', '2_21_10', 1), ('INCAVTVS', 335, 'incautiorem', '', '', '2_21_10', 1), ('NANCISCOR', 336, 'nancta', '', '', '2_21_10', 1), ('CVSTODIA', 337, 'custodiam', '', '', '2_21_10', 1), ('IN', 338, 'in', '', '', '2_21_10', 12), ('MAVSOLEVM', 339, 'mausoleum', '', '', '2_21_10', 1), ('SVI/1', 340, 'se', '', '', '2_21_10', 5), ('SEPVLCRVM', 341, 'sepulchra', '', '', '2_21_10', 1), ('REX', 342, 'regum', '', '', '2_21_10', 2), ('SIC', 343, 'sic', '', '', '2_21_10', 2), ('VOCO', 344, 'uocant', '', '', '2_21_10', 1), ('RECIPIO', 345, 'recepit', '', '', '2_21_10', 1), ('IBI', 346, 'Ibi', '', '', '2_21_12', 1), ('MAGNVS', 347, 'maximos', '', '', '2_21_12', 1), ('VT/4', 348, 'ut', '', '', '2_21_12', 4), ('SOLEO', 349, 'solebat', '', '', '2_21_12', 1), ('INDVO', 350, 'induta', '', '', '2_21_12', 1), ('CVLTVS/1', 351, 'cultus', '', '', '2_21_12', 2), ('IN', 352, 'in', '', '', '2_21_12', 12), ('REFERO', 353, 'referto', '', '', '2_21_12', 1), ('ODOR', 354, 'odoribus', '', '', '2_21_12', 1), ('SOLIVM', 355, 'solio', '', '', '2_21_12', 1), ('IVXTA/1', 356, 'iuxta', '', '', '2_21_12', 1), ('SVVS', 357, 'suum', '', '', '2_21_12', 1), ('SVI/1', 358, 'se', '', '', '2_21_12', 5), ('COLLOCO', 359, 'conlocauit', '', '', '2_21_12', 1), ('ANTONIVS/N', 360, 'Antonium', '', '', '2_21_12', 5), ('ADMOVEO', 361, 'admotis', '', '', '2_21_12', 1), ('QVE', 362, 'que', '', '', '2_21_12', 9), ('AD/2', 363, 'ad', '', '', '2_21_12', 8), ('VENA', 364, 'uenas', '', '', '2_21_12', 1), ('SERPENS', 365, 'serpentibus', '', '', '2_21_12', 1), ('SIC', 366, 'sic', '', '', '2_21_12', 2), ('MORS', 367, 'morte', '', '', '2_21_12', 1), ('QVASI/1', 368, 'quasi', '', '', '2_21_12', 3), ('SOMNVS', 369, 'somno', '', '', '2_21_12', 1), ('SOLVO', 370, 'soluta', '', '', '2_21_12', 1), ('SVM/1', 371, 'est', '', '', '2_21_12', 5)]
section_list ={'1.1.1': 'start', '2.21.1': 'start', '2.21.2': '2.21.1', '2.21.3': '2.21.2', '2.21.4': '2.21.3', '2.21.5': '2.21.4', '2.21.6': '2.21.5', '2.21.7': '2.21.6', '2.21.8': '2.21.7', '2.21.9': '2.21.8', '2.21.10': '2.21.9', '2.21.12': '2.21.10', 'end': '2.21.12', 'start': 'start'}
title = "Florus, Epitome 2.21 (Cleopatra) "
section_level =  3
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)