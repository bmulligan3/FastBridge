
from fastapi import APIRouter, WebSocket, Request, File, Form, UploadFile, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import importlib
from pathlib import Path
import DefinitionTools
from collections import namedtuple
import math
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
@router.post("/{language}/result/{sourcetexts}/{starts}-{ends}/")
@router.get("/{language}/result/{sourcetexts}/{starts}-{ends}/")
async def simple_result(request : Request, starts : str, ends : str, sourcetexts : str, language : str):
    context = {"request": request}
    triple = DefinitionTools.make_quads_or_trips(sourcetexts, starts, ends)
    print("made trips")
    words = []
    titles =[]
    for text, start, end in triple:
        book = DefinitionTools.get_text(text).book
        titles += (book.get_words(start, end))
    print("got titles")
    if not running_list:
        dups = set()
        new_titles = []

        for title in titles:
            if (title[0]) not in dups:
                dups.add((title[0]))
                new_titles.append(title)
                titles = sorted(new_titles, key=lambda x: x[1])
        print(titles)
    words, POS_list, columnheaders, row_filters = (DefinitionTools.get_lang_data(titles, language))

    section =", ".join(["{text}: {start} - {end}".format(text = text.replace("_", " "), start = start, end = end) for text, start, end in triple])
    #this insane oneliner goes through the triples, and converts it to a nice, human readable, format that we render on the page.
    #context["basic_defs"] = [word[3] for word in words]
    context["section"] = section
    context["len"] = len(words)
    style = f""
    checks = f""
    for POS in POS_list:
        checks+= f'<div class="form-group"> <div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" value = "hide"  id="{POS}" onchange="hide_show_row(this.id);" checked><label class="custom-control-label" for="{POS}">{POS.replace("_", " ")}</label></div></div>'
        style+= f".{POS}_hide {{display:none!important;}}\n"
    filters = f""
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4]) #I am sorry this was too cool not to use: https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement

    for filter, POS_for_filter in row_filters:
        display_filter = filter.replace("_", " ")
        if display_filter[-1] != "0" or display_filter[-1] != "T":
            display_filter = ordinal(int(filter[-1])) + f" {display_filter[:-1]}"
        else:
            display_filter = display_filter[:-1]

        filters+=f'<div class="form-group"> <div class="custom-control custom-checkbox">   <input type="checkbox" value="hide" class="custom-control-input" value = "hide" id="{filter}" onchange="hide_show_row(this.id);" checked> <label class="custom-control-label" for="{filter}">{display_filter}</label></div></div>'
        style+= f".{filter}_hide {{display:none!important;}}\n"
    headers = f""
    for header in columnheaders:
        headers+= f'<div class="form-group"> <div class="custom-control custom-checkbox">'
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            headers+= f'<input type="checkbox" class="custom-control-input" value="hide" id="{header}" onchange="hide_show_column(this.id);" checked>'
        else:
            headers+= f'<input type="checkbox" class="custom-control-input" value="show" id="{header}" onchange="hide_show_column(this.id);">'

        headers+=f'<label class="custom-control-label" for="{header}">{header.replace("_", " ").title()}</label></div></div>'
    other_headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            other_headers+=f'<th id="{header}_head">{header.replace("_", " ")}</th>'
        else:
            other_headers+=f'<th id="{header}_head">{header.replace("_", " ")}</th>'
    render_words = f""
    for word, row_filter in words:
        render_words+= f'<tr class = "{row_filter}">'
        for i in range(len(columnheaders)):
            if columnheaders[i] == "DISPLAY_LEMMA" or columnheaders[i] == "SHORT_DEFINITION":
                render_words+= f'<td class="{columnheaders[i]}">{word[i]}</td>'

            elif(columnheaders[i] == "LOCAL_DEFINITION"):
                render_words+= f'<td class="{columnheaders[i]}">{word[-1]}</td>'
            else:
                render_words+= f'<td class="{columnheaders[i]}">{word[i]}</td>'
        render_words+= f'</tr>'
    context["style"] = style
    context["headers"] = headers
    context["POS_list"] = checks
    context["filters"] = filters
    context["other_headers"]  = other_headers
    context["render_words"] = render_words

    #print(context["words"][0])
    return templates.TemplateResponse("result.html", context)

#full case, now that I worked out the simpler idea URLs wise, it is easier to keep these seperate

@router.post("/{language}/result/{sourcetexts}/{starts}-{ends}/{in_exclude}/{othertexts}/{otherstarts}-{otherends}/")
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
    titles = sorted(titles, key=lambda x: x[1])
    ##print(titles)
    words, POS_list, columnheaders, row_filters = (DefinitionTools.get_lang_data(titles, language))

    sextuple = list(zip(source, other))
    section = ", ".join(["{text}: {start} - {end} without {other}: {other_start} - {other_end}".format(text = text[0].replace("_", " "), start = text[1], end = text[2], other = other[0].replace("_", " "), other_start= other[1], other_end = other[2]) for text, other in sextuple])

    context["section"] = section
    context["len"] = len(words)
    style = f""
    checks = f""
    for POS in POS_list:
        checks+= f'<div class="form-group"><div class="custom-control custom-checkbox"><input type="checkbox" value="hide" id="{POS}" onchange="hide_show_row(this.id);" checked><label class="custom-control-label" for="{POS}">{POS.replace("_", " ")}</label></div></div>'
        style+= f".{POS}_hide {{display:none!important;}}\n"
    filters = f""
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4]) #I am sorry this was too cool not to use: https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement

    for filter, POS_for_filter in row_filters:
        display_filter = filter.replace("_", " ")
        if display_filter[-1] != "0":
            display_filter = ordinal(int(filter[-1])) + f" {display_filter[:-1]}"
        else:
            display_filter = display_filter[:-1]
            style+= f".{filter}_show {{display:table-cell!important;}}\n"
        filters+=f'<div><input type="checkbox" value="hide" id="{filter}" onchange="hide_show_row(this.id);" checked>{display_filter}<br></div>'
        style+= f".{filter}_hide {{display:none!important;}}\n"
        style+= f".{filter}_show {{display:table-cell!important;}}\n"
    headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            headers+= f'<input type="checkbox" value="hide" id="{header}" onchange="hide_show_column(this.id);" checked>{header.replace("_", " ")}'
        else:
            headers+= f'<input type="checkbox" value="show" id="{header}" onchange="hide_show_column(this.id);">{header.replace("_", " ")}'
        headers+=f'<br>'
    other_headers = f""
    for header in columnheaders:
        if header == "DISPLAY_LEMMA" or header == "SHORT_DEFINITION":
            other_headers+=f'<th id="{header}_head">{header.replace("_", " ")}</th>'
        else:
            other_headers+=f'<th id="{header}_head">{header.replace("_", " ")}</th>'
    render_words = f""
    for word, row_filter in words:
        render_words+= f'<tr class = "{row_filter}">'
        for i in range(len(columnheaders)):
            if columnheaders[i] == "DISPLAY_LEMMA" or columnheaders[i] == "SHORT_DEFINITION":
                render_words+= f'<td class="{columnheaders[i]}">{word[i]}</td>'

            else:
                render_words+= f'<td class="{columnheaders[i]}">{word[i]}</td>'
        render_words+= f'</tr>'

    context["style"] = style
    context["headers"] = headers
    context["POS_list"] = checks
    context["filters"] = filters
    context["other_headers"]  = other_headers
    context["render_words"] = render_words
    return templates.TemplateResponse("result.html", context)
