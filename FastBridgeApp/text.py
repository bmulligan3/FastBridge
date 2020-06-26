class Text(object):
    """A Text object. It really could just be a struct."""

    def __init__(self, name : str, sections : dict, words : list, section_linkedlist : dict, subsections : int, language : str):
        self.name = name
        self.sections = sections
        self.words =  words
        self.section_linkedlist = section_linkedlist
        self.subsections = subsections
        self.language = language


    def get_section(self, range_start, range_end):
        """
        Converts the human section citation of 1-3 sections to the keys of the section dictionary, and retrives the indices for self.words that the sections correspond to.

        """
        print(range_start, range_end)
        if range_start == "start":
            internal_range_start =  range_start
        elif range_start.count(".") == 0 and self.subsections == 1:
        #for things with one level and 1 level is expected
            internal_range_start =  range_start
        elif range_start.count(".") == 0 and self.subsections == 2:
        #for things with one level and 2 level was expected
            internal_range_start = range_start + ".1"
        elif range_start.count(".") == 0 and self.subsections == 3:
            #for things with one level and 3 level was expected
                internal_range_start = range_start + ".1.1"
        elif range_start.count(".") == 1 and self.subsections == 2:
            #for things with two levels, and two were given
            internal_range_start = range_start
        elif range_start.count(".") == 1 and self.subsections == 3:
            #for things with three levels, and two were given
            internal_range_start = range_start + ".1"
        elif range_start.count(".") == 2 and self.subsections == 3:
            internal_range_start = range_start
        if range_end == "end":
            internal_range_end = range_end
        elif range_end.count(".") == 0 and self.subsections == 1:
            #for input with one level and 1 level is expected
                internal_range_end = range_end
        elif range_end.count(".") == 0 and self.subsections == 2:
            #for input with one level and 2 level was expected
            internal_range_end = range_end + ".1"
                #sections should be another attribute of TEXT with an ordered list of sections, or maybe a dictionary. This is because we really want to go to the index  of the start of the next range -1, too keep the dictionary half the size. What is currently here will not work for lettered sections.
        elif range_end.count(".") == 0 and self.subsections == 3:
            #for things with one level and 3 level was expected
            internal_range_end = range_end + ".1.1"

        elif range_end.count(".") == 1 and self.subsections == 2:
                #for things with two levels, and two were given
            internal_range_end =  range_end

        elif range_end.count(".") == 1 and self.subsections == 3:
            #for things with three levels, and two were given
            internal_range_end = range_end + ".1"
        elif range_end.count(".") == 2 and self.subsections == 3:
            internal_range_end = range_end
        #start ends up being the end of the previous section + 1
        print(self.section_linkedlist[internal_range_start])
        return (self.sections[self.section_linkedlist[internal_range_start]] + 1, (self.sections[internal_range_end]+1))



    def get_words(self, user_start, user_end):
        """
        Convienent wrapper method. Gets the correct sublist of TITLES, based on user's selection.
        """
        #text will usually be a text class that is our target text, for this early demo/figuring things out phase we will not use one, it is hardcoded to Ovid Met 1.
        #really: Text.text_list(), a method to return the text list if present and error other wise
        start, end = self.get_section(user_start, user_end)
        wordlist = self.words[start: end]
        return wordlist
