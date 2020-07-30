import text
nan=""
section_words = {'start': -1, '18': 295, '4': 256, '28': 273, '17': 279, '33': 193, '13': 236, '22': 281, '32': 213, '36': 241, '26': 302, '34': 277, '30': 271, '23': 291, '1': 260, '27': 165, '15': 237, '6': 288, '10': 283, '40': 289, '16': 248, '25': 293, '42': 253, '5': 296, '24': 249, '35': 286, '41': 225, '20': 301, '38': 299, '11': 278, '29': 259, '31': 285, '12': 282, '9': 264, '21': 251, '7': 280, '37': 267, '3': 294, '8': 276, '39': 235, '14': 287, '43': 243, '2': 298, '19': 300, 'end': -2}
the_text =  [('AB', 0, 'a', '', '', '18', 3), ('AB', 1, 'ab', '', '', '4', 3), ('AB', 2, 'ab', '', '', '28', 3), ('ACVMEN', 3, 'acuminis', '', '', '17', 1), ('ADEO/2', 4, 'adeo', '', '', '33', 2), ('ADEO/2', 5, 'adire', '', '', '13', 2), ('AGNOSCO', 6, 'agnouit', '', '', '22', 1), ('ADMIRATIO', 7, 'admiratione', '', '', '32', 1), ('ASPICIO', 8, 'aspexit', '', '', '22', 1), ('ALIQVANDO', 9, 'aliquando', '', '', '36', 1), ('ALIQVIS', 10, 'alicuius', '', '', '26', 2), ('ALIQVIS', 11, 'aliquid', '', '', '34', 2), ('ALIVS', 12, 'alia', '', '', '30', 4), ('ALIVS', 13, 'aliis', '', '', '23', 4), ('ALIVS', 14, 'alia', '', '', '28', 4), ('ALIVS', 15, 'aliis', '', '', '28', 4), ('ALIAS', 16, 'alias', '', '', '1', 1), ('AMNIS', 17, 'amnis', '', '', '27', 1), ('AMOENITAS', 18, 'amoenitates', '', '', '27', 1), ('ANIMA', 19, 'anima', '', '', '22', 1), ('ANIMVS', 20, 'animo', '', '', '15', 1), ('ARDVVS', 21, 'arduum', '', '', '6', 2), ('ARDVVS', 22, 'ardua', '', '', '30', 2), ('ARS', 23, 'artes', '', '', '10', 1), ('AC/1', 24, 'ac', '', '', '10', 1), ('AVCTOR', 25, 'auctorem', '', '', '40', 1), ('AVDEO', 26, 'ausi sunt', '', '', '16', 1), ('AVT', 27, 'aut', '', '', '26', 3), ('AVT', 28, 'aut', '', '', '26', 3), ('AVT', 29, 'aut', '', '', '27', 3), ('BENEFICIVM', 30, 'beneficio', '', '', '25', 1), ('BONVS', 31, 'bonas', '', '', '10', 1), ('CAELESTIS', 32, 'caelesti', '', '', '42', 1), ('CAELVM/1', 33, 'caeli', '', '', '16', 1), ('CAPIO/2', 34, 'capiuntur', '', '', '32', 1), ('CE', 35, '-ce', '', '', '30', 1), ('CETERVS', 36, 'ceteri ceteri', '', '', '5', 3), ('CETERVS', 37, 'ceteris', '', '', '24', 3), ('CETERVS', 38, 'ceterum', '', '', '35', 3), ('COGITATIO', 39, 'cogitatione', '', '', '41', 3), ('COGITATIO', 40, 'cogitationum', '', '', '20', 3), ('COGITATIO', 41, 'cogitationibus', '', '', '17', 3), ('COMPLECTOR', 42, 'complexi', '', '', '42', 1), ('COMPLEO', 43, 'conpleti', '', '', '24', 1), ('COMPREHENDO', 44, 'esset . . . conprehensa', '', '', '38', 1), ('CONDICIO', 45, 'condicione', '', '', '18', 1), ('CONGRVO', 46, 'congruere', '', '', '11', 1), ('CONSIDERO', 47, 'consideranti', '', '', '1', 1), ('CONTEMPLOR', 48, 'contemplandum esset', '', '', '35', 2), ('CONTEMPLOR', 49, 'contemplari', '', '', '36', 2), ('CONTINGO/1', 50, 'contingere', '', '', '41', 1), ('CORPVS', 51, 'corpore', '', '', '13', 1), ('CORYCVS/N', 52, 'Coryci', '', '', '29', 1), ('CREDO', 53, 'credidit', '', '', '11', 2), ('CREDO', 54, 'credidissent', '', '', '38', 2), ('CVM/2', 55, 'cum', '', '', '10', 6), ('CVM/2', 56, 'cum & quom cum', '', '', '31', 6), ('CVM/2', 57, 'quom cum cum', '', '', '4', 6), ('CVM/2', 58, 'quom cum cum', '', '', '12', 6), ('CVM/2', 59, 'quom cum cum', '', '', '18', 6), ('CVM/2', 60, 'quom cum cum', '', '', '33', 6), ('CONDVCO', 61, 'cumducere', '', '', '9', 1), ('CVR/1', 62, 'cur', '', '', '42', 1), ('CVRA', 63, 'curam', '', '', '12', 1), ('CVRRICVLVM', 64, 'curriculo', '', '', '20', 1), ('DE', 65, 'de', '', '', '21', 2), ('DE', 66, 'de', '', '', '41', 2), ('DEFERO', 67, 'deferatur', '', '', '9', 1), ('DESCRIBO', 68, 'describunt', '', '', '26', 2), ('DESCRIBO', 69, 'descripta', '', '', '28', 2), ('DESPICIO', 70, 'despexit', '', '', '7', 1), ('DEVS', 71, 'deorum', '', '', '24', 1), ('DICO/2', 72, 'dicemus', '', '', '41', 2), ('DICO/2', 73, 'dicere', '', '', '10', 2), ('DIGNVS', 74, 'dignas', '', '', '37', 1), ('DILIGENTIA', 75, 'diligentia', '', '', '35', 1), ('DILIGO/3', 76, 'diligentius', '', '', '1', 1), ('DISCEPTATIO', 77, 'disceptatio', '', '', '9', 1), ('DIVINVS/2', 78, 'diuino', '', '', '24', 4), ('DIVINVS/2', 79, 'diuinarum', '', '', '3', 4), ('DIVINVS/2', 80, 'diuinarum', '', '', '8', 4), ('DIVINVS/2', 81, 'diuinis', '', '', '22', 4), ('DOCEO', 82, 'doctissimum', '', '', '39', 1), ('DOMICILIVM', 83, 'domicilio', '', '', '14', 1), ('DVMTAXAT', 84, 'dumtaxat', '', '', '30', 1), ('DVX', 85, 'ducem', '', '', '15', 1), ('EFFOR', 86, 'effantur', '', '', '24', 1), ('EGO', 87, 'mihi', '', '', '1', 1), ('EIVSMODI', 88, 'eiusmodi', '', '', '6', 2), ('EIVSMODI', 89, 'eiusmodi', '', '', '10', 2), ('ET/2', 90, 'et', '', '', '1', 21), ('ET/2', 91, 'et', '', '', '3', 21), ('ET/2', 92, 'et', '', '', '4', 21), ('ET/2', 93, 'et', '', '', '6', 21), ('ET/2', 94, 'et', '', '', '8', 21), ('ET/2', 95, 'et', '', '', '10', 21), ('ET/2', 96, 'et', '', '', '11', 21), ('ET/2', 97, 'et', '', '', '12', 21), ('ET/2', 98, 'et', '', '', '25', 21), ('ET/2', 99, 'et', '', '', '27', 21), ('ET/2', 100, 'et', '', '', '29', 21), ('ET/2', 101, 'et', '', '', '29', 21), ('ET/2', 102, 'et', '', '', '30', 21), ('ET/2', 103, 'et', '', '', '30', 21), ('ET/2', 104, 'et', '', '', '32', 21), ('ET/2', 105, 'et', '', '', '37', 21), ('ET/2', 106, 'et', '', '', '39', 21), ('ET/2', 107, 'et', '', '', '40', 21), ('ET/2', 108, 'et', '', '', '42', 21), ('ET/2', 109, 'et', '', '', '42', 21), ('ET/2', 110, 'et', '', '', '42', 21), ('ETIAM', 111, 'etiam', '', '', '23', 1), ('EVENIO', 112, 'euenire', '', '', '33', 1), ('EXIGVVS', 113, 'exiguas', '', '', '37', 1), ('EXISTIMO', 114, 'existimauit', '', '', '8', 2), ('EXISTIMO', 115, 'existimarent', '', '', '7', 2), ('EXPLICO', 116, 'explicabimus', '', '', '43', 1), ('EXPLORATIO', 117, 'exploratione', '', '', '17', 1), ('EXPVLTRIX', 118, 'expultrix', '', '', '2', 1), ('EXTOLLO', 119, 'extollunt', '', '', '31', 1), ('FACILIS', 120, 'facillime', '', '', '21', 1), ('FAVSTINVS/N', 121, 'Faustine', '', '', '2', 1), ('FILIVS', 122, 'fili', '', '', '2', 1), ('FLVENTVM', 123, 'fluenta', '', '', '27', 1), ('HIC/1', 124, 'hac', '', '', '41', 3), ('HIC/1', 125, 'his', '', '', '16', 3), ('HIC/1', 126, 'hoc', '', '', '33', 3), ('HOMO', 127, 'homines', '', '', '13', 1), ('HVIVSMODI', 128, 'modi huiuscemodi', '', '', '30', 1), ('HVMANVS', 129, 'humanarum', '', '', '9', 1), ('ILLE', 130, 'illis', '', '', '33', 2), ('ILLE', 131, 'illas', '', '', '14', 2), ('IMBVO', 132, 'inbuti', '', '', '15', 1), ('INDAGATRIX', 133, 'indagatrix', '', '', '2', 1), ('INDIGNVS', 134, 'indignam', '', '', '8', 1), ('INEXPLEBILIS', 135, 'inexplebili', '', '', '32', 1), ('INGENIVM', 136, 'ingenium', '', '', '8', 2), ('INGENIVM', 137, 'ingenia', '', '', '25', 2), ('INGENVITAS', 138, 'ingenuitate', '', '', '10', 1), ('IMMENSITAS', 139, 'inmensitati', '', '', '19', 1), ('INSPICIO', 140, 'inspicerent', '', '', '14', 1), ('INTENDO', 141, 'intenderint', '', '', '34', 1), ('INTERPRETATIO', 142, 'interpretationem', '', '', '4', 1), ('INTERVALLVM', 143, 'interualli', '', '', '18', 1), ('INTIMO', 144, 'intimaret', '', '', '21', 1), ('INTVEOR', 145, 'intuenti', '', '', '1', 1), ('INVENIO', 146, 'inuentis', '', '', '15', 1), ('INVESTIGATIO', 147, 'inuestigationem', '', '', '5', 1), ('IPSE', 148, 'ipsius', '', '', '18', 1), ('IS', 149, 'eius', '', '', '13', 8), ('IS', 150, 'eius', '', '', '20', 8), ('IS', 151, 'eius', '', '', '37', 8), ('IS', 152, 'eius', '', '', '15', 8), ('IS', 153, 'eius', '', '', '22', 8), ('IS', 154, 'eius', '', '', '23', 8), ('IS', 155, 'eos', '', '', '25', 8), ('IS', 156, 'ea', '', '', '21', 8), ('ISTIVSMODI', 157, 'istiusmodi', '', '', '11', 1), ('ITER', 158, 'itineribus', '', '', '16', 1), ('IVGVM', 159, 'iuga', '', '', '29', 1), ('LABOR/2', 160, 'laborem', '', '', '6', 1), ('LAVS', 161, 'laudibus', '', '', '37', 1), ('LEGO/2', 162, 'legunt', '', '', '29', 1), ('LOCVS', 163, 'loci', '', '', '25', 1), ('MAGNITVDO', 164, 'magnitudine', '', '', '6', 2), ('MAGNITVDO', 165, 'magnitudines', '', '', '27', 2), ('MAGNVS', 166, 'magnis', '', '', '32', 1), ('MAIOR', 167, 'maius', '', '', '33', 2), ('MAIOR', 168, 'maiore', '', '', '34', 2), ('MAXIME', 169, 'maxime', '', '', '4', 1), ('MAIESTAS', 170, 'maiestate', '', '', '24', 1), ('MIRABILIS', 171, 'mirabile', '', '', '33', 1), ('MISEREO', 172, 'miseret', '', '', '31', 1), ('MOENIA', 173, 'moenia', '', '', '26', 1), ('MONS', 174, 'montium', '', '', '28', 1), ('MOS', 175, 'moribus', '', '', '12', 1), ('MOVEO', 176, 'moueantur', '', '', '43', 1), ('MVLTVS', 177, 'multa', '', '', '28', 1), ('MVNDVS/2', 178, 'mundi', '', '', '19', 3), ('MVNDVS/2', 179, 'mundum', '', '', '12', 3), ('MVNDVS/2', 180, 'mundum', '', '', '36', 3), ('NAM', 181, 'nam', '', '', '5', 2), ('NAM', 182, 'nam', '', '', '12', 2), ('NANCISCOR', 183, 'nancti', '', '', '15', 1), ('NATVRA', 184, 'natura', '', '', '19', 3), ('NATVRA', 185, 'naturae', '', '', '4', 3), ('NATVRA', 186, 'naturas', '', '', '42', 3), ('NEQVE', 187, 'nec', '', '', '8', 3), ('NEQVE', 188, 'nec', '', '', '31', 3), ('NEQVE', 189, 'neque', '', '', '34', 3), ('NIHIL', 190, 'nihil', '', '', '33', 1), ('NON', 191, 'non', '', '', '7', 3), ('NON', 192, 'non', '', '', '13', 3), ('NON', 193, 'non', '', '', '33', 3), ('NOSTER', 194, 'nostrarum', '', '', '20', 1), ('NVNC', 195, 'nunc', '', '', '3', 1), ('NYSA/N', 196, 'Nysae', '', '', '29', 1), ('OCVLVS', 197, 'oculis', '', '', '5', 2), ('OCVLVS', 198, 'oculis', '', '', '22', 2), ('OFFICIVM', 199, 'officia', '', '', '42', 1), ('OLYMPVS/N', 200, 'Olympi', '', '', '29', 1), ('OMNIS', 201, 'omnem', '', '', '36', 2), ('OMNIS', 202, 'omni', '', '', '41', 2), ('OPERA', 203, 'operam', '', '', '10', 1), ('OPPIDO', 204, 'oppido', '', '', '32', 1), ('OPVS/1', 205, 'opere', '', '', '31', 1), ('ORBIS', 206, 'orbem', '', '', '35', 1), ('ORIGO', 207, 'origo', '', '', '22', 1), ('OSSA/N', 208, 'Ossae', '', '', '30', 1), ('PAR/2', 209, 'pariter', '', '', '36', 1), ('PARS', 210, 'partes', '', '', '37', 1), ('PARTICEPS/2', 211, 'particeps', '', '', '3', 1), ('PARVVS/2', 212, 'minus', '', '', '37', 1), ('PAVCI', 213, 'paucis', '', '', '32', 1), ('PENETRALIS', 214, 'penetralia', '', '', '13', 2), ('PENETRALIS', 215, 'penetralia', '', '', '29', 2), ('PER', 216, 'per', '', '', '16', 1), ('PEREGRINOR', 217, 'peregrinari', '', '', '15', 1), ('PERNICITAS', 218, 'pernicitas', '', '', '21', 1), ('PERVIVS', 219, 'peruia', '', '', '17', 1), ('PHILOSOPHIA', 220, 'philosophia', '', '', '3', 2), ('PHILOSOPHIA', 221, 'philosophiam', '', '', '14', 2), ('PHILOSOPHVS/2', 222, 'philosophorum', '', '', '40', 1), ('PLAGA/1', 223, 'plagas', '', '', '16', 1), ('PLERVSQVE', 224, 'plerique', '', '', '28', 1), ('POSSVM/1', 225, 'possumus', '', '', '41', 3), ('POSSVM/1', 226, 'possent', '', '', '13', 3), ('POSSVM/1', 227, 'potuisset', '', '', '36', 3), ('PROFESSIO', 228, 'professionis', '', '', '11', 1), ('PROFVNDVS', 229, 'profundum', '', '', '6', 1), ('PROPHETA', 230, 'prophetae', '', '', '23', 1), ('PRVDENS', 231, 'prudentissimus prudentissimum', '', '', '39', 1), ('QVALITAS', 232, 'qualitates', '', '', '26', 1), ('QVANTVM/3', 233, 'quantum', '', '', '40', 1), ('QVARE/1', 234, 'quare', '', '', '25', 2), ('QVARE/1', 235, 'quare', '', '', '39', 2), ('QVE', 236, 'que', '', '', '13', 7), ('QVE', 237, 'que', '', '', '15', 7), ('QVE', 238, 'que', '', '', '20', 7), ('QVE', 239, 'que', '', '', '21', 7), ('QVE', 240, 'que', '', '', '26', 7), ('QVE', 241, 'que', '', '', '36', 7), ('QVE', 242, 'que', '', '', '42', 7), ('QVEMADMODVM/2', 243, 'quemadmodum', '', '', '43', 1), ('QVI/1', 244, 'quod', '', '', '34', 8), ('QVI/1', 245, 'cui', '', '', '8', 8), ('QVI/1', 246, 'qui', '', '', '25', 8), ('QVI/1', 247, 'quorum', '', '', '31', 8), ('QVI/1', 248, 'quae', '', '', '16', 8), ('QVI/1', 249, 'quae', '', '', '24', 8), ('QVI/1', 250, 'quibus', '', '', '38', 8), ('QVI/1', 251, 'quibus', '', '', '21', 8), ('QVIDAM', 252, 'quidam', '', '', '23', 1), ('RATIO', 253, 'ratione', '', '', '42', 1), ('REGIO', 254, 'regiones', '', '', '14', 1), ('RELINQVO', 255, 'relicto', '', '', '14', 1), ('REMOVEO', 256, 'remotarum', '', '', '4', 1), ('RES', 257, 'rei', '', '', '6', 2), ('RES', 258, 'rerum', '', '', '3', 2), ('SACER', 259, 'sacra', '', '', '29', 1), ('SAEPE', 260, 'saepe', '', '', '1', 1), ('SAPIENTIA', 261, 'sapientiae', '', '', '17', 1), ('SCIENTIA', 262, 'scientiam', '', '', '23', 1), ('SECERNO', 263, 'secretos', '', '', '19', 1), ('SED', 264, 'sed', '', '', '9', 1), ('SEQVOR', 265, 'secuti', '', '', '40', 1), ('SI/2', 266, 'si', '', '', '35', 1), ('SINGVLVS', 267, 'singulas', '', '', '37', 2), ('SINGVLVS', 268, 'singula', '', '', '30', 2), ('SOLVS', 269, 'sola', '', '', '7', 4), ('SOLVS', 270, 'soli', '', '', '25', 4), ('SOLVS', 271, 'sola', '', '', '30', 4), ('SOLVS', 272, 'solis', '', '', '17', 4), ('STVDIOSVS', 273, 'studiose', '', '', '28', 1), ('STVDIVM', 274, 'studiis', '', '', '12', 1), ('SVI/1', 275, 'sibi', '', '', '5', 2), ('SVI/1', 276, 'se', '', '', '8', 2), ('SVSPICIO/2', 277, 'suspexerint', '', '', '34', 1), ('SVVS', 278, 'suae', '', '', '11', 4), ('SVVS', 279, 'sui', '', '', '17', 4), ('SVVS', 280, 'suum', '', '', '7', 4), ('SVVS', 281, 'suis', '', '', '22', 4), ('TALIS', 282, 'talibus', '', '', '12', 1), ('TAM', 283, 'tam', '', '', '10', 1), ('TAMEN', 284, 'tamen', '', '', '20', 1), ('TANTVS', 285, 'tanto', '', '', '31', 1), ('TERRA', 286, 'terrarum', '', '', '35', 1), ('TERRENVS', 287, 'terreno', '', '', '14', 1), ('TERREO', 288, 'territi', '', '', '6', 1), ('THEOPHRASTVS/N', 289, 'Theophrastum', '', '', '40', 1), ('TRADO', 290, 'tradidit', '', '', '23', 1), ('VELVT/1', 291, 'ueluti', '', '', '23', 1), ('VICINIA', 292, 'uicinia', '', '', '19', 1), ('VIDEO', 293, 'uident', '', '', '25', 3), ('VIDEO', 294, 'uidebatur', '', '', '3', 3), ('VIDEO', 295, 'uiderant', '', '', '18', 3), ('VINDICO', 296, 'uindicet', '', '', '5', 1), ('VIRTVS', 297, 'uirtutis', '', '', '2', 1), ('VITIVM', 298, 'uitiorum', '', '', '2', 1), ('VNIVERSITAS', 299, 'uniuersitas', '', '', '38', 1), ('VOLO/3', 300, 'uoluisset', '', '', '19', 1), ('VOLVCER', 301, 'uolucri', '', '', '20', 1), ('VRBS', 302, 'urbis', '', '', '26', 1)]
section_list ={'1': '23', '18': 'start', '4': '18', '28': '4', '17': '28', '33': '17', '13': '33', '22': '13', '32': '22', '36': '32', '26': '36', '34': '26', '30': '34', '23': '30', '27': '1', '15': '27', '6': '15', '10': '6', '40': '10', '16': '40', '25': '16', '42': '25', '5': '42', '24': '5', '35': '24', '41': '35', '20': '41', '38': '20', '11': '38', '29': '11', '31': '29', '12': '31', '9': '12', '21': '9', '7': '21', '37': '7', '3': '37', '8': '3', '39': '8', '14': '39', '43': '14', '2': '43', '19': '2', 'end': '19', 'start': 'start'}
title = "Apuleius, De Mundo (Prologus)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)