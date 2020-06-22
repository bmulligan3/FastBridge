
from fastapi import APIRouter, WebSocket, Request, File, Form, UploadFile, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import importlib
from pathlib import Path
import DefinitionTools
from collections import namedtuple
running_list = True

router = APIRouter()
router_path = Path.cwd()
templates = Jinja2Templates(directory="templates")
"""Expected Prefix: /select"""


@router.get("/{language}/")
async def select(request : Request, language : str):
    book_name = importlib.import_module(language).texts
    return templates.TemplateResponse("select.html", {"request": request, "book_name": book_name})



#this is the simple result, if they exclude nothing.
@router.get("/{language}/result/{sourcetexts}/{starts}-{ends}/")
async def simple_result(request : Request, starts : str, ends : str, sourcetexts : str, language : str):
    context = {"request": request}
    triple = DefinitionTools.make_quads_or_trips(sourcetexts, starts, ends)
    words = []
    titles =[]
    for text, start, end in triple:
        book = DefinitionTools.get_text(text).book
        titles += (book.get_words(start, end))

    if not running_list:
        dups = set()
        new_titles = []
        for title in titles:
            if (title[0], title[1]) not in dups:
                dups.add((title[0], title[1]))
                new_titles.append(title)
                titles = sorted(new_titles, key=lambda x: x[-1])
    words, POS_list, columnheaders, row_filters = (DefinitionTools.get_lang_data(titles, language))

    section =", ".join(["{text}: {start} - {end}".format(text = text.replace("_", " "), start = start, end = end) for text, start, end in triple])
    #this insane oneliner goes through the triples, and converts it to a nice, human readable, format that we render on the page.
    #context["basic_defs"] = [word[3] for word in words]
    context["section"] = section
    context["len"] = len(words)
    checks = f""
    for POS in POS_list:
        checks+= f'<input type="checkbox" value="hide" id="{POS}" onchange="hide_show_row(this.id);" checked> {POS.replace("_", " ")}<br>'

    filters = f""
    for filter, POS_for_filter in row_filters:
        filters+=f'<div class="{POS_for_filter }"> <input type="checkbox" class = "{POS_for_filter}" value="hide" id="{filter}" onchange="hide_show_row(this.id);" checked> {filter.replace("_", " ")}<br></div>'

    headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            headers+= f'<input type="checkbox" value="hide" id="{header}" onchange="hide_show_column(this.id);" checked>{header.replace("_", " ")}'
        else:
            headers+= f'<input type="checkbox" value="show" id="{header}" onchange="hide_show_column(this.id);" > {header.replace("_", " ")}'
        headers+=f'<br>'
    other_headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            other_headers+=f' <th id = "{header}_head" > {header.replace("_", " ")} </th>'
        else:
            other_headers+=f'<th style="display: none;" id = "{header}_head" > {header.replace("_", " ")} </th>'
    render_words = f""
    for word, row_filter in words:
        render_words+= f'<tr class = "{row_filter}">'
        for i in range(len(columnheaders)):
            if columnheaders[i] == "DISPLAY_LEMMA" or columnheaders[i] == "SHORT_DEFINITION":
                render_words+= f'<td class = "{columnheaders[i]}">{word[i]}</td>'

            else:
                render_words+= f'<td style="display: none;" class = "{columnheaders[i]}">{word[i]}</td>'
        render_words+= f'</tr>'

    context["headers"] = headers
    context["POS_list"] = checks
    context["filters"] = filters
    context["other_headers"]  = other_headers
    #display_lemmas =([(word[0], word[3]) for word in words])

    context["render_words"] = render_words

    #print(context["words"][0])
    return templates.TemplateResponse("result.html", context)

