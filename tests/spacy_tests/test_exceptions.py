# coding: utf-8
from __future__ import unicode_literals

import pytest
import spacy
import sys

def test_tokenizer_handles_emoticons(combined_all_model_fixture):
    # Tweebo challenge (CMU)
    text = """:o :/ :'( >:o (: :) >.< XD -__- o.O ;D :-) @_@ :P 8D :1 >:( :D =| ") :> ...."""
    tokens = combined_all_model_fixture(text)
    assert tokens[0].text == ":o"
    assert tokens[1].text == ":/"
    assert tokens[2].text == ":'("
    assert tokens[3].text == ">:o"
    assert tokens[4].text == "(:"
    assert tokens[5].text == ":)"
    assert tokens[6].text == ">.<"
    assert tokens[7].text == "XD"
    assert tokens[8].text == "-__-"
    assert tokens[9].text == "o.O"
    assert tokens[10].text == ";D"
    assert tokens[11].text == ":-)"
    assert tokens[12].text == "@_@"
    assert tokens[13].text == ":P"
    assert tokens[14].text == "8D"
    assert tokens[15].text == ":1"
    assert tokens[16].text == ">:("
    assert tokens[17].text == ":D"
    assert tokens[18].text == "=|"
    assert tokens[19].text == '")'
    assert tokens[20].text == ':>'
    assert tokens[21].text == '....'


@pytest.mark.parametrize('text,length', [("example:)", 3), ("108)", 2), ("XDN", 1)])
def test_tokenizer_excludes_false_pos_emoticons(combined_all_model_fixture, text, length):
    tokens = combined_all_model_fixture(text)
    assert len(tokens) == length

@pytest.mark.parametrize('text,length', [('can you still dunk?🍕🍔😵LOL', 8),
                                         ('i💙you', 3), ('🤘🤘yay!', 4)])
def test_tokenizer_handles_emoji(combined_all_model_fixture, text, length):
    # These break on narrow unicode builds, e.g. Windows
    if sys.maxunicode >= 1114111:
        tokens = combined_all_model_fixture(text)
        assert len(tokens) == length
