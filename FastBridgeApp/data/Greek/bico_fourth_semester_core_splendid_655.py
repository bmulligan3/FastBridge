import text
nan=""
section_words = {'start': -1, '1': 653, 'end': -2}
the_text =  [('ΑΓΑΘΟΣ', 0, 'αγαθος', '', '', '1', 1), ('ΑΓΑΠΗ', 1, 'αγαπη', '', '', '1', 1), ('ΑΓΓΕΛΛΩ', 2, 'αγγελλω', '', '', '1', 1), ('ΑΓΓΕΛΟΣ', 3, 'αγγελος', '', '', '1', 1), ('ΑΓΩ', 4, 'αγω', '', '', '1', 1), ('ΑΓΩΝ', 5, 'αγων', '', '', '1', 1), ('ΑΔΕΛΦΟΣ', 6, 'αδελφος', '', '', '1', 1), ('ΑΔΙΚΕΩ', 7, 'αδικεω', '', '', '1', 1), ('ΑΔΙΚΟΣ', 8, 'αδικος', '', '', '1', 1), ('ΑΔΥΝΑΤΟΣ', 9, 'αδυνατος', '', '', '1', 1), ('ΑΕΙ', 10, 'αει', '', '', '1', 1), ('ΑΘΑΝΑΤΟΣ', 11, 'αθανατος', '', '', '1', 1), ('ΑΙΜΑ', 12, 'αιμα', '', '', '1', 1), ('ΑΙΡΕΩ', 13, 'αιρεω', '', '', '1', 1), ('ΑΙΡΩ', 14, 'αιρω', '', '', '1', 1), ('ΑΙΣΘΑΝΟΜΑΙ', 15, 'αισθανομαι', '', '', '1', 1), ('ΑΙΣΧΡΟΣ', 16, 'αισχρος', '', '', '1', 1), ('ΑΙΣΧΥΝΩ', 17, 'αισχυνω', '', '', '1', 1), ('ΑΙΤΕΩ', 18, 'αιτεω', '', '', '1', 1), ('ΑΙΤΙΑ', 19, 'αιτια', '', '', '1', 1), ('ΑΙΤΙΟΣ', 20, 'αιτιος', '', '', '1', 1), ('ΑΚΟΥΩ', 21, 'ακουω', '', '', '1', 1), ('ΑΚΡΙΒΗΣ', 22, 'ακριβης', '', '', '1', 1), ('ΑΛΗΘΕΙΑ', 23, 'αληθεια', '', '', '1', 1), ('ΑΛΗΘΗΣ', 24, 'αληθης', '', '', '1', 1), ('ΑΛΙΣΚΟΜΑΙ', 25, 'αλισκομαι', '', '', '1', 1), ('ΑΛΛΑ', 26, 'αλλα', '', '', '1', 1), ('ΑΛΛΗΛΩΝ', 27, 'αλληλων', '', '', '1', 1), ('ΑΛΛΟΣ', 28, 'αλλος', '', '', '1', 1), ('ΑΛΛΩΣ', 29, 'αλλως', '', '', '1', 1), ('ΑΛΟΓΟΣ', 30, 'αλογος', '', '', '1', 1), ('ΑΜΑ', 31, 'αμα', '', '', '1', 1), ('ΑΜΑΡΤΑΝΩ', 32, 'αμαρτανω', '', '', '1', 1), ('ΑΜΕΙΒΩ', 33, 'αμειβω', '', '', '1', 1), ('ΑΜΕΙΝΩΝ', 34, 'αμεινων', '', '', '1', 1), ('ΑΜΦΙ', 35, 'αμφι', '', '', '1', 1), ('ΑΜΦΟΤΕΡΟΣ', 36, 'αμφοτερος', '', '', '1', 1), ('ΑΝ', 37, 'αν', '', '', '1', 1), ('ΑΝΑ', 38, 'ανα', '', '', '1', 1), ('ΑΝΑΓΚΗ', 39, 'αναγκη', '', '', '1', 1), ('ΑΝΑΘΗΜΑ', 40, 'αναθημα', '', '', '1', 1), ('ΑΝΑΙΡΕΩ', 41, 'αναιρεω', '', '', '1', 1), ('ΑΝΑΞ', 42, 'αναξ', '', '', '1', 1), ('ΑΝΕΥ', 43, 'ανευ', '', '', '1', 1), ('ΑΝΗΡ', 44, 'ανηρ', '', '', '1', 1), ('ΑΝΘΡΩΠΟΣ', 45, 'ανθρωπος', '', '', '1', 1), ('ΑΝΤΙ', 46, 'αντι', '', '', '1', 1), ('ΑΝΩ/2', 47, 'ανυω', '', '', '1', 1), ('ΑΞΙΟΣ', 48, 'αξιος', '', '', '1', 1), ('ΑΞΙΟΩ', 49, 'αξιοω', '', '', '1', 1), ('ΑΠΑΛΛΑΣΣΩ', 50, 'απαλλασσω', '', '', '1', 1), ('ΑΠΑΣ', 51, 'απας', '', '', '1', 1), ('ΑΠΛΩΣ', 52, 'απλως', '', '', '1', 1), ('ΑΠΟ', 53, 'απο', '', '', '1', 1), ('ΑΠΟΔΕΙΚΝΥΜΙ', 54, 'αποδεικνυμι', '', '', '1', 1), ('ΑΠΟΔΙΔΩΜΙ', 55, 'αποδιδωμι', '', '', '1', 1), ('ΑΠΟΘΝΗΙΣΚΩ', 56, 'αποθνῃσκω', '', '', '1', 1), ('ΑΠΟΚΡΙΝΩ', 57, 'αποκρινω', '', '', '1', 1), ('ΑΠΟΚΤΕΙΝΩ', 58, 'αποκτεινω', '', '', '1', 1), ('ΑΠΟΛΛΥΜΙ', 59, 'απολλυμι', '', '', '1', 1), ('ΑΡΑ', 60, 'αρα', '', '', '1', 1), ('ΑΡΑ/2', 61, 'αρα', '', '', '1', 1), ('ΑΡΓΥΡΙΟΝ', 62, 'αργυριον', '', '', '1', 1), ('ΑΡΕΤΗ', 63, 'αρετη', '', '', '1', 1), ('ΑΡΙΘΜΟΣ', 64, 'αριθμος', '', '', '1', 1), ('ΑΡΙΣΤΟΣ', 65, 'αριστος', '', '', '1', 1), ('ΑΡΧΗ', 66, 'αρχη', '', '', '1', 1), ('ΑΡΧΩ', 67, 'αρχω', '', '', '1', 1), ('ΑΡΧΩΝ', 68, 'αρχων', '', '', '1', 1), ('ΑΣΠΙΣ', 69, 'ασπις', '', '', '1', 1), ('ΑΣΤΥ', 70, 'αστυ', '', '', '1', 1), ('ΑΤΕ', 71, 'ατε', '', '', '1', 1), ('ΑΥ', 72, 'αυ', '', '', '1', 1), ('ΑΥΔΑΩ', 73, 'αυδαω', '', '', '1', 1), ('ΑΥΤΑΡ', 74, 'αυταρ', '', '', '1', 1), ('ΑΥΤΕ', 75, 'αυτε', '', '', '1', 1), ('ΑΥΤΙΚΑ', 76, 'αυτικα', '', '', '1', 1), ('ΑΥΤΟΣ', 77, 'αυτος', '', '', '1', 1), ('ΑΥΤΟΥ', 78, 'αυτου', '', '', '1', 1), ('ΑΦΑΙΡΕΩ', 79, 'αφαιρεω', '', '', '1', 1), ('ΑΦΙΗΜΙ', 80, 'αφιημι', '', '', '1', 1), ('ΑΦΙΚΝΕΟΜΑΙ', 81, 'αφικνεομαι', '', '', '1', 1), ('ΑΦΙΣΤΗΜΙ', 82, 'αφιστημι', '', '', '1', 1), ('ΒΑΙΝΩ', 83, 'βαινω', '', '', '1', 1), ('ΒΑΛΛΩ', 84, 'βαλλω', '', '', '1', 1), ('ΒΑΡΒΑΡΟΣ/2', 85, 'βαρβαρος', '', '', '1', 1), ('ΒΑΡΥΣ', 86, 'βαρυς', '', '', '1', 1), ('ΒΑΣΙΛΕΙΟΣ', 87, 'βασιλειος', '', '', '1', 1), ('ΒΑΣΙΛΕΥΣ', 88, 'βασιλευς', '', '', '1', 1), ('ΒΑΣΙΛΕΥΩ', 89, 'βασιλευω', '', '', '1', 1), ('ΒΑΣΙΛΗΙΗ', 90, 'βασιληιη', '', '', '1', 1), ('ΒΕΛΤΙΩΝ', 91, 'βελτιων', '', '', '1', 1), ('ΒΙΒΛΟΣ', 92, 'βιβλος', '', '', '1', 1), ('ΒΙΟΣ', 93, 'βιος', '', '', '1', 1), ('ΒΛΑΠΤΩ', 94, 'βλαπτω', '', '', '1', 1), ('ΒΛΕΠΩ', 95, 'βλεπω', '', '', '1', 1), ('ΒΟΗΘΕΩ', 96, 'βοηθεω', '', '', '1', 1), ('ΒΟΥΚΟΛΟΣ', 97, 'βουκολος', '', '', '1', 1), ('ΒΟΥΛΕΥΩ', 98, 'βουλευω', '', '', '1', 1), ('ΒΟΥΛΗ', 99, 'βουλη', '', '', '1', 1), ('ΒΟΥΛΟΜΑΙ', 100, 'βουλομαι', '', '', '1', 1), ('ΒΟΥΣ', 101, 'βους', '', '', '1', 1), ('ΒΡΑΔΥΣ', 102, 'βραδυς', '', '', '1', 1), ('ΒΡΑΧΥΣ', 103, 'βραχυς', '', '', '1', 1), ('ΓΑΙΑ', 104, 'γαια', '', '', '1', 1), ('ΓΑΡ', 105, 'γαρ', '', '', '1', 1), ('ΓΕ', 106, 'γε', '', '', '1', 1), ('ΓΕΝΟΣ', 107, 'γενος', '', '', '1', 1), ('ΓΕΡΩΝ', 108, 'γερων', '', '', '1', 1), ('ΓΗ', 109, 'γη', '', '', '1', 1), ('ΓΙΓΝΟΜΑΙ', 110, 'γιγνομαι', '', '', '1', 1), ('ΓΙΓΝΩΣΚΩ', 111, 'γιγνωσκω', '', '', '1', 1), ('ΓΛΩΣΣΑ', 112, 'γλωσσα', '', '', '1', 1), ('ΓΝΩΜΗ', 113, 'γνωμη', '', '', '1', 1), ('ΓΡΑΜΜΑ', 114, 'γραμμα', '', '', '1', 1), ('ΓΡΑΦΗ', 115, 'γραφη', '', '', '1', 1), ('ΓΡΑΦΩ', 116, 'γραφω', '', '', '1', 1), ('ΓΥΝΗ', 117, 'γυνη', '', '', '1', 1), ('ΔΑΙΜΩΝ', 118, 'δαιμων', '', '', '1', 1), ('ΔΕ', 119, 'δε', '', '', '1', 1), ('ΔΕΔΟΙΚΑ', 120, 'δεδοικα', '', '', '1', 1), ('ΔΕΙ', 121, 'δει', '', '', '1', 1), ('ΔΕΙΚΝΥΜΙ', 122, 'δεικνυμι', '', '', '1', 1), ('ΔΕΙΝΟΣ', 123, 'δεινος', '', '', '1', 1), ('ΔΕΚΑ', 124, 'δεκα', '', '', '1', 1), ('ΔΕΚΑΤΟΣ', 125, 'δεκατος', '', '', '1', 1), ('ΔΕΣΠΟΤΗΣ', 126, 'δεσποτης', '', '', '1', 1), ('ΔΕΥΤΕΡΟΣ', 127, 'δευτερος', '', '', '1', 1), ('ΔΕΧΟΜΑΙ', 128, 'δεχομαι', '', '', '1', 1), ('ΔΕΩ', 129, 'δεω', '', '', '1', 1), ('ΔΗ', 130, 'δη', '', '', '1', 1), ('ΔΗΛΟΣ', 131, 'δηλος', '', '', '1', 1), ('ΔΗΛΟΩ', 132, 'δηλοω', '', '', '1', 1), ('ΔΗΜΟΣ', 133, 'δημος', '', '', '1', 1), ('ΔΙΑ', 134, 'δια', '', '', '1', 1), ('ΔΙΑΦΕΡΩ', 135, 'διαφερω', '', '', '1', 1), ('ΔΙΑΦΘΕΙΡΩ', 136, 'διαφθειρω', '', '', '1', 1), ('ΔΙΑΦΟΡΑ', 137, 'διαφορα', '', '', '1', 1), ('ΔΙΔΑΣΚΩ', 138, 'διδασκω', '', '', '1', 1), ('ΔΙΔΩΜΙ', 139, 'διδωμι', '', '', '1', 1), ('ΔΙΚΑΙΟΣ', 140, 'δικαιος', '', '', '1', 1), ('ΔΙΚΗ', 141, 'δικη', '', '', '1', 1), ('ΔΙΟΣ', 142, 'διος', '', '', '1', 1), ('ΔΙΩΚΩ', 143, 'διωκω', '', '', '1', 1), ('ΔΟΚΕΙ', 144, 'δοκει', '', '', '1', 1), ('ΔΟΚΕΩ', 145, 'δοκεω', '', '', '1', 1), ('ΔΟΞΑ', 146, 'δοξα', '', '', '1', 1), ('ΔΟΡΥ', 147, 'δορυ', '', '', '1', 1), ('ΔΟΥΛΕΥΩ', 148, 'δουλευω', '', '', '1', 1), ('ΔΟΥΛΟΣ', 149, 'δουλος', '', '', '1', 1), ('ΔΡΑΩ', 150, 'δραω', '', '', '1', 1), ('ΔΥΝΑΜΑΙ', 151, 'δυναμαι', '', '', '1', 1), ('ΔΥΝΑΜΙΣ', 152, 'δυναμις', '', '', '1', 1), ('ΔΥΝΑΤΟΣ', 153, 'δυνατος', '', '', '1', 1), ('ΔΥΟ', 154, 'δυο', '', '', '1', 1), ('ΔΩΜΑ', 155, 'δωμα', '', '', '1', 1), ('ΔΩΡΟΝ', 156, 'δωρον', '', '', '1', 1), ('ΕΑΝ', 157, 'εαν', '', '', '1', 1), ('ΕΑΥΤΟΥ', 158, 'εαυτου', '', '', '1', 1), ('ΕΑΩ', 159, 'εαω', '', '', '1', 1), ('ΕΒΔΟΜΟΣ', 160, 'έβδομος', '', '', '1', 1), ('ΕΓΧΟΣ', 161, 'εγχος', '', '', '1', 1), ('ΕΓΩ', 162, 'εγω', '', '', '1', 1), ('ΕΘΕΛΩ', 163, 'εθελω', '', '', '1', 1), ('ΕΘΝΟΣ', 164, 'εθνος', '', '', '1', 1), ('ΕΙ', 165, 'ει', '', '', '1', 1), ('ΕΙΔΟΝ', 166, 'ειδον', '', '', '1', 1), ('ΕΙΔΟΣ', 167, 'ειδος', '', '', '1', 1), ('ΕΙΚΟΣ', 168, 'εικος', '', '', '1', 1), ('ΕΙΚΟΣΙ', 169, 'εικοσι', '', '', '1', 1), ('ΕΙΚΟΣΤΟΣ', 170, 'εικοστος', '', '', '1', 1), ('ΕΙΜΙ', 171, 'ειμι', '', '', '1', 1), ('ΕΙΜΙ/2', 172, 'ειμι', '', '', '1', 1), ('ΕΙΝΕΚΑ', 173, 'εινεκα', '', '', '1', 1), ('ΕΙΠΟΝ', 174, 'ειπον,', '', '', '1', 1), ('ΕΙΡΗΝΗ', 175, 'ειρηνη', '', '', '1', 1), ('ΕΙΣ', 176, 'εις', '', '', '1', 1), ('ΕΙΣ/2', 177, 'εις', '', '', '1', 1), ('ΕΙΤΑ', 178, 'ειτα', '', '', '1', 1), ('ΕΙΤΕ', 179, 'ειτε', '', '', '1', 1), ('ΕΚ', 180, 'εκ', '', '', '1', 1), ('ΕΚΑΣΤΟΣ', 181, 'εκαστος', '', '', '1', 1), ('ΕΚΑΤΕΡΟΣ', 182, 'εκατερος', '', '', '1', 1), ('ΕΚΑΤΟΝ', 183, 'εκατον', '', '', '1', 1), ('ΕΚΑΤΟΣΤΟΣ', 184, 'εκατοστος', '', '', '1', 1), ('ΕΚΔΙΔΩΜΙ', 185, 'εκδιδωμι', '', '', '1', 1), ('ΕΚΕΙ', 186, 'εκει', '', '', '1', 1), ('ΕΚΕΙΝΟΣ', 187, 'εκεινος', '', '', '1', 1), ('ΕΚΤΟΣ/2', 188, 'έκτος', '', '', '1', 1), ('ΕΛΑΣΣΩΝ', 189, 'ελασσων', '', '', '1', 1), ('ΕΛΑΥΝΩ', 190, 'ελαυνω', '', '', '1', 1), ('ΕΛΕΓΟΣ', 191, 'ελεγος', '', '', '1', 1), ('ΕΛΕΥΘΕΡΟΣ', 192, 'ελευθερος', '', '', '1', 1), ('ΕΛΛΗΝ', 193, 'ελλην', '', '', '1', 1), ('ΕΛΠΙΣ', 194, 'ελπις', '', '', '1', 1), ('ΕΜΑΥΤΟΥ', 195, 'εμαυτου', '', '', '1', 1), ('ΕΜΟΣ', 196, 'εμος', '', '', '1', 1), ('ΕΝ', 197, 'εν', '', '', '1', 1), ('ΕΝΑΝΤΙΟΣ', 198, 'εναντιος', '', '', '1', 1), ('ΕΝΑΤΟΣ', 199, 'ένατος', '', '', '1', 1), ('ΕΝΕΚΑ', 200, 'ενεκα', '', '', '1', 1), ('ΕΝΘΑ', 201, 'ενθα', '', '', '1', 1), ('ΕΝΝΕΑ', 202, 'εννεα', '', '', '1', 1), ('ΕΝΤΑΥΘΑ', 203, 'ενταυθα', '', '', '1', 1), ('ΕΝΤΕΛΛΩ', 204, 'εντελλω', '', '', '1', 1), ('ΕΝΤΕΥΘΕΝ', 205, 'εντευθεν', '', '', '1', 1), ('ΕΞ', 206, 'εξ', '', '', '1', 1), ('ΕΞΕΣΤΙ', 207, 'εξεστι', '', '', '1', 1), ('ΕΞΩ', 208, 'εξω', '', '', '1', 1), ('ΕΟΙΚΑ', 209, 'εοικα', '', '', '1', 1), ('ΕΟΣ', 210, 'εος', '', '', '1', 1), ('ΕΠΕΙ', 211, 'επει', '', '', '1', 1), ('ΕΠΕΙΤΑ', 212, 'επειτα', '', '', '1', 1), ('ΕΠΙ', 213, 'επι', '', '', '1', 1), ('ΕΠΙΔΕΙΚΝΥΜΙ', 214, 'επιδεικνυμι', '', '', '1', 1), ('ΕΠΙΣΤΑΜΑΙ', 215, 'επισταμαι', '', '', '1', 1), ('ΕΠΙΣΤΗΜΗ', 216, 'επιστημη', '', '', '1', 1), ('ΕΠΟΜΑΙ', 217, 'επομαι', '', '', '1', 1), ('ΕΠΟΣ', 218, 'επος', '', '', '1', 1), ('ΕΠΤΑ', 219, 'επτα', '', '', '1', 1), ('ΕΠΩ', 220, 'επω', '', '', '1', 1), ('ΕΡΓΑΖΟΜΑΙ', 221, 'εργαζομαι', '', '', '1', 1), ('ΕΡΓΟΝ', 222, 'εργον', '', '', '1', 1), ('ΕΡΟΜΑΙ', 223, 'ερομαι', '', '', '1', 1), ('ΕΡΧΟΜΑΙ', 224, 'ερχομαι', '', '', '1', 1), ('ΕΡΩ', 225, 'ερω', '', '', '1', 1), ('ΕΡΩΤΑΩ', 226, 'ερωταω', '', '', '1', 1), ('ΕΣΧΑΤΟΣ', 227, 'εσχατος', '', '', '1', 1), ('ΕΤΑΙΡΟΣ', 228, 'εταιρος', '', '', '1', 1), ('ΕΤΕΡΟΣ', 229, 'ετερος', '', '', '1', 1), ('ΕΤΙ', 230, 'ετι', '', '', '1', 1), ('ΕΤΟΣ', 231, 'ετος', '', '', '1', 1), ('ΕΥ', 232, 'ευ', '', '', '1', 1), ('ΕΥΓΕΝΗΣ', 233, 'ευγενης', '', '', '1', 1), ('ΕΥΔΑΙΜΩΝ', 234, 'ευδαιμων', '', '', '1', 1), ('ΕΥΘΥΣ', 235, 'ευθυς', '', '', '1', 1), ('ΕΥΡΙΔΙΗΣ', 236, 'ευριδιης', '', '', '1', 1), ('ΕΥΡΙΣΚΩ', 237, 'ευρισκω', '', '', '1', 1), ('ΕΥΤΥΧΗΣ', 238, 'ευτυχης', '', '', '1', 1), ('ΕΦΙΣΤΗΜΙ', 239, 'εφιστημι', '', '', '1', 1), ('ΕΧΘΡΟΣ/2', 240, 'εχθρος', '', '', '1', 1), ('ΕΧΩ', 241, 'εχω', '', '', '1', 1), ('ΕΩΣ', 242, 'εως', '', '', '1', 1), ('ΖΑΩ', 243, 'ζαω', '', '', '1', 1), ('ΖΕΥΣ', 244, 'Ζευς', '', '', '1', 1), ('ΖΗΤΕΩ', 245, 'ζητεω', '', '', '1', 1), ('ΖΩΙΟΝ', 246, 'ζῳον', '', '', '1', 1), ('Η', 247, 'η', '', '', '1', 1), ('Η/2', 248, 'η', '', '', '1', 1), ('ΗΓΕΜΩΝ', 249, 'ηγεμων', '', '', '1', 1), ('ΗΓΕΟΜΑΙ', 250, 'ηγεομαι', '', '', '1', 1), ('ΗΔΕ', 251, 'ηδε', '', '', '1', 1), ('ΗΔΗ', 252, 'ηδη', '', '', '1', 1), ('ΗΔΟΝΗ', 253, 'ηδονη', '', '', '1', 1), ('ΗΔΥΣ', 254, 'ηδυς', '', '', '1', 1), ('ΗΚΩ', 255, 'ηκω', '', '', '1', 1), ('ΗΛΙΟΣ', 256, 'ηλιος', '', '', '1', 1), ('ΗΜΕΙΣ', 257, 'ημεις', '', '', '1', 1), ('ΗΜΕΡΑ', 258, 'ημερα', '', '', '1', 1), ('ΗΜΕΤΕΡΟΣ', 259, 'ημετερος', '', '', '1', 1), ('ΗΣΣΩΝ', 260, 'ησσων', '', '', '1', 1), ('ΘΑΛΑΣΣΑ', 261, 'θαλασσα', '', '', '1', 1), ('ΘΑΝΑΤΟΣ', 262, 'θανατος', '', '', '1', 1), ('ΘΑΠΤΩ', 263, 'θαπτω', '', '', '1', 1), ('ΘΑΥΜΑΖΩ', 264, 'θαυμαζω', '', '', '1', 1), ('ΘΕΑ', 265, 'θεα', '', '', '1', 1), ('ΘΕΑΟΜΑΙ', 266, 'θεαομαι', '', '', '1', 1), ('ΘΕΑΤΡΟΝ', 267, 'θεατρον', '', '', '1', 1), ('ΘΕΙΟΣ', 268, 'θειος', '', '', '1', 1), ('ΘΕΟΣ', 269, 'θεος', '', '', '1', 1), ('ΘΝΗΣΚΩ', 270, 'θνησκω', '', '', '1', 1), ('ΘΥΓΑΤΗΡ', 271, 'θυγατηρ', '', '', '1', 1), ('ΘΥΜΟΣ', 272, 'θυμος', '', '', '1', 1), ('ΘΥΩ', 273, 'θυω', '', '', '1', 1), ('ΙΑΤΡΟΣ', 274, 'ιατρος', '', '', '1', 1), ('ΙΔΙΟΣ', 275, 'ιδιος', '', '', '1', 1), ('ΙΕΡΕΥΣ', 276, 'ιερευς', '', '', '1', 1), ('ΙΕΡΟΣ', 277, 'ιερος', '', '', '1', 1), ('ΙΗΜΙ', 278, 'ιημι', '', '', '1', 1), ('ΙΚΑΝΟΣ', 279, 'ικανος', '', '', '1', 1), ('ΙΚΝΕΟΜΑΙ', 280, 'ικνεομαι', '', '', '1', 1), ('ΙΝΑ', 281, 'ινα', '', '', '1', 1), ('ΙΠΠΕΥΣ', 282, 'ιππευς', '', '', '1', 1), ('ΙΠΠΟΣ', 283, 'ιππος', '', '', '1', 1), ('ΙΣΟΣ', 284, 'ισος', '', '', '1', 1), ('ΙΣΤΗΜΙ', 285, 'ιστημι', '', '', '1', 1), ('ΙΣΧΥΡΟΣ', 286, 'ισχυρος', '', '', '1', 1), ('ΙΣΩΣ', 287, 'ίσως', '', '', '1', 1), ('ΚΑΘΙΣΤΗΜΙ', 288, 'καθιστημι', '', '', '1', 1), ('ΚΑΙ', 289, 'και', '', '', '1', 1), ('ΚΑΙΠΕΡ', 290, 'καιπερ', '', '', '1', 1), ('ΚΑΙΡΟΣ', 291, 'καιρος', '', '', '1', 1), ('ΚΑΙΤΟΙ', 292, 'καιτοι', '', '', '1', 1), ('ΚΑΚΟΣ', 293, 'κακος', '', '', '1', 1), ('ΚΑΛΕΩ', 294, 'καλεω', '', '', '1', 1), ('ΚΑΛΛΟΣ', 295, 'καλλος', '', '', '1', 1), ('ΚΑΛΟΣ', 296, 'καλος', '', '', '1', 1), ('ΚΑΝ', 297, 'καν', '', '', '1', 1), ('ΚΑΡΤΑ', 298, 'καρτα', '', '', '1', 1), ('ΚΑΤΑ', 299, 'κατα', '', '', '1', 1), ('ΚΑΤΑΛΑΜΒΑΝΩ', 300, 'καταλαμβανω', '', '', '1', 1), ('ΚΑΤΑΣΚΕΥΑΖΩ', 301, 'κατασκευαζω', '', '', '1', 1), ('ΚΑΤΑΣΤΡΕΦΩ', 302, 'καταστρεφω', '', '', '1', 1), ('ΚΑΤΗΓΟΡΕΩ', 303, 'κατηγορεω', '', '', '1', 1), ('ΚΑΤΙΣΤΗΜΙ', 304, 'κατίστημι', '', '', '1', 1), ('ΚΕ', 305, 'κε', '', '', '1', 1), ('ΚΕΙΜΑΙ', 306, 'κειμαι', '', '', '1', 1), ('ΚΕΛΕΥΩ', 307, 'κελευω', '', '', '1', 1), ('ΚΕΡΔΟΣ', 308, 'κερδος', '', '', '1', 1), ('ΚΕΦΑΛΗ', 309, 'κεφαλη', '', '', '1', 1), ('ΚΗΡΥΞ', 310, 'κηρυξ', '', '', '1', 1), ('ΚΙΝΔΥΝΟΣ', 311, 'κινδυνος', '', '', '1', 1), ('ΚΙΝΕΩ', 312, 'κινεω', '', '', '1', 1), ('ΚΛΕΠΤΩ', 313, 'κλεπτω', '', '', '1', 1), ('ΚΟΙΝΟΣ', 314, 'κοινος', '', '', '1', 1), ('ΚΟΜΙΖΩ', 315, 'κομιζω', '', '', '1', 1), ('ΚΟΣΜΟΣ', 316, 'κοσμος', '', '', '1', 1), ('ΚΡΑΤΕΩ', 317, 'κρατεω', '', '', '1', 1), ('ΚΡΑΤΟΣ', 318, 'κρατος', '', '', '1', 1), ('ΚΡΕΙΣΣΩΝ', 319, 'κρεισσων', '', '', '1', 1), ('ΚΡΙΝΩ', 320, 'κρινω', '', '', '1', 1), ('ΚΤΑΟΜΑΙ', 321, 'κταομαι', '', '', '1', 1), ('ΚΤΕΙΝΩ', 322, 'κτεινω', '', '', '1', 1), ('ΚΥΚΛΟΣ', 323, 'κυκλος', '', '', '1', 1), ('ΚΥΡΙΟΣ', 324, 'κυριος', '', '', '1', 1), ('ΚΩΛΥΩ', 325, 'κωλυω', '', '', '1', 1), ('ΛΑΛΕΩ', 326, 'λαλεω', '', '', '1', 1), ('ΛΑΜΒΑΝΩ', 327, 'λαμβανω', '', '', '1', 1), ('ΛΑΜΠΡΟΣ', 328, 'λαμπρος', '', '', '1', 1), ('ΛΑΝΘΑΝΩ', 329, 'λανθανω', '', '', '1', 1), ('ΛΑΟΣ/2', 330, 'λαος', '', '', '1', 1), ('ΛΕΓΩ', 331, 'λεγω', '', '', '1', 1), ('ΛΕΙΠΩ', 332, 'λειπω', '', '', '1', 1), ('ΛΙΘΟΣ', 333, 'λιθος', '', '', '1', 1), ('ΛΟΓΟΣ', 334, 'λογος', '', '', '1', 1), ('ΛΟΙΠΟΣ', 335, 'λοιπος', '', '', '1', 1), ('ΛΥΩ', 336, 'λυω', '', '', '1', 1), ('ΜΑΘΗΤΗΣ', 337, 'μαθητης', '', '', '1', 1), ('ΜΑΚΡΟΣ', 338, 'μακρος', '', '', '1', 1), ('ΜΑΛΑ', 339, 'μαλα', '', '', '1', 1), ('ΜΑΛΙΣΤΑ', 340, 'μαλιστα', '', '', '1', 1), ('ΜΑΛΛΟΝ', 341, 'μαλλον', '', '', '1', 1), ('ΜΑΝΘΑΝΩ', 342, 'μανθανω', '', '', '1', 1), ('ΜΑΡΤΥΣ', 343, 'μαρτυς', '', '', '1', 1), ('ΜΑΧΗ', 344, 'μαχη', '', '', '1', 1), ('ΜΑΧΟΜΑΙ', 345, 'μαχομαι', '', '', '1', 1), ('ΜΕΓΑΡΟΝ', 346, 'μεγαρον', '', '', '1', 1), ('ΜΕΓΑΣ', 347, 'μεγας', '', '', '1', 1), ('ΜΕΓΕΘΟΣ', 348, 'μεγεθος', '', '', '1', 1), ('ΜΕΙΓΝΥΜΙ', 349, 'μιγνυμι', '', '', '1', 1), ('ΜΕΛΛΩ', 350, 'μελλω', '', '', '1', 1), ('ΜΕΝ', 351, 'μεν', '', '', '1', 1), ('ΜΕΝ-ΔΕ', 352, 'μεν...δε', '', '', '1', 1), ('ΜΕΝΤΟΙ', 353, 'μεντοι', '', '', '1', 1), ('ΜΕΝΩ', 354, 'μενω', '', '', '1', 1), ('ΜΕΡΟΣ', 355, 'μερος', '', '', '1', 1), ('ΜΕΣΟΣ', 356, 'μεσος', '', '', '1', 1), ('ΜΕΤΑ', 357, 'μετα', '', '', '1', 1), ('ΜΕΤΑΞΥ', 358, 'μεταξυ', '', '', '1', 1), ('ΜΕΧΡΙ', 359, 'μεχρι', '', '', '1', 1), ('ΜΗ', 360, 'μη', '', '', '1', 1), ('ΜΗΔΕ', 361, 'μηδε', '', '', '1', 1), ('ΜΗΔΕΙΣ', 362, 'μηδεις', '', '', '1', 1), ('ΜΗΝ/2', 363, 'μην', '', '', '1', 1), ('ΜΗΤΕ', 364, 'μητε...μητε', '', '', '1', 1), ('ΜΗΤΗΡ', 365, 'μητηρ', '', '', '1', 1), ('ΜΙΓΝΥΜΙ', 366, 'μιγνυμι', '', '', '1', 1), ('ΜΙΚΡΟΣ', 367, 'μικρος', '', '', '1', 1), ('ΜΙΜΝΗΣΚΩ', 368, 'μιμνησκω', '', '', '1', 1), ('ΜΙΝ', 369, 'μιν', '', '', '1', 1), ('ΜΝΗΣΤΗΡ', 370, 'μνηστηρ', '', '', '1', 1), ('ΜΟΙΡΑ', 371, 'μοιρα', '', '', '1', 1), ('ΜΟΝΟΝ', 372, 'μονον', '', '', '1', 1), ('ΜΟΝΟΣ', 373, 'μονος', '', '', '1', 1), ('ΜΟΥΣΑ', 374, 'Μουσα', '', '', '1', 1), ('ΜΥΘΟΣ', 375, 'μυθος', '', '', '1', 1), ('ΜΥΡΙΟΙ', 376, 'μυριοι', '', '', '1', 1), ('ΜΥΡΙΟΣ', 377, 'μυριος', '', '', '1', 1), ('ΝΑΙ', 378, 'ναι', '', '', '1', 1), ('ΝΑΟΣ', 379, 'ναος', '', '', '1', 1), ('ΝΑΥΣ', 380, 'ναυς', '', '', '1', 1), ('ΝΕΑΝΙΑΣ', 381, 'νεανιας', '', '', '1', 1), ('ΝΕΟΣ', 382, 'νεος', '', '', '1', 1), ('ΝΗΣΟΣ', 383, 'νησος', '', '', '1', 1), ('ΝΙΚΑΩ', 384, 'νικαω', '', '', '1', 1), ('ΝΙΚΗ', 385, 'νικη', '', '', '1', 1), ('ΝΟΜΙΖΩ', 386, 'νομιζω', '', '', '1', 1), ('ΝΟΜΟΣ', 387, 'νομος', '', '', '1', 1), ('ΝΟΣΟΣ', 388, 'νοσος', '', '', '1', 1), ('ΝΟΥΣ', 389, 'νους', '', '', '1', 1), ('ΝΥΝ', 390, 'νυν', '', '', '1', 1), ('ΝΥΞ', 391, 'νυξ', '', '', '1', 1), ('ΞΕΝΟΣ', 392, 'ξενος', '', '', '1', 1), ('Ο', 393, 'ο', '', '', '1', 1), ('ΟΓΔΟΟΣ', 394, 'όγδοος', '', '', '1', 1), ('ΟΔΕ', 395, 'οδε', '', '', '1', 1), ('ΟΔΟΣ', 396, 'οδος', '', '', '1', 1), ('ΟΘΕΝ', 397, 'οθεν', '', '', '1', 1), ('ΟΘΙ', 398, 'οθι', '', '', '1', 1), ('ΟΙ', 399, 'οι', '', '', '1', 1), ('ΟΙΔΑ', 400, 'οιδα', '', '', '1', 1), ('ΟΙΚΕΙΟΣ', 401, 'οικειος', '', '', '1', 1), ('ΟΙΚΕΩ', 402, 'οικεω', '', '', '1', 1), ('ΟΙΚΙΑ', 403, 'οικια', '', '', '1', 1), ('ΟΙΚΟΣ', 404, 'οικος', '', '', '1', 1), ('ΟΙΝΟΣ', 405, 'οινος', '', '', '1', 1), ('ΟΙΟΜΑΙ', 406, 'οιομαι', '', '', '1', 1), ('ΟΙΟΣ', 407, 'οιος', '', '', '1', 1), ('ΟΙΟΣ/2', 408, 'οιος', '', '', '1', 1), ('ΟΚΤΩ', 409, 'οκτω', '', '', '1', 1), ('ΟΚΩΣ', 410, 'οκως', '', '', '1', 1), ('ΟΛΙΓΟΣ', 411, 'ολιγος', '', '', '1', 1), ('ΟΛΛΥΜΙ', 412, 'ολλυμι', '', '', '1', 1), ('ΟΛΟΣ', 413, 'ολος', '', '', '1', 1), ('ΟΛΩΣ', 414, 'ολως', '', '', '1', 1), ('ΟΜΟΙΟΣ', 415, 'ομοιος', '', '', '1', 1), ('ΟΜΟΛΟΓΕΩ', 416, 'ομολογεω', '', '', '1', 1), ('ΟΜΩΣ', 417, 'ομως', '', '', '1', 1), ('ΟΝΟΜΑ', 418, 'ονομα', '', '', '1', 1), ('ΟΝΟΜΑΖΩ', 419, 'ονομαζω', '', '', '1', 1), ('ΟΞΥΣ', 420, 'οξυς', '', '', '1', 1), ('ΟΠΛΟΝ', 421, 'οπλον', '', '', '1', 1), ('ΟΠΟΥ', 422, 'οπου', '', '', '1', 1), ('ΟΠΩΣ', 423, 'οπως', '', '', '1', 1), ('ΟΡΑΩ', 424, 'οραω', '', '', '1', 1), ('ΟΡΘΟΣ', 425, 'ορθος', '', '', '1', 1), ('ΟΡΜΑΩ', 426, 'ορμαω', '', '', '1', 1), ('ΟΡΝΥΜΙ', 427, 'ορνυμι', '', '', '1', 1), ('ΟΡΟΣ', 428, 'ορος', '', '', '1', 1), ('ΟΡΥΣΣΩ', 429, 'ορυσσω', '', '', '1', 1), ('ΟΣ', 430, 'ος', '', '', '1', 1), ('ΟΣΟΣ', 431, 'οσος', '', '', '1', 1), ('ΟΣΠΕΡ', 432, 'οσπερ', '', '', '1', 1), ('ΟΣΤΕ', 433, 'οστε', '', '', '1', 1), ('ΟΣΤΙΣ', 434, 'οστις', '', '', '1', 1), ('ΟΤΑΝ', 435, 'οταν', '', '', '1', 1), ('ΟΤΕ', 436, 'οτε', '', '', '1', 1), ('ΟΤΙ', 437, 'οτι', '', '', '1', 1), ('ΟΥ', 438, 'ουκ', '', '', '1', 1), ('ΟΥ/2', 439, 'ου', '', '', '1', 1), ('ΟΥΔΕ', 440, 'ουδε', '', '', '1', 1), ('ΟΥΔΕΙΣ', 441, 'ουδεις', '', '', '1', 1), ('ΟΥΚΕΤΙ', 442, 'ουκετι', '', '', '1', 1), ('ΟΥΚΟΥΝ', 443, 'ουκουν', '', '', '1', 1), ('ΟΥΚΟΥΝ/2', 444, 'ουκουν', '', '', '1', 1), ('ΟΥΝ', 445, 'ουν', '', '', '1', 1), ('ΟΥΠΟΤΕ', 446, 'ουποτε', '', '', '1', 1), ('ΟΥΡΑΝΟΣ', 447, 'ουρανος', '', '', '1', 1), ('ΟΥΣΙΑ', 448, 'ουσια', '', '', '1', 1), ('ΟΥΤΕ', 449, 'ουτε...ουτε', '', '', '1', 1), ('ΟΥΤΟΣ', 450, 'ουτος', '', '', '1', 1), ('ΟΥΤΩΣ', 451, 'ουτως', '', '', '1', 1), ('ΟΦΘΑΛΜΟΣ', 452, 'οφθαλμος', '', '', '1', 1), ('ΟΦΡΑ', 453, 'οφρα', '', '', '1', 1), ('ΠΑΘΟΣ', 454, 'παθος', '', '', '1', 1), ('ΠΑΙΔΕΥΩ', 455, 'παιδευω', '', '', '1', 1), ('ΠΑΙΣ', 456, 'παις', '', '', '1', 1), ('ΠΑΛΑΙΟΣ', 457, 'παλαιος', '', '', '1', 1), ('ΠΑΛΙΝ', 458, 'παλιν', '', '', '1', 1), ('ΠΑΝΤΩΣ', 459, 'παντως', '', '', '1', 1), ('ΠΑΝΥ', 460, 'πανυ', '', '', '1', 1), ('ΠΑΡΑ', 461, 'παρα', '', '', '1', 1), ('ΠΑΡΑΔΙΔΩΜΙ', 462, 'παραδιδωμι', '', '', '1', 1), ('ΠΑΡΑΣΚΕΥΑΖΩ', 463, 'παρασκευαζω', '', '', '1', 1), ('ΠΑΡΕΙΜΙ', 464, 'παρειμι', '', '', '1', 1), ('ΠΑΡΕΧΩ', 465, 'παρεχω', '', '', '1', 1), ('ΠΑΣ', 466, 'πας', '', '', '1', 1), ('ΠΑΣΧΩ', 467, 'πασχω', '', '', '1', 1), ('ΠΑΤΗΡ', 468, 'πατηρ', '', '', '1', 1), ('ΠΑΤΡΙΣ', 469, 'πατρις', '', '', '1', 1), ('ΠΑΥΩ', 470, 'παυω', '', '', '1', 1), ('ΠΕΙΘΩ', 471, 'πειθω', '', '', '1', 1), ('ΠΕΙΡΑ', 472, 'πειρα', '', '', '1', 1), ('ΠΕΙΡΑΩ', 473, 'πειραω', '', '', '1', 1), ('ΠΕΜΠΤΟΣ', 474, 'πεμπτος', '', '', '1', 1), ('ΠΕΜΠΩ', 475, 'πεμπω', '', '', '1', 1), ('ΠΕΝΤΕ', 476, 'πεντε', '', '', '1', 1), ('ΠΕΡ', 477, 'περ', '', '', '1', 1), ('ΠΕΡΙ', 478, 'περι', '', '', '1', 1), ('ΠΙΝΩ', 479, 'πινω', '', '', '1', 1), ('ΠΙΠΤΩ', 480, 'πιπτω', '', '', '1', 1), ('ΠΙΣΤΕΥΩ', 481, 'πιστευω', '', '', '1', 1), ('ΠΙΣΤΙΣ', 482, 'πιστις', '', '', '1', 1), ('ΠΛΕΙΣΤΟΣ', 483, 'πλειστος', '', '', '1', 1), ('ΠΛΕΙΩΝ', 484, 'πλεων', '', '', '1', 1), ('ΠΛΕΟΝ', 485, 'πλεον', '', '', '1', 1), ('ΠΛΕΩ', 486, 'πλεω', '', '', '1', 1), ('ΠΛΗΘΟΣ', 487, 'πληθος', '', '', '1', 1), ('ΠΛΗΝ', 488, 'πλην', '', '', '1', 1), ('ΠΝΕΥΜΑ', 489, 'πνευμα', '', '', '1', 1), ('ΠΟΙΕΩ', 490, 'ποιεω', '', '', '1', 1), ('ΠΟΙΗΤΗΣ', 491, 'ποιητης', '', '', '1', 1), ('ΠΟΙΟΣ', 492, 'ποιος', '', '', '1', 1), ('ΠΟΙΟΣ/2', 493, 'ποιος', '', '', '1', 1), ('ΠΟΛΕΜΕΩ', 494, 'πολεμεω', '', '', '1', 1), ('ΠΟΛΕΜΙΟΣ', 495, 'πολεμιος', '', '', '1', 1), ('ΠΟΛΕΜΟΣ', 496, 'πολεμος', '', '', '1', 1), ('ΠΟΛΙΣ', 497, 'πολις', '', '', '1', 1), ('ΠΟΛΙΤΕΙΑ', 498, 'πολιτεια', '', '', '1', 1), ('ΠΟΛΙΤΗΣ', 499, 'πολιτης', '', '', '1', 1), ('ΠΟΛΛΑΚΙΣ', 500, 'πολλακις', '', '', '1', 1), ('ΠΟΛΥΣ', 501, 'πολυς', '', '', '1', 1), ('ΠΟΝΗΡΟΣ', 502, 'πονηρος', '', '', '1', 1), ('ΠΟΝΟΣ', 503, 'πονος', '', '', '1', 1), ('ΠΟΡΕΥΩ', 504, 'πορευω', '', '', '1', 1), ('ΠΟΤΑΜΟΣ', 505, 'ποταμος', '', '', '1', 1), ('ΠΟΤΕ', 506, 'ποτε', '', '', '1', 1), ('ΠΟΤΕ/2', 507, 'ποτε', '', '', '1', 1), ('ΠΟΤΕΡΟΣ', 508, 'ποτερος', '', '', '1', 1), ('ΠΟΥ', 509, 'που', '', '', '1', 1), ('ΠΟΥ/2', 510, 'που', '', '', '1', 1), ('ΠΟΥΣ', 511, 'πους', '', '', '1', 1), ('ΠΡΑΓΜΑ', 512, 'πραγμα', '', '', '1', 1), ('ΠΡΑΞΙΣ', 513, 'πραξις', '', '', '1', 1), ('ΠΡΑΣΣΩ', 514, 'πρασσω', '', '', '1', 1), ('ΠΡΕΣΒΥΣ', 515, 'πρεσβυς', '', '', '1', 1), ('ΠΡΙΝ', 516, 'πριν', '', '', '1', 1), ('ΠΡΟ', 517, 'προ', '', '', '1', 1), ('ΠΡΟΔΙΔΩΜΙ', 518, 'προδιδωμι', '', '', '1', 1), ('ΠΡΟΣ', 519, 'προς', '', '', '1', 1), ('ΠΡΟΣΗΚΩ', 520, 'προσηκω', '', '', '1', 1), ('ΠΡΟΣΤΙΘΗΜΙ', 521, 'προστιθημι', '', '', '1', 1), ('ΠΡΟΣΩΠΟΝ', 522, 'προσωπον', '', '', '1', 1), ('ΠΡΟΤΕΡΟΣ', 523, 'προτερος', '', '', '1', 1), ('ΠΡΩΤΟΣ', 524, 'πρωτος', '', '', '1', 1), ('ΠΥΝΘΑΝΟΜΑΙ', 525, 'πυνθανομαι', '', '', '1', 1), ('ΠΥΡ', 526, 'πυρ', '', '', '1', 1), ('ΠΩΣ', 527, 'πως', '', '', '1', 1), ('ΠΩΣ/2', 528, 'πως', '', '', '1', 1), ('ΡΑΙΔΙΟΣ', 529, 'ῥᾳδιος', '', '', '1', 1), ('ΡΕΩ', 530, 'ῥεω', '', '', '1', 1), ('ΡΗΤΩΡ', 531, 'ῥητωρ', '', '', '1', 1), ('ΣΑΦΗΣ', 532, 'σαφης', '', '', '1', 1), ('ΣΕΑΥΤΟΥ', 533, 'σαυτου', '', '', '1', 1), ('ΣΗΜΑΙΝΩ', 534, 'σημαινω', '', '', '1', 1), ('ΣΚΟΠΕΩ', 535, 'σκοπεω', '', '', '1', 1), ('ΣΟΣ', 536, 'σος', '', '', '1', 1), ('ΣΟΦΟΣ', 537, 'σοφος', '', '', '1', 1), ('ΣΤΑΔΙΟΝ', 538, 'σταδιον', '', '', '1', 1), ('ΣΤΑΡΤΙΩΤΗΣ', 539, 'στρατιωτης', '', '', '1', 1), ('ΣΤΟΜΑ', 540, 'στομα', '', '', '1', 1), ('ΣΤΡΑΤΕΥΩ', 541, 'στρατευω', '', '', '1', 1), ('ΣΤΡΑΤΗΓΟΣ', 542, 'στρατηγος', '', '', '1', 1), ('ΣΤΡΑΤΙΑ', 543, 'στρατια', '', '', '1', 1), ('ΣΤΡΑΤΙΩΤΗΣ', 544, 'στρατιωτης', '', '', '1', 1), ('ΣΤΡΑΤΟΣ', 545, 'στρατος', '', '', '1', 1), ('ΣΥ', 546, 'συ', '', '', '1', 1), ('ΣΥΜΒΑΙΝΩ', 547, 'συμβαινω', '', '', '1', 1), ('ΣΥΜΜΑΧΟΣ/2', 548, 'συμμαχος', '', '', '1', 1), ('ΣΥΜΦΕΡΩ', 549, 'συμφερω', '', '', '1', 1), ('ΣΥΜΦΟΡΑ', 550, 'συμφορα', '', '', '1', 1), ('ΣΥΝ', 551, 'συν', '', '', '1', 1), ('ΣΦΕΙΣ', 552, 'σφεις', '', '', '1', 1), ('ΣΧΗΜΑ', 553, 'σχημα', '', '', '1', 1), ('ΣΩΖΩ', 554, 'σωζω', '', '', '1', 1), ('ΣΩΜΑ', 555, 'σωμα', '', '', '1', 1), ('ΣΩΤΗΡΙΑ', 556, 'σωτηρια', '', '', '1', 1), ('ΣΩΦΡΩΝ', 557, 'σωφρων', '', '', '1', 1), ('ΤΑΞΙΣ', 558, 'ταξις', '', '', '1', 1), ('ΤΑΣΣΩ', 559, 'τασσω', '', '', '1', 1), ('ΤΑΧΙΣΤΟΣ', 560, 'ταχιστος', '', '', '1', 1), ('ΤΑΧΥΣ', 561, 'ταχυς', '', '', '1', 1), ('ΤΕ', 562, 'τε', '', '', '1', 1), ('ΤΕΙΧΟΣ', 563, 'τειχος', '', '', '1', 1), ('ΤΕΚΝΟΝ', 564, 'τεκνον', '', '', '1', 1), ('ΤΕΛΕΥΤΑΩ', 565, 'τελευταω', '', '', '1', 1), ('ΤΕΛΟΣ', 566, 'τελος', '', '', '1', 1), ('ΤΕΜΝΩ', 567, 'τεμνω', '', '', '1', 1), ('ΤΕΣΣΑΡΕΣ', 568, 'τεσσαρες', '', '', '1', 1), ('ΤΕΤΑΡΤΟΣ', 569, 'τεταρτος', '', '', '1', 1), ('ΤΕΧΝΗ', 570, 'τεχνη', '', '', '1', 1), ('ΤΙΘΗΜΙ', 571, 'τιθημι', '', '', '1', 1), ('ΤΙΚΤΩ', 572, 'τικτω', '', '', '1', 1), ('ΤΙΜΑΩ', 573, 'τιμαω', '', '', '1', 1), ('ΤΙΜΗ', 574, 'τιμη', '', '', '1', 1), ('ΤΙΣ', 575, 'τις', '', '', '1', 1), ('ΤΙΣ/2', 576, 'τις', '', '', '1', 1), ('ΤΟΙΝΥΝ', 577, 'τοινυν', '', '', '1', 1), ('ΤΟΙΟΣΔΕ', 578, 'τοιοσδε', '', '', '1', 1), ('ΤΟΙΟΥΤΟΣ', 579, 'τοιουτος', '', '', '1', 1), ('ΤΟΛΜΑΩ', 580, 'τολμαω', '', '', '1', 1), ('ΤΟΠΟΣ', 581, 'τοπος', '', '', '1', 1), ('ΤΟΣΟΥΤΟΣ', 582, 'τοσουτος', '', '', '1', 1), ('ΤΟΤΕ', 583, 'τοτε', '', '', '1', 1), ('ΤΡΕΙΣ', 584, 'τρεις', '', '', '1', 1), ('ΤΡΕΠΩ', 585, 'τρεπω', '', '', '1', 1), ('ΤΡΕΦΩ', 586, 'τρεφω', '', '', '1', 1), ('ΤΡΙΑΚΟΝΤΑ', 587, 'τριακοντα', '', '', '1', 1), ('ΤΡΙΑΚΟΣΤΟΣ', 588, 'τριακοστος', '', '', '1', 1), ('ΤΡΙΤΟΣ', 589, 'τριτος', '', '', '1', 1), ('ΤΡΟΠΟΣ', 590, 'τροπος', '', '', '1', 1), ('ΤΡΟΦΗ', 591, 'τροφη', '', '', '1', 1), ('ΤΥΓΧΑΝΩ', 592, 'τυγχανω', '', '', '1', 1), ('ΤΥΧΗ', 593, 'τυχη', '', '', '1', 1), ('ΥΒΡΙΣ', 594, 'υβρις', '', '', '1', 1), ('ΥΔΩΡ', 595, 'υδωρ', '', '', '1', 1), ('ΥΙΟΣ', 596, 'υιος', '', '', '1', 1), ('ΥΜΕΙΣ', 597, 'υμεις', '', '', '1', 1), ('ΥΜΕΤΕΡΟΣ', 598, 'υμετερος', '', '', '1', 1), ('ΥΠΑΡΧΩ', 599, 'υπαρχω', '', '', '1', 1), ('ΥΠΕΡ', 600, 'υπερ', '', '', '1', 1), ('ΥΠΟ', 601, 'υπο', '', '', '1', 1), ('ΥΠΟΛΑΜΒΑΝΩ', 602, 'υπολαμβανω', '', '', '1', 1), ('ΥΣΤΕΡΟΣ', 603, 'υστερος', '', '', '1', 1), ('ΦΑΙΝΩ', 604, 'φαινω', '', '', '1', 1), ('ΦΑΝΕΡΟΣ', 605, 'φανερος', '', '', '1', 1), ('ΦΕΡΩ', 606, 'φερω', '', '', '1', 1), ('ΦΕΥΓΩ', 607, 'φευγω', '', '', '1', 1), ('ΦΗΜΙ', 608, 'φημι', '', '', '1', 1), ('ΦΘΑΝΩ', 609, 'φθανω', '', '', '1', 1), ('ΦΙΛΕΩ', 610, 'φιλεω', '', '', '1', 1), ('ΦΙΛΙΑ', 611, 'φιλια', '', '', '1', 1), ('ΦΙΛΙΟΣ', 612, 'φιλιος', '', '', '1', 1), ('ΦΙΛΟΣ', 613, 'φιλος', '', '', '1', 1), ('ΦΙΛΟΣ/2', 614, 'φιλος', '', '', '1', 1), ('ΦΟΒΕΩ', 615, 'φοβεω', '', '', '1', 1), ('ΦΟΒΟΣ', 616, 'φοβος', '', '', '1', 1), ('ΦΡΑΖΩ', 617, 'φραζω', '', '', '1', 1), ('ΦΡΗΝ', 618, 'φρην', '', '', '1', 1), ('ΦΡΟΝΕΩ', 619, 'φρονεω', '', '', '1', 1), ('ΦΥΛΑΞ', 620, 'φυλαξ', '', '', '1', 1), ('ΦΥΛΑΣΣΩ', 621, 'φυλασσω', '', '', '1', 1), ('ΦΥΣΙΣ', 622, 'φυσις', '', '', '1', 1), ('ΦΥΩ', 623, 'φυω', '', '', '1', 1), ('ΦΩΝΕΩ', 624, 'φωνεω', '', '', '1', 1), ('ΦΩΝΗ', 625, 'φωνη', '', '', '1', 1), ('ΦΩΣ', 626, 'φως', '', '', '1', 1), ('ΧΑΙΡΩ', 627, 'χαιρω', '', '', '1', 1), ('ΧΑΛΕΠΟΣ', 628, 'χαλεπος', '', '', '1', 1), ('ΧΑΛΚΟΣ', 629, 'χαλκος', '', '', '1', 1), ('ΧΑΛΚΟΥΣ', 630, 'χαλκους', '', '', '1', 1), ('ΧΑΡΙΣ', 631, 'χαρις', '', '', '1', 1), ('ΧΕΙΡ', 632, 'χειρ', '', '', '1', 1), ('ΧΕΙΡΩΝ', 633, 'χειρων', '', '', '1', 1), ('ΧΕΩ', 634, 'χεω', '', '', '1', 1), ('ΧΡΑΟΜΑΙ', 635, 'χραομαι', '', '', '1', 1), ('ΧΡΗ', 636, 'χρη', '', '', '1', 1), ('ΧΡΗΜΑ', 637, 'χρημα', '', '', '1', 1), ('ΧΡΗΣΙΜΟΣ', 638, 'χρησιμος', '', '', '1', 1), ('ΧΡΗΣΤΗΡΙΟΝ', 639, 'χρηστηριον', '', '', '1', 1), ('ΧΡΟΝΟΣ', 640, 'χρονος', '', '', '1', 1), ('ΧΡΥΣΕΟΣ', 641, 'χρυσεος', '', '', '1', 1), ('ΧΡΥΣΟΣ', 642, 'χρυσος', '', '', '1', 1), ('ΧΩΡΑ', 643, 'χωρᾱ', '', '', '1', 1), ('ΧΩΡΕΩ', 644, 'χωρεω', '', '', '1', 1), ('ΧΩΡΙΟΝ', 645, 'χωριον', '', '', '1', 1), ('ΧΩΡΙΣ', 646, 'χωρις', '', '', '1', 1), ('ΨΕΥΔΗΣ', 647, 'ψευδης', '', '', '1', 1), ('ΨΥΧΗ', 648, 'ψυχη', '', '', '1', 1), ('Ω', 649, 'ω', '', '', '1', 1), ('ΩΔΕ', 650, 'ωδε', '', '', '1', 1), ('ΩΣ', 651, 'ως', '', '', '1', 1), ('ΩΣΠΕΡ', 652, 'ωσπερ', '', '', '1', 1), ('ΩΣΤΕ', 653, 'ωστε', '', '', '1', 1)]
section_list ={'1': 'start', 'end': '1', 'start': 'start'}
title = "BiCo Fourth Semester Core: Splendid 655"
section_level =  1
language = "Greek"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)