#full case, now that I worked out the simpler idea URLs wise, it is easier to keep these seperate
@router.get("/{language}/result/{sourcetexts}/{starts}-{ends}/{in_exclude}/{othertexts}/{otherstarts}-{otherends}/")
async def result(request : Request, starts : str, ends : str, sourcetexts : str, in_exclude : str, othertexts : str, otherstarts : str, otherends : str, language : str):
    context = {"request": request}
    source = DefinitionTools.make_quads_or_trips(sourcetexts, starts, ends)
    other = DefinitionTools.make_quads_or_trips(othertexts, otherstarts, otherends)
    other_titles = set()
    for text, start, end in other:
        book = DefinitionTools.get_text(text).book
        other_titles = other_titles.union(set((book.get_words(start, end)))) #book.get_words gets a list of words, which we convert to a set and then union with the existing set to intersect or remove.
    other_titles = set([(new[0], new[1]) for new in other_titles]) #remove ordering information, we don't need it in this set
    ##print(other_titles)
    ##print("\n")
    titles = set()
    for text, start, end in source:
        book = DefinitionTools.get_text(text).book
        titles = titles.union(set((book.get_words(start, end))))
    to_operate = set([(new[0], new[1]) for new in titles])
    ##print(to_operate)
    ##print("\n")
    ##print(in_exclude)
    if in_exclude == "exclude":
        to_operate= to_operate.difference(other_titles)
    elif in_exclude == "include":
        to_operate.intersection_update(other_titles)

    #if always_show: #if we add lists to always include, they would be added here
        #titles = titles.union(commonly_confused) #if we make in_exclue more felxible (a list with elements in quads or trips) then we can specify for each text selected there what we do, and we can add this force show option more sensibly.
    titles =  [title for title in titles if (title[0], title[1]) in to_operate]

    ##print(titles)
    titles = sorted(titles, key=lambda x: x[-1])
    ##print(titles)
    words, POS_list = (DefinitionTools.get_lang_data(titles, language)) #this should be illegal because book should be out of scope, but it isn't.

    sextuple = list(zip(source, other))
    section = ", ".join(["{text}: {start} - {end} without {other}: {other_start} - {other_end}".format(text = text[0].replace("_", " "), start = text[1], end = text[2], other = other[0].replace("_", " "), other_start= other[1], other_end = other[2]) for text, other in sextuple])

    context["section"] = section
    context["len"] = len(words)

    checks = f""
    for POS in POS_list:
        checks+= f'<input type="checkbox" value="hide" id="{POS}" onchange="hide_show_row(this.id);" checked> {POS.replace("_", " ")}<br>'

    filters = f""
    for filter, POS_for_filter in row_filters:
        filters+=f'<div class="{POS_for_filter }"> <input type="checkbox" class = "{POS_for_filter}" value="hide" id="{filter}" onchange="hide_show_row(this.id);" checked> {filter.replace("_", " ")}<br></div>'

    headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            headers+= f'<input type="checkbox" value="hide" id="{header}" onchange="hide_show_column(this.id);" checked>{header.replace("_", " ")}'
        else:
            headers+= f'<input type="checkbox" value="show" id="{header}" onchange="hide_show_column(this.id);" > {header.replace("_", " ")}'
        headers+=f'<br>'
    other_headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            other_headers+=f' <th id = "{header}_head" > {header.replace("_", " ")} </th>'
        else:
            other_headers+=f'<th style="display: none;" id = "{header}_head" > {header.replace("_", " ")} </th>'
    render_words = f""
    for word, row_filter in words:
        render_words+= f'<tr class = "{row_filter}">'
        for i in range(len(columnheaders)):
            if columnheaders[i] == "DISPLAY_LEMMA" or columnheaders[i] == "SHORT_DEFINITION":
                render_words+= f'<td class = "{columnheaders[i]}">{word[i]}</td>'

            else:
                render_words+= f'<td style="display: none;" class = "{columnheaders[i]}">{word[i]}</td>'
        render_words+= f'</tr>'

    context["headers"] = headers
    context["POS_list"] = checks
    context["filters"] = filters
    context["other_headers"]  = other_headers
    context["render_words"] = render_words
    return templates.TemplateResponse("result.html", context)
