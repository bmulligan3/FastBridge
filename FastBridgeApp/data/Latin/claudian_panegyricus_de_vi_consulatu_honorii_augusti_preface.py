import text
nan=""
section_words = {'start': -1, '1': 5, '2': 10, '3': 16, '4': 24, '5': 29, '6': 35, '7': 41, '8': 47, '9': 53, '10': 58, '11': 65, '12': 69, '13': 76, '14': 82, '15': 89, '16': 94, '17': 101, '18': 107, '19': 114, '20': 118, '21': 126, '22': 132, '23': 138, '24': 144, '25': 152, '26': 157, 'end': -2}
the_text =  [('DIVRNVS', 0, 'DIURNUS', '', '', '1', 1), ('OMNIS', 1, 'OMNIS', '', '', '1', 1), ('QVI/1', 2, 'QUI', '', '', '1', 1), ('SENSVS', 3, 'SENSUS', '', '', '1', 1), ('VOLVO', 4, 'UOLUERE', '', '', '1', 1), ('VOVEO', 5, 'UOUERE', '', '', '1', 1), ('AMICVS/2', 6, 'AMICUS', '', '', '2', 1), ('PECTVS', 7, 'PECTUS', '', '', '2', 1), ('QVIES', 8, 'QUIES', '', '', '2', 1), ('REDDO', 9, 'REDDERE', '', '', '2', 1), ('SOPIO', 10, 'SOPIRE', '', '', '2', 1), ('CVM/3', 11, 'CUM', '', '', '3', 1), ('DEFETISCOR', 12, 'DEFESSUS', '', '', '3', 1), ('MEMBRVM', 13, 'MEMBRUM', '', '', '3', 1), ('REPONO', 14, 'REPONERE', '', '', '3', 1), ('TORVS', 15, 'TORUS', '', '', '3', 1), ('VENATOR', 16, 'UENATOR', '', '', '3', 1), ('AD/2', 17, 'AD', '', '', '4', 1), ('ET/2', 18, 'ET', '', '', '4', 3), ('LVSTRVM/1', 19, 'LUSTRUM', '', '', '4', 1), ('MENS', 20, 'MENS', '', '', '4', 1), ('REDEO/1', 21, 'REDIRE', '', '', '4', 1), ('SILVA', 22, 'SILUA', '', '', '4', 1), ('SVVS', 23, 'SUUS', '', '', '4', 1), ('TAMEN', 24, 'TAMEN', '', '', '4', 1), ('AVRIGA', 25, 'AURIGA', '', '', '5', 1), ('CVRRVS', 26, 'CURRUS', '', '', '5', 1), ('IVDEX', 27, 'IUDEX', '', '', '5', 1), ('LIS', 28, 'LIS', '', '', '5', 1), ('SOMNIVM', 29, 'SOMNIUM', '', '', '5', 2), ('CAVEO', 30, 'CAUERE', '', '', '6', 1), ('EQVVS', 31, 'EQUUS', '', '', '6', 1), ('META', 32, 'META', '', '', '6', 1), ('NOCTVRNVS', 33, 'NOCTURNUS', '', '', '6', 1), ('QVE', 34, 'QUE', '', '', '6', 5), ('VANVS', 35, 'UANUS', '', '', '6', 1), ('AMO', 36, 'AMARE', '', '', '7', 1), ('FVRTVM', 37, 'FURTUM', '', '', '7', 1), ('GAVDEO', 38, 'GAUDERE', '', '', '7', 1), ('MERCES', 39, 'MERCES', '', '', '7', 1), ('NAVTA', 40, 'NAUITA', '', '', '7', 1), ('PERMVTO/2', 41, 'PERMUTARE', '', '', '7', 1), ('AVARVS/2', 42, 'AUARUS', '', '', '8', 1), ('ELABOR/2', 43, 'ELABI', '', '', '8', 1), ('ET/2', 44, 'ET', '', '', '8', 3), ('OPS', 45, 'OPS', '', '', '8', 1), ('QVAERO', 46, 'QUAERERE', '', '', '8', 1), ('VIGIL/2', 47, 'UIGIL', '', '', '8', 1), ('AEGER/2', 48, 'AEGER', '', '', '9', 1), ('BLANDVS', 49, 'BLANDUS', '', '', '9', 1), ('FRVSTRA', 50, 'FRUSTRA', '', '', '9', 1), ('LARGIOR', 51, 'LARGIRI', '', '', '9', 1), ('QVE', 52, 'QUE', '', '', '9', 5), ('SITIO', 53, 'SITIRE', '', '', '9', 1), ('FONS', 54, 'FONS', '', '', '10', 1), ('GELIDVS', 55, 'GELIDUS', '', '', '10', 1), ('IRRIGVVS', 56, 'INRIGUUS', '', '', '10', 1), ('POCVLVM', 57, 'POCULUM', '', '', '10', 1), ('SOPOR', 58, 'SOPOR', '', '', '10', 2), ('EGO', 59, 'EGO', '', '', '11', 3), ('MVSA/N', 60, 'MUSA', '', '', '11', 1), ('NOX', 61, 'NOX', '', '', '11', 1), ('QVOQVE', 62, 'QUOQUE', '', '', '11', 1), ('SILEO', 63, 'SILERE', '', '', '11', 1), ('STVDIVM', 64, 'STUDIUM', '', '', '11', 1), ('SVB', 65, 'SUB', '', '', '11', 1), ('ARS', 66, 'ARS', '', '', '12', 1), ('ASSVESCO', 67, 'ASSUESCERE', '', '', '12', 1), ('SOLEO', 68, 'SOLERE', '', '', '12', 1), ('SOLLICITO', 69, 'SOLLICITARE', '', '', '12', 1), ('ARX', 70, 'ARX', '', '', '13', 1), ('IN', 71, 'IN', '', '', '13', 1), ('MEDIVS', 72, 'MEDIUS', '', '', '13', 1), ('NAM', 73, 'NAMQUE', '', '', '13', 1), ('POLVS', 74, 'POLUS', '', '', '13', 1), ('STELLO', 75, 'STELLANS', '', '', '13', 1), ('VIDEO', 76, 'UIDERE', '', '', '13', 1), ('ANTE/2', 77, 'ANTE', '', '', '14', 1), ('CARMEN/1', 78, 'CARMEN', '', '', '14', 2), ('FERO', 79, 'FERRE', '', '', '14', 1), ('IVPPITER/N', 80, 'IUPPITER', '', '', '14', 2), ('PES', 81, 'PES', '', '', '14', 1), ('SVPERVS', 82, 'SUPERUS', '', '', '14', 1), ('DICO/2', 83, 'DICERE', '', '', '15', 1), ('FAVEO', 84, 'FAUERE', '', '', '15', 1), ('NVMEN', 85, 'NUMEN', '', '', '15', 1), ('PLAVDO', 86, 'PLAUDERE', '', '', '15', 1), ('QVE', 87, 'QUE', '', '', '15', 5), ('SOMNVS', 88, 'SOMNUS', '', '', '15', 1), ('VT/4', 89, 'UT', '', '', '15', 1), ('CHORVS', 90, 'CHORUS', '', '', '16', 1), ('CIRCVMFVNDO/2', 91, 'CIRCUMFUNDERE', '', '', '16', 1), ('CORONA', 92, 'CORONA', '', '', '16', 1), ('ET/2', 93, 'ET', '', '', '16', 3), ('SACER', 94, 'SACER', '', '', '16', 1), ('CARMEN/1', 95, 'CARMEN', '', '', '17', 2), ('EGO', 96, 'EGO', '', '', '17', 3), ('ENCELADVS/N', 97, 'ENCELADUS', '', '', '17', 1), ('SVM/1', 98, 'ESSE', '', '', '17', 1), ('QVE', 99, 'QUE', '', '', '17', 5), ('TYPHOEVS/N', 100, 'TYPHOEUS', '', '', '17', 1), ('VINCO', 101, 'UINCERE', '', '', '17', 1), ('AETNA/N', 102, 'AETNA', '', '', '18', 1), ('DOMO', 103, 'DOMARE', '', '', '18', 1), ('GRAVIS', 104, 'GRAUIS', '', '', '18', 1), ('HIC/1', 105, 'HIC', '', '', '18', 1), ('INARIME/N', 106, 'INARIME', '', '', '18', 1), ('SVBEO/1', 107, 'SUBIRE', '', '', '18', 1), ('AETHER', 108, 'AETHER', '', '', '19', 1), ('BELLVM', 109, 'BELLUM', '', '', '19', 1), ('IVPPITER/N', 110, 'IUPPITER', '', '', '19', 2), ('LAETVS/2', 111, 'LAETUS', '', '', '19', 1), ('POST/2', 112, 'POST', '', '', '19', 1), ('QVAM/1', 113, 'QUAM', '', '', '19', 1), ('SVSCIPIO', 114, 'SUSCIPERE', '', '', '19', 1), ('MILITIA', 115, 'MILITIA', '', '', '20', 1), ('PHLEGRAEVS/A', 116, 'PHLEGRAEUS', '', '', '20', 1), ('PRAEMIVM', 117, 'PRAEMIUM', '', '', '20', 1), ('REFERO', 118, 'REFERRE', '', '', '20', 1), ('ADDO', 119, 'ADDERE', '', '', '21', 1), ('ECCE', 120, 'ECCE', '', '', '21', 1), ('EGO', 121, 'EGO', '', '', '21', 3), ('FIDES/2', 122, 'FIDES', '', '', '21', 1), ('IMAGO', 123, 'IMAGO', '', '', '21', 1), ('LVDO', 124, 'LUDERE', '', '', '21', 1), ('MEVS', 125, 'MEUS', '', '', '21', 1), ('NEQVE', 126, 'NEQUE', '', '', '21', 2), ('EBVR', 127, 'EBUR', '', '', '22', 1), ('FALLO', 128, 'FALLERE', '', '', '22', 1), ('IRRITVS', 129, 'INRITUS', '', '', '22', 1), ('MITTO', 130, 'MITTERE', '', '', '22', 1), ('NEQVE', 131, 'NEQUE', '', '', '22', 2), ('SOMNIVM', 132, 'SOMNIUM', '', '', '22', 2), ('AEQVO', 133, 'AEQUARE', '', '', '23', 1), ('APEX', 134, 'APEX', '', '', '23', 1), ('EN', 135, 'EN', '', '', '23', 2), ('OLYMPVS/N', 136, 'OLYMPUS', '', '', '23', 1), ('ORBIS', 137, 'ORBIS', '', '', '23', 1), ('PRINCEPS/1', 138, 'PRINCEPS', '', '', '23', 1), ('DEVS', 139, 'DEUS', '', '', '24', 1), ('EN', 140, 'EN', '', '', '24', 2), ('MEMINI', 141, 'MEMINISSE', '', '', '24', 1), ('QVALIS/1', 142, 'QUALIS', '', '', '24', 1), ('TVRBA', 143, 'TURBA', '', '', '24', 1), ('VEREOR', 144, 'UERERI', '', '', '24', 1), ('ALO', 145, 'ALERE', '', '', '25', 1), ('FINGO', 146, 'FINGERE', '', '', '25', 1), ('MAGNVS', 147, 'MAGNUS', '', '', '25', 1), ('NIHIL', 148, 'NIHIL', '', '', '25', 1), ('POSSVM/1', 149, 'POSSE', '', '', '25', 1), ('QVE', 150, 'QUE', '', '', '25', 5), ('SOPOR', 151, 'SOPOR', '', '', '25', 2), ('VATES', 152, 'UATES', '', '', '25', 1), ('AVLA/1', 153, 'AULA', '', '', '26', 1), ('CAELVM/1', 154, 'CAELUM', '', '', '26', 1), ('CONVENTVS', 155, 'CONUENTUS', '', '', '26', 1), ('PAR/2', 156, 'PAR', '', '', '26', 1), ('PRAEBEO', 157, 'PRAEBERE', '', '', '26', 1)]
section_list ={'1': 'start', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': '10', '12': '11', '13': '12', '14': '13', '15': '14', '16': '15', '17': '16', '18': '17', '19': '18', '20': '19', '21': '20', '22': '21', '23': '22', '24': '23', '25': '24', '26': '25', 'end': '26', 'start': 'start'}
title = "Claudian, Panegyricus de VI Consulatu Honorii Augusti (Preface)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)