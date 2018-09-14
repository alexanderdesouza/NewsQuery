# !/usr/bin/env python3

import re

# Precompiled regular expressions utilized by the filtering functions below
re_abbr = re.compile(r'(?:^|\s)((?:\w(\.\s|\s|\.))(?:\w\2)+)', re.UNICODE)
re_abbr_separator = re.compile(r'(\s|\.)', re.UNICODE)
re_specialchar_removal = re.compile(r'(!|@|#|&|\(|\)|\+|=|\{|\}|\[|\]|:|;|\"|\'|,|\.$|\?)', re.UNICODE)
re_dash_removal = re.compile(r'-|_', re.UNICODE)


def abbreviations_to_words(text):
    """
    Converts all abbreviations found in the input string to a single word format.
    """
    text += " "
    all_abbreviations = [x[0] for x in re_abbr.findall(text + " ")]
    for abbreviation in all_abbreviations:
        new_form = re_abbr_separator.sub('', abbreviation)
        text = text.replace(abbreviation, new_form)
    return text.strip()


def preprocessor(text):
    """
    Applies the following preprocessing steps to any input text:
        - lowercases all text
        - maps abbreviations to same format (e.g., A.D., A. D., A D to AD)
        - removes general special characters (e.g., an '!' or an '&' symbol)
        - splits words that contains dashes or underscores
        - strips the any newline characters
    """
    text = text.lower()
    text = abbreviations_to_words(text)
    text = re_specialchar_removal.sub('', text)
    text = re_dash_removal.sub(' ', text)
    return text.strip()
