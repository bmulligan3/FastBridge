import text
nan=""
section_words = {'start': -1, '171': 0, '227': 1, '106': 2, '275': 3, '313': 4, '370': 5, '120': 6, '371': 7, '254': 8, '149': 9, '255': 10, '372': 11, '129': 12, '373': 13, '237': 14, '55': 15, '228': 16, '23': 17, '172': 18, '180': 19, '166': 20, '214': 21, '49': 22, '46': 23, '374': 24, '238': 25, '276': 26, '44': 27, '75': 28, '291': 29, '239': 30, '334': 31, '314': 32, '181': 33, '58': 34, '194': 35, '375': 36, '315': 37, '256': 38, '292': 39, '376': 40, '257': 41, '335': 42, '83': 43, '336': 44, '316': 45, '107': 46, '87': 47, '143': 48, '240': 49, '150': 50, '66': 51, '337': 52, '229': 53, '11': 54, '84': 55, '50': 56, '258': 57, '215': 58, '195': 59, '377': 60, '121': 61, '60': 62, '167': 63, '182': 64, '293': 65, '317': 66, '294': 67, '159': 68, '216': 69, '95': 70, '13': 71, '111': 72, '295': 73, '151': 74, '19': 75, '318': 76, '196': 77, '173': 78, '54': 79, '2': 80, '217': 81, '338': 82, '112': 83, '339': 84, '160': 85, '197': 86, '14': 87, '259': 88, '340': 89, '102': 90, '277': 91, '378': 92, '230': 93, '113': 94, '260': 95, '261': 96, '78': 97, '341': 98, '342': 99, '379': 100, '343': 101, '43': 102, '31': 103, '22': 104, '130': 105, '122': 106, '51': 107, '98': 108, '296': 109, '6': 110, '108': 111, '136': 112, '80': 113, '125': 114, '8': 115, '26': 116, '103': 117, '380': 118, '183': 119, '81': 120, '146': 121, '157': 122, '381': 123, '88': 124, '382': 125, '73': 126, '12': 127, '241': 128, '231': 129, '218': 130, '206': 131, '298': 132, '344': 133, '345': 134, '262': 135, '71': 136, '383': 137, '346': 138, '232': 139, '20': 140, '319': 141, '299': 142, '347': 143, '348': 144, '161': 145, '242': 146, '131': 147, '198': 148, '243': 149, '300': 150, '349': 151, '114': 152, '101': 153, '320': 154, '94': 155, '162': 156, '199': 157, '244': 158, '24': 159, '350': 160, '351': 161, '61': 162, '278': 163, '384': 164, '123': 165, '279': 166, '174': 167, '263': 168, '385': 169, '79': 170, '184': 171, '207': 172, '386': 173, '115': 174, '185': 175, '219': 176, '208': 177, '186': 178, '301': 179, '72': 180, '264': 181, '3': 182, '152': 183, '67': 184, '220': 185, '321': 186, '245': 187, '280': 188, '209': 189, '33': 190, '175': 191, '233': 192, '246': 193, '104': 194, '265': 195, '352': 196, '387': 197, '281': 198, '302': 199, '353': 200, '354': 201, '25': 202, '388': 203, '282': 204, '283': 205, '35': 206, '389': 207, '303': 208, '137': 209, '139': 210, '29': 211, '390': 212, '70': 213, '304': 214, '47': 215, '355': 216, '305': 217, '234': 218, '132': 219, '200': 220, '163': 221, '306': 222, '221': 223, '187': 224, '201': 225, '356': 226, '40': 227, '307': 228, '222': 229, '10': 231, '188': 232, '247': 233, '56': 234, '322': 235, '45': 236, '323': 237, '202': 238, '324': 239, '68': 240, '284': 241, '325': 242, '391': 243, '158': 244, '392': 245, '62': 246, '326': 247, '116': 248, '154': 249, '210': 250, '327': 251, '393': 252, '211': 253, '189': 254, '147': 255, '138': 256, '394': 257, '42': 258, '308': 259, '248': 260, '1': 261, '32': 262, '168': 263, '36': 264, '176': 265, '117': 266, '223': 267, '395': 268, '396': 269, '190': 270, '155': 271, '328': 272, '285': 273, '191': 274, '357': 275, '89': 276, '224': 277, '133': 278, '266': 279, '225': 280, '212': 281, '17': 282, '92': 283, '69': 284, '109': 285, '18': 286, '267': 287, '118': 288, '52': 289, '63': 290, '77': 291, '7': 292, '48': 293, '286': 294, '34': 295, '249': 296, '64': 297, '329': 298, '397': 299, '110': 300, '287': 301, '398': 302, '16': 303, '358': 304, '169': 305, '288': 306, '268': 307, '148': 308, '269': 309, '164': 310, '93': 311, '250': 312, '96': 313, '65': 314, '399': 315, '38': 316, '289': 317, '192': 318, '251': 319, '400': 320, '359': 321, '330': 322, '270': 323, '21': 324, '401': 325, '165': 326, '360': 327, '53': 328, '41': 329, '57': 330, '144': 331, '402': 332, '203': 333, '361': 334, '37': 335, '39': 336, '403': 337, '76': 338, '235': 339, '99': 340, '226': 341, '85': 342, '404': 343, '204': 344, '362': 345, '100': 346, '363': 347, '126': 348, '177': 349, '127': 350, '27': 351, '364': 352, '365': 353, '366': 354, '405': 355, '28': 356, '406': 357, '252': 358, '119': 359, '140': 360, '9': 361, '124': 362, '367': 363, '141': 364, '331': 365, '30': 366, '178': 367, '368': 368, '4': 369, '5': 370, '134': 371, '128': 372, '407': 373, '369': 374, '156': 375, '309': 376, '310': 377, '142': 378, '193': 379, '332': 380, '408': 381, '59': 382, '409': 383, '213': 384, '97': 385, '271': 386, '82': 387, '272': 388, '333': 389, '273': 390, '290': 391, '311': 392, '274': 393, '410': 394, '74': 395, '411': 396, '312': 397, '145': 398, '170': 399, '90': 400, '135': 401, '236': 402, '91': 403, '86': 404, '253': 405, '105': 406, '205': 407, '412': 408, '15': 409, '179': 410, 'end': -2}
the_text =  [('ΑΓΑΘΟΣ', 0, 'αγαθος', '', '', '171', 1), ('ΑΓΓΕΛΟΣ', 1, 'αγγελος', '', '', '227', 1), ('ΑΓΩ', 2, 'αγω', '', '', '106', 1), ('ΑΕΙ', 3, 'αει', '', '', '275', 1), ('ΑΕΚΩΝ', 4, 'αεκων', '', '', '313', 1), ('ΑΘΗΝΑΙΗ', 5, 'Αθηναίη', '', '', '370', 1), ('ΑΘΗΝΑΙΟΣ', 6, 'Αθηναιος', '', '', '120', 1), ('ΑΙΓΥΠΤΟΣ', 7, 'Αιγυπτος', '', '', '371', 1), ('ΑΙΟΛΕΥΣ', 8, 'Αιολευς', '', '', '254', 1), ('ΑΙΡΕΩ', 9, 'αιρεω', '', '', '149', 1), ('ΑΙΤΙΟΣ', 10, 'αιτιος', '', '', '255', 1), ('ΑΚΕΟΜΑΙ', 11, 'ακέομαι', '', '', '372', 1), ('ΑΚΟΥΩ', 12, 'ακουω', '', '', '129', 1), ('ΑΚΡΟΠΟΛΙΣ', 13, 'ακροπολις', '', '', '373', 1), ('ΑΛΙΣΚΟΜΑΙ', 14, 'αλισκομαι', '', '', '237', 1), ('ΑΛΛΑ', 15, 'αλλα', '', '', '55', 1), ('ΑΛΛΗΛΩΝ', 16, 'αλληλων', '', '', '228', 1), ('ΑΛΛΟΣ', 17, 'αλλος', '', '', '23', 1), ('ΑΛΥΑΤΤΗΣ', 18, 'Αλυαττης', '', '', '172', 1), ('ΑΜΑ', 19, 'αμα', '', '', '180', 1), ('ΑΜΕΙΒΩ', 20, 'αμειβω', '', '', '166', 1), ('ΑΜΦΟΤΕΡΟΣ', 21, 'αμφοτερος', '', '', '214', 1), ('ΑΝ', 22, 'αν', '', '', '49', 1), ('ΑΝΑ', 23, 'ανα', '', '', '46', 1), ('ΑΝΑΒΑΙΝΩ', 24, 'αναβαινω', '', '', '374', 1), ('ΑΝΑΘΗΜΑ', 25, 'αναθημα', '', '', '238', 1), ('ΑΝΑΤΙΘΗΜΙ', 26, 'ανατιθημι', '', '', '276', 1), ('ΑΝΗΡ', 27, 'ανηρ', '', '', '44', 1), ('ΑΝΘΡΩΠΟΣ', 28, 'ανθρωπος', '', '', '75', 1), ('ΑΝΤΙ', 29, 'αντι', '', '', '291', 1), ('ΑΝΩ/2', 30, 'ανυω', '', '', '239', 1), ('ΑΞΙΟΣ', 31, 'αξιος', '', '', '334', 1), ('ΑΠΑΛΛΑΣΣΩ', 32, 'απαλλασσω', '', '', '314', 1), ('ΑΠΑΣ', 33, 'απας', '', '', '181', 1), ('ΑΠΟ', 34, 'απο', '', '', '58', 1), ('ΑΠΟΔΕΙΚΝΥΜΙ', 35, 'αποδεικνυμι', '', '', '194', 1), ('ΑΠΟΘΝΗΙΣΚΩ', 36, 'αποθνῃσκω', '', '', '375', 1), ('ΑΠΟΚΤΕΙΝΩ', 37, 'αποκτεινω', '', '', '315', 1), ('ΑΠΟΛΛΥΜΙ', 38, 'απολλυμι', '', '', '256', 1), ('ΑΠΟΠΕΜΠΩ', 39, 'αποπεμπω', '', '', '292', 1), ('ΑΡΑΞΗΣ', 40, 'Αραξης', '', '', '376', 1), ('ΑΡΓΕΙΟΣ', 41, 'Αργειος', '', '', '257', 1), ('ΑΡΙΣΤΟΣ', 42, 'αριστος', '', '', '335', 1), ('ΑΡΠΑΓΟΣ', 43, 'Αρπαγος', '', '', '83', 1), ('ΑΡΠΑΖΩ', 44, 'αρπαζω', '', '', '336', 1), ('ΑΡΧΑΙΟΣ', 45, 'αρχαιος', '', '', '316', 1), ('ΑΡΧΗ', 46, 'αρχη', '', '', '107', 1), ('ΑΡΧΩ', 47, 'αρχω', '', '', '87', 1), ('ΑΣΙΗ', 48, 'Ασιη', '', '', '143', 1), ('ΑΣΣΥΡΙΟΣ', 49, 'Ασσυριος', '', '', '240', 1), ('ΑΣΤΥ', 50, 'αστυ', '', '', '150', 1), ('ΑΣΤΥΑΓΗΣ', 51, 'Αστυαγης', '', '', '66', 1), ('ΑΥ', 52, 'αυ', '', '', '337', 1), ('ΑΥΤΙΚΑ', 53, 'αυτικα', '', '', '229', 1), ('ΑΥΤΟΣ', 54, 'αυτος', '', '', '11', 1), ('ΑΥΤΟΥ', 55, 'αυτου', '', '', '84', 1), ('ΑΦΙΚΝΕΟΜΑΙ', 56, 'αφικνεομαι', '', '', '50', 1), ('ΑΦΙΣΤΗΜΙ', 57, 'αφιστημι', '', '', '258', 1), ('ΒΑΒΥΛΩΝ', 58, 'βαβυλών', '', '', '215', 1), ('ΒΑΒΥΛΩΝΙΟΣ', 59, 'βαβυλώνιος', '', '', '195', 1), ('ΒΑΡΒΑΡΟΣ/2', 60, 'βαρβαρος', '', '', '377', 1), ('ΒΑΣΙΛΕΙΟΣ', 61, 'βασιλειος', '', '', '121', 1), ('ΒΑΣΙΛΕΥΣ', 62, 'βασιλευς', '', '', '60', 1), ('ΒΑΣΙΛΕΥΩ', 63, 'βασιλευω', '', '', '167', 1), ('ΒΑΣΙΛΗΙΗ', 64, 'βασιληιη', '', '', '182', 1), ('ΒΑΣΙΛΗΙΟΝ', 65, 'βασιληιον', '', '', '293', 1), ('ΒΙΟΣ', 66, 'βιος', '', '', '317', 1), ('ΒΙΟΩ', 67, 'βιοω', '', '', '294', 1), ('ΒΟΥΚΟΛΟΣ', 68, 'βουκολος', '', '', '159', 1), ('ΒΟΥΛΕΥΩ', 69, 'βουλευω', '', '', '216', 1), ('ΒΟΥΛΟΜΑΙ', 70, 'βουλομαι', '', '', '95', 1), ('ΓΑΡ', 71, 'γαρ', '', '', '13', 1), ('ΓΕ', 72, 'γε', '', '', '111', 1), ('ΓΕΝΟΣ', 73, 'γενος', '', '', '295', 1), ('ΓΗ', 74, 'γη', '', '', '151', 1), ('ΓΙΓΝΟΜΑΙ', 75, 'γιγνομαι', '', '', '19', 1), ('ΓΛΩΣΣΑ', 76, 'γλωσσα', '', '', '318', 1), ('ΓΝΩΜΗ', 77, 'γνωμη', '', '', '196', 1), ('ΓΥΓΗΣ/2', 78, 'γυγης', '', '', '173', 1), ('ΓΥΝΗ', 79, 'γυνη', '', '', '54', 1), ('ΔΕ', 80, 'δε', '', '', '2', 1), ('ΔΕΙ', 81, 'δει', '', '', '217', 1), ('ΔΕΙΝΟΣ', 82, 'δεινος', '', '', '338', 1), ('ΔΕΛΦΟΙ', 83, 'δελφοι', '', '', '112', 1), ('ΔΕΣΠΟΤΗΣ', 84, 'δεσποτης', '', '', '339', 1), ('ΔΕΥΤΕΡΟΣ', 85, 'δευτερος', '', '', '160', 1), ('ΔΕΩ', 86, 'δεω', '', '', '197', 1), ('ΔΗ', 87, 'δη', '', '', '14', 1), ('ΔΗΙΟΚΗΣ', 88, 'δηϊοκης', '', '', '259', 1), ('ΔΗΜΟΣ', 89, 'δημος', '', '', '340', 1), ('ΔΙΑ', 90, 'δια', '', '', '102', 1), ('ΔΙΑΒΑΙΝΩ', 91, 'διαβαινω', '', '', '277', 1), ('ΔΙΑΚΟΣΜΕΩ', 92, 'διακοσμέω', '', '', '378', 1), ('ΔΙΑΦΘΕΙΡΩ', 93, 'διαφθειρω', '', '', '230', 1), ('ΔΙΔΩΜΙ', 94, 'διδωμι', '', '', '113', 1), ('ΔΙΚΗ', 95, 'δικη', '', '', '260', 1), ('ΔΙΟ', 96, 'διο', '', '', '261', 1), ('ΔΟΚΕΩ', 97, 'δοκεω', '', '', '78', 1), ('ΔΟΡΥΦΟΡΟΣ', 98, 'δορυφορος', '', '', '341', 1), ('ΔΥΝΑΜΑΙ', 99, 'δυναμαι', '', '', '342', 1), ('ΔΥΝΑΜΙΣ', 100, 'δυναμις', '', '', '379', 1), ('ΔΩΔΕΚΑ', 101, 'δωδεκα', '', '', '343', 1), ('ΕΑΝ', 102, 'εαν', '', '', '43', 1), ('ΕΑΥΤΟΥ', 103, 'εαυτου', '', '', '31', 1), ('ΕΓΩ', 104, 'εγω', '', '', '22', 1), ('ΕΘΕΛΩ', 105, 'εθελω', '', '', '130', 1), ('ΕΘΝΟΣ', 106, 'εθνος', '', '', '122', 1), ('ΕΙ', 107, 'ει', '', '', '51', 1), ('ΕΙΔΟΝ', 108, 'ειδον', '', '', '98', 1), ('ΕΙΚΟΣΙ', 109, 'εικοσι', '', '', '296', 1), ('ΕΙΜΙ', 110, 'ειμι', '', '', '6', 1), ('ΕΙΜΙ/2', 111, 'ειμι', '', '', '108', 1), ('ΕΙΝΕΚΑ', 112, 'εινεκα', '', '', '136', 1), ('ΕΙΠΟΝ', 113, 'ειπον,', '', '', '80', 1), ('ΕΙΣ', 114, 'εις', '', '', '125', 1), ('ΕΙΣ/2', 115, 'εις', '', '', '8', 1), ('ΕΚ', 116, 'εκ', '', '', '26', 1), ('ΕΚΑΣΤΟΣ', 117, 'εκαστος', '', '', '103', 1), ('ΕΚΑΤΕΡΟΣ', 118, 'εκατερος', '', '', '380', 1), ('ΕΚΔΙΔΩΜΙ', 119, 'εκδιδωμι', '', '', '183', 1), ('ΕΚΕΙΝΟΣ', 120, 'εκεινος', '', '', '81', 1), ('ΕΛΑΥΝΩ', 121, 'ελαυνω', '', '', '146', 1), ('ΕΛΕΓΟΣ', 122, 'ελεγος', '', '', '157', 1), ('ΕΛΚΩ', 123, 'ελκω', '', '', '381', 1), ('ΕΛΛΗΝ', 124, 'ελλην', '', '', '88', 1), ('ΕΛΠΙΖΩ', 125, 'ελπιζω', '', '', '382', 1), ('ΕΜΟΣ', 126, 'εμος', '', '', '73', 1), ('ΕΝ', 127, 'εν', '', '', '12', 1), ('ΕΝΘΑ', 128, 'ενθα', '', '', '241', 1), ('ΕΝΤΑΥΘΑ', 129, 'ενταυθα', '', '', '231', 1), ('ΕΝΤΕΛΛΩ', 130, 'εντελλω', '', '', '218', 1), ('ΕΝΤΕΥΘΕΝ', 131, 'εντευθεν', '', '', '206', 1), ('ΕΞΕΛΑΥΝΩ', 132, 'εξελαυνω', '', '', '298', 1), ('ΕΞΕΣΤΙ', 133, 'εξεστι', '', '', '344', 1), ('ΕΞΕΥΡΙΣΚΩ', 134, 'εξευρίσκω', '', '', '345', 1), ('ΕΠΕΑΝ', 135, 'επεαν', '', '', '262', 1), ('ΕΠΕΙ', 136, 'επει', '', '', '71', 1), ('ΕΠΕΙΜΙ', 137, 'επειμι', '', '', '383', 1), ('ΕΠΕΙΡΟΜΑΙ', 138, 'επειρομαι', '', '', '346', 1), ('ΕΠΕΡΩΤΑΩ', 139, 'επερωταω', '', '', '232', 1), ('ΕΠΙ', 140, 'επι', '', '', '20', 1), ('ΕΠΙΣΤΑΜΑΙ', 141, 'επισταμαι', '', '', '319', 1), ('ΕΠΟΜΑΙ', 142, 'επομαι', '', '', '299', 1), ('ΕΠΟΣ', 143, 'επος', '', '', '347', 1), ('ΕΡΓΑΖΟΜΑΙ', 144, 'εργαζομαι', '', '', '348', 1), ('ΕΡΓΟΝ', 145, 'εργον', '', '', '161', 1), ('ΕΡΟΜΑΙ', 146, 'ερομαι', '', '', '242', 1), ('ΕΡΧΟΜΑΙ', 147, 'ερχομαι', '', '', '131', 1), ('ΕΡΩ', 148, 'ερω', '', '', '198', 1), ('ΕΡΩΤΑΩ', 149, 'ερωταω', '', '', '243', 1), ('ΕΣΒΑΛΛΩ', 150, 'εσβαλλω', '', '', '300', 1), ('ΕΣΣΟΟΜΑΙ', 151, 'εσσοομαι', '', '', '349', 1), ('ΕΤΕΡΟΣ', 152, 'ετερος', '', '', '114', 1), ('ΕΤΙ', 153, 'ετι', '', '', '101', 1), ('ΕΤΟΙΜΟΣ', 154, 'ετοιμος', '', '', '320', 1), ('ΕΤΟΣ', 155, 'ετος', '', '', '94', 1), ('ΕΥ', 156, 'ευ', '', '', '162', 1), ('ΕΥΡΙΣΚΩ', 157, 'ευρισκω', '', '', '199', 1), ('ΕΦΙΣΤΗΜΙ', 158, 'εφιστημι', '', '', '244', 1), ('ΕΧΩ', 159, 'εχω', '', '', '24', 1), ('ΕΩΘΑ', 160, 'εωθα', '', '', '350', 1), ('ΖΕΥΣ', 161, 'Ζευς', '', '', '351', 1), ('Η', 162, 'η', '', '', '61', 1), ('ΗΔΗ', 163, 'ηδη', '', '', '278', 1), ('ΗΚΩ', 164, 'ηκω', '', '', '384', 1), ('ΗΜΕΡΑ', 165, 'ημερα', '', '', '123', 1), ('ΗΠΕΙΡΟΣ', 166, 'ηπειρος', '', '', '279', 1), ('ΘΑΛΑΣΣΑ', 167, 'θαλασσα', '', '', '174', 1), ('ΘΕΑΟΜΑΙ', 168, 'θεαομαι', '', '', '263', 1), ('ΘΕΟΠΡΟΠΟΣ', 169, 'θεοπροπος', '', '', '385', 1), ('ΘΕΟΣ', 170, 'θεος', '', '', '79', 1), ('ΘΥΓΑΤΗΡ', 171, 'θυγατηρ', '', '', '184', 1), ('ΘΥΩ', 172, 'θυω', '', '', '207', 1), ('ΙΔΡΥΩ', 173, 'ιδρυω', '', '', '386', 1), ('ΙΕΡΟΣ', 174, 'ιερος', '', '', '115', 1), ('ΙΗΜΙ', 175, 'ιημι', '', '', '185', 1), ('ΙΝΑ', 176, 'ινα', '', '', '219', 1), ('ΙΠΠΟΣ', 177, 'ιππος', '', '', '208', 1), ('ΙΣΤΗΜΙ', 178, 'ιστημι', '', '', '186', 1), ('ΙΣΧΥΡΟΣ', 179, 'ισχυρος', '', '', '301', 1), ('ΙΩΝΕΣ', 180, 'Ιωνες', '', '', '72', 1), ('ΙΩΝΙΑ/2', 181, 'Ιωνια', '', '', '264', 1), ('ΚΑΙ', 182, 'και', '', '', '3', 1), ('ΚΑΚΟΣ', 183, 'κακος', '', '', '152', 1), ('ΚΑΛΕΩ', 184, 'καλεω', '', '', '67', 1), ('ΚΑΛΟΣ', 185, 'καλος', '', '', '220', 1), ('ΚΑΝΔΑΥΛΗΣ', 186, 'Κανδαυλης', '', '', '321', 1), ('ΚΑΡ', 187, 'Καρ', '', '', '245', 1), ('ΚΑΡΠΟΣ', 188, 'καρπος', '', '', '280', 1), ('ΚΑΡΤΑ', 189, 'καρτα', '', '', '209', 1), ('ΚΑΤΑ', 190, 'κατα', '', '', '33', 1), ('ΚΑΤΑΣΤΡΕΦΩ', 191, 'καταστρεφω', '', '', '175', 1), ('ΚΑΤΙΣΤΗΜΙ', 192, 'κατίστημι', '', '', '233', 1), ('ΚΕΙΜΑΙ', 193, 'κειμαι', '', '', '246', 1), ('ΚΕΛΕΥΩ', 194, 'κελευω', '', '', '104', 1), ('ΚΗΡΥΞ', 195, 'κηρυξ', '', '', '265', 1), ('ΚΟΙΟΣ', 196, 'κοιος', '', '', '352', 1), ('ΚΟΣΜΕΩ', 197, 'κοσμεω', '', '', '387', 1), ('ΚΟΤΕ', 198, 'κοτέ', '', '', '281', 1), ('ΚΟΥ', 199, 'κου', '', '', '302', 1), ('ΚΡΕΑΣ', 200, 'κρέας', '', '', '353', 1), ('ΚΡΗΤΗΡΗΡΟΣ', 201, 'κρητηρ', '', '', '354', 1), ('ΚΡΟΙΣΟΣ', 202, 'Κροισος', '', '', '25', 1), ('ΚΤΕΙΝΩ', 203, 'κτεινω', '', '', '388', 1), ('ΚΥΑΞΑΡΗΣ', 204, 'Κυαξαρης', '', '', '282', 1), ('ΚΥΚΛΟΣ', 205, 'κυκλος', '', '', '283', 1), ('ΚΥΡΟΣ', 206, 'Κυρος', '', '', '35', 1), ('ΚΩ', 207, 'κω', '', '', '389', 1), ('ΚΩΜΗ', 208, 'κωμη', '', '', '303', 1), ('ΛΑΚΕΔΑΙΜΟΝΙΟΣ', 209, 'Λακεδαιμονιος', '', '', '137', 1), ('ΛΑΜΒΑΝΩ', 210, 'λαμβανω', '', '', '139', 1), ('ΛΕΓΩ', 211, 'λεγω', '', '', '29', 1), ('ΛΙΜΝΗ', 212, 'λιμνη', '', '', '390', 1), ('ΛΟΓΟΣ', 213, 'λογος', '', '', '70', 1), ('ΛΟΙΠΟΣ', 214, 'λοιπος', '', '', '304', 1), ('ΛΥΔΟΣ', 215, 'Λυδος', '', '', '47', 1), ('ΛΥΚΙΟΣ', 216, 'Λυκιος', '', '', '355', 1), ('ΜΑΓΟΙ', 217, 'Μαγοι', '', '', '305', 1), ('ΜΑΚΡΟΣ', 218, 'μακρος', '', '', '234', 1), ('ΜΑΛΙΣΤΑ', 219, 'μαλιστα', '', '', '132', 1), ('ΜΑΛΛΟΝ', 220, 'μαλλον', '', '', '200', 1), ('ΜΑΝΘΑΝΩ', 221, 'μανθανω', '', '', '163', 1), ('ΜΑΝΤΗΙΟΝ', 222, 'μαντηιον', '', '', '306', 1), ('ΜΑΣΣΑΓΕΤΑΙ', 223, 'Μασσαγέται', '', '', '221', 1), ('ΜΑΧΗ', 224, 'μαχη', '', '', '187', 1), ('ΜΑΧΟΜΑΙ', 225, 'μαχομαι', '', '', '201', 1), ('ΜΕΓΑΛΩΣ', 226, 'μεγαλως', '', '', '356', 1), ('ΜΕΓΑΣ', 227, 'μεγας', '', '', '40', 1), ('ΜΕΓΕΘΟΣ', 228, 'μεγεθος', '', '', '307', 1), ('ΜΕΛΛΩ', 229, 'μελλω', '', '', '222', 1), ('ΜΕΝ', 230, 'μεν', '', '', '10', 1), ('ΜΕΝ-ΔΕ', 231, 'μεν...δε', '', '', '10', 1), ('ΜΕΝΤΟΙ', 232, 'μεντοι', '', '', '188', 1), ('ΜΕΣΟΣ', 233, 'μεσος', '', '', '247', 1), ('ΜΕΤΑ', 234, 'μετα', '', '', '56', 1), ('ΜΕΤΙΗΜΙ', 235, 'μέτιημι', '', '', '322', 1), ('ΜΗ', 236, 'μη', '', '', '45', 1), ('ΜΗΔΕ', 237, 'μηδε', '', '', '323', 1), ('ΜΗΔΕΙΣ', 238, 'μηδεις', '', '', '202', 1), ('ΜΗΔΙΚΟΣ', 239, 'Μηδικος', '', '', '324', 1), ('ΜΗΔΟΣ', 240, 'Μηδος', '', '', '68', 1), ('ΜΗΤΕ', 241, 'μητε...μητε', '', '', '284', 1), ('ΜΗΤΗΡ', 242, 'μητηρ', '', '', '325', 1), ('ΜΗΧΑΝΑΟΜΑΙ', 243, 'μηχαναομαι', '', '', '391', 1), ('ΜΙΛΗΣΙΟΣ', 244, 'Μιλησιος', '', '', '158', 1), ('ΜΙΛΗΤΟΣ', 245, 'Μίλητος', '', '', '392', 1), ('ΜΙΝ', 246, 'μιν', '', '', '62', 1), ('ΜΟΙΡΑ', 247, 'μοιρα', '', '', '326', 1), ('ΜΟΝΟΣ', 248, 'μονος', '', '', '116', 1), ('ΝΑΟΣ', 249, 'ναος', '', '', '154', 1), ('ΝΑΥΣ', 250, 'ναυς', '', '', '210', 1), ('ΝΕΚΡΟΣ', 251, 'νεκρος', '', '', '327', 1), ('ΝΕΟΣ', 252, 'νεος', '', '', '393', 1), ('ΝΗΣΟΣ', 253, 'νησος', '', '', '211', 1), ('ΝΙΚΑΩ', 254, 'νικαω', '', '', '189', 1), ('ΝΟΜΙΖΩ', 255, 'νομιζω', '', '', '147', 1), ('ΝΟΜΟΣ', 256, 'νομος', '', '', '138', 1), ('ΝΟΣΟΣ', 257, 'νοσος', '', '', '394', 1), ('ΝΥΝ', 258, 'νυν', '', '', '42', 1), ('ΝΥΞ', 259, 'νυξ', '', '', '308', 1), ('ΞΕΝΟΣ', 260, 'ξενος', '', '', '248', 1), ('Ο', 261, 'ο', '', '', '1', 1), ('ΟΔΕ', 262, 'οδε', '', '', '32', 1), ('ΟΔΟΣ', 263, 'οδος', '', '', '168', 1), ('ΟΙ', 264, 'οι', '', '', '36', 1), ('ΟΙΔΑ', 265, 'οιδα', '', '', '176', 1), ('ΟΙΚΕΩ', 266, 'οικεω', '', '', '117', 1), ('ΟΙΚΙΑ', 267, 'οικια', '', '', '223', 1), ('ΟΙΚΟΔΟΜΕΩ', 268, 'οικοδομεω', '', '', '395', 1), ('ΟΙΝΟΣ', 269, 'οινος', '', '', '396', 1), ('ΟΙΟΣ/2', 270, 'οιος', '', '', '190', 1), ('ΟΚΩΣ', 271, 'οκως', '', '', '155', 1), ('ΟΛΒΙΟΣ', 272, 'ολβιος', '', '', '328', 1), ('ΟΛΙΓΟΣ', 273, 'ολιγος', '', '', '285', 1), ('ΟΜΟΙΟΣ', 274, 'ομοιος', '', '', '191', 1), ('ΟΝΕΙΡΟΣ', 275, 'ονειρος', '', '', '357', 1), ('ΟΝΟΜΑ', 276, 'ονομα', '', '', '89', 1), ('ΟΠΙΣΩ', 277, 'οπίσω', '', '', '224', 1), ('ΟΡΑΩ', 278, 'οραω', '', '', '133', 1), ('ΟΡΜΑΩ', 279, 'ορμαω', '', '', '266', 1), ('ΟΡΟΣ', 280, 'ορος', '', '', '225', 1), ('ΟΡΥΣΣΩ', 281, 'ορυσσω', '', '', '212', 1), ('ΟΣ', 282, 'ος', '', '', '17', 1), ('ΟΣΟΣ', 283, 'οσος', '', '', '92', 1), ('ΟΣΤΙΣ', 284, 'οστις', '', '', '69', 1), ('ΟΤΙ', 285, 'οτι', '', '', '109', 1), ('ΟΥ', 286, 'ουκ', '', '', '18', 1), ('ΟΥΔΑΜΟΣ', 287, 'ουδαμος', '', '', '267', 1), ('ΟΥΔΕ', 288, 'ουδε', '', '', '118', 1), ('ΟΥΔΕΙΣ', 289, 'ουδεις', '', '', '52', 1), ('ΟΥΝ', 290, 'ουν', '', '', '63', 1), ('ΟΥΤΕ', 291, 'ουτε...ουτε', '', '', '77', 1), ('ΟΥΤΟΣ', 292, 'ουτος', '', '', '7', 1), ('ΟΥΤΩΣ', 293, 'ουτως', '', '', '48', 1), ('ΟΨΙΣ', 294, 'οψις', '', '', '286', 1), ('ΠΑΙΣ', 295, 'παις', '', '', '34', 1), ('ΠΑΚΤΥΗΣ', 296, 'Πακτυης', '', '', '249', 1), ('ΠΑΡΑ', 297, 'παρα', '', '', '64', 1), ('ΠΑΡΑΔΙΔΩΜΙ', 298, 'παραδιδωμι', '', '', '329', 1), ('ΠΑΡΑΠΛΗΣΙΟΣ', 299, 'παραπλησιος', '', '', '397', 1), ('ΠΑΡΕΙΜΙ', 300, 'παρειμι', '', '', '110', 1), ('ΠΑΡΕΧΩ', 301, 'παρεχω', '', '', '287', 1), ('ΠΑΡΙΗΜΙ', 302, 'παρίημι', '', '', '398', 1), ('ΠΑΣ', 303, 'πας', '', '', '16', 1), ('ΠΑΣΧΩ', 304, 'πασχω', '', '', '358', 1), ('ΠΑΤΗΡ', 305, 'πατηρ', '', '', '169', 1), ('ΠΑΥΩ', 306, 'παυω', '', '', '288', 1), ('ΠΕΔΙΟΝ', 307, 'πεδιον', '', '', '268', 1), ('ΠΕΙΘΩ', 308, 'πειθω', '', '', '148', 1), ('ΠΕΙΡΑΩ', 309, 'πειραω', '', '', '269', 1), ('ΠΕΙΣΙΣΤΡΑΤΟΣ', 310, 'Πεισίστρατος', '', '', '164', 1), ('ΠΕΜΠΩ', 311, 'πεμπω', '', '', '93', 1), ('ΠΕΝΤΕ', 312, 'πεντε', '', '', '250', 1), ('ΠΕΡ', 313, 'περ', '', '', '96', 1), ('ΠΕΡΙ', 314, 'περι', '', '', '65', 1), ('ΠΕΡΙΕΙΜΙ', 315, 'περιειμι', '', '', '399', 1), ('ΠΕΡΣΗΣ', 316, 'Περσης', '', '', '38', 1), ('ΠΛΕΙΣΤΟΣ', 317, 'πλειστος', '', '', '289', 1), ('ΠΛΕΙΩΝ', 318, 'πλεων', '', '', '192', 1), ('ΠΛΕΩ', 319, 'πλεω', '', '', '251', 1), ('ΠΛΕΩΣ', 320, 'πλεως', '', '', '400', 1), ('ΠΛΗΘΟΣ', 321, 'πληθος', '', '', '359', 1), ('ΠΛΗΝ', 322, 'πλην', '', '', '330', 1), ('ΠΛΟΙΟΝ', 323, 'πλοιον', '', '', '270', 1), ('ΠΟΙΕΩ', 324, 'ποιεω', '', '', '21', 1), ('ΠΟΛΕΜΕΩ', 325, 'πολεμεω', '', '', '401', 1), ('ΠΟΛΕΜΟΣ', 326, 'πολεμος', '', '', '165', 1), ('ΠΟΛΙΟΡΚΕΩ', 327, 'πολιορκεω', '', '', '360', 1), ('ΠΟΛΙΣ', 328, 'πολις', '', '', '53', 1), ('ΠΟΛΥΣ', 329, 'πολυς', '', '', '41', 1), ('ΠΟΤΑΜΟΣ', 330, 'ποταμος', '', '', '57', 1), ('ΠΡΑΓΜΑ', 331, 'πραγμα', '', '', '144', 1), ('ΠΡΑΣΣΩ', 332, 'πρασσω', '', '', '402', 1), ('ΠΡΙΝ', 333, 'πριν', '', '', '203', 1), ('ΠΡΟ', 334, 'προ', '', '', '361', 1), ('ΠΡΟΣ', 335, 'προς', '', '', '37', 1), ('ΠΡΟΤΕΡΟΣ', 336, 'προτερος', '', '', '39', 1), ('ΠΡΟΤΙΘΗΜΙ', 337, 'προτίθημι', '', '', '403', 1), ('ΠΡΩΤΟΣ', 338, 'πρωτος', '', '', '76', 1), ('ΠΥΘΙΗ', 339, 'Πυθίη', '', '', '235', 1), ('ΠΥΝΘΑΝΟΜΑΙ', 340, 'πυνθανομαι', '', '', '99', 1), ('ΡΕΩ', 341, 'ῥεω', '', '', '226', 1), ('ΣΑΡΔΙΣ', 342, 'Σαρδις', '', '', '85', 1), ('ΣΗΜΑΙΝΩ', 343, 'σημαινω', '', '', '404', 1), ('ΣΚΥΘΗΣ', 344, 'Σκυθης', '', '', '204', 1), ('ΣΟΛΩΝ', 345, 'Σολων', '', '', '362', 1), ('ΣΟΣ', 346, 'σος', '', '', '100', 1), ('ΣΤΑΔΙΟΝ', 347, 'σταδιον', '', '', '363', 1), ('ΣΤΡΑΤΕΥΩ', 348, 'στρατευω', '', '', '126', 1), ('ΣΤΡΑΤΙΑ', 349, 'στρατια', '', '', '177', 1), ('ΣΤΡΑΤΟΣ', 350, 'στρατος', '', '', '127', 1), ('ΣΥ', 351, 'συ', '', '', '27', 1), ('ΣΥΜΒΑΛΛΩ', 352, 'συμβαλλω', '', '', '364', 1), ('ΣΥΜΦΟΡΑ', 353, 'συμφορα', '', '', '365', 1), ('ΣΥΝ', 354, 'συν', '', '', '366', 1), ('ΣΥΝΟΙΚΕΩ', 355, 'συνοικέω', '', '', '405', 1), ('ΣΦΕΙΣ', 356, 'σφεις', '', '', '28', 1), ('ΤΑΣΣΩ', 357, 'τασσω', '', '', '406', 1), ('ΤΑΥΤΗΙ', 358, 'ταυτῃ', '', '', '252', 1), ('ΤΑΧΙΣΤΟΣ', 359, 'ταχιστος', '', '', '119', 1), ('ΤΑΧΥΣ', 360, 'ταχυς', '', '', '140', 1), ('ΤΕ', 361, 'τε', '', '', '9', 1), ('ΤΕΙΧΟΣ', 362, 'τειχος', '', '', '124', 1), ('ΤΕΚΝΟΝ', 363, 'τεκνον', '', '', '367', 1), ('ΤΕΛΕΥΤΑΩ', 364, 'τελευταω', '', '', '141', 1), ('ΤΕΛΕΥΤΗ', 365, 'τελευτη', '', '', '331', 1), ('ΤΗΙ', 366, 'τῃ', '', '', '30', 1), ('ΤΙΘΗΜΙ', 367, 'τιθημι', '', '', '178', 1), ('ΤΙΜΑΩ', 368, 'τιμαω', '', '', '368', 1), ('ΤΙΣ', 369, 'τις', '', '', '4', 1), ('ΤΙΣ/2', 370, 'τις', '', '', '5', 1), ('ΤΟΙΟΣΔΕ', 371, 'τοιοσδε', '', '', '134', 1), ('ΤΟΙΟΥΤΟΣ', 372, 'τοιουτος', '', '', '128', 1), ('ΤΟΜΥΡΙΣ', 373, 'Τομυρις', '', '', '407', 1), ('ΤΟΣΟΥΤΟΣ', 374, 'τοσουτος', '', '', '369', 1), ('ΤΟΤΕ', 375, 'τοτε', '', '', '156', 1), ('ΤΡΕΙΣ', 376, 'τρεις', '', '', '309', 1), ('ΤΡΕΠΩ', 377, 'τρεπω', '', '', '310', 1), ('ΤΡΟΠΟΣ', 378, 'τροπος', '', '', '142', 1), ('ΤΥΓΧΑΝΩ', 379, 'τυγχανω', '', '', '193', 1), ('ΤΥΡΑΝΝΙΣ', 380, 'τυραννις', '', '', '332', 1), ('ΥΔΩΡ', 381, 'υδωρ', '', '', '408', 1), ('ΥΠΟ', 382, 'υπο', '', '', '59', 1), ('ΥΣΤΕΡΟΣ', 383, 'υστερος', '', '', '409', 1), ('ΦΑΙΝΩ', 384, 'φαινω', '', '', '213', 1), ('ΦΕΡΩ', 385, 'φερω', '', '', '97', 1), ('ΦΕΥΓΩ', 386, 'φευγω', '', '', '271', 1), ('ΦΗΜΙ', 387, 'φημι', '', '', '82', 1), ('ΦΙΛΟΣ/2', 388, 'φιλος', '', '', '272', 1), ('ΦΡΑΖΩ', 389, 'φραζω', '', '', '333', 1), ('ΦΥΛΑΣΣΩ', 390, 'φυλασσω', '', '', '273', 1), ('ΦΩΚΑΙΚΕΥΣ', 391, 'Φωκαικευς', '', '', '290', 1), ('ΧΑΛΚΟΥΣ', 392, 'χαλκους', '', '', '311', 1), ('ΧΕΙΡ', 393, 'χειρ', '', '', '274', 1), ('ΧΙΟΙ', 394, 'Χιοι', '', '', '410', 1), ('ΧΡΑΟΜΑΙ', 395, 'χραομαι', '', '', '74', 1), ('ΧΡΑΩ/2', 396, 'χραω', '', '', '411', 1), ('ΧΡΗ', 397, 'χρη', '', '', '312', 1), ('ΧΡΗΜΑ', 398, 'χρημα', '', '', '145', 1), ('ΧΡΗΣΤΗΡΙΟΝ', 399, 'χρηστηριον', '', '', '170', 1), ('ΧΡΟΝΟΣ', 400, 'χρονος', '', '', '90', 1), ('ΧΡΥΣΕΟΣ', 401, 'χρυσεος', '', '', '135', 1), ('ΧΡΥΣΟΣ', 402, 'χρυσος', '', '', '236', 1), ('ΧΩΡΑ', 403, 'χωρᾱ', '', '', '91', 1), ('ΧΩΡΕΩ', 404, 'χωρεω', '', '', '86', 1), ('ΧΩΡΟΣ', 405, 'χωρος', '', '', '253', 1), ('Ω', 406, 'ω', '', '', '105', 1), ('ΩΔΕ', 407, 'ωδε', '', '', '205', 1), ('ΩΡΑ', 408, 'ωρα', '', '', '412', 1), ('ΩΣ', 409, 'ως', '', '', '15', 1), ('ΩΣΤΕ', 410, 'ωστε', '', '', '179', 1)]
section_list ={'1': '248', '171': 'start', '227': '171', '106': '227', '275': '106', '313': '275', '370': '313', '120': '370', '371': '120', '254': '371', '149': '254', '255': '149', '372': '255', '129': '372', '373': '129', '237': '373', '55': '237', '228': '55', '23': '228', '172': '23', '180': '172', '166': '180', '214': '166', '49': '214', '46': '49', '374': '46', '238': '374', '276': '238', '44': '276', '75': '44', '291': '75', '239': '291', '334': '239', '314': '334', '181': '314', '58': '181', '194': '58', '375': '194', '315': '375', '256': '315', '292': '256', '376': '292', '257': '376', '335': '257', '83': '335', '336': '83', '316': '336', '107': '316', '87': '107', '143': '87', '240': '143', '150': '240', '66': '150', '337': '66', '229': '337', '11': '229', '84': '11', '50': '84', '258': '50', '215': '258', '195': '215', '377': '195', '121': '377', '60': '121', '167': '60', '182': '167', '293': '182', '317': '293', '294': '317', '159': '294', '216': '159', '95': '216', '13': '95', '111': '13', '295': '111', '151': '295', '19': '151', '318': '19', '196': '318', '173': '196', '54': '173', '2': '54', '217': '2', '338': '217', '112': '338', '339': '112', '160': '339', '197': '160', '14': '197', '259': '14', '340': '259', '102': '340', '277': '102', '378': '277', '230': '378', '113': '230', '260': '113', '261': '260', '78': '261', '341': '78', '342': '341', '379': '342', '343': '379', '43': '343', '31': '43', '22': '31', '130': '22', '122': '130', '51': '122', '98': '51', '296': '98', '6': '296', '108': '6', '136': '108', '80': '136', '125': '80', '8': '125', '26': '8', '103': '26', '380': '103', '183': '380', '81': '183', '146': '81', '157': '146', '381': '157', '88': '381', '382': '88', '73': '382', '12': '73', '241': '12', '231': '241', '218': '231', '206': '218', '298': '206', '344': '298', '345': '344', '262': '345', '71': '262', '383': '71', '346': '383', '232': '346', '20': '232', '319': '20', '299': '319', '347': '299', '348': '347', '161': '348', '242': '161', '131': '242', '198': '131', '243': '198', '300': '243', '349': '300', '114': '349', '101': '114', '320': '101', '94': '320', '162': '94', '199': '162', '244': '199', '24': '244', '350': '24', '351': '350', '61': '351', '278': '61', '384': '278', '123': '384', '279': '123', '174': '279', '263': '174', '385': '263', '79': '385', '184': '79', '207': '184', '386': '207', '115': '386', '185': '115', '219': '185', '208': '219', '186': '208', '301': '186', '72': '301', '264': '72', '3': '264', '152': '3', '67': '152', '220': '67', '321': '220', '245': '321', '280': '245', '209': '280', '33': '209', '175': '33', '233': '175', '246': '233', '104': '246', '265': '104', '352': '265', '387': '352', '281': '387', '302': '281', '353': '302', '354': '353', '25': '354', '388': '25', '282': '388', '283': '282', '35': '283', '389': '35', '303': '389', '137': '303', '139': '137', '29': '139', '390': '29', '70': '390', '304': '70', '47': '304', '355': '47', '305': '355', '234': '305', '132': '234', '200': '132', '163': '200', '306': '163', '221': '306', '187': '221', '201': '187', '356': '201', '40': '356', '307': '40', '222': '307', '10': '222', '188': '10', '247': '188', '56': '247', '322': '56', '45': '322', '323': '45', '202': '323', '324': '202', '68': '324', '284': '68', '325': '284', '391': '325', '158': '391', '392': '158', '62': '392', '326': '62', '116': '326', '154': '116', '210': '154', '327': '210', '393': '327', '211': '393', '189': '211', '147': '189', '138': '147', '394': '138', '42': '394', '308': '42', '248': '308', '32': '1', '168': '32', '36': '168', '176': '36', '117': '176', '223': '117', '395': '223', '396': '395', '190': '396', '155': '190', '328': '155', '285': '328', '191': '285', '357': '191', '89': '357', '224': '89', '133': '224', '266': '133', '225': '266', '212': '225', '17': '212', '92': '17', '69': '92', '109': '69', '18': '109', '267': '18', '118': '267', '52': '118', '63': '52', '77': '63', '7': '77', '48': '7', '286': '48', '34': '286', '249': '34', '64': '249', '329': '64', '397': '329', '110': '397', '287': '110', '398': '287', '16': '398', '358': '16', '169': '358', '288': '169', '268': '288', '148': '268', '269': '148', '164': '269', '93': '164', '250': '93', '96': '250', '65': '96', '399': '65', '38': '399', '289': '38', '192': '289', '251': '192', '400': '251', '359': '400', '330': '359', '270': '330', '21': '270', '401': '21', '165': '401', '360': '165', '53': '360', '41': '53', '57': '41', '144': '57', '402': '144', '203': '402', '361': '203', '37': '361', '39': '37', '403': '39', '76': '403', '235': '76', '99': '235', '226': '99', '85': '226', '404': '85', '204': '404', '362': '204', '100': '362', '363': '100', '126': '363', '177': '126', '127': '177', '27': '127', '364': '27', '365': '364', '366': '365', '405': '366', '28': '405', '406': '28', '252': '406', '119': '252', '140': '119', '9': '140', '124': '9', '367': '124', '141': '367', '331': '141', '30': '331', '178': '30', '368': '178', '4': '368', '5': '4', '134': '5', '128': '134', '407': '128', '369': '407', '156': '369', '309': '156', '310': '309', '142': '310', '193': '142', '332': '193', '408': '332', '59': '408', '409': '59', '213': '409', '97': '213', '271': '97', '82': '271', '272': '82', '333': '272', '273': '333', '290': '273', '311': '290', '274': '311', '410': '274', '74': '410', '411': '74', '312': '411', '145': '312', '170': '145', '90': '170', '135': '90', '236': '135', '91': '236', '86': '91', '253': '86', '105': '253', '205': '105', '412': '205', '15': '412', '179': '15', 'end': '179', 'start': 'start'}
title = "Herodotus, Book 1 (High Frequency Vocabulary)"
section_level =  1
language = "Greek"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)