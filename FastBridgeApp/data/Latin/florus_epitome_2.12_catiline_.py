import text
nan=""
section_words = {'start': -1, '2.12.1': 25, '2.12.2': 51, '2.12.3': 82, '2.12.4': 100, '2.12.5': 122, '2.12.6': 133, '2.12.7': 159, '2.12.8': 193, '2.12.9': 229, '2.12.10': 240, '2.12.11': 268, '2.12.12': 305, 'end': -2}
the_text =  [('CATILINA/N', 0, 'Catilinam', '', '', '2_12_1', 4), ('LVXVRIA', 1, 'luxuria', '', '', '2_12_1', 1), ('PRIMVM', 2, 'primum', '', '', '2_12_1', 1), ('TVM', 3, 'tum', '', '', '2_12_1', 4), ('HINC', 4, 'hinc', '', '', '2_12_1', 1), ('CONFLO', 5, 'conflata', '', '', '2_12_1', 1), ('EGESTAS', 6, 'egestas', '', '', '2_12_1', 1), ('RES', 7, 'rei', '', '', '2_12_1', 2), ('FAMILIARIS/2', 8, 'familiaris', '', '', '2_12_1', 1), ('SIMVL/1', 9, 'simul', '', '', '2_12_1', 1), ('OCCASIO', 10, 'occasio', '', '', '2_12_1', 1), ('QVI/1', 11, 'quod', '', '', '2_12_1', 10), ('IN', 12, 'in', '', '', '2_12_1', 9), ('EXTREMVS', 13, 'extremis', '', '', '2_12_1', 1), ('FINIS', 14, 'finibus', '', '', '2_12_1', 1), ('MVNDVS/1', 15, 'mundi', '', '', '2_12_1', 1), ('ARMA', 16, 'arma', '', '', '2_12_1', 2), ('ROMANVS/A', 17, 'Romana', '', '', '2_12_1', 1), ('PEREGRINOR', 18, 'peregrinabantur', '', '', '2_12_1', 1), ('IN', 19, 'in', '', '', '2_12_1', 9), ('NEFARIVS', 20, 'nefaria', '', '', '2_12_1', 1), ('CONSILIVM', 21, 'consilia', '', '', '2_12_1', 1), ('OPPRIMO', 22, 'opprimendae', '', '', '2_12_1', 4), ('PATRIA', 23, 'patriae', '', '', '2_12_1', 3), ('SVVS', 24, 'suae', '', '', '2_12_1', 4), ('COMPELLO/2', 25, 'conpulere', '', '', '2_12_1', 1), ('SENATVS', 26, 'Senatum', '', '', '2_12_2', 4), ('CONFODIO', 27, 'confodere', '', '', '2_12_2', 1), ('CONSVL', 28, 'consules', '', '', '2_12_2', 3), ('TRVCIDO', 29, 'trucidare', '', '', '2_12_2', 1), ('DISTRINGO', 30, 'distringere', '', '', '2_12_2', 1), ('INCENDIVM', 31, 'incendiis', '', '', '2_12_2', 2), ('VRBS', 32, 'urbem', '', '', '2_12_2', 3), ('DIRIPIO', 33, 'diripere', '', '', '2_12_2', 1), ('AERARIVM', 34, 'aerarium', '', '', '2_12_2', 1), ('TOTVS', 35, 'totam', '', '', '2_12_2', 2), ('DENIQVE', 36, 'denique', '', '', '2_12_2', 1), ('RESPVBLICA', 37, 'rem publicam', '', '', '2_12_2', 1), ('FVNDITVS', 38, 'funditus', '', '', '2_12_2', 1), ('TOLLO', 39, 'tollere', '', '', '2_12_2', 1), ('ET/2', 40, 'et', '', '', '2_12_2', 3), ('QVISQVIS/2', 41, 'quidquid', '', '', '2_12_2', 1), ('NEQVE', 42, 'nec', '', '', '2_12_2', 2), ('HANNIBAL/N', 43, 'Annibal', '', '', '2_12_2', 1), ('VIDEO', 44, 'uideretur', '', '', '2_12_2', 1), ('OPTO', 45, 'optasse', '', '', '2_12_2', 1), ('QVI/1', 46, 'quibus', '', '', '2_12_2', 10), ('O', 47, '—o', '', '', '2_12_2', 1), ('NEFAS', 48, 'nefas', '', '', '2_12_2', 2), ('SOCIVS/1', 49, 'sociis', '', '', '2_12_2', 1), ('AGGREDIOR', 50, 'adgressus', '', '', '2_12_2', 1), ('SVM/1', 51, 'est', '', '', '2_12_2', 8), ('IPSE', 52, 'Ipse', '', '', '2_12_3', 1), ('PATRICIVS', 53, 'patricius', '', '', '2_12_3', 2), ('SED', 54, 'sed', '', '', '2_12_3', 3), ('HIC/1', 55, 'hoc', '', '', '2_12_3', 2), ('PARVVS/2', 56, 'minus', '', '', '2_12_3', 1), ('SVM/1', 57, 'est', '', '', '2_12_3', 8), ('CVRIVS/N', 58, 'Curii', '', '', '2_12_3', 1), ('PORCIVS/A', 59, 'Porcii', '', '', '2_12_3', 1), ('SVLLA/N', 60, 'Sullae', '', '', '2_12_3', 1), ('CETHEGVS/N', 61, 'Cethegi', '', '', '2_12_3', 1), ('AVTRONIVS/N', 62, 'Autronii', '', '', '2_12_3', 1), ('VARGVNTEIVS/N', 63, 'Uarguntei', '', '', '2_12_3', 1), ('ATQVE/1', 64, 'atque', '', '', '2_12_3', 2), ('LONGINVS/N', 65, 'Longini', '', '', '2_12_3', 1), ('QVI/1', 66, 'quae', '', '', '2_12_3', 10), ('FAMILIA', 67, 'familiae', '', '', '2_12_3', 2), ('QVI/1', 68, 'quae', '', '', '2_12_3', 10), ('SENATVS', 69, 'senatus', '', '', '2_12_3', 4), ('INSIGNE', 70, 'insignia', '', '', '2_12_3', 1), ('LENTVLVS/N', 71, 'Lentulus', '', '', '2_12_3', 2), ('QVOQVE', 72, 'quoque', '', '', '2_12_3', 1), ('TVM', 73, 'tum', '', '', '2_12_3', 4), ('CVM/3', 74, 'cum', '', '', '2_12_3', 1), ('MAXIME', 75, 'maxime', '', '', '2_12_3', 1), ('PRAETOR', 76, 'praetor', '', '', '2_12_3', 3), ('HIC/1', 77, 'Hoc', '', '', '2_12_3', 2), ('OMNIS', 78, 'omnis', '', '', '2_12_3', 2), ('IMMANIS', 79, 'inmanissimi', '', '', '2_12_3', 1), ('FACINVS', 80, 'facinoris', '', '', '2_12_3', 1), ('SATELLES', 81, 'satellites', '', '', '2_12_3', 1), ('HABEO', 82, 'habuit', '', '', '2_12_3', 2), ('ADDO', 83, 'Additum', '', '', '2_12_4', 1), ('SVM/1', 84, 'est', '', '', '2_12_4', 8), ('PIGNVS', 85, 'pignus', '', '', '2_12_4', 1), ('CONIVRATIO', 86, 'coniurationis', '', '', '2_12_4', 3), ('SANGVIS', 87, 'sanguis', '', '', '2_12_4', 1), ('HVMANVS', 88, 'humanus', '', '', '2_12_4', 1), ('QVI/1', 89, 'quem', '', '', '2_12_4', 10), ('CIRCVMFERO', 90, 'circumlatum', '', '', '2_12_4', 1), ('PATERA', 91, 'pateris', '', '', '2_12_4', 1), ('BIBO/2', 92, 'bibere', '', '', '2_12_4', 2), ('SVMMVS', 93, 'summum', '', '', '2_12_4', 1), ('NEFAS', 94, 'nefas', '', '', '2_12_4', 2), ('NI/2', 95, 'ni', '', '', '2_12_4', 1), ('AMPLVS', 96, 'amplius', '', '', '2_12_4', 2), ('SVM/1', 97, 'esset', '', '', '2_12_4', 8), ('PROPTER/2', 98, 'propter', '', '', '2_12_4', 1), ('QVI/1', 99, 'quod', '', '', '2_12_4', 10), ('BIBO/2', 100, 'biberunt', '', '', '2_12_4', 2), ('AGO', 101, 'Actum', '', '', '2_12_5', 2), ('SVM/1', 102, 'erat', '', '', '2_12_5', 8), ('DE', 103, 'de', '', '', '2_12_5', 2), ('PVLCHER', 104, 'pulcherrimo', '', '', '2_12_5', 2), ('IMPERIVM', 105, 'imperio', '', '', '2_12_5', 2), ('NISI', 106, 'nisi', '', '', '2_12_5', 2), ('ILLE', 107, 'illa', '', '', '2_12_5', 2), ('CONIVRATIO', 108, 'coniuratio', '', '', '2_12_5', 3), ('IN', 109, 'in', '', '', '2_12_5', 9), ('CICERO/N', 110, 'Ciceronem', '', '', '2_12_5', 2), ('ET/2', 111, 'et', '', '', '2_12_5', 3), ('ANTONIVS/N', 112, 'Antonium', '', '', '2_12_5', 2), ('CONSVL', 113, 'consules', '', '', '2_12_5', 3), ('INCIDO/1', 114, 'incidisset', '', '', '2_12_5', 1), ('QVI/1', 115, 'quorum', '', '', '2_12_5', 10), ('ALTER', 116, 'alter', '', '', '2_12_5', 3), ('INDVSTRIA', 117, 'industria', '', '', '2_12_5', 1), ('RES', 118, 'rem', '', '', '2_12_5', 2), ('PATEFACIO', 119, 'patefecit', '', '', '2_12_5', 1), ('ALTER', 120, 'alter', '', '', '2_12_5', 3), ('MANVS/1', 121, 'manu', '', '', '2_12_5', 2), ('OPPRIMO', 122, 'oppressit', '', '', '2_12_5', 4), ('TANTVS', 123, 'Tanti', '', '', '2_12_6', 1), ('SCELVS', 124, 'sceleris', '', '', '2_12_6', 2), ('INDICIVM', 125, 'indicium', '', '', '2_12_6', 1), ('PER', 126, 'per', '', '', '2_12_6', 1), ('FVLVIVS/N', 127, 'Fuluiam', '', '', '2_12_6', 1), ('EMERGO', 128, 'emersit', '', '', '2_12_6', 1), ('VILIS', 129, 'uilissimum', '', '', '2_12_6', 1), ('SCORTVM', 130, 'scortum', '', '', '2_12_6', 1), ('SED', 131, 'sed', '', '', '2_12_6', 3), ('PATRICIVS', 132, 'patriciis', '', '', '2_12_6', 2), ('INNOCENS', 133, 'innocentius', '', '', '2_12_6', 1), ('CONSVL', 134, 'Consul', '', '', '2_12_7', 3), ('HABEO', 135, 'habito', '', '', '2_12_7', 2), ('SENATVS', 136, 'senatu', '', '', '2_12_7', 4), ('IN', 137, 'in', '', '', '2_12_7', 9), ('PRAESENS', 138, 'praesentem', '', '', '2_12_7', 1), ('REVS', 139, 'reum', '', '', '2_12_7', 1), ('PERORO', 140, 'perorauit', '', '', '2_12_7', 1), ('SED', 141, 'sed', '', '', '2_12_7', 3), ('NON', 142, 'non', '', '', '2_12_7', 2), ('AMPLVS', 143, 'amplius', '', '', '2_12_7', 2), ('PROFICISCOR', 144, 'profectum', '', '', '2_12_7', 2), ('QVAM/1', 145, 'quam', '', '', '2_12_7', 2), ('VT/4', 146, 'ut', '', '', '2_12_7', 1), ('HOSTIS', 147, 'hostis', '', '', '2_12_7', 3), ('EVADO/2', 148, 'euaderet', '', '', '2_12_7', 1), ('SVI/1', 149, 'se', '', '', '2_12_7', 2), ('QVE', 150, 'que', '', '', '2_12_7', 1), ('TVM', 151, 'tum', '', '', '2_12_7', 4), ('PALAM/1', 152, 'palam', '', '', '2_12_7', 2), ('ATQVE/1', 153, 'ac', '', '', '2_12_7', 2), ('PROFITEOR', 154, 'professe', '', '', '2_12_7', 1), ('INCENDIVM', 155, 'incendium', '', '', '2_12_7', 2), ('SVVS', 156, 'suum', '', '', '2_12_7', 4), ('RESTINGVO', 157, 'restincturum', '', '', '2_12_7', 1), ('RVINA', 158, 'ruina', '', '', '2_12_7', 1), ('MINOR', 159, 'minaretur', '', '', '2_12_7', 1), ('ET/2', 160, 'Et', '', '', '2_12_8', 3), ('ILLE', 161, 'ille', '', '', '2_12_8', 2), ('QVIDEM', 162, 'quidem', '', '', '2_12_8', 1), ('AD/2', 163, 'ad', '', '', '2_12_8', 2), ('PRAEPARO/2', 164, 'praeparatum', '', '', '2_12_8', 1), ('AB', 165, 'a', '', '', '2_12_8', 5), ('MANLIVS/N', 166, 'Manlio', '', '', '2_12_8', 1), ('IN', 167, 'in', '', '', '2_12_8', 9), ('ETRVRIA/N', 168, 'Etruria', '', '', '2_12_8', 2), ('EXERCITVS/1', 169, 'exercitum', '', '', '2_12_8', 2), ('PROFICISCOR', 170, 'proficiscitur', '', '', '2_12_8', 2), ('SIGNVM', 171, 'signa', '', '', '2_12_8', 2), ('INFERO', 172, 'inlaturus', '', '', '2_12_8', 1), ('VRBS', 173, 'urbi', '', '', '2_12_8', 3), ('LENTVLVS/N', 174, 'Lentulus', '', '', '2_12_8', 2), ('DESTINO', 175, 'destinatum', '', '', '2_12_8', 1), ('FAMILIA', 176, 'familiae', '', '', '2_12_8', 2), ('SVVS', 177, 'suae', '', '', '2_12_8', 4), ('SIBYLLINVS/A', 178, 'Sibyllinis', '', '', '2_12_8', 1), ('VERSVS/1', 179, 'uersibus', '', '', '2_12_8', 1), ('REGNVM', 180, 'regnum', '', '', '2_12_8', 1), ('SVI/1', 181, 'sibi', '', '', '2_12_8', 2), ('VATICINOR', 182, 'uaticinans', '', '', '2_12_8', 1), ('AD/2', 183, 'ad', '', '', '2_12_8', 2), ('PRAESTITVO', 184, 'praestitutum', '', '', '2_12_8', 1), ('AB', 185, 'a', '', '', '2_12_8', 5), ('CATILINA/N', 186, 'Catilina', '', '', '2_12_8', 4), ('DIES', 187, 'diem', '', '', '2_12_8', 1), ('VRBS', 188, 'urbe', '', '', '2_12_8', 3), ('TOTVS', 189, 'tota', '', '', '2_12_8', 2), ('VIR', 190, 'uiros', '', '', '2_12_8', 1), ('FAX', 191, 'faces', '', '', '2_12_8', 1), ('TELVM', 192, 'tela', '', '', '2_12_8', 1), ('DISPONO', 193, 'disponit', '', '', '2_12_8', 1), ('NEQVE', 194, 'Nec', '', '', '2_12_9', 2), ('CIVILIS', 195, 'ciuili', '', '', '2_12_9', 1), ('CONSPIRATIO', 196, 'conspiratione', '', '', '2_12_9', 1), ('CONTENDO', 197, 'contentus', '', '', '2_12_9', 1), ('LEGATVS', 198, 'legatos', '', '', '2_12_9', 1), ('ALLOBROX/A', 199, 'Allobrogum', '', '', '2_12_9', 1), ('QVI/1', 200, 'qui', '', '', '2_12_9', 10), ('TVM', 201, 'tum', '', '', '2_12_9', 4), ('FORTE', 202, 'forte', '', '', '2_12_9', 1), ('ASSVM/1', 203, 'aderant', '', '', '2_12_9', 1), ('IN', 204, 'in', '', '', '2_12_9', 9), ('ARMA', 205, 'arma', '', '', '2_12_9', 2), ('SOLLICITO', 206, 'sollicitat', '', '', '2_12_9', 1), ('EO/1', 207, 'Isset', '', '', '2_12_9', 1), ('VLTRA/2', 208, 'ultra', '', '', '2_12_9', 1), ('ALPES/N', 209, 'Alpes', '', '', '2_12_9', 1), ('FVROR/1', 210, 'furor', '', '', '2_12_9', 1), ('NISI', 211, 'nisi', '', '', '2_12_9', 2), ('ALTER', 212, 'altera', '', '', '2_12_9', 3), ('PRODITIO/1', 213, 'proditione', '', '', '2_12_9', 1), ('VVLTVRCIVS/N', 214, 'Uolturci', '', '', '2_12_9', 1), ('PRAETOR', 215, 'praetoris', '', '', '2_12_9', 3), ('LITTERA', 216, 'litterae', '', '', '2_12_9', 1), ('TENEO', 217, 'tenerentur', '', '', '2_12_9', 1), ('STATIM', 218, 'Statim', '', '', '2_12_9', 1), ('CICERO/N', 219, 'Ciceronis', '', '', '2_12_9', 2), ('IMPERIVM', 220, 'imperio', '', '', '2_12_9', 2), ('INICIO', 221, 'iniecta', '', '', '2_12_9', 1), ('SVM/1', 222, 'est', '', '', '2_12_9', 8), ('BARBARVS/2', 223, 'barbaris', '', '', '2_12_9', 1), ('MANVS/1', 224, 'manus', '', '', '2_12_9', 2), ('PALAM/1', 225, 'palam', '', '', '2_12_9', 2), ('PRAETOR', 226, 'praetor', '', '', '2_12_9', 3), ('IN', 227, 'in', '', '', '2_12_9', 9), ('SENATVS', 228, 'senatu', '', '', '2_12_9', 4), ('CONVINCO', 229, 'conuincitur', '', '', '2_12_9', 1), ('DE', 230, 'De', '', '', '2_12_10', 2), ('SVPPLICIVM', 231, 'supplicio', '', '', '2_12_10', 1), ('AGO', 232, 'agentibus', '', '', '2_12_10', 2), ('CAESAR/N', 233, 'Caesar', '', '', '2_12_10', 1), ('PARCO', 234, 'parcendum', '', '', '2_12_10', 1), ('DIGNITAS', 235, 'dignitati', '', '', '2_12_10', 1), ('CATO/N', 236, 'Cato', '', '', '2_12_10', 1), ('ANIMADVERTO', 237, 'animaduertendum', '', '', '2_12_10', 1), ('PRO/1', 238, 'pro', '', '', '2_12_10', 2), ('SCELVS', 239, 'scelere', '', '', '2_12_10', 2), ('CENSEO', 240, 'censebat', '', '', '2_12_10', 1), ('QVI/1', 241, 'Quam', '', '', '2_12_11', 10), ('SENTENTIA', 242, 'sententiam', '', '', '2_12_11', 1), ('SEQVOR', 243, 'secutis', '', '', '2_12_11', 1), ('OMNIS', 244, 'omnibus', '', '', '2_12_11', 2), ('IN', 245, 'in', '', '', '2_12_11', 9), ('CARCER', 246, 'carcere', '', '', '2_12_11', 1), ('PARRICIDA', 247, 'parricidae', '', '', '2_12_11', 1), ('STRANGVLO', 248, 'strangulantur', '', '', '2_12_11', 1), ('QVAMVIS/1', 249, 'Quamuis', '', '', '2_12_11', 1), ('PARS', 250, 'parte', '', '', '2_12_11', 1), ('CONIVRATIO', 251, 'coniurationis', '', '', '2_12_11', 3), ('OPPRIMO', 252, 'oppressa', '', '', '2_12_11', 4), ('TAMEN', 253, 'tamen', '', '', '2_12_11', 1), ('AB', 254, 'ab', '', '', '2_12_11', 5), ('INCIPIO', 255, 'incepto', '', '', '2_12_11', 1), ('CATILINA/N', 256, 'Catilina', '', '', '2_12_11', 4), ('NON', 257, 'non', '', '', '2_12_11', 2), ('DESISTO', 258, 'destitit', '', '', '2_12_11', 1), ('INFESTVS', 259, 'infestis', '', '', '2_12_11', 1), ('AB', 260, 'ab', '', '', '2_12_11', 5), ('ETRVRIA/N', 261, 'Etruria', '', '', '2_12_11', 2), ('SIGNVM', 262, 'signis', '', '', '2_12_11', 2), ('PATRIA', 263, 'patriam', '', '', '2_12_11', 3), ('PETO', 264, 'petens', '', '', '2_12_11', 1), ('OBVIVS', 265, 'obuio', '', '', '2_12_11', 1), ('ANTONIVS/N', 266, 'Antonii', '', '', '2_12_11', 2), ('EXERCITVS/1', 267, 'exercitu', '', '', '2_12_11', 2), ('OPPRIMO', 268, 'opprimitur', '', '', '2_12_11', 4), ('QVAM/1', 269, 'Quam', '', '', '2_12_12', 2), ('ATROX', 270, 'atrociter', '', '', '2_12_12', 1), ('DIMICO', 271, 'dimicatum', '', '', '2_12_12', 1), ('SVM/1', 272, 'sit', '', '', '2_12_12', 8), ('EXITVS', 273, 'exitus', '', '', '2_12_12', 1), ('DOCEO', 274, 'docuit', '', '', '2_12_12', 1), ('NEMO', 275, 'Nemo', '', '', '2_12_12', 1), ('HOSTIS', 276, 'hostium', '', '', '2_12_12', 3), ('BELLVM', 277, 'bello', '', '', '2_12_12', 1), ('SVPERSVM/1', 278, 'superfuit', '', '', '2_12_12', 1), ('QVI/1', 279, 'quem', '', '', '2_12_12', 10), ('QVISQVE/2', 280, 'quis', '', '', '2_12_12', 1), ('IN', 281, 'in', '', '', '2_12_12', 9), ('PVGNO', 282, 'pugnando', '', '', '2_12_12', 1), ('CAPIO/2', 283, 'ceperat', '', '', '2_12_12', 1), ('LOCVS', 284, 'locum', '', '', '2_12_12', 1), ('IS', 285, 'eum', '', '', '2_12_12', 1), ('AMITTO', 286, 'amissa', '', '', '2_12_12', 1), ('ANIMA', 287, 'anima', '', '', '2_12_12', 1), ('CORPVS', 288, 'corpore', '', '', '2_12_12', 1), ('TEGO', 289, 'tegebat', '', '', '2_12_12', 1), ('CATILINA/N', 290, 'Catilina', '', '', '2_12_12', 4), ('LONGVS', 291, 'longe', '', '', '2_12_12', 1), ('AB', 292, 'a', '', '', '2_12_12', 5), ('SVVS', 293, 'suis', '', '', '2_12_12', 4), ('INTER', 294, 'inter', '', '', '2_12_12', 1), ('HOSTIS', 295, 'hostium', '', '', '2_12_12', 3), ('CADAVER', 296, 'cadauera', '', '', '2_12_12', 1), ('REPERIO', 297, 'repertus', '', '', '2_12_12', 1), ('SVM/1', 298, 'est', '', '', '2_12_12', 8), ('PVLCHER', 299, 'pulcherrima', '', '', '2_12_12', 2), ('MORS', 300, 'morte', '', '', '2_12_12', 1), ('SI/2', 301, 'si', '', '', '2_12_12', 1), ('PRO/1', 302, 'pro', '', '', '2_12_12', 2), ('PATRIA', 303, 'patria', '', '', '2_12_12', 3), ('SIC', 304, 'sic', '', '', '2_12_12', 1), ('CONCIDO/1', 305, 'concidisset', '', '', '2_12_12', 1)]
section_list ={'1.1.1': 'start', '2.12.1': 'start', '2.12.2': '2.12.1', '2.12.3': '2.12.2', '2.12.4': '2.12.3', '2.12.5': '2.12.4', '2.12.6': '2.12.5', '2.12.7': '2.12.6', '2.12.8': '2.12.7', '2.12.9': '2.12.8', '2.12.10': '2.12.9', '2.12.11': '2.12.10', '2.12.12': '2.12.11', 'end': '2.12.12', 'start': 'start'}
title = "Florus, Epitome 2.12 (Catiline) "
section_level =  3
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)