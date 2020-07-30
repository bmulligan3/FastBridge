import text
nan=""
section_words = {'start': -1, '1': 6, '2': 22, '3': 64, '4': 76, '5': 87, '6': 103, '7': 134, '8': 153, '9': 166, '10': 180, '11': 209, '12': 234, '13': 249, '14': 259, '15': 266, 'end': -2}
the_text =  [('RENA/N', 0, 'Rena', '', '', '1', 14), ('SVM/1', 1, 'est', '', '', '1', 31), ('ANIMAL', 2, 'animal', '', '', '1', 1), ('INFANS/1', 3, 'infans', '', '', '1', 3), ('RENA/N', 4, 'Rena', '', '', '1', 14), ('SVM/1', 5, 'est', '', '', '1', 31), ('RHINOCEROS', 6, 'rhinoceros', '', '', '1', 10), ('MATER', 7, 'Mater', '', '', '2', 8), ('RHINOCEROS', 8, 'Rhinoceros', '', '', '2', 10), ('SVM/1', 9, 'est', '', '', '2', 31), ('INGENS', 10, 'ingens', '', '', '2', 1), ('MATER', 11, 'Mater', '', '', '2', 8), ('RHINOCEROS', 12, 'Rhinoceros', '', '', '2', 10), ('SVM/1', 13, 'est', '', '', '2', 31), ('CANVS', 14, 'cana', '', '', '2', 6), ('COLOR', 15, 'colore', '', '', '2', 6), ('MATER', 16, 'Mater', '', '', '2', 8), ('RHINOCEROS', 17, 'Rhinoceros', '', '', '2', 10), ('CORNV', 18, 'cornu', '', '', '2', 11), ('MAGNVS', 19, 'magnum', '', '', '2', 3), ('IN', 20, 'in', '', '', '2', 14), ('NASVS', 21, 'naso', '', '', '2', 13), ('HABEO', 22, 'habet', '', '', '2', 14), ('MATER', 23, 'Mater', '', '', '3', 8), ('DICO/2', 24, 'dicit', '', '', '3', 7), ('RENA/N', 25, 'Rena', '', '', '3', 14), ('TV', 26, 'tu', '', '', '3', 9), ('SVM/1', 27, 'est', '', '', '3', 31), ('CANVS', 28, 'cana', '', '', '3', 6), ('COLOR', 29, 'colore', '', '', '3', 6), ('EGO', 30, 'ego', '', '', '3', 4), ('SVM/1', 31, 'sum', '', '', '3', 31), ('CANVS', 32, 'cana', '', '', '3', 6), ('COLOR', 33, 'colore', '', '', '3', 6), ('PELLIS', 34, 'Pellis', '', '', '3', 5), ('TVVS', 35, 'tua', '', '', '3', 3), ('SVM/1', 36, 'est', '', '', '3', 31), ('CRASSVS', 37, 'crassa', '', '', '3', 5), ('PELLIS', 38, 'pellis', '', '', '3', 5), ('MEVS', 39, 'mea', '', '', '3', 3), ('SVM/1', 40, 'est', '', '', '3', 31), ('CRASSVS', 41, 'crassa', '', '', '3', 5), ('SED', 42, 'Sed', '', '', '3', 5), ('TV', 43, 'tu', '', '', '3', 9), ('CORNV', 44, 'cornu', '', '', '3', 11), ('IN', 45, 'in', '', '', '3', 14), ('NASVS', 46, 'naso', '', '', '3', 13), ('HABEO', 47, 'habes', '', '', '3', 14), ('QVIS/1', 48, 'Quid', '', '', '3', 3), ('SVM/1', 49, 'sum', '', '', '3', 31), ('TV', 50, 'Tu', '', '', '3', 9), ('SVM/1', 51, 'est', '', '', '3', 31), ('RHINOCEROS', 52, 'rhinoceros', '', '', '3', 10), ('CARVS', 53, 'cara', '', '', '3', 2), ('DICO/2', 54, 'dicit', '', '', '3', 7), ('MATER', 55, 'mater', '', '', '3', 8), ('SI/2', 56, 'Si', '', '', '3', 1), ('RHINOCEROS', 57, 'rhinoceros', '', '', '3', 10), ('SVM/1', 58, 'sum', '', '', '3', 31), ('CVR/1', 59, 'cur', '', '', '3', 1), ('CORNV', 60, 'cornu', '', '', '3', 11), ('IN', 61, 'in', '', '', '3', 14), ('NASVS', 62, 'naos', '', '', '3', 13), ('NON', 63, 'non', '', '', '3', 9), ('HABEO', 64, 'habeo', '', '', '3', 14), ('TV', 65, 'Tu', '', '', '4', 9), ('SVM/1', 66, 'es', '', '', '4', 31), ('INFANS/1', 67, 'infans', '', '', '4', 3), ('CARVS', 68, 'cara', '', '', '4', 2), ('FORTASSE', 69, 'Fortasse', '', '', '4', 3), ('CORNV', 70, 'cornu', '', '', '4', 11), ('NON', 71, 'non', '', '', '4', 9), ('HABEO', 72, 'habes', '', '', '4', 14), ('QVI/1', 73, 'quod', '', '', '4', 2), ('TV', 74, 'tu', '', '', '4', 9), ('SVM/1', 75, 'es', '', '', '4', 31), ('PARVVS/2', 76, 'parua', '', '', '4', 3), ('INFANS/1', 77, 'Infans', '', '', '5', 3), ('SVM/1', 78, 'sum', '', '', '5', 31), ('SED', 79, 'sed', '', '', '5', 5), ('CORNV', 80, 'cornu', '', '', '5', 11), ('DESIDERO', 81, 'desidero', '', '', '5', 2), ('RHINOCEROS', 82, 'Rhinoceros', '', '', '5', 10), ('CORNV', 83, 'cornu', '', '', '5', 11), ('IN', 84, 'in', '', '', '5', 14), ('NASVS', 85, 'naso', '', '', '5', 13), ('HABEO', 86, 'habere', '', '', '5', 14), ('DEBEO', 87, 'debet', '', '', '5', 1), ('RENA/N', 88, 'Rena', '', '', '6', 14), ('RHINOCEROS', 89, 'Rhinoceros', '', '', '6', 10), ('IN', 90, 'in', '', '', '6', 14), ('GRAMEN', 91, 'gramine', '', '', '6', 1), ('AMBVLO', 92, 'ambulat', '', '', '6', 2), ('RHINOCEROS', 93, 'Rhinoceros', '', '', '6', 10), ('NON', 94, 'non', '', '', '6', 9), ('SVM/1', 95, 'sum', '', '', '6', 31), ('CORNV', 96, 'cornu', '', '', '6', 11), ('IN', 97, 'in', '', '', '6', 14), ('NASVS', 98, 'naso', '', '', '6', 13), ('NON', 99, 'non', '', '', '6', 9), ('HABEO', 100, 'habeo', '', '', '6', 14), ('FORTASSE', 101, 'Fortasse', '', '', '6', 3), ('ELEPHANTVS', 102, 'elephantus', '', '', '6', 8), ('SVM/1', 103, 'sum', '', '', '6', 31), ('RENA/N', 104, 'Rena', '', '', '7', 14), ('PARVVS/2', 105, 'paruum', '', '', '7', 3), ('ELEPHANTVS', 106, 'elephantum', '', '', '7', 8), ('SPECTO', 107, 'spectat', '', '', '7', 6), ('ELEPHANTVS', 108, 'Elephantus', '', '', '7', 8), ('SVM/1', 109, 'est', '', '', '7', 31), ('CANVS', 110, 'canus', '', '', '7', 6), ('COLOR', 111, 'colore', '', '', '7', 6), ('ELEPHANTVS', 112, 'Elephantus', '', '', '7', 8), ('PELLIS', 113, 'pellem', '', '', '7', 5), ('CRASSVS', 114, 'crassam', '', '', '7', 5), ('HABEO', 115, 'habet', '', '', '7', 14), ('ELEPHANTVS', 116, 'Elephantus', '', '', '7', 8), ('CORNV', 117, 'coru', '', '', '7', 11), ('NE/2', 118, 'ne', '', '', '7', 5), ('IN', 119, 'in', '', '', '7', 14), ('NASVS', 120, 'naso', '', '', '7', 13), ('NON', 121, 'non', '', '', '7', 9), ('HABEO', 122, 'habet', '', '', '7', 14), ('SED', 123, 'sed', '', '', '7', 5), ('ELEPHANTVS', 124, 'elephantus', '', '', '7', 8), ('PROBOSCIS', 125, 'proboscidem', '', '', '7', 1), ('HABEO', 126, 'habet', '', '', '7', 14), ('NON', 127, 'Non', '', '', '7', 9), ('SVM/1', 128, 'sum', '', '', '7', 31), ('ELEPHANTVS', 129, 'elephantus', '', '', '7', 8), ('DICO/2', 130, 'dicit', '', '', '7', 7), ('RENA/N', 131, 'Rena', '', '', '7', 14), ('FORTASSE', 132, 'Fortasse', '', '', '7', 3), ('HIPPOPOTAMVS', 133, 'hippopotamus', '', '', '7', 6), ('SVM/1', 134, 'sum', '', '', '7', 31), ('RENA/N', 135, 'Rena', '', '', '8', 14), ('PARVVS/2', 136, 'paruum', '', '', '8', 3), ('HIPPOPOTAMVS', 137, 'hippopotamum', '', '', '8', 6), ('SPECTO', 138, 'spectat', '', '', '8', 6), ('HIPPOPOTAMVS', 139, 'Hippopotamus', '', '', '8', 6), ('SVM/1', 140, 'est', '', '', '8', 31), ('CANVS', 141, 'canus', '', '', '8', 6), ('COLOR', 142, 'colore', '', '', '8', 6), ('HIPPOPOTAMVS', 143, 'Hippopotamus', '', '', '8', 6), ('PELLIS', 144, 'pellem', '', '', '8', 5), ('CRASSVS', 145, 'crassam', '', '', '8', 5), ('HABEO', 146, 'habet', '', '', '8', 14), ('SED', 147, 'Sed', '', '', '8', 5), ('HIPPOPOTAMVS', 148, 'hippopotamus', '', '', '8', 6), ('NASVS', 149, 'nasum', '', '', '8', 13), ('LATVS/2', 150, 'latum', '', '', '8', 1), ('ET/2', 151, 'et', '', '', '8', 7), ('SAETA', 152, 'saetas', '', '', '8', 1), ('HABEO', 153, 'habet', '', '', '8', 14), ('NON', 154, 'Non', '', '', '9', 9), ('SVM/1', 155, 'sum', '', '', '9', 31), ('HIPPOPOTAMVS', 156, 'hippopotamus', '', '', '9', 6), ('DICO/2', 157, 'dicit', '', '', '9', 7), ('RENA/N', 158, 'Rena', '', '', '9', 14), ('NON', 159, 'Non', '', '', '9', 9), ('SVM/1', 160, 'sum', '', '', '9', 31), ('ELEPHANTVS', 161, 'elephantus', '', '', '9', 8), ('O', 162, 'O', '', '', '9', 1), ('QVIS/1', 163, 'quid', '', '', '9', 3), ('SVM/1', 164, 'sum', '', '', '9', 31), ('QVIS/1', 165, 'Quid', '', '', '9', 3), ('SVM/1', 166, 'sum', '', '', '9', 31), ('MATER', 167, 'Mater', '', '', '10', 8), ('QVI/1', 168, 'quae', '', '', '10', 2), ('AMBVLO', 169, 'ambulat', '', '', '10', 2), ('POST/2', 170, 'post', '', '', '10', 1), ('RENA/N', 171, 'Renam', '', '', '10', 14), ('DICO/2', 172, 'dicit', '', '', '10', 7), ('RENA/N', 173, 'Rena', '', '', '10', 14), ('SPECTO', 174, 'specta', '', '', '10', 6), ('IN', 175, 'in', '', '', '10', 14), ('AQVA', 176, 'aquam', '', '', '10', 2), ('SPECTO', 177, 'Specta', '', '', '10', 6), ('TV', 178, 'te', '', '', '10', 9), ('ET/2', 179, 'et', '', '', '10', 7), ('EGO', 180, 'me', '', '', '10', 4), ('SVM/1', 181, 'Es', '', '', '11', 31), ('NE/2', 182, 'ne', '', '', '11', 5), ('TV', 183, 'tu', '', '', '11', 9), ('SIMILIS', 184, 'simili', '', '', '11', 2), ('EGO', 185, 'mihi', '', '', '11', 4), ('SVM/1', 186, 'Es', '', '', '11', 31), ('NE/2', 187, 'ne', '', '', '11', 5), ('CANVS', 188, 'cana', '', '', '11', 6), ('COLOR', 189, 'colore', '', '', '11', 6), ('SVM/1', 190, 'Est', '', '', '11', 31), ('NE/2', 191, 'ne', '', '', '11', 5), ('PELLIS', 192, 'poellis', '', '', '11', 5), ('TVVS', 193, 'tua', '', '', '11', 3), ('CRASSVS', 194, 'crassa', '', '', '11', 5), ('SVM/1', 195, 'Est', '', '', '11', 31), ('NE/2', 196, 'ne', '', '', '11', 5), ('NASVS', 197, 'nasus', '', '', '11', 13), ('TVVS', 198, 'tuus', '', '', '11', 3), ('SIMILIS', 199, 'similis', '', '', '11', 2), ('NASVS', 200, 'naso', '', '', '11', 13), ('MEVS', 201, 'meo', '', '', '11', 3), ('SED', 202, 'Sed', '', '', '11', 5), ('CORNV', 203, 'cornu', '', '', '11', 11), ('IN', 204, 'in', '', '', '11', 14), ('NASVS', 205, 'naso', '', '', '11', 13), ('NON', 206, 'non', '', '', '11', 9), ('HABEO', 207, 'habeo', '', '', '11', 14), ('DICO/2', 208, 'dicit', '', '', '11', 7), ('RENA/N', 209, 'Rena', '', '', '11', 14), ('CORNV', 210, 'Cornu', '', '', '12', 11), ('IN', 211, 'in', '', '', '12', 14), ('NASVS', 212, 'naso', '', '', '12', 13), ('HABEO', 213, 'habebis', '', '', '12', 14), ('CVM/3', 214, 'cum', '', '', '12', 1), ('SVM/1', 215, 'eris', '', '', '12', 31), ('MAGNVS', 216, 'magna', '', '', '12', 3), ('NVNC', 217, 'Nunc', '', '', '12', 2), ('SVM/1', 218, 'est', '', '', '12', 31), ('TEMPVS/1', 219, 'tempus', '', '', '12', 2), ('CRESCO', 220, 'crescere', '', '', '12', 3), ('ET/2', 221, 'et', '', '', '12', 7), ('DISCO', 222, 'discere', '', '', '12', 3), ('CRESCO', 223, 'Crese', '', '', '12', 3), ('ET/2', 224, 'et', '', '', '12', 7), ('DISCO', 225, 'disce', '', '', '12', 3), ('NVNC', 226, 'nunc', '', '', '12', 2), ('ET/2', 227, 'et', '', '', '12', 7), ('IN', 228, 'in', '', '', '12', 14), ('TEMPVS/1', 229, 'tempore', '', '', '12', 2), ('SVM/1', 230, 'eris', '', '', '12', 31), ('MAGNVS', 231, 'magna', '', '', '12', 3), ('ET/2', 232, 'et', '', '', '12', 7), ('BONVS', 233, 'bona', '', '', '12', 1), ('RHINOCEROS', 234, 'rhinoceros', '', '', '12', 10), ('EXSPECTO', 235, 'Exspectabo', '', '', '13', 1), ('MATER', 236, 'mater', '', '', '13', 8), ('DICO/2', 237, 'dicit', '', '', '13', 7), ('RENA/N', 238, 'Rena', '', '', '13', 14), ('DESIDERO', 239, 'Desidero', '', '', '13', 2), ('CRESCO', 240, 'crescere', '', '', '13', 3), ('ET/2', 241, 'et', '', '', '13', 7), ('DISCO', 242, 'discere', '', '', '13', 3), ('GRATIA', 243, 'Gratias', '', '', '13', 1), ('TV', 244, 'tibi', '', '', '13', 9), ('AGO', 245, 'ago', '', '', '13', 1), ('EGO', 246, 'Ego', '', '', '13', 4), ('TV', 247, 'te', '', '', '13', 9), ('AMO', 248, 'amo', '', '', '13', 1), ('MATER', 249, 'mater', '', '', '13', 8), ('RENA/N', 250, 'Rena', '', '', '14', 14), ('IN', 251, 'in', '', '', '14', 14), ('AQVA', 252, 'aquam', '', '', '14', 2), ('ITERVM', 253, 'iterum', '', '', '14', 1), ('SPECTO', 254, 'spectat', '', '', '14', 6), ('TVBER', 255, 'Tuber', '', '', '14', 1), ('IN', 256, 'in', '', '', '14', 14), ('NASVS', 257, 'naso', '', '', '14', 13), ('MEVS', 258, 'meo', '', '', '14', 3), ('SPECTO', 259, 'specto', '', '', '14', 6), ('MOX', 260, 'Mox', '', '', '15', 1), ('CORNV', 261, 'cornu', '', '', '15', 11), ('IN', 262, 'in', '', '', '15', 14), ('NASVS', 263, 'naso', '', '', '15', 13), ('HABEO', 264, 'habebo', '', '', '15', 14), ('RENA/N', 265, 'Rena', '', '', '15', 14), ('CLAMO', 266, 'clamat', '', '', '15', 1)]
section_list ={'1': 'start', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': '10', '12': '11', '13': '12', '14': '13', '15': '14', 'end': '15', 'start': 'start'}
title = "Williams, Rena Rhinoceros"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)