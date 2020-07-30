import text
nan=""
section_words = {'start': -1, '14': 86, '10': 107, '13': 109, '18': 105, '16': 82, '5': 104, '17': 99, '1': 97, '9': 98, '3': 114, '8': 116, '20': 115, '19': 72, '7': 92, '11': 112, '15': 117, '6': 110, '2': 101, '12': 96, '4': 111, 'end': -2}
the_text =  [('AB', 0, 'AB', '', '', '14', 1), ('AH', 1, 'AH', '', '', '10', 1), ('AEQVALIS/2', 2, 'AEQUALIS', '', '', '13', 1), ('AESTIMO', 3, 'AESTIMARE', '', '', '18', 1), ('ALA', 4, 'ALA', '', '', '13', 1), ('ALTERNVS', 5, 'ALTERNUS', '', '', '16', 1), ('AMOR', 6, 'AMOR', '', '', '10', 1), ('AN', 7, 'AN', '', '', '5', 1), ('AQVILA', 8, 'AQUILA', '', '', '17', 1), ('ARMIGER/1', 9, 'ARMIGER', '', '', '13', 1), ('AVDEO', 10, 'AUDERE', '', '', '1', 1), ('AVDIO', 11, 'AUDIRE', '', '', '9', 1), ('AVGEO', 12, 'AUGERE', '', '', '3', 1), ('AVRIS', 13, 'AURIS', '', '', '9', 1), ('AVIS', 14, 'AUIS', '', '', '16', 1), ('AXIS', 15, 'AXIS', '', '', '16', 1), ('CASTRA/2', 16, 'CASTRA', '', '', '5', 1), ('CATERVA', 17, 'CATERUA', '', '', '1', 1), ('CELSVS', 18, 'CELSUS', '', '', '3', 1), ('CERNO', 19, 'CERNERE', '', '', '8', 1), ('CERTVS', 20, 'CERTUS', '', '', '18', 1), ('COITVS', 21, 'COETUS', '', '', '20', 1), ('COGNOSCO', 22, 'COGNOSCERE', '', '', '17', 1), ('COLLIGO/3', 23, 'COLLIGERE', '', '', '19', 1), ('CONCILIVM', 24, 'CONCILIUM', '', '', '19', 1), ('CONFERO', 25, 'CONFERRE', '', '', '16', 1), ('CONSVL', 26, 'CONSUL', '', '', '10', 1), ('CONTINVVS', 27, 'CONTINUUS', '', '', '5', 1), ('CRESCO', 28, 'CRESCERE', '', '', '5', 1), ('CVLMEN', 29, 'CULMEN', '', '', '7', 1), ('CVM/3', 30, 'CUM', '', '', '11', 1), ('CVRO', 31, 'CURARE', '', '', '17', 1), ('DISCO', 32, 'DISCERE', '', '', '11', 1), ('DVO', 33, 'DUO', '', '', '13', 1), ('EGO', 34, 'EGO', '', '', '19', 1), ('EOVS/A', 35, 'EOUS', '', '', '14', 1), ('ET/2', 36, 'ET', '', '', '8', 1), ('EXSVLTO', 37, 'EXULTARE', '', '', '8', 1), ('FAMA', 38, 'FAMA', '', '', '3', 1), ('FERO', 39, 'FERRE', '', '', '15', 1), ('FIDVCIA', 40, 'FIDUCIA', '', '', '5', 1), ('GALLIA/N', 41, 'GALLIA', '', '', '8', 1), ('GEMINVS', 42, 'GEMINUS', '', '', '15', 1), ('HABEO', 43, 'HABERE', '', '', '6', 1), ('HIC/1', 44, 'HIC', '', '', '19', 2), ('HIC/1', 45, 'HIC', '', '', '20', 2), ('IAM', 46, 'IAM', '', '', '6', 1), ('IMPERIVM', 47, 'IMPERIUM', '', '', '18', 1), ('IN', 48, 'IN', '', '', '18', 1), ('INTER', 49, 'INTER', '', '', '2', 1), ('IPSE', 50, 'IPSE', '', '', '12', 1), ('EO/1', 51, 'IRE', '', '', '10', 1), ('IVNGO', 52, 'IUNGERE', '', '', '15', 1), ('IVPPITER/N', 53, 'IUPPITER', '', '', '11', 1), ('LABOR/1', 54, 'LABOR', '', '', '4', 1), ('LOQVOR', 55, 'LOQUI', '', '', '2', 1), ('MAIESTAS', 56, 'MAIESTAS', '', '', '7', 1), ('METIOR', 57, 'METIRI', '', '', '19', 1), ('MICO', 58, 'MICARE', '', '', '20', 1), ('MILES', 59, 'MILES', '', '', '6', 1), ('MINVO', 60, 'MINUERE', '', '', '4', 1), ('MITTO', 61, 'MITTERE', '', '', '14', 1), ('MVNDVS/2', 62, 'MUNDUS', '', '', '9', 1), ('NATVRA', 63, 'NATURA', '', '', '12', 1), ('NE/2', 64, 'NE', '', '', '1', 1), ('NEQVE', 65, 'NEQUE', '', '', '3', 1), ('NESCIVS', 66, 'NESCIUS', '', '', '12', 1), ('NIMIVS', 67, 'NIMIUS', '', '', '10', 1), ('NON', 68, 'NON', '', '', '17', 1), ('NOSTER', 69, 'NOSTER', '', '', '2', 1), ('OCCIDVVS', 70, 'OCCIDUUS', '', '', '14', 1), ('OMNIS', 71, 'OMNIS', '', '', '9', 1), ('ORBIS', 72, 'ORBIS', '', '', '19', 1), ('PARNASVS/N', 73, 'PARNASUS', '', '', '15', 1), ('PECTVS', 74, 'PECTUS', '', '', '6', 1), ('PER', 75, 'PER', '', '', '9', 1), ('PERHIBEO', 76, 'PERHIBERE', '', '', '11', 1), ('PLAGA/2', 77, 'PLAGA', '', '', '14', 1), ('PRECOR', 78, 'PRECARI', '', '', '1', 1), ('PRINCEPS/1', 79, 'PRINCEPS', '', '', '17', 1), ('PROCER', 80, 'PROCERES', '', '', '2', 1), ('PVDOR', 81, 'PUDOR', '', '', '4', 1), ('PYTHIVS/N', 82, 'PYTHIUS', '', '', '16', 1), ('QVE', 83, 'QUE', '', '', '6', 4), ('QVE', 84, 'QUE', '', '', '7', 4), ('QVE', 85, 'QUE', '', '', '9', 4), ('QVE', 86, 'QUE', '', '', '14', 4), ('QVI/1', 87, 'QUI', '', '', '3', 2), ('QVI/1', 88, 'QUI', '', '', '8', 2), ('QVISQVIS/2', 89, 'QUISQUIS', '', '', '20', 1), ('REGNVM', 90, 'REGNUM', '', '', '12', 1), ('ROMANVS/A', 91, 'ROMANUS', '', '', '7', 1), ('SENATVS', 92, 'SENATUS', '', '', '7', 1), ('SERVO', 93, 'SERUARE', '', '', '4', 1), ('SPATIVM', 94, 'SPATIUM', '', '', '11', 1), ('SVBICIO', 95, 'SUBICERE', '', '', '1', 1), ('SVVS', 96, 'SUUS', '', '', '12', 1), ('TANTVS', 97, 'TANTUS', '', '', '1', 1), ('TERRA', 98, 'TERRA', '', '', '9', 2), ('TERRA', 99, 'TERRA', '', '', '17', 2), ('THALIA/N', 100, 'THALIA', '', '', '2', 1), ('TOT', 101, 'TOT', '', '', '2', 1), ('TOTVS', 102, 'TOTUS', '', '', '6', 1), ('TV', 103, 'TU', '', '', '3', 3), ('TV', 104, 'TU', '', '', '5', 3), ('TV', 105, 'TU', '', '', '18', 3), ('VBIQVE', 106, 'UBIQUE', '', '', '20', 1), ('VRGEO', 107, 'URGERE', '', '', '10', 1), ('VT/4', 108, 'UT', '', '', '11', 1), ('VTRIMQVE', 109, 'UTRIMQUE', '', '', '13', 1), ('VATES', 110, 'UATES', '', '', '6', 1), ('VEL/1', 111, 'UEL', '', '', '4', 1), ('VOLO/3', 112, 'UELLE', '', '', '11', 1), ('VERVS', 113, 'UERUS', '', '', '3', 1), ('VETO', 114, 'UETARE', '', '', '3', 1), ('VIDEO', 115, 'UIDERE', '', '', '20', 1), ('VIR', 116, 'UIR', '', '', '8', 1), ('VOLATVS', 117, 'UOLATUS', '', '', '15', 1)]
section_list ={'1.1': 'start', '14': 'start', '10': '14', '13': '10', '18': '13', '16': '18', '5': '16', '17': '5', '1': '17', '9': '1', '3': '9', '8': '3', '20': '8', '19': '20', '7': '19', '11': '7', '15': '11', '6': '15', '2': '6', '12': '2', '4': '12', 'end': '4', 'start': 'start'}
title = "Claudian, De Raptu Prosperinae"
section_level =  2
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)